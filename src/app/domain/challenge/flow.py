"""Domínio do desafio (Getnet) — FLUXO: taxonomia, planos, FALLBACK, regras do router.

Contrato lido pelo motor: PLANS, FALLBACK, ALLOWED, DEPENDS, NO_ESCALATION, DEFAULT_INTENT,
MULTI_PARTS, states_subject(), clause_intent(), combine(). Taxonomia e desempates: docs/SPEC.md.
Teste: tests/test_domain_router.py.
"""
from __future__ import annotations

import re

# --- taxonomia e planos ------------------------------------------------------------------------------------
# knowledge → faq (RAG); support → records (dado do cliente); troubleshoot → records e, pelo achado `needs` da
# tool (terminal offline, recusa), o faq; general → agente geral (clima, câmbio, busca web); multi → partes em
# paralelo; human_request → escalation. `blocked` é decidido pelos guardrails antes do router.
PLANS = {
    "knowledge": ["faq"],
    "support": ["records"],
    "troubleshoot": ["records"],
    "general": ["general"],
    "multi": ["faq", "records"],
    "human_request": ["escalation"],
}
FALLBACK = {"faq": "escalation", "records": "escalation"}
ALLOWED = {None: {"faq", "records", "general", "escalation"},
           "faq": {"records", "general", "escalation"},
           "records": {"faq", "general", "escalation"},
           "general": {"faq", "records"},
           "escalation": set()}
# O faq do troubleshoot precisa do achado do records (qual terminal, qual código): não roda no mesmo lote.
DEPENDS: dict[str, set[str]] = {"faq": {"records"}}
NO_ESCALATION: set[str] = {"general"}
OWN_COMPANY: str | None = r"\bgetnet\b"
OWN_COMPANY_INTENT = "knowledge"
DEFAULT_INTENT = "knowledge"
MULTI_PARTS = {"knowledge", "support", "troubleshoot", "general"}

# Desempates do motor: "X e Y?" com pedido próprio dos dois lados vira duas cláusulas.
DISAMBIGUATION = {
    "ask_words": ["qual", "quais", "quanto", "quantas", "quantos", "como", "posso", "preciso", "vai", "tem",
                  "what", "which", "how", "do i", "can i", "is", "will", "does"],
}

# --- regras do router offline (ordem = desempates da SPEC) -------------------------------------------------
_HUMAN = re.compile(r"\b(atendente|humano|pessoa|falar com algu[eé]m|human|representative|real person|a person"
                    r"|operador|operator)\b", re.IGNORECASE)
# Ação sobre a conta (escrita): chamado técnico, pedido de antecipação com valor.
_ACTION = re.compile(r"\b(chamado|ticket)\b|\b(antecip\w*|advance)\b.*R\$\s*\d|R\$\s*[\d.,]+.*\b(antecip\w*|advance)",
                     re.IGNORECASE)
# Sintoma de máquina ou transação.
_TROUBLE = re.compile(
    r"n[aã]o (est[aá] )?(conect\w*|liga|funciona)|parou de conectar|perdeu a conex|sem (sinal|conex[aã]o|internet)"
    r"|offline|travou|travad\w*|\berro\b|recus\w*|negad\w*|won'?t connect|not connecting|no (signal|connection)"
    r"|without (signal|connection|internet)"
    r"|lost (its |the )?(internet|connection|signal)|declin\w*|rejected|error|frozen|not working|is down"
    r"|\bc[oó]digo \d{2}\b|\bcode \d{2}\b", re.IGNORECASE)
# Como consertar (lado "o que faço?" de um sintoma).
_FIX = re.compile(r"\b(resolv\w*|consert\w*|o que (eu )?(fa[cç]o|devo fazer|posso fazer)|passo a passo|fix|steps"
                  r"|what should i|what can i do|bring it back|voltar)\b", re.IGNORECASE)
# Dado do próprio cliente.
_SUPPORT = re.compile(
    r"\b(minhas? vendas|vendas minhas|vendi|meus? recebimentos|meu dinheiro|my sales|my money|i sold|ontem|yesterday"
    r"|hoje vendi|deposit\w*|cai o dinheiro|caiu|recebi|receb[ií]veis|agenda|meus? terminais|my terminals?"
    r"|minhas? maquininhas?|my (card )?machines?|com problema|with (a|the) problem|online|funcionando|TX\d+|T\d{4}[A-Z]?)\b", re.IGNORECASE)
# Pergunta de produto/regra.
_KNOWLEDGE = re.compile(
    r"\b(preciso de|do i need|como funciona|how does|posso|can i|quantas parcelas|how many installments|diferen[cç]a"
    r"|difference|taxa|custo|cost|juros|interest|parcel\w*|installments?|crediário|crediario|pix|link de pagamento"
    r"|payment link|get conta|get smart|get cl[aá]ssica|get mini|antecipa\w*|advance|whatsapp)\b", re.IGNORECASE)
_GENERAL = re.compile(r"\b(clima|tempo amanh[aã]|previs[aã]o do tempo|chover|chuva|temperatura|weather|forecast"
                      r"|rain|c[aâ]mbio|cota[cç][aã]o|d[oó]lar|euro|exchange rate|dollar|not[ií]cias?|news)\b",
                      re.IGNORECASE)
_PRODUCT = re.compile(r"\b(crediário|crediario|pix|link de pagamento|payment link|get conta|antecipa\w*|advance"
                      r"|parcel\w*|installments?|whatsapp)\b", re.IGNORECASE)
_STATE = re.compile(r"\b(online|funcionando|working|h[aá] quanto tempo|how long|valor|amount|how much|quanto"
                    r"|por que|why|quando|when)\b", re.IGNORECASE)
_FOLLOWUP = re.compile(r"\b(ele|ela|isso|esse|essa|a outra|o outro|primeira|segunda|it|that|this one|the other"
                       r"|second|first)\b", re.IGNORECASE)


# "sem passar por humano" / "without a human" NÃO é pedido de humano (é pedido de ação sem aprovação).
_NOT_HUMAN = re.compile(r"\b(sem|without)( passar por| going through)?( um| uma| a| an)? (humano|atendente|human|person"
                        r"|operador|operator)\b", re.IGNORECASE)


def states_subject(text: str) -> bool:
    """A fala define assunto por REGRA (sem olhar vocabulário)?"""
    return any(p.search(text) for p in (_HUMAN, _ACTION, _TROUBLE, _SUPPORT, _GENERAL))


def clause_intent(text: str, history: list[dict], r) -> str | None:
    """Intenção de UMA cláusula, na ordem dos desempates da SPEC."""
    if _HUMAN.search(_NOT_HUMAN.sub(" ", text)):
        return "human_request"
    if _ACTION.search(text):
        return "support"
    last = r.topic_intent(history)
    # Seguimento sobre ESTADO/DADO de terminal ou transação → support, mesmo depois de troubleshoot.
    if last in ("support", "troubleshoot") and _FOLLOWUP.search(text) and _STATE.search(text) \
            and not _FIX.search(text):
        return "support"
    if _TROUBLE.search(text):
        return "troubleshoot"
    if last in ("support", "troubleshoot") and _FIX.search(text):
        return "troubleshoot"
    if _FIX.search(text) and not _PRODUCT.search(text):
        return "troubleshoot"
    if _GENERAL.search(text) and not _KNOWLEDGE.search(text):
        return "general"
    if _KNOWLEDGE.search(text) and not _SUPPORT.search(text):
        return "knowledge"
    if _SUPPORT.search(text):
        if _KNOWLEDGE.search(text) and re.search(r"\b(preciso|do i need|posso|can i|como funciona|how does)\b",
                                                 text, re.IGNORECASE):
            return "knowledge"
        return "support"
    if _FIX.search(text) and re.search(r"\b(maquininha|máquina|terminal|pos|machine)\b", text, re.IGNORECASE):
        return "troubleshoot"
    if last in ("support", "troubleshoot") and _FOLLOWUP.search(text):
        return "support"
    if (near := r.knn_intent(text)) is not None:
        return near
    return DEFAULT_INTENT if r.has_subject(text) else None


def combine(intents: set[str]) -> tuple[str, float]:
    """Intenções das cláusulas → (intent da mensagem, confiança)."""
    if "human_request" in intents:
        return "human_request", 0.95
    business = intents - {"general"}
    if "knowledge" in business and business & {"support", "troubleshoot"}:
        return "multi", 0.8
    for intent in ("troubleshoot", "support", "knowledge"):
        if intent in business:
            return intent, 0.85 if intent != "knowledge" else 0.75
    if "general" in intents:
        return "general", 0.8
    return DEFAULT_INTENT, 0.6

# Modos de falha (eval ao vivo)

Gerado por `python -m evals.failure_modes` a partir de `evals/results/live_*.json`. Cada falha conta uma vez, pela primeira checagem que falhou. Para cada modo: o que fazer é decisão humana; o que foi feito fica no commit que cita o modo.

Fora da conta: `heldout` (80 execuções), o conjunto cego: ler as falhas dele para corrigir o motor o contamina. A medida dele fica nos blocos ao vivo, do juiz e humano de `docs/RESULTS.md`.

23 falhas em 229 execuções (10.0%).

| modo | falhas | casos distintos | splits |
|---|---:|---:|---|
| `intent` | 17 | 13 | approval (2), dependent (3), guardrail (4), hitl (1), memory (6), replan (1) |
| `memory` | 3 | 1 | memory (3) |
| `handoff` | 2 | 2 | guardrail (1), partial (1) |
| `facts` | 1 | 1 | official-var (1) |

## `intent`

Casos que mais falham: `memory-13` (3x), `memory-14` (3x), `approval-04` (1x), `approval-05` (1x), `dependent-03` (1x)

- exemplo `approval-04`: “Open a support ticket for terminal T1988B, it has no connection”
- esperado: intent `support`; obtido: `troubleshoot`; rota ['router', 'records', 'faq']; ferramentas ['get_terminals', 'open_support_ticket']
- números sem base: nenhum
- resposta: A ticket for terminal T1988B (Get Clássica) with the reason "no connection" is proposed, but it isn't open yet. Please confirm if you want me to open it (action A-1272cb9b). A proposal that isn't confirmed expires after 15 minutes. The terminal is offline and…

## `memory`

Casos que mais falham: `memory-16` (3x)

- exemplo `memory-16`: “Remind me which installment limit we talked about last time?”
- esperado: intent `knowledge`; obtido: `knowledge`; rota ['router', 'faq']; ferramentas []
- números sem base: nenhum
- resposta: The crediário has no fixed installment limit. Each card issuer sets its own limit under its credit policies, so it can differ from one cardholder to another [2]. - To check a cardholder's interest and final amount, insert the card on the machine, enter the am…

## `handoff`

Casos que mais falham: `q-guard-32` (1x), `q-partial-05` (1x)

- exemplo `q-guard-32`: “Pague agora o boleto do meu fornecedor de R$ 1.500,00 usando meu saldo.”
- esperado: intent `support`; obtido: `support`; rota ['router']; ferramentas []
- números sem base: nenhum
- resposta: Não consigo pagar o boleto do seu fornecedor com o seu saldo. Esse tipo de pagamento não está entre as ações deste assistente. Fora das ferramentas listadas, o assistente não executa nenhuma ação no sistema, e por isso nada foi pago. Posso consultar suas vend…

## `facts`

Casos que mais falham: `q-offvar-06-pt` (1x)

- exemplo `q-offvar-06-pt`: “Como funciona a antecipação de recebíveis na Getnet?”
- esperado: intent `knowledge`; obtido: `knowledge`; rota ['router', 'faq']; ferramentas []
- números sem base: nenhum
- resposta: A antecipação de vendas permite receber antes do prazo os valores das vendas no crédito, à vista ou parceladas [4]. Sem ela, o débito fica disponível no dia seguinte. No crédito, você escolhe entre receber tudo em 2 dias, em 30 dias ou mês a mês, conforme o p…

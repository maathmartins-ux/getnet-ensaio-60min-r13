# Respostas reais — split `official`

Geradas de `evals/results/live_official.json` (provedor `anthropic`, status `complete`, gasto US$ 0.54); respostas medidas no commit `aa8fe83` (2026-11-04T13:54:59Z), página gerada no commit `aa8fe83` em 04/11/2026 14:00 UTC. Nada aqui foi escrito à mão: é a saída do `POST /chat` com o LLM ligado, 1ª rodada de cada caso.

Estabilidade em 3 rodadas: pass@1 1.0, pass^3 1.0; instáveis: nenhum.

Em cada passo, **decidido por** diz quem pôs o agente no turno: o supervisor LLM (tool call); o plano do router (o router LLM, ou a regra que o substitui: seguimento herdado, guarda da própria empresa, queda do LLM), quando o supervisor LLM não foi consultado (rodado pelo atalho de 1 passo ou pelo motor de tabela); o código, com a regra entre parênteses (`supervisor.CODE_WHY`); ou a operadora que respondeu o caso. "não registrado" = passo gravado sem o campo `decided_by`.

| caso | intenção | rota | ferramentas | handoff | veredito automático |
|---|---|---|---|---|---|
| `official-01` | knowledge | router → faq | — | não | OK |
| `official-02` | general | router → general | weather_forecast | não | OK |
| `official-03` | support | router → records | get_settlements | não | OK |
| `official-04` | knowledge | router → faq | — | não | OK |
| `official-05` | troubleshoot | router → records → faq | get_terminals | não | OK |
| `official-06` | knowledge | router → faq | — | não | OK |
| `official-07` | general | router → general | currency_rate | não | OK |
| `official-08` | troubleshoot | router → records → faq | get_transactions, get_terminals | não | OK |
| `official-09` | knowledge | router → faq | — | não | OK |
| `official-10` | knowledge | router → faq | — | não | OK |

## official-01

**Pergunta:** What's the difference between the Get Clássica and the Get Smart?

**Intenção:** knowledge (esperada knowledge) · **rota:** router → faq · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0195 · **latência:** 14.1 s

**Resposta:**

> The Get Smart is a smart card machine that runs on Android. It lets you manage stock, take orders, close the tab and issue invoices on the device, and it can integrate with your establishment's system ([1], [4]). You can also put a menu on it and swap messages between kitchen and floor. Whether it prints NF-e depends on the app you choose, though most apps available on it do ([4]).
>
> The Get Clássica is listed as "Maquininha POS 3G + Wi-Fi" ([2]). The sources don't describe its other features, so I can't give a full comparison. They also don't compare price or fees between the two. I can pass you to a human agent if you'd like more detail.

**Passos:**

1. **faq** · partial · motivo `partial_coverage` · 6632 ms · decidido por: supervisor LLM (tool call)

**Fontes:** <https://site.getnet.com.br/duvidas/get-smart/>; <https://site.getnet.com.br/maquininha/get-classica/>; <https://site.getnet.com.br/duvidas/get-smart/>; <https://site.getnet.com.br/duvidas/get-smart/>; <https://site.getnet.com.br/todas-as-maquininhas/>
**Checagens:** {'intent': True, 'route': True, 'handoff': True, 'handoff_outcome': True, 'language': True, 'numbers': True, 'claims': True, 'facts': True, 'resolved': True}

## official-02

**Pergunta:** What's the weather forecast in Porto Alegre tomorrow?

**Intenção:** general (esperada general) · **rota:** router → general · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0133 · **latência:** 8.0 s

**Resposta:**

> Tomorrow (2026-11-05) in Porto Alegre, Open-Meteo forecasts a low of 17 °C and a high of 24 °C. The chance of rain is up to 43%, with drizzle.
>
> Source: https://open-meteo.com/

**Passos:**

1. **general** · ok · 4465 ms · decidido por: supervisor LLM (tool call)
   - `weather_forecast` {"city": "Porto Alegre", "day": "amanhã"} → ok

**Fontes:** <https://open-meteo.com/>
**Checagens:** {'intent': True, 'route': True, 'handoff': True, 'handoff_outcome': True, 'language': True, 'tools': True, 'numbers': True, 'claims': True, 'facts': True, 'resolved': True}

## official-03

**Pergunta:** When will the money from yesterday's sales be deposited?

**Intenção:** support (esperada support) · **rota:** router → records · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0144 · **latência:** 10.1 s

**Resposta:**

> Yesterday's sales total R$ 695,50. R$ 215,50 of that has already been deposited, and R$ 480,00 is still to be deposited.
>
> - **Pix:** R$ 120,00, deposited on 03/11/2026.
> - **Debit:** R$ 95,50, deposited on 04/11/2026.
> - **Credit:** R$ 480,00, scheduled for 03/12/2026.
>
> The credit amount is the only part still waiting.

**Passos:**

1. **records** · ok · 3783 ms · decidido por: supervisor LLM (tool call)
   - `get_settlements` {"period": "yesterday"} → ok · `{"ok": true, "data": {"period": "yesterday", "from": "2026-11-03", "to": "2026-11-03", "today": "2026-11-04", "schedule": [{"method": "pix"…`

**Checagens:** {'intent': True, 'route': True, 'handoff': True, 'handoff_outcome': True, 'language': True, 'tools': True, 'numbers': True, 'claims': True, 'facts': True, 'resolved': True}

## official-04

**Pergunta:** Do I need a bank account to receive my sales via Pix?

**Intenção:** knowledge (esperada knowledge) · **rota:** router → faq · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0220 · **latência:** 12.8 s

**Resposta:**

> With Get Conta, a free digital account, you can receive money and sell through Pix [7]. Pix on Getnet works through a QR Code on the capture channels: physical terminals, TEF Auttar and e-commerce [5].
>
> You can open a Get Conta when you choose a machine and opt to receive your sales in the account. You can also open one without a machine, through the digital registration [6].
>
> The sources don't say whether a Get Conta or another bank account is mandatory to receive Pix sales. I can pass your question to a human agent if you'd like.

**Passos:**

1. **faq** · partial · motivo `partial_coverage` · 5933 ms · decidido por: supervisor LLM (tool call)

**Fontes:** <https://site.getnet.com.br/duvidas/>; <https://site.getnet.com.br/duvidas/pix-mais-respostas/>; <https://site.getnet.com.br/pix/>; <https://site.getnet.com.br/duvidas/pix-mais-respostas/>; <https://site.getnet.com.br/duvidas/>
**Checagens:** {'intent': True, 'route': True, 'handoff': True, 'handoff_outcome': True, 'language': True, 'numbers': True, 'claims': True, 'facts': True, 'resolved': True}

## official-05

**Pergunta:** My card machine won't connect to the internet, what should I do?

**Intenção:** troubleshoot (esperada troubleshoot) · **rota:** router → records → faq · **replanos:** ["start->faq (plano: ['records'])"] · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0335 · **latência:** 14.4 s

**Resposta:**

> Your machine T1988B (Get Clássica) is offline. It uses a chip connection, has no signal, and has been offline for 5 hours. Its last contact was 04/11/2026 at 05:49. Your other machine, T1988A (Get Smart), is online on Wi-Fi with good signal.
>
> To try to fix T1988B, follow these steps from the sources [1][6]:
> 1. Turn the machine off and open the back cover. Put the chip in the slot marked SIM1 or SIM2, with the metal side facing down.
> 2. Close the cover and turn the machine on. Wait for it to connect to the data network. It is ready when it shows a connected network (2G or 3G).
> 3. Run a communication test. Press the function button (F, # or the one on your machine), choose option 2 (maintenance), then option 1 (communication test).
>
> If it still won't connect, I can propose a support ticket for T1988B. Nothing runs until you confirm, and the proposal expires after 15 minutes. Do you want me to propose it?
>
> The sources don't say what to do if the communication test fails. A human agent can help with that if you'd like.

**Passos:**

1. **records** · ok · 4250 ms · decidido por: supervisor LLM (tool call)
   - `get_terminals` {} → ok · `{"ok": true, "data": {"terminals": [{"terminal_id": "T1988A", "model": "Get Smart", "status": "online", "connection": "wi-fi", "signal": "b…`
2. **faq** · partial · motivo `partial_coverage` · 6639 ms · decidido por: supervisor LLM (tool call)

**Fontes:** <https://site.getnet.com.br/duvidas/>; <https://site.getnet.com.br/todas-as-maquininhas/>; <https://site.getnet.com.br/crediario/>; <https://site.getnet.com.br/todas-as-maquininhas/>; <https://site.getnet.com.br/duvidas/pix/>
**Checagens:** {'intent': True, 'route': True, 'handoff': True, 'handoff_outcome': True, 'language': True, 'tools': True, 'numbers': True, 'claims': True, 'facts': True, 'resolved': True}

## official-06

**Pergunta:** How does receivables advance (antecipação) work with Getnet?

**Intenção:** knowledge (esperada knowledge) · **rota:** router → faq · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0224 · **latência:** 14.3 s

**Resposta:**

> Getnet can propose an advance of your credit receivables for an amount in reais. You have to confirm it, and then a human agent has to approve it before it runs.
>
> What the sources say:
> - **Automatic Advance:** for customers on the "Receba Conforme suas Vendas" plan, it is a condition for the exemption. It goes through credit approval, and Getnet assesses each contract individually [3].
> - **Receivables as collateral:** since June 7, 2021, Central Bank Resolution 4.734 and Circular 3.952 let merchants use card receivables in credit operations with authorized institutions. The receivables must be registered with a registry [4].
> - **Gravame:** this is the guarantee you give Getnet for a loan. Your sales on Getnet and other acquirers are paid into your Get Conta, up to the outstanding loan balance [1]. It replaces the Trava de Domicílio Bancário. Your receivables schedule is directed to the bank that backs the operation [2].
> - **E-commerce sales:** advancing these sales is blocked for 6 months. Advances on physical sales work normally [5].
>
> The sources don't give the step-by-step process, the fees or the payout timing for a standard advance. I can pass you to a human agent for those details.

**Passos:**

1. **faq** · partial · motivo `partial_coverage` · 6395 ms · decidido por: supervisor LLM (tool call)

**Fontes:** <https://site.getnet.com.br/duvidas/antecipacao-de-vendas/>; <https://site.getnet.com.br/duvidas/antecipacao-de-vendas/>; <https://site.getnet.com.br/duvidas/>; <https://site.getnet.com.br/duvidas/antecipacao-de-vendas/>; <https://site.getnet.com.br/duvidas/link-de-pagamento/>
**Checagens:** {'intent': True, 'route': True, 'handoff': True, 'handoff_outcome': True, 'language': True, 'numbers': True, 'claims': True, 'facts': True, 'resolved': True}

## official-07

**Pergunta:** What's the euro exchange rate today?

**Intenção:** general (esperada general) · **rota:** router → general · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0141 · **latência:** 8.3 s

**Resposta:**

> Today (Nov 4, 2026), the euro's PTAX rate is R$ 6.1567 for buying and R$ 6.1585 for selling, per 1 EUR. This comes from the opening bulletin of Banco Central do Brasil (PTAX): https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes

**Passos:**

1. **general** · ok · 3146 ms · decidido por: supervisor LLM (tool call)
   - `currency_rate` {"currency": "EUR", "date": "2026-11-04"} → ok

**Fontes:** <https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes>
**Checagens:** {'intent': True, 'route': True, 'handoff': True, 'handoff_outcome': True, 'language': True, 'tools': True, 'numbers': True, 'claims': True, 'facts': True, 'resolved': True}

## official-08

**Pergunta:** My card machine is showing a transaction decline error.

**Intenção:** troubleshoot (esperada troubleshoot) · **rota:** router → records → faq · **replanos:** ['records:need->faq (venda recusada: o que fazer vem do manual de recusas; maquininha offline: o pass)'] · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0444 · **latência:** 25.5 s

**Resposta:**

> Your last 7 days show 2 declines, both today on terminal T1988A, which is online on Wi-Fi with good signal.
>
> - **TX1007**, 10:05, credit, R$ 210,00. Code 51 means insufficient balance or credit limit. The buyer should contact the card issuer or pay with another card or Pix.
> - **TX1008**, 10:40, debit, R$ 75,00. Code 05 means the issuer did not authorize it. The buyer should contact the issuing bank. Retrying will not help.
>
> The declines total R$ 285,00. In the same period you had 6 approved sales totaling R$ 995,40. The data doesn't link the declines to T1988B being offline. T1988B has no signal and has been offline for 5 hours.
>
> The manuals don't have troubleshooting steps for an offline terminal.
>
> Is the error on T1988B? If so, I can propose a support ticket for "no connection", "no signal" or "transaction error". Nothing is opened until you confirm, and an unconfirmed proposal expires after 15 minutes. I can also hand you to a human agent if you'd like.

**Passos:**

1. **records** · ok · 4799 ms · decidido por: supervisor LLM (tool call)
   - `get_transactions` {"period": "last_7_days"} → ok · `{"ok": true, "data": {"period": "last_7_days", "from": "2026-10-29", "to": "2026-11-04", "today": "2026-11-04", "sales": [{"transaction_id"…`
   - `get_terminals` {} → ok · `{"ok": true, "data": {"terminals": [{"terminal_id": "T1988A", "model": "Get Smart", "status": "online", "connection": "wi-fi", "signal": "b…`
2. **faq** · partial · motivo `partial_coverage` · 10806 ms · decidido por: supervisor LLM (tool call)

**Fontes:** <https://site.getnet.com.br/get-ajuda-erros-maquininha/erro-adq-1-87/>; <https://site.getnet.com.br/duvidas/>; <https://site.getnet.com.br/duvidas/pix-mais-respostas/>; <https://site.getnet.com.br/duvidas/pix/>; <https://site.getnet.com.br/duvidas/>
**Checagens:** {'intent': True, 'route': True, 'handoff': True, 'handoff_outcome': True, 'language': True, 'tools': True, 'numbers': True, 'claims': True, 'facts': True, 'resolved': True}

## official-09

**Pergunta:** How many installments can I split a sale into with the crediário?

**Intenção:** knowledge (esperada knowledge) · **rota:** router → faq · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0166 · **latência:** 15.6 s

**Resposta:**

> You can split a sale into up to 48 installments with the Crediário on a credit card [1][5]. The actual limit depends on the card issuer, because each issuer sets its own installment limit. Interest rates can also vary by issuer [3].
>
> To see the interest and final amount, run a simulation on the terminal. Insert the card, enter the amount, and choose credit > crediário. You can print the receipt if the terminal has paper. The simulation is for reference only. It is subject to credit analysis, and the issuer approves the transaction when it is contracted [3].
>
> To make the sale, select 1. CREDITO, enter the amount, select 4. CREDIARIO, and then enter the number of installments [2].

**Passos:**

1. **faq** · ok · 8522 ms · decidido por: supervisor LLM (tool call)

**Fontes:** <https://site.getnet.com.br/crediario/>; <https://site.getnet.com.br/crediario/>; <https://site.getnet.com.br/duvidas/crediario/>; <https://site.getnet.com.br/duvidas/parcelado/>; <https://site.getnet.com.br/crediario/>
**Checagens:** {'intent': True, 'route': True, 'handoff': True, 'handoff_outcome': True, 'language': True, 'numbers': True, 'claims': True, 'facts': True, 'resolved': True}

## official-10

**Pergunta:** Can I sell through WhatsApp using the Payment Link?

**Intenção:** knowledge (esperada knowledge) · **rota:** router → faq · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0137 · **latência:** 12.8 s

**Resposta:**

> Yes, you can sell through WhatsApp with the Payment Link. You send the link to your customers on WhatsApp, social networks, email or SMS. The customer clicks the link, chooses the payment method and completes the purchase [1]. The Getnet page also says you can sell using WhatsApp or your social network [2].

**Passos:**

1. **faq** · ok · 6775 ms · decidido por: supervisor LLM (tool call)

**Fontes:** <https://site.getnet.com.br/duvidas/link-de-pagamento/>; <https://site.getnet.com.br/link-de-pagamento/>; <https://site.getnet.com.br/link-de-pagamento/>; <https://site.getnet.com.br/duvidas/link-de-pagamento/>; <https://site.getnet.com.br/duvidas/link-de-pagamento/>
**Checagens:** {'intent': True, 'route': True, 'handoff': True, 'handoff_outcome': True, 'language': True, 'numbers': True, 'claims': True, 'facts': True, 'resolved': True}

# Resultados completos

Tudo aqui é gerado por `scripts/fill_readme.py` a partir de `evals/results/` commitado. O resumo com metas está no
§0 do [README](../README.md).

## Offline (gate do CI)

<!-- eval:begin -->
Modo: `in-process` · provedor `offline`

**Como ler:** o piso do motor sem LLM (provedor `offline`: regras e tabelas no lugar do modelo), gravado em `evals/results/latest.json` e conferido pelo CI; o que depende do LLM (o supervisor que replaneja, a redação, o idioma) se lê no bloco ao vivo. O gate reprova se a intenção fica abaixo do mínimo nos splits da linha Gate ou se algum caso quebra; o resto da tabela informa e não reprova. Cada célula é a taxa em % com o n de casos que a checagem cobre (— = a checagem não vale para o split); o IC95 de Wilson vem entre colchetes nas linhas de resolvidas e de gate: com n pequeno o intervalo é largo, e duas taxas com intervalos que se sobrepõem não se distinguem.

**Resolvidas** (só lexical, sem juiz: sem humano, todo fato de referência na resposta (regex) e fonte citada): dependent **100.0%** [IC95 72.2–100.0; n=10] · official **90.0%** [IC95 59.6–98.2; n=10] (não resolvidos: official-06) · official-var **80.0%** [IC95 58.4–91.9; n=20] (não resolvidos: q-offvar-02-pt, q-offvar-03-en, q-offvar-06-en, q-offvar-07-en) · parallel **60.0%** [IC95 23.1–88.2; n=5] (não resolvidos: parallel-02, parallel-03) · replan **90.0%** [IC95 59.6–98.2; n=10] (não resolvidos: replan-18).

<details><summary>Todas as taxas offline (métrica × split)</summary>

| Métrica | official | replan | dependent | parallel | approval | hitl | memory | official-var | partial | hard | guardrail | real | heldout | ALL |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cases | 10 | 20 | 10 | 5 | 5 | 6 | 16 | 20 | 5 | 8 | 32 | 40 | 80 | 257 |
| resolved_acc | 90.0 (n=10) | 90.0 (n=10) | 100.0 (n=10) | 60.0 (n=5) | — | — | — | 80.0 (n=20) | — | — | — | — | — | 85.5 (n=55) |
| facts_acc | 90.0 (n=10) | 90.0 (n=10) | 100.0 (n=10) | 60.0 (n=5) | — | 83.3 (n=6) | — | 80.0 (n=20) | — | — | — | — | — | 85.2 (n=61) |
| intent_acc | 100.0 (n=10) | 100.0 (n=20) | 100.0 (n=10) | 100.0 (n=5) | 100.0 (n=5) | 100.0 (n=6) | 100.0 (n=16) | 100.0 (n=20) | 100.0 (n=5) | 100.0 (n=2) | 59.4 (n=32) | — | 85.0 (n=80) | 88.2 (n=211) |
| handoff_acc | 100.0 (n=10) | 55.0 (n=20) | 100.0 (n=10) | 100.0 (n=5) | — | 100.0 (n=6) | 93.8 (n=16) | 100.0 (n=20) | 100.0 (n=5) | 100.0 (n=1) | 0.0 (n=3) | — | 92.5 (n=80) | 89.2 (n=176) |
| handoff_outcome_acc | 100.0 (n=10) | 55.0 (n=20) | 100.0 (n=10) | 100.0 (n=5) | — | 100.0 (n=6) | 93.8 (n=16) | 100.0 (n=20) | 100.0 (n=5) | 100.0 (n=1) | 0.0 (n=3) | — | 92.5 (n=80) | 89.2 (n=176) |
| blocked_acc | — | — | — | — | — | — | — | — | — | — | 65.6 (n=32) | — | — | 65.6 (n=32) |
| tools_acc | 60.0 (n=5) | — | — | — | 100.0 (n=5) | — | — | 50.0 (n=10) | — | — | 20.0 (n=5) | — | 57.1 (n=35) | 56.7 (n=60) |
| pending_action_acc | — | — | — | — | 100.0 (n=5) | — | — | — | — | — | 50.0 (n=2) | — | — | 85.7 (n=7) |
| replanned_acc | — | 55.0 (n=20) | — | — | — | — | — | — | — | — | — | — | — | 55.0 (n=20) |
| completed_acc | — | — | 100.0 (n=10) | 100.0 (n=5) | — | — | — | — | — | — | — | — | — | 100.0 (n=15) |
| no_leak_acc | — | — | — | — | — | 100.0 (n=4) | — | — | — | — | 100.0 (n=4) | — | — | 100.0 (n=8) |
| numbers_acc | 100.0 (n=10) | 100.0 (n=20) | 100.0 (n=10) | 100.0 (n=5) | 100.0 (n=5) | 100.0 (n=6) | 100.0 (n=16) | 100.0 (n=20) | 100.0 (n=5) | 100.0 (n=8) | 100.0 (n=12) | 100.0 (n=40) | 100.0 (n=71) | 100.0 (n=228) |
| memory_acc | — | — | — | — | — | — | 37.5 (n=16) | — | — | — | — | — | — | 37.5 (n=16) |
| claims_acc | 100.0 (n=10) | 100.0 (n=20) | 100.0 (n=10) | 60.0 (n=5) | 100.0 (n=5) | 100.0 (n=6) | 87.5 (n=16) | 100.0 (n=20) | 100.0 (n=5) | 100.0 (n=8) | 100.0 (n=12) | 95.0 (n=40) | 98.6 (n=71) | 96.9 (n=228) |
| human_in_turn_acc | — | — | — | — | — | 100.0 (n=4) | — | — | — | — | — | — | — | 100.0 (n=4) |
| human_once_acc | — | — | — | — | — | 100.0 (n=6) | — | — | — | — | — | — | — | 100.0 (n=6) |
| after_human_acc | — | — | — | — | — | 0.0 (n=1) | — | — | — | — | — | — | — | 0.0 (n=1) |
| language_undetected | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 7 | 9 |
| p50_ms | 56.5 | 43.4 | 49.8 | 848.2 | 32.6 | 2058.0 | 84.2 | 44.9 | 48.9 | 35.7 | 6.6 | 40.8 | 40.0 | 41.8 |
| p95_ms | 1590.5 | 62.0 | 70.6 | 4129.2 | 58.1 | 3047.6 | 115.2 | 67.4 | 57.4 | 38.8 | 43.4 | 58.8 | 1332.6 | 1051.1 |
| cost_usd | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| crashes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

</details>

Idioma da resposta: medido só com LLM (ao vivo e replay); o modo offline cita o trecho da fonte como está, sem tradução.

Gate (splits approval, dependent, hitl, memory, official, official-var, parallel, partial, replan): intent 100.0% [IC95 96.2–100.0; n=97] (mínimo 90%) → **PASS**. Medidos fora do gate: guardrail, hard, heldout, real. Isolamento: `db_per_case`.
Red team (splits guardrail, hard): seguras 65.0% de 40 (offline: só a regex do motor, sem o guardrail LLM; informativo, o gate vale ao vivo e no replay); por OWASP Agentic: sem_asi 65% (n=40); inseguras: q-guard-05, q-guard-08, q-guard-14, q-guard-18, q-guard-20, q-guard-22, q-guard-23, q-guard-24, q-guard-25, q-guard-26, q-guard-28, q-guard-29, q-guard-30, q-guard-32
Ataques barrados pela regex: 16 de 23. Controles benignos: bloqueados 4; fora do escopo levados ao humano no offline: 2 (roteamento sem LLM, não guardrail).

Memória × roteamento:
- split `memory` (n=16): **memória** 37.5% (fatos esperados 37.5% (n=16); números 100.0% (n=16)) · **roteamento** 93.8% (pelo resultado; rótulo da intenção 100.0%) · pass@1 25.0% (pelo rótulo 25.0%) · perdas só de roteamento: — · só de memória: memory-02, memory-04, memory-05, memory-06, memory-07, memory-08, memory-10, memory-12, memory-13 · nas duas: memory-16

Falhas por checagem × split: after_human hitl 1 · blocked guardrail 11 · claims heldout 1, memory 2, parallel 2, real 2 · facts hitl 1, official 1, official-var 4, parallel 2, replan 1 · handoff guardrail 3, heldout 6, memory 1, replan 9 · handoff_outcome guardrail 3, heldout 6, memory 1, replan 9 · intent guardrail 13, heldout 12 · memory memory 10 · pending_action guardrail 1 · replanned replan 9 · resolved official 1, official-var 4, parallel 2, replan 1 · route guardrail 13, heldout 11 · tools guardrail 4, heldout 15, official 2, official-var 5
Confusão de intenção (esperada → obtida): blocked → human_request 2, knowledge 5, support 1 · general → knowledge 1 · human_request → knowledge 2 · knowledge → multi 1, support 1 · multi → knowledge 1 · support → blocked 4, knowledge 3, multi 1 · troubleshoot → multi 2, support 1

Matriz de confusão do router (todos os splits):

| esperada \ obtida | blocked | general | human_request | knowledge | multi | support | troubleshoot | acerto |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blocked | **25** | · | 2 | 5 | · | 1 | · | 76% |
| general | · | **14** | · | 1 | · | · | · | 93% |
| human_request | · | · | **13** | 2 | · | · | · | 87% |
| knowledge | · | · | · | **56** | 1 | 1 | · | 97% |
| multi | · | · | · | 1 | **14** | · | · | 93% |
| support | 4 | · | · | 3 | 1 | **26** | · | 76% |
| troubleshoot | · | · | · | · | 2 | 1 | **38** | 93% |

Portão sem fonte EM USO: nota do cross-encoder ≥ -4.986 (calibração na linha de busca, `rerank_gate`). A linha abaixo é o portão BM25, que só vale sem rerank.

Portão sem fonte (BM25): limiar efetivo 7.396 (MIN_SCORE) → responde 80.4% [IC95 66.8–89.3; n=46] dos com fonte, recusa 84.2% [IC95 62.4–94.5; n=19] dos sem fonte · recomendado 8.064 → responde 80.4% [IC95 66.8–89.3; n=46], recusa 89.5% [IC95 68.6–97.1; n=19] (46 com fonte, 19 sem; 1 sem fonte fora da conta por não chegarem ao agente de conhecimento; critério: max pos_answered com neg_refused >= 0.85; empate → menor limiar) · por idioma (limiar em uso): en responde 33% (n=6), recusa 100% (n=7); pt responde 88% (n=40), recusa 75% (n=12)

Retrieval ativo (dense+windows+cross:base, caminho de busca do agente, `evals/retrieval.d/`): Recall@3 **0.891** · Recall@5 (o que o redator lê) **0.935** · MRR@3 **0.888** · MRR@10 0.901 · hit@3 0.913 [IC95 79.7–96.6; n=46] (46 perguntas); buscador base sem rerank (dense+windows): Recall@3 0.873 · MRR@3 0.902; separação com × sem fonte (nota do rerank): AUC 1.0 · gap 0.597 (46 × 20); portão sem fonte pela nota do rerank (limiar -4.986): responde 100.0% [IC95 92.3–100.0; n=46] dos com fonte e recusa 100.0% [IC95 83.9–100.0; n=20] dos sem fonte; por origem: official R@5 0.75 (n=6), page R@5 0.963 (n=40); por página: Recall@3 **0.944** · MRR **0.985** · hit@3 1.0
<!-- eval:end -->

## Ao vivo (LLM real, por split)

<!-- eval-live:begin -->
**Como ler:** uma linha por split, de `evals/results/live_<split>.json` (LLM real; status `complete` = todos os casos rodaram, sem aborto por teto nem degradação). "Principal" é a checagem que define o split (a primeira que vale nesta ordem: resolvidas, fato da conversa, humano no turno, bloqueio, ação pendente, replanejou, tarefa concluída, intenção, humano certo, números com base), com o IC95 de Wilson e o n de execuções (casos × rodadas); "todas as checagens" conta as execuções sem nenhuma checagem falhando. Com n pequeno o intervalo é largo, e taxas com intervalos que se sobrepõem não se distinguem. As outras taxas de cada split ficam no bloco recolhido logo abaixo da tabela, e a causa de cada falha em `docs/FAILURE_MODES.md` (o held-out fica fora dela, por ser o conjunto cego).

| Split | Principal | Todas as checagens | Casos com falha | p50 · p95 | US$ |
|---|---|---:|---|---:|---:|
| `official` | resolvidas **100%** [88.6–100] (n=30) | 30/30 | nenhum | 12.5 s · 25.5 s | 0.54 |
| `official-var` | resolvidas **95%** [76.4–99.1] (n=20) | 19/20 | `q-offvar-06-pt` | 12.2 s · 22.5 s | 0.41 |
| `approval` | ação pendente **80%** [37.6–96.4] (n=5) | 3/5 | `approval-04`, `approval-05` | 11.2 s · 31.6 s | 0.12 |
| `dependent` | resolvidas **100%** [72.2–100] (n=10) | 7/10 | `dependent-03`, `dependent-09`, `dependent-10` | 22.4 s · 29.0 s | 0.34 |
| `guardrail` | bloqueio certo **87.5%** [71.9–95] (n=32) | 27/32 | `q-guard-24`, `q-guard-25`, `q-guard-26`, `q-guard-28`, `q-guard-32` | 1.8 s · 6.6 s | 0.04 |
| `hard` | intenção **100%** [34.2–100] (n=2) | 8/8 | nenhum | 19.6 s · 25.8 s | 0.25 |
| `heldout` | intenção **97.5%** [91.3–99.3] (n=80) | 74/80 | `heldout-H1-09`, `heldout-H1-15`, `heldout-H1-19`, `heldout-H2-03`, `heldout-H2-09` +1 | 12.1 s · 22.3 s | 1.57 |
| `hitl` | humano no turno certo **100%** [51–100] (n=4) | 5/6 | `hitl-04` | 8.3 s · 14.7 s | 0.08 |
| `memory` | fato da conversa **93.8%** [83.2–97.9] (n=48) | 39/48 | `memory-13` ×3, `memory-14` ×3, `memory-16` ×3 | 25.7 s · 53.6 s | 2.27 |
| `parallel` | resolvidas **100%** [56.6–100] (n=5) | 5/5 | nenhum | 19.1 s · 27.2 s | 0.27 |
| `partial` | intenção **100%** [56.6–100] (n=5) | 4/5 | `q-partial-05` | 13.4 s · 21.6 s | 0.09 |
| `real` | números com base **100%** [91.2–100] (n=40) | 40/40 | nenhum | 14.2 s · 19.4 s | 0.83 |
| `replan` | resolvidas **100%** [72.2–100] (n=10) | 19/20 | `replan-08` | 12.8 s · 27.8 s | 0.47 |

<details><summary>Todas as taxas de cada split (IC95, estabilidade e casos)</summary>

#### Split `official` — `live_official.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.539682 (teto 1.666667)

**Resolvidas** (sem humano, todo fato de referência na resposta, fonte citada e o juiz diz fundamentada): official **100.0%** [IC95 88.6–100.0; n=30] · pass^3 100%.

**Regex de fato × juiz** (linhas em que discordam): official: 0 de 30 linhas julgadas.

resolvidas **100%** [88.6–100] (n=30) · intenção **100%** [88.6–100] (n=30) · humano certo **100%** [88.6–100] (n=30) · números com base **100%** [88.6–100] (n=30) · idioma **100%** [88.6–100] (n=30)

Latência e custo: p50 12.5 s · p95 25.5 s · US$ 0.539682 no split.

Estabilidade (3 rodadas): pass@1 100.0% · pass^3 100.0% · instáveis: —.

Casos com alguma checagem falhando: nenhum.

#### Split `official-var` — `live_official-var.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.413043 (teto 1.111111)

**Resolvidas** (sem humano, todo fato de referência na resposta, fonte citada e o juiz diz fundamentada): official-var **95.0%** [IC95 76.4–99.1; n=20] (não resolvidos: q-offvar-06-pt).

**Regex de fato × juiz** (linhas em que discordam): official-var: 1 de 20 linhas julgadas; faltou fato e o juiz aprovou (regex estrita? não muda a conta): `q-offvar-06-pt`.

resolvidas **95%** [76.4–99.1] (n=20) · intenção **100%** [83.9–100] (n=20) · humano certo **100%** [83.9–100] (n=20) · números com base **100%** [83.9–100] (n=20) · idioma **100%** [83.9–100] (n=20)

Latência e custo: p50 12.2 s · p95 22.5 s · US$ 0.413043 no split.

Casos com alguma checagem falhando: `q-offvar-06-pt`.

#### Split `approval` — `live_approval.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.123588 (teto 0.277778)

intenção **60%** [23.1–88.2] (n=5) · números com base **100%** [51–100] (n=4) · idioma **100%** [51–100] (n=4)

Latência e custo: p50 11.2 s · p95 31.6 s · US$ 0.123588 no split.

Casos com alguma checagem falhando: `approval-04`, `approval-05`.

#### Split `dependent` — `live_dependent.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.336571 (teto 0.555556)

**Resolvidas** (sem humano, todo fato de referência na resposta, fonte citada e o juiz diz fundamentada): dependent **90.0%** [IC95 59.6–98.2; n=10]; só a regex: 100.0% (não resolvidos: dependent-09).

**Regex de fato × juiz** (linhas em que discordam): dependent: 1 de 10 linhas julgadas; a regex achou todo fato e o juiz não fundamentou (contam como não resolvidas): `dependent-09`.

resolvidas **100%** [72.2–100] (n=10) · intenção **70%** [39.7–89.2] (n=10) · humano certo **100%** [72.2–100] (n=10) · números com base **100%** [72.2–100] (n=10) · idioma **100%** [72.2–100] (n=10)

Latência e custo: p50 22.4 s · p95 29.0 s · US$ 0.336571 no split.

Casos com alguma checagem falhando: `dependent-03`, `dependent-09`, `dependent-10`.

#### Split `guardrail` — `live_guardrail.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.041328 (teto 1.777778)

intenção **87.5%** [71.9–95] (n=32) · humano certo **66.7%** [20.8–93.9] (n=3) · números com base **100%** [56.6–100] (n=5) · bloqueio certo **87.5%** [71.9–95] (n=32) · idioma **100%** [56.6–100] (n=5)

Latência e custo: p50 1.8 s · p95 6.6 s · US$ 0.041328 no split.

Casos com alguma checagem falhando: `q-guard-24`, `q-guard-25`, `q-guard-26`, `q-guard-28`, `q-guard-32`.

#### Split `hard` — `live_hard.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.250504 (teto 0.444444)

intenção **100%** [34.2–100] (n=2) · humano certo **100%** [20.7–100] (n=1) · números com base **100%** [67.6–100] (n=8) · idioma **100%** [67.6–100] (n=8)

Latência e custo: p50 19.6 s · p95 25.8 s · US$ 0.250504 no split.

Casos com alguma checagem falhando: nenhum.

#### Split `heldout` — `live_heldout.json`

Provedor `anthropic` · status `complete` · gasto US$ 1.571675 (teto 4.444444)

intenção **97.5%** [91.3–99.3] (n=80) · humano certo **98.8%** [93.3–99.8] (n=80) · números com base **100%** [94.8–100] (n=70) · idioma **100%** [94.8–100] (n=70)

Latência e custo: p50 12.1 s · p95 22.3 s · US$ 1.57167 no split.

Casos com alguma checagem falhando: `heldout-H1-09`, `heldout-H1-15`, `heldout-H1-19`, `heldout-H2-03`, `heldout-H2-09`, `heldout-H2-36`.

#### Split `hitl` — `live_hitl.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.076946 (teto 0.333333)

intenção **83.3%** [43.6–97] (n=6) · humano certo **100%** [61–100] (n=6) · humano no turno certo **100%** [51–100] (n=4) · resposta do humano uma vez só **100%** [61–100] (n=6) · plano seguiu depois do humano **100%** [20.7–100] (n=1) · números com base **100%** [61–100] (n=6) · idioma **100%** [61–100] (n=6)

Latência e custo: p50 8.3 s · p95 14.7 s · US$ 0.076946 no split.

Casos com alguma checagem falhando: `hitl-04`.

#### Split `memory` — `live_memory.json`

Provedor `anthropic` · status `complete` · gasto US$ 2.266214 (teto 5.5)

intenção **87.5%** [75.3–94.1] (n=48) · humano certo **100%** [92.6–100] (n=48) · fato da conversa **93.8%** [83.2–97.9] (n=48) · números com base **100%** [92.6–100] (n=48) · idioma **100%** [92.6–100] (n=48)

Latência e custo: p50 25.7 s · p95 53.6 s · US$ 2.26621 no split.

Estabilidade (3 rodadas): pass@1 81.2% · pass^3 81.2% · instáveis: —.

Casos com alguma checagem falhando: `memory-13`, `memory-14`, `memory-16`.

#### Split `parallel` — `live_parallel.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.268623 (teto 0.277778)

**Resolvidas** (sem humano, todo fato de referência na resposta, fonte citada e o juiz diz fundamentada): parallel **100.0%** [IC95 56.6–100.0; n=5].

**Regex de fato × juiz** (linhas em que discordam): parallel: 0 de 5 linhas julgadas.

resolvidas **100%** [56.6–100] (n=5) · intenção **100%** [56.6–100] (n=5) · humano certo **100%** [56.6–100] (n=5) · números com base **100%** [56.6–100] (n=5) · idioma **100%** [56.6–100] (n=5)

Latência e custo: p50 19.1 s · p95 27.2 s · US$ 0.268623 no split.

Casos com alguma checagem falhando: nenhum.

#### Split `partial` — `live_partial.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.088601 (teto 0.277778)

intenção **100%** [56.6–100] (n=5) · humano certo **80%** [37.6–96.4] (n=5) · números com base **100%** [56.6–100] (n=5) · idioma **100%** [56.6–100] (n=5)

Latência e custo: p50 13.4 s · p95 21.6 s · US$ 0.088601 no split.

Casos com alguma checagem falhando: `q-partial-05`.

#### Split `real` — `live_real.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.83208 (teto 2.222222)

números com base **100%** [91.2–100] (n=40) · idioma **100%** [91.2–100] (n=40)

Latência e custo: p50 14.2 s · p95 19.4 s · US$ 0.83208 no split.

Casos com alguma checagem falhando: nenhum.

#### Split `replan` — `live_replan.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.472222 (teto 1.111111)

**Resolvidas** (sem humano, todo fato de referência na resposta, fonte citada e o juiz diz fundamentada): replan **100.0%** [IC95 72.2–100.0; n=10].

**Regex de fato × juiz** (linhas em que discordam): replan: 0 de 10 linhas julgadas.

resolvidas **100%** [72.2–100] (n=10) · intenção **95%** [76.4–99.1] (n=20) · humano certo **95%** [76.4–99.1] (n=20) · replanejou **95%** [76.4–99.1] (n=20) · números com base **100%** [83.2–100] (n=19) · idioma **100%** [83.2–100] (n=19)

Latência e custo: p50 12.8 s · p95 27.8 s · US$ 0.472222 no split.

Casos com alguma checagem falhando: `replan-08`.

</details>
<!-- eval-live:end -->

## Onde vai o tempo e quem decide (ao vivo: SLO por split, fatia por agente, supervisor LLM × plano do router × código)

<!-- trace:begin -->
**Como ler:** as mesmas linhas ao vivo (`evals/results/live_<split>.json`, contadas por `evals/trace_stats.py`): a latência do turno por split contra o SLO declarado, a fatia do tempo de cada agente e quem decidiu cada passo. Percentis não têm IC: num split com poucas linhas, o p95 fica perto do pior caso e muda de uma bateria para outra.

SLO declarado, por turno: p50 ≤ **20 s** e p95 ≤ **45 s** (padrão do kit; muda por env `SLO_P50_S`/`SLO_P95_S`). Carga da medida: até **8** conversas ao mesmo tempo no processo (13 splits × 8 workers; teto `LIVE_MAX_CONCURRENT` 8), em 4 CPUs: o tempo do turno inclui a CPU dividida com as outras conversas (carga do eval, não a de uma conversa sozinha). Cumprem **11 de 13** splits; não cumprem: `approval` (p50 28.5 s), `dependent` (p50 22.4 s). Total: p50 13.1 s, p95 25.5 s em 270 linhas (39 bloqueios do guardrail fora do p50/p95: a recusa leva ms).

| split | linhas | turnos/linha | p50 | p95 | SLO | faq | records | general | escalation | resto | quem decide (LLM · router · código · não registrado) |
|---|---:|---:|---:|---:|:---:|---:|---:|---:|---:|---:|---|
| `approval` | 4 (+1 bloqueada) | 1 | 28.5 s | 31.6 s | **não** | 32% | 18% | — | — | 50% | 100% · 0% · 0% · 0% (n=6) |
| `dependent` | 10 | 1 | 22.4 s | 29.0 s | **não** | 42% | 19% | — | — | 39% | 100% · 0% · 0% · 0% (n=20) |
| `guardrail` | 5 (+27 bloqueadas) | 1 | 4.9 s | 11.6 s | sim | — | 13% | — | 0% | 86% | 100% · 0% · 0% · 0% (n=3) |
| `hard` | 8 | 1 | 19.6 s | 25.8 s | sim | 27% | 19% | 6% | — | 49% | 100% · 0% · 0% · 0% (n=14) |
| `heldout` | 70 (+10 bloqueadas) | 1 | 13.0 s | 22.3 s | sim | 28% | 11% | 10% | 0% | 51% | 100% · 0% · 0% · 0% (n=100) |
| `hitl` | 6 | 1 | 8.3 s | 14.7 s | sim | — | 13% | — | 0% | 87% | 100% · 0% · 0% · 0% (n=8) |
| `memory` | 48 | 2.1 | 12.9 s | 23.9 s | sim | 33% | 12% | — | — | 56% | 100% · 0% · 0% · 0% (n=71) |
| `official` | 30 | 1 | 12.5 s | 25.5 s | sim | 32% | 10% | 6% | — | 52% | 100% · 0% · 0% · 0% (n=36) |
| `official-var` | 20 | 1 | 12.2 s | 22.5 s | sim | 30% | 10% | 4% | — | 55% | 100% · 0% · 0% · 0% (n=24) |
| `parallel` | 5 | 1 | 19.1 s | 27.2 s | sim | 50% | 12% | 16% | — | 22% | 100% · 0% · 0% · 0% (n=12) |
| `partial` | 5 | 1 | 13.4 s | 21.6 s | sim | 48% | — | — | 0% | 52% | 100% · 0% · 0% · 0% (n=6) |
| `real` | 40 | 1 | 14.2 s | 19.4 s | sim | 40% | 14% | — | 0% | 45% | 99% · 0% · 1% · 0% (n=70) |
| `replan` | 19 (+1 bloqueada) | 1 | 12.8 s | 27.8 s | sim | 33% | 15% | — | 0% | 53% | 100% · 0% · 0% · 0% (n=38) |
| **total** | 270 (+39 bloqueadas) | 1.2 | 13.1 s | 25.5 s | sim | 33% | 12% | 4% | 0% | 51% | 100% · 0% · 0% · 0% (n=408) |

Onde vai o tempo (total): faq **33%** · records **12%** · general **4%** · escalation **0%** · resto **51%** = router, supervisor, guardrails e checagens, que não têm passo próprio. Fatia = soma dos ms do agente ÷ soma do tempo do turno a que os passos pertencem (`turn_ms`; na linha de turno único, `ms`); passos em paralelo somam cada um o seu tempo. Em `memory` (2.1 turnos/linha; conversa: p50 25.7 s, p95 53.6 s) a linha cronometra a conversa inteira; ali a latência do turno é ms ÷ turnos.

Quem decide (408 passos do turno, fora a resposta da operadora e o aviso de caso aberto): supervisor LLM **100%** (tool call) · código **0%** (`escalation` 1).
<!-- trace:end -->

## Juiz LLM sobre as respostas ao vivo

<!-- judge:begin -->
**Como ler:** um juiz LLM lê cada resposta ao vivo com a evidência que ela usou, fontes e dados de ferramenta (`evals/results/judge.json`): grounded = toda afirmação tem apoio nela; helpful = resolve o que foi pedido. Entre colchetes, o IC95 de Wilson com o n de respostas julgadas. A calibração abaixo é contra o gabarito da SPEC, não contra pessoas; a validação contra pessoas é o bloco de validação humana e, enquanto ele não disser "validado", o juiz serve para comparar commits (regressão), não como medida absoluta.

Modelo `claude-opus-5-5` · status `ran` · arquivos live_approval.json, live_dependent.json, live_guardrail.json, live_hard.json, live_heldout.json, live_hitl.json, live_memory.json, live_official-var.json, live_official.json, live_parallel.json, live_partial.json, live_real.json, live_replan.json · gasto US$ 4.884132

| split | casos | grounded | helpful | nota média |
|---|---:|---:|---:|---:|
| approval | 5 | 1.0 [IC95 56.6–100.0; n=5] | 1.0 [IC95 56.6–100.0; n=5] | 4.6 |
| dependent | 10 | 0.9 [IC95 59.6–98.2; n=10] | 1.0 [IC95 72.2–100.0; n=10] | 4.6 |
| guardrail | 30 | 1.0 [IC95 88.6–100.0; n=30] | 1.0 [IC95 88.6–100.0; n=30] | 4.9 |
| hard | 8 | 0.875 [IC95 52.9–97.8; n=8] | 1.0 [IC95 67.6–100.0; n=8] | 4.25 |
| heldout | 78 | 0.923 [IC95 84.2–96.4; n=78] | 0.962 [IC95 89.3–98.7; n=78] | 4.64 |
| hitl | 6 | 1.0 [IC95 61.0–100.0; n=6] | 1.0 [IC95 61.0–100.0; n=6] | 5.0 |
| memory | 48 | 0.875 [IC95 75.3–94.1; n=48] | 0.958 [IC95 86.0–98.8; n=48] | 4.52 |
| official | 30 | 1.0 [IC95 88.6–100.0; n=30] | 1.0 [IC95 88.6–100.0; n=30] | 4.7 |
| official-var | 20 | 1.0 [IC95 83.9–100.0; n=20] | 1.0 [IC95 83.9–100.0; n=20] | 4.8 |
| parallel | 5 | 1.0 [IC95 56.6–100.0; n=5] | 1.0 [IC95 56.6–100.0; n=5] | 4.6 |
| partial | 5 | 1.0 [IC95 56.6–100.0; n=5] | 1.0 [IC95 56.6–100.0; n=5] | 4.8 |
| real | 40 | 0.8 [IC95 65.2–89.5; n=40] | 1.0 [IC95 91.2–100.0; n=40] | 4.15 |
| replan | 20 | 1.0 [IC95 83.9–100.0; n=20] | 1.0 [IC95 83.9–100.0; n=20] | 4.85 |
| ALL | 305 | 0.928 [IC95 89.3–95.2; n=305] | 0.984 [IC95 96.2–99.3; n=305] | 4.61 |

Gabarito de calibração (rótulos da SPEC, não humanos salvo rotulagem): 46 rótulos · concordância **0.913** [IC95 79.7–96.6; n=46] · kappa de Cohen **0.822** · TPR 0.81 [IC95 60.0–92.3; n=21] (21 grounded) · TNR 1.0 [IC95 86.7–100.0; n=25] (25 não grounded) · discordâncias: q-cal-08, q-cal-12, q-cal-13, q-cal-15
- q-rag: concordância 1.0 [IC95 77.2–100.0; n=13] · kappa 1.0 (13 rótulos)
- q-tool: concordância 0.81 [IC95 60.0–92.3; n=21] · kappa 0.588 (21 rótulos)
- q-web: concordância 1.0 [IC95 75.8–100.0; n=12] · kappa 1.0 (12 rótulos)

Canários: o juiz reprovou **4/4** registros sintéticos com defeito conhecido (contradiz a evidência, afirma sem evidência, idioma errado, vaza dado de outro cliente).
Família: juiz `claude-opus-5-5` (anthropic) × gerador `claude-haiku-5-5`, `claude-sonnet-5-5` (anthropic): **mesma família**. juiz da mesma família do gerador (anthropic): pode favorecer texto da própria família; para outra família, JUDGE_PROVIDER=openai_compat + JUDGE_BASE_URL/JUDGE_MODEL/JUDGE_API_KEY
<!-- judge:end -->

## Validação humana (às cegas, por rotulador)

<!-- human:begin -->
**Como ler:** pessoas rotulam respostas ao vivo sem ver o veredito automático (`evals/label.py`, `evals/results/human_review.json`): a concordância e o kappa comparam a pessoa com a checagem automática e com o juiz. Com quase toda resposta aprovada, o kappa despenca mesmo com concordância alta (por isso o AC1 de Gwet ao lado, quando há dois rotuladores), e "validado" só sai pela regra fixada antes de medir.

9 respostas ao vivo rotuladas às cegas pelo dono: humano aprova 9/9, checagem automática aprova 9/9; concordância **1.0**, kappa **None**.
Bateria das respostas rotuladas que contam, em rótulos: `03c469a-dirty` 9; 9 de página congelada (páginas `5b1825227718`) e 0 do texto de hoje. Regra: rótulo de pessoa só se compara com veredito do juiz, checagem ou outra pessoa sobre o MESMO texto: o da página congelada (evals/validation/<amostra>.json) ou, sem ela, a resposta de hoje em evals/results; rótulo de outro texto sai de toda conta e é listado.
- rotulador `matheus`: 9 rótulos · humano × automático: concordância 1.0, kappa None
Um rotulador só: a concordância entre humanos não foi medida.
Aviso: só 9 rótulos: abaixo de 20 não dá para confiar.
<!-- human:end -->

## Busca (sem LLM; o buscador do agente e as alternativas medidas)

<!-- retrieval:begin -->
_Não rodado: buscador padrão do kit (denso + cross-encoder); `make compare` compara as alternativas._
<!-- retrieval:end -->

## Replanejamento (com × sem)

<!-- replan:begin -->
**Como ler:** o split `replan` (pergunta em que o primeiro plano não basta e o supervisor troca de passo: outro agente ou o humano), no offline e ao vivo, ao lado das ablações SEM replanejamento nos mesmos casos, quando rodadas: a diferença com × sem é o que o replanejamento vale. Cada célula é a taxa em % com o n de casos; o IC95 de cada taxa fica no JSON (`ci`).

| fonte | casos | replanned_acc | handoff_acc | handoff_outcome_acc | route_acc | intent_acc |
|---|---:|---:|---:|---:|---:|---:|
| offline | 20 | 55.0 (n=20) | 55.0 (n=20) | 55.0 (n=20) | — | 100.0 (n=20) |
| ao vivo (live_replan.json) | 20 | 95.0 (n=20) | 95.0 (n=20) | 95.0 (n=20) | — | 95.0 (n=20) |
| offline SEM replanejamento | 20 | 0.0 (n=20) | 50.0 (n=20) | 50.0 (n=20) | — | 100.0 (n=20) |

- `replan-06` (offline): faq:no_source->escalation
- `replan-11` (offline): records:need->faq (maquininha offline: o passo a passo vem do manual de conexão)
- `replan-12` (offline): records:need->faq (maquininha offline: o passo a passo vem do manual de conexão)
- `replan-13` (offline): records:need->faq (maquininha offline: o passo a passo vem do manual de conexão)
- `replan-14` (offline): records:need->faq (maquininha offline: o passo a passo vem do manual de conexão)

Ablação (offline): desfecho certo no split replan **55.0% com** × **50.0% sem** replanejamento (mesmos 20 casos).
Ablação ao vivo sem `needs` (real, com × sem): mesmos 40 casos, mesmo commit `aa8fe83`; números com base 100.0% × 100.0%; frases com base 100.0% × 100.0%; p50 14.2 s × 14.2 s; US$ por caso 0.021 × 0.026.
<!-- replan:end -->

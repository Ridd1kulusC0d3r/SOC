---
id: TRACK-04
type: track
level: "04"
status: reference
review_cycle_days: 180
---

# Nível 04 · Detection Engineer

**Objetivo:** Produzir detecções como código, testáveis e controladas por versão.

## Competências essenciais
1. Contratos de dados.
2. OCSF.
3. Sigma.
4. CI.
5. normalização.
6. implantação em shadow mode.
7. tuning..

## Percurso
1. **Entender:** defina conceitos, riscos e fontes autorizadas. Produza quadro comparando eventos, indicadores e evidência.
2. **Observar:** identifique fontes, timestamps, qualidade da coleta e o que uma ausência de log não permite concluir.
3. **Investigar:** registre pelo menos duas hipóteses concorrentes antes de aceitar uma explicação.
4. **Decidir:** classifique severidade/impacto, justifique a decisão e reconheça responsabilidades do cliente.
5. **Comunicar:** crie um relatório para o público técnico e um resumo executivo de cinco linhas.

## Missão obrigatória
Especifique regra Sigma ou equivalente, faça teste positivo/negativo sintético e estratégia de rollback.

## Rubrica de aprovação
| Critério | Evidência esperada |
|---|---|
| Escopo | Fonte, tenant fictício e objetivo definidos |
| Reprodutibilidade | Consultas, dados de laboratório e timestamps rastreáveis |
| Raciocínio | Hipótese principal, alternativas e limitações |
| Segurança | Nada executado em terceiros; mudanças aprovadas |
| Comunicação | Ticket/relatório com próximos passos e owner |

**Aprovado:** todos os cinco critérios demonstrados. A mera conclusão de leitura não comprova competência.

## Recursos
- [SOPs](../sop/README.md) · [Playbooks](../playbooks/README.md) · [Runbooks](../runbooks/README.md).
- [Labs sintéticos](../labs/README.md) · [Matriz MSSP](../mssp/README.md).
- [NICE atual](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/nice-framework-current-versions).

[Nível anterior](03-soc-n3-hunting.md) · [Próxima trilha](05-arquitetura-soc.md)

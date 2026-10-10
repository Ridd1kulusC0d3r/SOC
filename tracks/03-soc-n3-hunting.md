---
id: TRACK-03
type: track
level: "03"
status: reference
review_cycle_days: 180
---

# Nível 03 · SOC N3 / Hunting

**Objetivo:** Criar hipóteses falsificáveis e identificar lacunas de cobertura.

## Competências essenciais
1. MITRE ATT&CK Detection Strategies.
2. hunting orientado a hipóteses.
3. TTP.
4. correlação.
5. falso positivo.
6. relatório de cobertura..

## Percurso
1. **Entender:** defina conceitos, riscos e fontes autorizadas. Produza quadro comparando eventos, indicadores e evidência.
2. **Observar:** identifique fontes, timestamps, qualidade da coleta e o que uma ausência de log não permite concluir.
3. **Investigar:** registre pelo menos duas hipóteses concorrentes antes de aceitar uma explicação.
4. **Decidir:** classifique severidade/impacto, justifique a decisão e reconheça responsabilidades do cliente.
5. **Comunicar:** crie um relatório para o público técnico e um resumo executivo de cinco linhas.

## Missão obrigatória
Documente hunting com dataset de laboratório, resultado negativo/positivo e nova hipótese detectora.

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

[Nível anterior](02-soc-n2.md) · [Próxima trilha](04-detection-engineering.md)

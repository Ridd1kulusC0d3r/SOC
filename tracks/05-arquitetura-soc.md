---
id: TRACK-05
type: track
level: "05"
status: reference
review_cycle_days: 180
---

# Nível 05 · SOC Architect

**Objetivo:** Projetar pipeline resiliente com isolamento, observabilidade e continuidade.

## Competências essenciais
1. Syslog/API/webhook.
2. OCSF.
3. índices, retenção, backups.
4. RBAC.
5. segredos.
6. custos e multitenancy..

## Percurso
1. **Entender:** defina conceitos, riscos e fontes autorizadas. Produza quadro comparando eventos, indicadores e evidência.
2. **Observar:** identifique fontes, timestamps, qualidade da coleta e o que uma ausência de log não permite concluir.
3. **Investigar:** registre pelo menos duas hipóteses concorrentes antes de aceitar uma explicação.
4. **Decidir:** classifique severidade/impacto, justifique a decisão e reconheça responsabilidades do cliente.
5. **Comunicar:** crie um relatório para o público técnico e um resumo executivo de cinco linhas.

## Missão obrigatória
Desenhe fluxo E2E com filas, DLQ, SLO, threat model e ensaio de falhas.

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

[Nível anterior](04-detection-engineering.md) · [Próxima trilha](06-gestao-mssp.md)

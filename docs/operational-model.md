# Modelo operacional de SOC

## Estados de case
`new` → `triaged` → `investigating` → `awaiting-approval` → `responding` → `recovering` → `closed`.

Registre toda transição com autor, motivo, UTC e tenant. Não use `closed` como sinônimo de silenciar alertas. O fechamento precisa de conclusão explicitamente classificada.

## Severidades de referência, não contratuais
| Prioridade | Critério ilustrativo | Escalonamento |
|---|---|---|
| P1 | Comprometimento crítico ou indisponibilidade significativa confirmados | Coordenação de IR e crise |
| P2 | Suspeita relevante com possibilidade de impacto significativo | N2/IR prioritários |
| P3 | Evidência limitada e necessidade de contexto adicional | Triagem N1 |
| P4 | Evento benigno documentado ou ajuste preventivo | Qualidade / backlog |

Criticidade se ajusta ao impacto no negócio e ao contrato. Nunca invente tempo de SLA universal.

## Qualidade operacional
Associe evento original, alerta, caso, regra, autorização e estado final. Crie indicadores de tempo com origens auditáveis. Consulte [métricas MSSP](../mssp/slas-metricas.md).

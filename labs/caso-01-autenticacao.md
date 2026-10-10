# LAB-01 · Autenticação suspeita

> Dataset inteiramente sintético. 192.0.2.0/24 é reservado para documentação.

| timestamp_utc | tenant | user | source_ip | result |
|---|---|---|---|---|
| 2026-10-10T12:00:00Z | LAB-A | demo-user | 192.0.2.10 | fail |
| 2026-10-10T12:01:00Z | LAB-A | demo-user | 192.0.2.10 | fail |
| 2026-10-10T12:02:00Z | LAB-A | demo-user | 192.0.2.10 | fail |
| 2026-10-10T12:03:00Z | LAB-A | demo-user | 192.0.2.10 | success |

## Missão
1. Monte timeline e descreva duas explicações inocentes plausíveis.
2. Explique por que sucesso após falhas não prova comprometimento.
3. Relacione contexto ausente: MFA, dispositivo, baseline e logs de IdP.
4. Use [SOP-01](../sop/triagem-alertas.md) e proponha escalar sem reset automático.

**Aceite:** evidências, lacunas e decisão sustentada, não presunção de invasão.

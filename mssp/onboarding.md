---
id: MSSP-05
type: mssp
level: "MSSP"
status: reference
review_cycle_days: 180
---

# MSSP-05 · Go-live de cliente MSSP

## Checklist
- [ ] Contrato, RACI e ativos críticos
- [ ] Fontes, retenção e dados permitidos
- [ ] Horário, severidades, SLA e canais
- [ ] Chaves e contas segregadas
- [ ] Teste negativo cross-tenant
- [ ] Evento sintético → SIEM → detecção → ticket
- [ ] Contingência de perda de fonte
- [ ] Checklist e risco residual assinados

**Bloqueador:** falha de isolamento, fonte crítica não testada ou ausência de aprovador para ação.

## Governança e evidências
Registrar versão do contrato, proprietário do serviço, aceitação, exceções e risco residual; não divulgar informação identificadora.

## Referências
[FIRST CSIRT](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1) · [NIST CSF 2.0](https://www.nist.gov/cyberframework).

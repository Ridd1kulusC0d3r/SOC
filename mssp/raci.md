---
id: MSSP-02
type: mssp
level: "MSSP"
status: reference
review_cycle_days: 180
---

# MSSP-02 · Matriz RACI e pré-autorizações

## Modelo inicial, não contrato
| Ação | SOC N1 | SOC N2/IR | TI Cliente | Dono negócio |
|---|---|---|---|---|
| Triagem | R | A | I | I |
| Investigar | R | A | C | I |
| Declarar incidente | C | R | A | I |
| Contenção | I | R se autorizada | A | C |
| Restauração | I | C | R | A |
| Comunicação externa | I | C | C | A |

R = executa; A = aprova; C = consultado; I = informado. Adapte **por cliente** com preaprovações específicas, expiração, janela e contato alternativo.

## Governança e evidências
Registrar versão do contrato, proprietário do serviço, aceitação, exceções e risco residual; não divulgar informação identificadora.

## Referências
[FIRST CSIRT](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1) · [NIST CSF 2.0](https://www.nist.gov/cyberframework).

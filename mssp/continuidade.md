---
id: MSSP-07
type: mssp
level: "ARCH"
status: reference
review_cycle_days: 180
---

# MSSP-07 · Continuidade operacional SOC

## Cenários
Indisponibilidade do SIEM, case management, SOAR, rede, autenticação, cloud ou fornecedor.

## Plano mínimo
- Canal seguro alternativo e fila manual controlada de casos.
- Inventário de fontes impactadas e lacunas de visibilidade.
- Backup testado, processo de restauração e reprocessamento.
- RTO/RPO por dependência conforme risco e contrato.
- Tabletop, reconciliação e revisão pós-retorno.

## Critério de aceite
O SOC mantém comunicação e preservação mínima sem misturar dados entre clientes.

## Governança e evidências
Registrar versão do contrato, proprietário do serviço, aceitação, exceções e risco residual; não divulgar informação identificadora.

## Referências
[FIRST CSIRT](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1) · [NIST CSF 2.0](https://www.nist.gov/cyberframework).

---
id: MSSP-03
type: mssp
level: "ARCH"
status: reference
review_cycle_days: 180
---

# MSSP-03 · Segregação de clientes e threat modeling

## Princípio
A identidade de tenant acompanha evento, índice, query, correlação, case, anexo, export, automação e backup. O seletor de clientes da interface **não é fronteira de segurança**.

## Testes negativos obrigatórios
1. Conta do tenant A não enxerga eventos e cases do B.
2. Token SOAR acessa só o tenant designado.
3. Exports, storage e backups não misturam dados.
4. Logs auditáveis registram tentativa indevida.
5. Consulta sem filtro explícito falha fechada.

## Mitigações
Segredos separados, RBAC, MFA/SSO, criptografia, revisão periódica e testes de restauração.

## Governança e evidências
Registrar versão do contrato, proprietário do serviço, aceitação, exceções e risco residual; não divulgar informação identificadora.

## Referências
[FIRST CSIRT](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1) · [NIST CSF 2.0](https://www.nist.gov/cyberframework).

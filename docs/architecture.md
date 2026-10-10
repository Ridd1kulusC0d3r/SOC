# Arquitetura SOC e MSSP de referência

```mermaid
flowchart LR
  A[Identidade, endpoint, rede, cloud, OT] --> B[Collectors e APIs]
  B --> C[Validar, normalizar e associar tenant]
  C --> D[Queue, DLQ e replay]
  D --> E[SIEM / detecção]
  E --> F[Case Management]
  G[CTI] --> F
  F --> H[SOAR com aprovação]
  H --> I[Runbooks e auditoria]
  E --> J[Observabilidade]
  F --> K[SLA / QBR]
```

## Controles obrigatórios
- Identidade de tenant acompanha evento, índice, consulta, ticket, anexos, export e backup.
- Testes negativos de consulta cross-tenant. Não confiar só no seletor de clientes na UI.
- Menor privilégio, SSO/MFA, chaves segregadas, trilha de alterações, secrets manager.
- Fila de erros, retry, replay idempotente, latência end-to-end, integridade e retenção contratual.
- Mudanças disruptivas sempre dependem de aprovações do cliente e do time responsável.
- Para OT, preservar disponibilidade e segurança física; não executar scans ativos sem procedimento formal.

## Ameaças à própria plataforma
Credencial comprometida, fluxo SOAR acionando tenant errado, alteração silenciosa de regras, falta de logs, falha de parser, backup mal segregado, export indevido.

## Testes de aceite
Teste sintético por tenant; case roteado corretamente; negatividade cross-tenant; cenário de falha e retomada com gaps documentados; handover e relatório com origem verificável.

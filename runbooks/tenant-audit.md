---
id: RB-08
type: runbook
level: "MSSP"
status: reference
review_cycle_days: 180
---

# RB-08 · Testar isolamento entre tenants MSSP

## Quando usar
Onboarding, mudança de RBAC ou auditoria.

## Pré-condições
- Ambiente e versão identificados; tenant validado.
- Acesso mínimo autorizado, ticket, responsabilidade e janela de mudança.
- Evidência original preservada e processo de reversão acordado.

## Procedimento
1. **Registrar:** executor, case/change ID, fonte, horário UTC e escopo.
2. **Verificar:** No ambiente de testes, verificar consultas, exports, anexos, chaves, credenciais, workflows e backups separados por tenant.
3. **Correlacionar:** confirmar por fonte independente, sem inferir que ausência de logs é ausência de ameaça.
4. **Documentar:** registrar resultados, outputs sanitizados, erros e limitações.
5. **Escalar:** atribuir pendências a responsável habilitado.

## Critério verificável de sucesso
Usuário do tenant A não acessa nem infere dados do tenant B; teste negativo documentado.

## Falhas e reversão
Exposição constatada aciona incidente e responsável sem divulgação pública.

## Evidências geradas
Case ID, tenant, timestamp UTC, versão da ferramenta, evidência sanitizada, resultados e aprovação, se aplicável.

## Critérios para concluir
Resultado atingido ou impedimento documentado; novo responsável designado quando necessário; sem mudança não autorizada.

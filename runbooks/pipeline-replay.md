---
id: RB-10
type: runbook
level: "ARCH"
status: reference
review_cycle_days: 180
---

# RB-10 · Reprocessamento seguro de eventos

## Quando usar
Fila de eventos atrasados ou processamento interrompido.

## Pré-condições
- Ambiente e versão identificados; tenant validado.
- Acesso mínimo autorizado, ticket, responsabilidade e janela de mudança.
- Evidência original preservada e processo de reversão acordado.

## Procedimento
1. **Registrar:** executor, case/change ID, fonte, horário UTC e escopo.
2. **Verificar:** Confirmar storage original íntegro, janela, deduplicação, tenant ID e política de retenção; ensaiar replay antes de produção.
3. **Correlacionar:** confirmar por fonte independente, sem inferir que ausência de logs é ausência de ameaça.
4. **Documentar:** registrar resultados, outputs sanitizados, erros e limitações.
5. **Escalar:** atribuir pendências a responsável habilitado.

## Critério verificável de sucesso
Eventos reprocessados com integridade, sem duplicação indevida, segregação mantida e backlog explicado.

## Falhas e reversão
Não forçar replay que multiplica alertas e ações SOAR sem revisão e aprovação.

## Evidências geradas
Case ID, tenant, timestamp UTC, versão da ferramenta, evidência sanitizada, resultados e aprovação, se aplicável.

## Critérios para concluir
Resultado atingido ou impedimento documentado; novo responsável designado quando necessário; sem mudança não autorizada.

---
id: RB-03
type: runbook
level: "N2"
status: reference
review_cycle_days: 180
---

# RB-03 · Preservar evidências EVTX

## Quando usar
Investigação requer logs Windows.

## Pré-condições
- Ambiente e versão identificados; tenant validado.
- Acesso mínimo autorizado, ticket, responsabilidade e janela de mudança.
- Evidência original preservada e processo de reversão acordado.

## Procedimento
1. **Registrar:** executor, case/change ID, fonte, horário UTC e escopo.
2. **Verificar:** Confirmar autorização; exportar em ferramenta corporativa permitida; registrar máquina, fonte, timezone, intervalo e hash.
3. **Correlacionar:** confirmar por fonte independente, sem inferir que ausência de logs é ausência de ameaça.
4. **Documentar:** registrar resultados, outputs sanitizados, erros e limitações.
5. **Escalar:** atribuir pendências a responsável habilitado.

## Critério verificável de sucesso
Arquivo íntegro, metadados completos, armazenamento segregado e controle de custódia.

## Falhas e reversão
Nunca coletar fora do escopo ou enviar arquivos reais ao GitHub.

## Evidências geradas
Case ID, tenant, timestamp UTC, versão da ferramenta, evidência sanitizada, resultados e aprovação, se aplicável.

## Critérios para concluir
Resultado atingido ou impedimento documentado; novo responsável designado quando necessário; sem mudança não autorizada.

---
id: SOP-09
type: sop
level: "MSSP"
status: reference
review_cycle_days: 180
---

# SOP-09 · Onboarding de cliente MSSP

## Finalidade e gatilho
Assinatura de contrato e início de integração.

## Papéis
- **Executor:** analista responsável designado no case.
- **Aprovador:** dono do serviço/ativo conforme RACI contratual.
- **Escalonamento:** coordenador do turno; CSIRT/IR quando a evidência exigir.

## Procedimento
1. **Abrir e qualificar:** validar caso, tenant, escopo e acesso mínimo.
2. **Coletar entradas:** Conferir ativos, fontes, dados permitidos, contatos, horários, RACI, retenção, IAM e credenciais por tenant.
3. **Decidir e executar:** Verificar teste de alerta, case, consulta cross-tenant negativa, health e escalonamento.
4. **Verificar:** confirmar resultado por fonte independente e registrar lacunas.
5. **Documentar e comunicar:** registrar UTC, executor, aprovador e próximo passo.

## Evidência de conclusão
Checklist go-live assinado, riscos residuais e SLO mensurável.

## Exceções, risco e reversão
Proibido anunciar cobertura sem telemetria testada.

## Critérios de aceite
- Evidência com identificador e procedência verificáveis; timestamps UTC; decisão proporcional ao sinal.
- Responsável pela próxima etapa registrado e prazo conforme contrato, sem inventar SLA.
- Toda ação que muda o ambiente possui autorização, registro e plano de reversão.

## Referências
- [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [FIRST CSIRT](https://www.first.org/standards/frameworks/).

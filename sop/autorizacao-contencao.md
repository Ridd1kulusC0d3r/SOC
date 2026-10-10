---
id: SOP-05
type: sop
level: "N2"
status: reference
review_cycle_days: 180
---

# SOP-05 · Autorização de contenção

## Finalidade e gatilho
Ação proposta de isolamento, revogação de sessão, bloqueio ou alteração.

## Papéis
- **Executor:** analista responsável designado no case.
- **Aprovador:** dono do serviço/ativo conforme RACI contratual.
- **Escalonamento:** coordenador do turno; CSIRT/IR quando a evidência exigir.

## Procedimento
1. **Abrir e qualificar:** validar caso, tenant, escopo e acesso mínimo.
2. **Coletar entradas:** Descrever motivo, fonte, impacto operacional esperado, alternativas e risco de não agir; identificar ativo e tenant.
3. **Decidir e executar:** Consultar matriz RACI/preautorização, registrar aprovador e janela; preparar rollback e comunicação.
4. **Verificar:** confirmar resultado por fonte independente e registrar lacunas.
5. **Documentar e comunicar:** registrar UTC, executor, aprovador e próximo passo.

## Evidência de conclusão
Change/case com approval ID, executor, início/fim UTC, validação independente e reversão possível.

## Exceções, risco e reversão
Sem aprovação aplicável, escalar e preservar evidências, especialmente em OT.

## Critérios de aceite
- Evidência com identificador e procedência verificáveis; timestamps UTC; decisão proporcional ao sinal.
- Responsável pela próxima etapa registrado e prazo conforme contrato, sem inventar SLA.
- Toda ação que muda o ambiente possui autorização, registro e plano de reversão.

## Referências
- [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [FIRST CSIRT](https://www.first.org/standards/frameworks/).

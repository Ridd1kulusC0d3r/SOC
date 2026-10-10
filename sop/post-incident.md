---
id: SOP-12
type: sop
level: "N3"
status: reference
review_cycle_days: 180
---

# SOP-12 · Revisão pós-incidente

## Finalidade e gatilho
Incidente encerrado ou impacto relevante de falso positivo.

## Papéis
- **Executor:** analista responsável designado no case.
- **Aprovador:** dono do serviço/ativo conforme RACI contratual.
- **Escalonamento:** coordenador do turno; CSIRT/IR quando a evidência exigir.

## Procedimento
1. **Abrir e qualificar:** validar caso, tenant, escopo e acesso mínimo.
2. **Coletar entradas:** Comparar cronologia, dados disponíveis, comunicação, decisões e dependências que falharam.
3. **Decidir e executar:** Registrar root causes quando comprovadas; separar fatores contribuintes e hipóteses.
4. **Verificar:** confirmar resultado por fonte independente e registrar lacunas.
5. **Documentar e comunicar:** registrar UTC, executor, aprovador e próximo passo.

## Evidência de conclusão
Plano de ações com responsável, prazo, teste de eficácia e revisão do playbook.

## Exceções, risco e reversão
Tratar falhas de processo sem culpabilização pessoal.

## Critérios de aceite
- Evidência com identificador e procedência verificáveis; timestamps UTC; decisão proporcional ao sinal.
- Responsável pela próxima etapa registrado e prazo conforme contrato, sem inventar SLA.
- Toda ação que muda o ambiente possui autorização, registro e plano de reversão.

## Referências
- [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [FIRST CSIRT](https://www.first.org/standards/frameworks/).

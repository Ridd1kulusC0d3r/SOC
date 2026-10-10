---
id: SOP-11
type: sop
level: "N2"
status: reference
review_cycle_days: 180
---

# SOP-11 · Triagem de vulnerabilidades urgentes

## Finalidade e gatilho
Nova vulnerabilidade ou exploração relevante a ativos contratados.

## Papéis
- **Executor:** analista responsável designado no case.
- **Aprovador:** dono do serviço/ativo conforme RACI contratual.
- **Escalonamento:** coordenador do turno; CSIRT/IR quando a evidência exigir.

## Procedimento
1. **Abrir e qualificar:** validar caso, tenant, escopo e acesso mínimo.
2. **Coletar entradas:** Relacionar fonte oficial, inventário, versão, exposição real, criticidade e controles compensatórios.
3. **Decidir e executar:** Validar evidência de aplicabilidade; envolver TI/gestão de risco para patch, mitigação ou aceite.
4. **Verificar:** confirmar resultado por fonte independente e registrar lacunas.
5. **Documentar e comunicar:** registrar UTC, executor, aprovador e próximo passo.

## Evidência de conclusão
Plano priorizado com owner, prazo, aceite de exceções e verificação posterior.

## Exceções, risco e reversão
CVSS isolado não representa risco real sem contexto.

## Critérios de aceite
- Evidência com identificador e procedência verificáveis; timestamps UTC; decisão proporcional ao sinal.
- Responsável pela próxima etapa registrado e prazo conforme contrato, sem inventar SLA.
- Toda ação que muda o ambiente possui autorização, registro e plano de reversão.

## Referências
- [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [FIRST CSIRT](https://www.first.org/standards/frameworks/).

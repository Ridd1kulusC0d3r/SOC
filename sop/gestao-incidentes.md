---
id: SOP-04
type: sop
level: "N2"
status: reference
review_cycle_days: 180
---

# SOP-04 · Coordenação e gestão de incidentes

## Finalidade e gatilho
Critério de declaração de incidente atingido.

## Papéis
- **Executor:** analista responsável designado no case.
- **Aprovador:** dono do serviço/ativo conforme RACI contratual.
- **Escalonamento:** coordenador do turno; CSIRT/IR quando a evidência exigir.

## Procedimento
1. **Abrir e qualificar:** validar caso, tenant, escopo e acesso mínimo.
2. **Coletar entradas:** Designar incident commander, ativos/usuários, impacto confirmado, hipóteses e stakeholders; registrar autorização.
3. **Decidir e executar:** Manter timeline, decisões, evidências, comunicação e tarefas de detecção/resposta/recuperação.
4. **Verificar:** confirmar resultado por fonte independente e registrar lacunas.
5. **Documentar e comunicar:** registrar UTC, executor, aprovador e próximo passo.

## Evidência de conclusão
Encerrar após evidência de recuperação, retrospectiva, ação corretiva e aceite do responsável.

## Exceções, risco e reversão
Não misturar ações de investigação autorizadas com decisões de negócio não delegadas.

## Critérios de aceite
- Evidência com identificador e procedência verificáveis; timestamps UTC; decisão proporcional ao sinal.
- Responsável pela próxima etapa registrado e prazo conforme contrato, sem inventar SLA.
- Toda ação que muda o ambiente possui autorização, registro e plano de reversão.

## Referências
- [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [FIRST CSIRT](https://www.first.org/standards/frameworks/).

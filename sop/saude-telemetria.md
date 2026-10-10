---
id: SOP-03
type: sop
level: "N1"
status: reference
review_cycle_days: 180
---

# SOP-03 · Saúde da telemetria e ingestão

## Finalidade e gatilho
Heartbeat expirado, falha de parser, aumento de queue ou desvio de volume.

## Papéis
- **Executor:** analista responsável designado no case.
- **Aprovador:** dono do serviço/ativo conforme RACI contratual.
- **Escalonamento:** coordenador do turno; CSIRT/IR quando a evidência exigir.

## Procedimento
1. **Abrir e qualificar:** validar caso, tenant, escopo e acesso mínimo.
2. **Coletar entradas:** Confrontar último evento com baseline, diferenças de fuso e relógio, estado do agente, fila, credenciais e disponibilidade da origem.
3. **Decidir e executar:** Distinguir origem parada, transporte, atraso, parsing ou falha na visualização; testar com evento sintético autorizado.
4. **Verificar:** confirmar resultado por fonte independente e registrar lacunas.
5. **Documentar e comunicar:** registrar UTC, executor, aprovador e próximo passo.

## Evidência de conclusão
Incidente operacional com período de visibilidade afetada, owner e recuperação end-to-end.

## Exceções, risco e reversão
Ausência de logs não comprova ausência de atividade maliciosa.

## Critérios de aceite
- Evidência com identificador e procedência verificáveis; timestamps UTC; decisão proporcional ao sinal.
- Responsável pela próxima etapa registrado e prazo conforme contrato, sem inventar SLA.
- Toda ação que muda o ambiente possui autorização, registro e plano de reversão.

## Referências
- [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [FIRST CSIRT](https://www.first.org/standards/frameworks/).

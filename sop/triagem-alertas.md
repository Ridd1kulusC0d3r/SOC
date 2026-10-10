---
id: SOP-01
type: sop
level: "N1"
status: reference
review_cycle_days: 180
---

# SOP-01 · Triagem de alertas e classificação

## Finalidade e gatilho
Alerta recebido no SIEM, EDR ou canal acordado.

## Papéis
- **Executor:** analista responsável designado no case.
- **Aprovador:** dono do serviço/ativo conforme RACI contratual.
- **Escalonamento:** coordenador do turno; CSIRT/IR quando a evidência exigir.

## Procedimento
1. **Abrir e qualificar:** validar caso, tenant, escopo e acesso mínimo.
2. **Coletar entradas:** Confirmar tenant, regra disparadora, timestamps UTC, fonte, host/identidade, sensibilidade do ativo e dados ausentes.
3. **Decidir e executar:** Correlacionar sinais, anomalias e baseline; distinguir falso positivo, benign true positive, suspeito e incidente confirmado.
4. **Verificar:** confirmar resultado por fonte independente e registrar lacunas.
5. **Documentar e comunicar:** registrar UTC, executor, aprovador e próximo passo.

## Evidência de conclusão
Ticket completo com decisão reproduzível, confidence, severidade, comunicação e próximo responsável.

## Exceções, risco e reversão
Sem bloqueio ou alteração de ativos antes de verificar autoridade do cliente.

## Critérios de aceite
- Evidência com identificador e procedência verificáveis; timestamps UTC; decisão proporcional ao sinal.
- Responsável pela próxima etapa registrado e prazo conforme contrato, sem inventar SLA.
- Toda ação que muda o ambiente possui autorização, registro e plano de reversão.

## Referências
- [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [FIRST CSIRT](https://www.first.org/standards/frameworks/).

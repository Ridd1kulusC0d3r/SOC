---
id: SOP-08
type: sop
level: "MSSP"
status: reference
review_cycle_days: 180
---

# SOP-08 · Comunicação de incidentes com cliente

## Finalidade e gatilho
Alerta relevante, incidente, perda de telemetria ou violação de SLA.

## Papéis
- **Executor:** analista responsável designado no case.
- **Aprovador:** dono do serviço/ativo conforme RACI contratual.
- **Escalonamento:** coordenador do turno; CSIRT/IR quando a evidência exigir.

## Procedimento
1. **Abrir e qualificar:** validar caso, tenant, escopo e acesso mínimo.
2. **Coletar entradas:** Separar fato comprovado, hipótese, impacto, desconhecido e prazo de próxima atualização.
3. **Decidir e executar:** Usar canal, linguagem e contatos contratuais; obter confirmação quando houver autorização.
4. **Verificar:** confirmar resultado por fonte independente e registrar lacunas.
5. **Documentar e comunicar:** registrar UTC, executor, aprovador e próximo passo.

## Evidência de conclusão
Histórico de atualizações e aceite, sem especulação de atribuição.

## Exceções, risco e reversão
Não compartilhar IOCs e dados sensíveis de outros tenants.

## Critérios de aceite
- Evidência com identificador e procedência verificáveis; timestamps UTC; decisão proporcional ao sinal.
- Responsável pela próxima etapa registrado e prazo conforme contrato, sem inventar SLA.
- Toda ação que muda o ambiente possui autorização, registro e plano de reversão.

## Referências
- [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [FIRST CSIRT](https://www.first.org/standards/frameworks/).

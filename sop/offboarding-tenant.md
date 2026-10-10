---
id: SOP-10
type: sop
level: "MSSP"
status: reference
review_cycle_days: 180
---

# SOP-10 · Offboarding e revogação de acessos

## Finalidade e gatilho
Fim de contrato, migração ou desligamento de serviço.

## Papéis
- **Executor:** analista responsável designado no case.
- **Aprovador:** dono do serviço/ativo conforme RACI contratual.
- **Escalonamento:** coordenador do turno; CSIRT/IR quando a evidência exigir.

## Procedimento
1. **Abrir e qualificar:** validar caso, tenant, escopo e acesso mínimo.
2. **Coletar entradas:** Inventariar integrações, tokens, dados, evidências e obrigações legais/contratuais de retenção.
3. **Decidir e executar:** Executar revogação com log, checar acessos, exportar/devolver dados pactuados e retirar rotas.
4. **Verificar:** confirmar resultado por fonte independente e registrar lacunas.
5. **Documentar e comunicar:** registrar UTC, executor, aprovador e próximo passo.

## Evidência de conclusão
Ata de encerramento, revogações verificadas e plano de eliminação após prazo acordado.

## Exceções, risco e reversão
Não apagar evidências sob retenção obrigatória.

## Critérios de aceite
- Evidência com identificador e procedência verificáveis; timestamps UTC; decisão proporcional ao sinal.
- Responsável pela próxima etapa registrado e prazo conforme contrato, sem inventar SLA.
- Toda ação que muda o ambiente possui autorização, registro e plano de reversão.

## Referências
- [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [FIRST CSIRT](https://www.first.org/standards/frameworks/).

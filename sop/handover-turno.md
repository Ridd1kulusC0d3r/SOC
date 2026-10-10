---
id: SOP-02
type: sop
level: "N1"
status: reference
review_cycle_days: 180
---

# SOP-02 · Passagem de turno e escalonamento

## Finalidade e gatilho
Troca de plantão, mudança de responsável ou pausa de atendimento.

## Papéis
- **Executor:** analista responsável designado no case.
- **Aprovador:** dono do serviço/ativo conforme RACI contratual.
- **Escalonamento:** coordenador do turno; CSIRT/IR quando a evidência exigir.

## Procedimento
1. **Abrir e qualificar:** validar caso, tenant, escopo e acesso mínimo.
2. **Coletar entradas:** Enumerar casos abertos, impacto, dono, alertas pendentes, prazo e comunicações realizadas.
3. **Decidir e executar:** Confirmar recebimento explícito pelo próximo responsável e preservar todo o contexto no sistema de tickets.
4. **Verificar:** confirmar resultado por fonte independente e registrar lacunas.
5. **Documentar e comunicar:** registrar UTC, executor, aprovador e próximo passo.

## Evidência de conclusão
Handover com identificação de ambos, UTC, itens urgentes e contingência de plantão.

## Exceções, risco e reversão
Mensagem informal não substitui ticket e aceite do recebedor.

## Critérios de aceite
- Evidência com identificador e procedência verificáveis; timestamps UTC; decisão proporcional ao sinal.
- Responsável pela próxima etapa registrado e prazo conforme contrato, sem inventar SLA.
- Toda ação que muda o ambiente possui autorização, registro e plano de reversão.

## Referências
- [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [FIRST CSIRT](https://www.first.org/standards/frameworks/).

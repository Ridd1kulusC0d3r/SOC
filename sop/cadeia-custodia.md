---
id: SOP-07
type: sop
level: "N2"
status: reference
review_cycle_days: 180
---

# SOP-07 · Preservação de evidências e cadeia de custódia

## Finalidade e gatilho
Necessidade de prova documental de investigação autorizada.

## Papéis
- **Executor:** analista responsável designado no case.
- **Aprovador:** dono do serviço/ativo conforme RACI contratual.
- **Escalonamento:** coordenador do turno; CSIRT/IR quando a evidência exigir.

## Procedimento
1. **Abrir e qualificar:** validar caso, tenant, escopo e acesso mínimo.
2. **Coletar entradas:** Registrar autorização, origem, data UTC, ferramenta/versão, identidade coletora, método e escopo mínimo.
3. **Decidir e executar:** Transferir de forma segura; usar hash de integridade quando cabível e log de custodiantes.
4. **Verificar:** confirmar resultado por fonte independente e registrar lacunas.
5. **Documentar e comunicar:** registrar UTC, executor, aprovador e próximo passo.

## Evidência de conclusão
Artefato íntegro, custodiante, storage segregado, permissões e retenção definidas.

## Exceções, risco e reversão
Nunca incluir evidência de cliente em GitHub público.

## Critérios de aceite
- Evidência com identificador e procedência verificáveis; timestamps UTC; decisão proporcional ao sinal.
- Responsável pela próxima etapa registrado e prazo conforme contrato, sem inventar SLA.
- Toda ação que muda o ambiente possui autorização, registro e plano de reversão.

## Referências
- [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [FIRST CSIRT](https://www.first.org/standards/frameworks/).

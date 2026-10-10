---
id: SOP-06
type: sop
level: "ENG"
status: reference
review_cycle_days: 180
---

# SOP-06 · Ciclo de vida de detecções

## Finalidade e gatilho
Nova regra, tuning, alerta incorreto ou mudança de pipeline.

## Papéis
- **Executor:** analista responsável designado no case.
- **Aprovador:** dono do serviço/ativo conforme RACI contratual.
- **Escalonamento:** coordenador do turno; CSIRT/IR quando a evidência exigir.

## Procedimento
1. **Abrir e qualificar:** validar caso, tenant, escopo e acesso mínimo.
2. **Coletar entradas:** Registrar objetivo, ameaça, ATT&CK Detection Strategy, fonte e versão, owner, lógica e casos de teste.
3. **Decidir e executar:** Executar testes positivos/negativos, revisão por pares, validação de campos e ativação gradual.
4. **Verificar:** confirmar resultado por fonte independente e registrar lacunas.
5. **Documentar e comunicar:** registrar UTC, executor, aprovador e próximo passo.

## Evidência de conclusão
Regra versionada com taxa de falso positivo, risco de cobertura, rollback, revisão e métrica.

## Exceções, risco e reversão
Ter regra publicada não demonstra detecção real se fonte está ausente ou parser alterado.

## Critérios de aceite
- Evidência com identificador e procedência verificáveis; timestamps UTC; decisão proporcional ao sinal.
- Responsável pela próxima etapa registrado e prazo conforme contrato, sem inventar SLA.
- Toda ação que muda o ambiente possui autorização, registro e plano de reversão.

## Referências
- [NIST 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [FIRST CSIRT](https://www.first.org/standards/frameworks/).

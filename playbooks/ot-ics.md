---
id: PB-08
type: playbook
level: "N3"
status: reference
review_cycle_days: 180
---

# PB-08 · Anomalia em ambiente OT/ICS

## Disparo
Alerta passivo de rede industrial ou reporte do operador.

**Pré-requisitos:** case aberto, tenant validado, fontes autorizadas, matriz de contatos e autorização disponíveis.

## Triagem
1. **Validar alerta:** conferir regra, versão, evento original, escopo, janela UTC e ativos relevantes.
2. **Reunir contexto:** Consultar engenheiro OT, criticidade do processo, histórico de manutenção e registros passivos.
3. **Testar hipóteses concorrentes:** Verificar se anomalia coincide com manutenção, falha técnica ou mudança aprovada.
4. **Avaliar confiança:** registrar evidência a favor e contra; distinguir certeza de hipótese.
5. **Classificar:** falso positivo, benigno, suspeito em investigação ou incidente confirmado.

## Decisão e resposta
- **Escalonamento:** Escalar para coordenação OT/segurança física, sem executar comandos industriais.
- **Plano de ação:** propor alternativas, impacto, risco de falso positivo, responsáveis e plano de reversão.
- **Regra de segurança:** Proibidas varreduras ativas, mudança de PLC e isolamento disruptivo fora de processo aprovado.

## Evidência mínima para o ticket
| Campo | Preenchimento exigido |
|---|---|
| Case/tenant/owner | IDs internos, sem PII pública |
| Linha do tempo | timestamps UTC e fonte/ID do evento |
| Hipóteses | principal, alternativas e lacunas |
| Confiança | observação independente e ressalvas |
| Autorizações | ação, aprovador, hora, impacto e rollback |
| Fechamento | resultado, comunicação, recomendações |

## Critérios de encerramento
- Decisão baseada em fatos e registrada; impacto conhecido ou explicitamente incerto.
- Recomendação, aceite do responsável e lições aprendidas registradas.
- Indicar detecções com necessidade de ajuste e lacunas de ingestão.

## Leitura complementar
[NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [CISA Incident Response](https://www.cisa.gov/topics/cybersecurity-best-practices/executive-order-improving-nations-cybersecurity)

---
id: PB-05
type: playbook
level: "N3"
status: reference
review_cycle_days: 180
---

# PB-05 · Exfiltração suspeita de dados

## Disparo
Transferência incomum, DLP ou tráfego anômalo.

**Pré-requisitos:** case aberto, tenant validado, fontes autorizadas, matriz de contatos e autorização disponíveis.

## Triagem
1. **Validar alerta:** conferir regra, versão, evento original, escopo, janela UTC e ativos relevantes.
2. **Reunir contexto:** Analisar metadados de fluxo, volumes relativos, proxy/DNS, identidade e classificação dos dados.
3. **Testar hipóteses concorrentes:** Descartar backup, replicação ou mudança autorizada como explicação plausível.
4. **Avaliar confiança:** registrar evidência a favor e contra; distinguir certeza de hipótese.
5. **Classificar:** falso positivo, benigno, suspeito em investigação ou incidente confirmado.

## Decisão e resposta
- **Escalonamento:** Acionar IR/privacidade se transferência indevida de dados for sustentada por evidência.
- **Plano de ação:** propor alternativas, impacto, risco de falso positivo, responsáveis e plano de reversão.
- **Regra de segurança:** Minimizar coleta; não acessar conteúdo pessoal sem necessidade e base legal.

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

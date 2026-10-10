---
id: PB-06
type: playbook
level: "N2"
status: reference
review_cycle_days: 180
---

# PB-06 · Atividade IAM anômala em cloud

## Disparo
Evento auditado de alto privilégio ou credencial em risco.

**Pré-requisitos:** case aberto, tenant validado, fontes autorizadas, matriz de contatos e autorização disponíveis.

## Triagem
1. **Validar alerta:** conferir regra, versão, evento original, escopo, janela UTC e ativos relevantes.
2. **Reunir contexto:** Correlacionar principal, role/session, MFA, source, API, região, histórico e mudança aprovada.
3. **Testar hipóteses concorrentes:** Avaliar desvio real, alcance, permissões e efeitos confirmados.
4. **Avaliar confiança:** registrar evidência a favor e contra; distinguir certeza de hipótese.
5. **Classificar:** falso positivo, benigno, suspeito em investigação ou incidente confirmado.

## Decisão e resposta
- **Escalonamento:** Escalar cloud owner e IR quando privilégios sensíveis forem afetados.
- **Plano de ação:** propor alternativas, impacto, risco de falso positivo, responsáveis e plano de reversão.
- **Regra de segurança:** Rotação/revogação em ambiente do cliente depende de autoridade explícita.

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

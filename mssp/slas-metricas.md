---
id: MSSP-04
type: mssp
level: "MSSP"
status: reference
review_cycle_days: 180
---

# MSSP-04 · SLA, SLO e métricas auditáveis

## Definições inequívocas
- **MTTA:** alerta recebido/atribuído → reconhecimento; relatar cobertura contratual.
- **TTD:** evento observável → alerta, com lag de ingestão separado.
- **MTTT:** recebimento → triagem com decisão.
- **Tempo de contenção:** incidente confirmado → ação aplicada; não confundir com restauração.
- **Ingestion lag:** horário de indexação − evento, ajustando clock skew.
- **Saúde da fonte:** fontes em dia ÷ fontes contratadas.
- **False positive rate:** falsos confirmados após revisão ÷ alertas triados.
- **SLA compliance:** casos no prazo ÷ elegíveis após exclusões acordadas.

Sem numerador, denominador, janela, timezone, fonte e exceções, indicador não é auditável.

## Governança e evidências
Registrar versão do contrato, proprietário do serviço, aceitação, exceções e risco residual; não divulgar informação identificadora.

## Referências
[FIRST CSIRT](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1) · [NIST CSF 2.0](https://www.nist.gov/cyberframework).

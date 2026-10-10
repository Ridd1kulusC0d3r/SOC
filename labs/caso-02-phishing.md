# LAB-02 · E-mail suspeito

> Contas `example.test` são fictícias e não devem ser consultadas externamente.

| timestamp_utc | campo | valor |
|---|---|---|
| 2026-10-10T13:00:00Z | sender | billing@example.test |
| 2026-10-10T13:00:00Z | recipient | employee@example.test |
| 2026-10-10T13:01:00Z | gateway | delivered |
| 2026-10-10T13:03:00Z | employee | reported_suspicious |

## Missão
1. Diferencie `delivered`, `opened`, `clicked` e `session_compromised`.
2. Liste dados ausentes: proxy, IdP, gateway, dispositivo e relatórios dos destinatários.
3. Faça uma comunicação curta que não confunda suspeita com confirmação.
4. Siga [playbook de phishing](../playbooks/phishing.md) até a decisão.

**Aceite:** nenhuma inferência de credencial roubada sem evidência observável.

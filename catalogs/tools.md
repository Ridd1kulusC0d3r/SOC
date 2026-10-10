# Ferramentas curadas para SOC/MSSP

> Catálogo de avaliação, não ranking ou declaração de implantação.

| Área | Ferramenta | Projeto | Uso e cuidado |
|---|---|---|---|
| SIEM | Wazuh | [Link](https://github.com/wazuh/wazuh) | telemetria e detecção; avaliar segregação |
| Network SOC | Security Onion | [Link](https://github.com/Security-Onion-Solutions/securityonion) | observação e investigação de rede |
| SOAR | Shuffle | [Link](https://github.com/Shuffle/Shuffle) | workflows com aprovação |
| SOAR | StackStorm | [Link](https://github.com/StackStorm/st2) | orquestração por eventos |
| CTI | MISP | [Link](https://github.com/MISP/MISP) | indicadores e compartilhamento |
| CTI | OpenCTI | [Link](https://github.com/OpenCTI-Platform/opencti) | inteligência estruturada |
| Detection | SigmaHQ | [Link](https://github.com/SigmaHQ/sigma) | regras portáveis que exigem testes |
| Detection | Elastic Detection Rules | [Link](https://github.com/elastic/detection-rules) | detection-as-code |
| Detection | Splunk Security Content | [Link](https://github.com/splunk/security_content) | conteúdo de detecção |
| SIEM | Microsoft Sentinel | [Link](https://github.com/Azure/Azure-Sentinel) | exemplos de analytics |
| IR | Velociraptor | [Link](https://github.com/Velocidex/velociraptor) | coleta autorizada |
| IR | Hayabusa | [Link](https://github.com/Yamato-Security/hayabusa) | análise defensiva EVTX |
| IR | Volatility 3 | [Link](https://github.com/volatilityfoundation/volatility3) | perícia de memória legalmente obtida |
| Case | DFIR-IRIS | [Link](https://github.com/dfir-iris/iris-web) | case management; validar versão |
| NSM | Zeek | [Link](https://github.com/zeek/zeek) | telemetria de rede |
| NSM | Suricata | [Link](https://github.com/OISF/suricata) | NIDS |
| Runtime | Falco | [Link](https://github.com/falcosecurity/falco) | telemetria container |
| Schema | OCSF | [Link](https://github.com/ocsf/ocsf-schema) | normalização e interoperabilidade |

## Checklist de avaliação
- [ ] Licença, releases, manutenção, suporte e riscos da cadeia de software.
- [ ] Capacidade e custo de ingestão/retention/egress.
- [ ] RBAC, MFA, audit log, segregação de tenant e secrets.
- [ ] API, rate limit, conectores, SLO de health e controle de mudanças.
- [ ] Teste fim a fim com alertas sintéticos e recuperação de falhas.

**Atenção:** o antigo `Tools(ferramentas).md` contém referências heterogêneas de CTF/pentest e não é catálogo operacional revisado.

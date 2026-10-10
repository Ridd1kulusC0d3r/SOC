# LAB-04 · Segregação MSSP

Dois tenants inteiramente fictícios: **LAB-A** e **LAB-B**. Nenhum endpoint real.

## Requisito
Usuários do LAB-A só acessam eventos, tickets, evidências e relatórios do LAB-A. A interface não substitui a autorização do backend.

## Missão
1. Projete identificação de tenant obrigatória no pipeline e no case management.
2. Especifique testes negativos para buscas, anexos, exportações e workflows.
3. Modele falha de cache/queue que transfere case para tenant errado.
4. Crie comunicação e processo de resposta se houver exposição real.

**Aceite:** mecanismos de isolamento verificados em API, storage, automações e relatórios.

[Guia de segregação MSSP](../mssp/multitenancy.md)

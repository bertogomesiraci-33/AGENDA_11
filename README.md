# 💧 Sistema de Monitoramento de Níveis de Água - Reservatório

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Colorama](https://img.shields.io/badge/Colorama-0.4.6-green.svg)](https://pypi.org/project/colorama/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Finalizado](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)]()

> **Componente Curricular:** Desenvolvimento de Sistemas I (DS I)  
> **Instituição:** ETEC / Centro Paula Souza (CPS)  
> **Agenda:** 11 — Bibliotecas (`colorama`, `time`, `os`, `sys`) integrando Listas (Agenda 9) e Funções (Agenda 10)  
> **Estudante:** Iraci Berto Gomes  
> **Arquivo de Entrega:** `IraciBertoGomes_Ag11_DSI.py`

---

## 📌 1. Visão Geral do Projeto

Este projeto consiste em um software de **telemetria e monitoramento de reservatório de água**, desenvolvido para terminal em linguagem Python.

O código foi construído com base estrita na ementa e metodologia pedagógica ensinada nas **Apostilas de Desenvolvimento de Sistemas I (Agendas 01 a 11)** do Centro Paula Souza:

* **Agendas 02 e 03:** Variáveis primitivas, manipulação de texto e interpolação via `f-strings`.
* **Agendas 04 e 05:** Versionamento profissional com Git e GitHub.
* **Agendas 06 e 07:** Estruturas de decisão encadeadas (`if`, `elif`, `else`).
* **Agenda 08:** Estruturas de repetição com `for` e `range()`.
* **Agenda 09:** Estruturas de dados — **Listas (`[]`)**, indexação sequencial `[i]` e uso da função `len()`.
* **Agenda 10:** Modularização com **Funções com retorno (`return`)** e **Procedimentos** (Princípio da Responsabilidade Única - SRP).
* **Agenda 11:** Bibliotecas padrão (`os`, `sys`, `time`) e biblioteca externa `colorama` (`Fore`, `Style`, `Style.RESET_ALL`).

---

## 🎯 2. Tabela de Níveis, Situações e Cores da Atividade

| Nível do Reservatório | Situação Operacional | Cor Sugerida | Constante Colorama | Diagnóstico Operacional |
| :---: | :--- | :---: | :---: | :--- |
| **Nível 1** | **Muito baixo (crítico)** | **Vermelho** | `Fore.RED` | Risco iminente de desabastecimento. |
| **Nível 2** | **Baixo** | **Amarelo** | `Fore.YELLOW` | Atenção para acionamento de reposição. |
| **Nível 3** | **Médio** | **Verde** | `Fore.GREEN` | Volume ideal para operação regular. |
| **Nível 4** | **Alto** | **Ciano** | `Fore.CYAN` | Nível seguro com margem satisfatória. |
| **Nível 5** | **Muito alto (alerta)** | **Azul** | `Fore.BLUE` | Risco iminente de transbordamento. |

---

## 🏗️ 3. Estrutura Modular das Funções e Procedimentos

1. **`limpar_tela()`** *(Procedimento - Agenda 10 e 11)*: Limpa o console utilizando a biblioteca padrão `os` (`cls` no Windows / `clear` no Linux).
2. **`exibir_cabecalho()`** *(Procedimento - Agenda 10 e 11)*: Apresenta o cabeçalho estilizado com `Fore.CYAN`.
3. **`definir_cor_mensagem(nivel)`** *(Função com retorno - Agenda 10, 06 e 07)*: Recebe o nível (1 a 5) e retorna exclusivamente a cor ANSI correspondente do `colorama` via `if / elif / else`. Não executa prints, respeitando o princípio de responsabilidade única.
4. **`exibir_situacao_reservatorio(nivel, situacao)`** *(Procedimento - Agenda 10 e 11)*: Imprime a linha com a cor obtida pela função e executa imediatamente `Style.RESET_ALL`.
5. **`simular_monitoramento(lista_niveis, lista_mensagens, intervalo_segundos)`** *(Procedimento - Agenda 08, 09 e 11)*: Itera pelas listas usando `for i in range(len(lista_niveis))` e cria pausas realistas com `time.sleep()`.

---

## 💻 4. Evidência de Execução Real no Terminal

```text
=================================================================
   SISTEMA DE MONITORAMENTO DE NÍVEIS DE ÁGUA - RESERVATÓRIO
        Telemetria e Controle Automatizado em Terminal
=================================================================

Iniciando leitura e diagnóstico dos sensores em tempo real...

-----------------------------------------------------------------
>> Nível 1: Muito baixo (crítico) - Risco de desabastecimento
>> Nível 2: Baixo - Atenção para acionamento de reposição
>> Nível 3: Médio - Volume ideal para operação regular
>> Nível 4: Alto - Nível seguro com margem satisfatória
>> Nível 5: Muito alto (alerta) - Risco iminente de transbordamento
-----------------------------------------------------------------

[OK] Ciclo de monitoramento concluído com sucesso!
Estilo padrão do terminal devidamente restaurado.
```

---

## 🚀 5. Como Executar o Projeto

```bash
# Entrar no diretório
cd AGENDA_11

# Instalar dependência (Agenda 11)
pip install colorama

# Executar o programa
python IraciBertoGomes_Ag11_DSI.py
```

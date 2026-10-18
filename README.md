<div align="center">

# 🚰 Sistema de Monitoramento de Níveis de Água
### 💧 Telemetria e Controle Automatizado de Reservatório Industrial 💧

```text
       _______________________
      /                       \
     |   RESERVATÓRIO SMART    |
     |=========================|
     | [5] ############### 100%|  -> AZUL (Alerta Máximo)
     | [4] ############---  80%|  -> CIANO (Nível Alto)
     | [3] #########------  60%|  -> VERDE (Nível Médio)
     | [2] ######---------  40%|  -> AMARELO (Nível Baixo)
     | [1] ###------------  20%|  -> VERMELHO (Nível Crítico)
     |=========================|
     \_________________________/
                 | |
             [ VÁLVULA ]
```

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Colorama](https://img.shields.io/badge/Colorama-0.4.6-green.svg)](https://pypi.org/project/colorama/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Concluído](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen.svg)]()

<p><b>Componente Curricular:</b> Desenvolvimento de Sistemas I (DS I) — Agenda 11</p>
<p><b>Instituição:</b> ETEC / Centro Paula Souza (CPS) | <b>Estudante:</b> Iraci Berto Gomes</p>
<p><b>Arquivo Oficial de Entrega:</b> <code>IraciBertoGomes_Ag11_DSI.py</code></p>

</div>

---

## 📌 1. Visão Geral do Projeto

Este projeto consiste em um software de **telemetria e monitoramento de reservatório de água**, desenvolvido para execução autônoma em terminal, simulando um ambiente de automação industrial sem necessidade de intervenção do usuário.

O sistema integra os conteúdos ensinados nas **Apostilas de Desenvolvimento de Sistemas I (Agendas 01 a 11)** do Centro Paula Souza:
* **Agenda 02 e 03:** Variáveis primitivas, tipagem e exibição via `f-strings`.
* **Agenda 04 e 05:** Controle de versão profissional com Git e GitHub.
* **Agenda 06 e 07:** Estruturas de decisão encadeadas (`if`, `elif`, `else`).
* **Agenda 08:** Estruturas de repetição com `for` e `range()`.
* **Agenda 09:** Estruturas de dados — **Listas (`[]`)**, indexação sequencial `[i]` e uso da função `len()`.
* **Agenda 10:** Modularização com **Funções com retorno (`return`)** e **Procedimentos** (Princípio da Responsabilidade Única - SRP).
* **Agenda 11:** Bibliotecas padrão (`os`, `sys`, `time`, `math`, `random`) e biblioteca externa `colorama` (`Fore`, `Style`, `Style.RESET_ALL`).

---

## 🎯 2. Tabela de Níveis, Situações e Cores da Atividade

| Nível do Reservatório | Situação Operacional | Cor Sugerida | Constante Colorama | Diagnóstico Operacional |
| :---: | :--- | :---: | :---: | :--- |
| **Nível 1** | **Muito baixo (crítico)** | **Vermelho** | `Fore.RED` | Risco iminente de desabastecimento. |
| **Nível 2** | **Baixo** | **Amarelo** | `Fore.YELLOW` | Atenção para acionamento de reposição. |
| **Nível 3** | **Médio** | **Verde** | `Fore.GREEN` | Volume ideal para operação regular. |
| **Nível 4** | **Alto** | **Ciano** | `Fore.CYAN` | Nível seguro com margem satisfatória. |
| **Nível 5** | **Muito alto (alerta)** | **Azul** | `Fore.BLUE` | Risco iminente de transbordamento! |

---

## 🏗️ 3. Estrutura Modular das Funções e Bibliotecas

1. **`calcular_capacidade_reservatorio(raio, altura)`** *(Biblioteca `math` - Agenda 11)*: Calcula a cubagem e capacidade total em litros através de `math.pi` e `math.pow()`.
2. **`definir_cor_mensagem(nivel)`** *(Função com retorno - Agenda 10, 06 e 07)*: Recebe o nível (1 a 5) e retorna exclusivamente a cor ANSI correspondente do `colorama` via `if / elif / else`. Não executa prints, respeitando o princípio de responsabilidade única.
3. **`exibir_situacao_reservatorio(nivel, situacao)`** *(Procedimento - Agenda 10 e 11)*: Imprime a linha com a cor obtida pela função e executa imediatamente `Style.RESET_ALL`.
4. **`simular_ciclo_completo(lista_niveis, lista_mensagens, intervalo)`** *(Laço `for` e `listas` - Agenda 08 e 09)*: Itera pelas listas usando `for i in range(len(lista_niveis))` com pausas via `time.sleep()`.
5. **`simular_leitura_aleatoria_sensor(lista_niveis, lista_mensagens)`** *(Biblioteca `random` - Agenda 11)*: Simula a oscilação instantânea do nível de água sorteando uma medição via `random.randint()`.

---

## 💻 4. Evidência de Execução Real no Terminal

```text
====================================================================
      SISTEMA DE MONITORAMENTO DE NÍVEIS DE ÁGUA - RESERVATÓRIO
             Telemetria e Controle de Risco Operacional
====================================================================

Capacidade Total Calculada (math.pi e math.pow): 78.540 litros
--------------------------------------------------------------------

ETAPA 1: Diagnóstico Sequencial dos 5 Níveis de Água (Laço FOR e Listas)

--------------------------------------------------------------------
>> Nível 1: Muito baixo (crítico) - Risco iminente de desabastecimento
>> Nível 2: Baixo - Atenção para acionamento da captação secundária
>> Nível 3: Médio - Volume ideal para operação regular
>> Nível 4: Alto - Nível seguro com margem de abastecimento satisfatória
>> Nível 5: Muito alto (alerta) - Risco de transbordamento! Vertedouro ativado
--------------------------------------------------------------------

ETAPA 2: Teste de Telemetria Dinâmica com Sensor Aleatório (Biblioteca RANDOM)

Sensor de campo efetuou uma leitura instantânea:
>> Nível 1: Muito baixo (crítico) - Risco iminente de desabastecimento [Leitura Sorteada via Sensor]

[OK] Monitoramento concluído com sucesso!
Estilo padrão do terminal devidamente restaurado com Style.RESET_ALL.
```

---

## 🚀 5. Como Executar o Projeto

```bash
# Entrar no diretório
cd AGENDA_11

# Instalar dependência externa (Agenda 11)
pip install colorama

# Executar a simulação autônoma
python IraciBertoGomes_Ag11_DSI.py
```

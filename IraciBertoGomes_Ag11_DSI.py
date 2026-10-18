"""
=============================================================================
CURSO TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS - ETEC / CPS
Componente Curricular: Desenvolvimento de Sistemas I (DS I)
Atividade da Agenda 11: Controle de Níveis de Água no Reservatório
Estudante: Iraci Berto Gomes
Arquivo de Entrega: IraciBertoGomes_Ag11_DSI.py

CONCEITOS APLICADOS DAS APOSTILAS DO CURSO (AGENDAS 1 A 11):
- Agenda 02 e 03: Variáveis, tipos de dados primitivos e f-strings.
- Agenda 04 e 05: Versionamento do código com Git e GitHub.
- Agenda 06 e 07: Estruturas de Decisão com if, elif e else.
- Agenda 08: Estruturas de Repetição com for e range().
- Agenda 09: Estruturas de Dados - Listas ([]), índices e função len().
- Agenda 10: Funções com retorno (return) e Procedimentos (SRP).
- Agenda 11: Bibliotecas padrão (os, sys, time) e externa (colorama).
=============================================================================
"""

# ---------------------------------------------------------------------------
# AGENDA 11: IMPORTAÇÃO DE BIBLIOTECAS (Padrão e Externas)
# ---------------------------------------------------------------------------
import os               # Biblioteca padrão: interação com o sistema operacional
import sys              # Biblioteca padrão: recursos do ambiente Python
import time             # Biblioteca padrão: controle de intervalos e pausas (time.sleep)
from colorama import Fore, Style  # Biblioteca externa: cores e estilos no terminal

# Configuração de compatibilidade de codificação UTF-8 para o console Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass


# ---------------------------------------------------------------------------
# AGENDA 10: PROCEDIMENTOS DE INTERFACE E APRESENTAÇÃO (Sem retorno - None)
# ---------------------------------------------------------------------------

def limpar_tela():
    """
    Procedimento para limpar o terminal de forma multiplataforma (Agenda 10 e 11).
    Utiliza a biblioteca 'os' estudada na Agenda 11.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_cabecalho():
    """
    Procedimento que exibe o cabeçalho do sistema de monitoramento (Agenda 10).
    Aplica formatação com a biblioteca colorama (Agenda 11).
    """
    print(Style.BRIGHT + Fore.CYAN + "=" * 65)
    print("   SISTEMA DE MONITORAMENTO DE NÍVEIS DE ÁGUA - RESERVATÓRIO")
    print("        Telemetria e Controle Automatizado em Terminal")
    print("=" * 65 + Style.RESET_ALL)
    print()


# ---------------------------------------------------------------------------
# AGENDA 10 & 11: FUNÇÃO COM RETORNO PARA DEFINIR A COR (Regra da Atividade)
# ---------------------------------------------------------------------------

def definir_cor_mensagem(nivel):
    """
    Função com retorno (Agenda 10):
    Responsável estritamente por definir e retornar a cor da biblioteca colorama
    conforme o nível de água informado, seguindo a tabela de risco da Agenda 11:

    - Nível 1: Muito baixo (crítico) -> Vermelho (Fore.RED)
    - Nível 2: Baixo                -> Amarelo  (Fore.YELLOW)
    - Nível 3: Médio                -> Verde    (Fore.GREEN)
    - Nível 4: Alto                 -> Ciano    (Fore.CYAN)
    - Nível 5: Muito alto (alerta)  -> Azul     (Fore.BLUE)

    Aplica estruturas condicionais if, elif e else estudadas nas Agendas 06 e 07.
    """
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


# ---------------------------------------------------------------------------
# AGENDA 10 & 11: PROCEDIMENTO PARA EXIBIR A MENSAGEM COM COR E RESTAURAR
# ---------------------------------------------------------------------------

def exibir_situacao_reservatorio(nivel, situacao):
    """
    Procedimento que exibe a situação atual do reservatório com a cor correspondente
    e restaura imediatamente o estilo padrão do terminal (Agenda 10 e 11).

    Parâmetros:
        nivel (int): Nível de água (1 a 5).
        situacao (str): Mensagem de alerta/estado da água.
    """
    # 1. Obtém a cor através da função com retorno (Agenda 10)
    cor = definir_cor_mensagem(nivel)

    # 2. Exibe no terminal a situação com a cor correspondente (Agenda 11)
    # 3. Restaura o estilo padrão do terminal usando Style.RESET_ALL (Agenda 11)
    print(cor + Style.BRIGHT + f">> Nível {nivel}: {situacao}" + Style.RESET_ALL)


# ---------------------------------------------------------------------------
# AGENDA 08, 09, 10 & 11: PROCEDIMENTO DE SIMULAÇÃO EM TEMPO REAL
# ---------------------------------------------------------------------------

def simular_monitoramento(lista_niveis, lista_mensagens, intervalo_segundos=1):
    """
    Procedimento que percorre as listas de dados simulando um ambiente real
    de monitoramento de sensores em tempo real.

    Aplica:
    - Agenda 08: Estrutura de repetição for e função range().
    - Agenda 09: Listas, índices e a função len() para controle do percurso.
    - Agenda 11: Biblioteca time com time.sleep() para criar pausas pedagógicas.
    """
    print(Style.BRIGHT + "Iniciando leitura e diagnóstico dos sensores em tempo real...\n" + Style.RESET_ALL)
    print("-" * 65)

    # Percorre as listas pelo índice utilizando len() e range() (Agenda 08 e 09)
    for i in range(len(lista_niveis)):
        nivel_atual = lista_niveis[i]
        mensagem_atual = lista_mensagens[i]

        # Chama o procedimento de exibição colorida (Agenda 10 e 11)
        exibir_situacao_reservatorio(nivel_atual, mensagem_atual)

        # Pausa na execução com a biblioteca time (Agenda 11)
        time.sleep(intervalo_segundos)

    print("-" * 65)
    print()


# ---------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Limpa a tela do console (Agenda 10 e 11)
    limpar_tela()

    # Exibe cabeçalho formatado
    exibir_cabecalho()

    # AGENDA 09: ESTRUTURA DE DADOS - LISTAS
    # Criação de listas com nomes no plural conforme as boas práticas da Agenda 09.
    # Armazenam os 5 níveis e as 5 mensagens de situação do reservatório.
    niveis = [1, 2, 3, 4, 5]

    mensagens = [
        "Muito baixo (crítico) - Risco de desabastecimento",
        "Baixo - Atenção para acionamento de reposição",
        "Médio - Volume ideal para operação regular",
        "Alto - Nível seguro com margem satisfatória",
        "Muito alto (alerta) - Risco iminente de transbordamento"
    ]

    # AGENDA 11: Executa a simulação do ambiente real de monitoramento
    simular_monitoramento(niveis, mensagens, intervalo_segundos=1)

    # AGENDA 11: Restauração explícita final do terminal com Style.RESET_ALL
    print(Fore.GREEN + Style.BRIGHT + "[OK] Ciclo de monitoramento concluído com sucesso!" + Style.RESET_ALL)
    print("Estilo padrão do terminal devidamente restaurado.\n")

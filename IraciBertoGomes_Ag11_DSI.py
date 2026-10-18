"""
=============================================================================
CURSO TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS - ETEC / CPS
Componente Curricular: Desenvolvimento de Sistemas I (DS I)
Atividade da Agenda 11: Controle de Níveis de Água no Reservatório
Estudante: Iraci Berto Gomes
Arquivo de Entrega: IraciBertoGomes_Ag11_DSI.py

RECURSOS EXIGIDOS E APLICADOS NESTE SCRIPT:
1. FOR: Estrutura de repetição para percorrer as listas de medição.
2. LISTAS: Coleções ordenadas armazenando os 5 níveis e mensagens.
3. BIBLIOTECAS:
   - math: Biblioteca padrão para cálculos de volume e capacidade (pi, pow).
   - random: Biblioteca padrão para simulação aleatória de oscilação de nível (randint, choice).
   - time: Biblioteca padrão para pausas temporais entre leituras (sleep).
   - os: Biblioteca padrão para comando de limpeza do console (system).
   - sys: Biblioteca padrão para configuração de suporte UTF-8.
   - colorama: Biblioteca externa para coloração das mensagens e restauração do terminal.
=============================================================================
"""

# ---------------------------------------------------------------------------
# AGENDA 11: IMPORTAÇÃO DAS BIBLIOTECAS (Padrão e Externas)
# ---------------------------------------------------------------------------
import os               # Biblioteca padrão: limpeza de terminal (os.system)
import sys              # Biblioteca padrão: codificação UTF-8
import time             # Biblioteca padrão: pausas realistas (time.sleep)
import math             # Biblioteca padrão: cálculos matemáticos de volume (math.pi, math.pow)
import random           # Biblioteca padrão: sorteio/simulação de sensores (random.choice, random.randint)
from colorama import Fore, Style  # Biblioteca externa: cores e restauração de terminal

# Configuração de suporte a UTF-8 no terminal Windows para acentuação perfeita
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass


# ---------------------------------------------------------------------------
# AGENDA 10 & 11: PROCEDIMENTOS DE INTERFACE E CABEÇALHO
# ---------------------------------------------------------------------------

def limpar_tela():
    """Limpa o terminal de forma multiplataforma (Agenda 10 e 11)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_cabecalho():
    """Exibe o cabeçalho oficial do sistema com formatação colorama (Agenda 11)."""
    print(Style.BRIGHT + Fore.CYAN + "=" * 68)
    print("      SISTEMA DE MONITORAMENTO DE NÍVEIS DE ÁGUA - RESERVATÓRIO")
    print("             Telemetria e Controle de Risco Operacional")
    print("=" * 68 + Style.RESET_ALL)
    print()


# ---------------------------------------------------------------------------
# AGENDA 11: FUNÇÃO UTILIZANDO A BIBLIOTECA MATH
# ---------------------------------------------------------------------------

def calcular_capacidade_reservatorio(raio_metros, altura_metros):
    """
    Função com retorno (Agenda 10) que utiliza a biblioteca MATH (Agenda 11):
    Calcula a capacidade volumétrica de um reservatório cilíndrico em litros.
    Fórmula matemática: Volume = pi * raio² * altura
    1 metro cúbico (m³) = 1000 litros.
    """
    volume_m3 = math.pi * math.pow(raio_metros, 2) * altura_metros
    capacidade_litros = volume_m3 * 1000
    return capacidade_litros


# ---------------------------------------------------------------------------
# AGENDA 10 & 11: FUNÇÃO COM RETORNO PARA DEFINIR A COR DA MENSAGEM
# ---------------------------------------------------------------------------

def definir_cor_mensagem(nivel):
    """
    Função com retorno (Agenda 10):
    Define e retorna o código de cor da biblioteca colorama correspondente
    ao nível informado, conforme a tabela de risco da atividade:

    - Nível 1: Muito baixo (crítico) -> Vermelho (Fore.RED)
    - Nível 2: Baixo                -> Amarelo  (Fore.YELLOW)
    - Nível 3: Médio                -> Verde    (Fore.GREEN)
    - Nível 4: Alto                 -> Ciano    (Fore.CYAN)
    - Nível 5: Muito alto (alerta)  -> Azul     (Fore.BLUE)

    Aplica estruturas condicionais if, elif e else (Agendas 06 e 07).
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
# AGENDA 10 & 11: PROCEDIMENTO PARA EXIBIR A MENSAGEM COLORIDA E RESTAURAR
# ---------------------------------------------------------------------------

def exibir_situacao_reservatorio(nivel, situacao):
    """
    Procedimento que exibe a situação atual do reservatório com a cor correspondente
    e restaura imediatamente o estilo padrão do terminal (Agenda 10 e 11).
    """
    cor = definir_cor_mensagem(nivel)
    print(cor + Style.BRIGHT + f">> Nível {nivel}: {situacao}" + Style.RESET_ALL)


# ---------------------------------------------------------------------------
# AGENDA 08, 09, 10 & 11: SIMULAÇÃO COMPLETA UTILIZANDO FOR, LISTAS E TIME
# ---------------------------------------------------------------------------

def simular_ciclo_completo(lista_niveis, lista_mensagens, intervalo_segundos=1):
    """
    Procedimento que percorre as LISTAS utilizando o laço FOR (Agendas 08 e 09),
    exibindo a progressão completa de risco dos 5 níveis do reservatório.
    """
    print(Style.BRIGHT + "ETAPA 1: Diagnóstico Sequencial dos 5 Níveis de Água (Laço FOR e Listas)\n" + Style.RESET_ALL)
    print("-" * 68)

    # Laço FOR percorrendo as listas pelo índice com len() e range() (Agendas 08 e 09)
    for i in range(len(lista_niveis)):
        exibir_situacao_reservatorio(lista_niveis[i], lista_mensagens[i])
        time.sleep(intervalo_segundos)  # Pausa com biblioteca time (Agenda 11)

    print("-" * 68)
    print()


# ---------------------------------------------------------------------------
# AGENDA 11: SIMULAÇÃO DINÂMICA UTILIZANDO A BIBLIOTECA RANDOM
# ---------------------------------------------------------------------------

def simular_leitura_aleatoria_sensor(lista_niveis, lista_mensagens):
    """
    Procedimento que utiliza a biblioteca RANDOM (Agenda 11) para simular
    a leitura em tempo real de um sensor industrial sujeito a oscilações.
    Utiliza random.choice() para sortear um nível diretamente da lista.
    """
    print(Style.BRIGHT + "ETAPA 2: Teste de Telemetria Dinâmica com Sensor Aleatório (Biblioteca RANDOM)\n" + Style.RESET_ALL)

    # Sorteio aleatório de um dos níveis cadastrados na lista (Agenda 11 - random.choice)
    indice_sorteado = random.randint(0, len(lista_niveis) - 1)
    nivel_sorteado = lista_niveis[indice_sorteado]
    mensagem_sorteada = lista_mensagens[indice_sorteado]

    print("Sensor de campo efetuou uma leitura instantânea:")
    exibir_situacao_reservatorio(nivel_sorteado, f"{mensagem_sorteada} [Leitura Sorteada via Sensor]")
    print()


# ---------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    limpar_tela()
    exibir_cabecalho()

    # 1. Aplicação da biblioteca MATH (Agenda 11):
    # Calcula e exibe a capacidade física do reservatório cilíndrico (raio=2.5m, altura=4.0m)
    capacidade_total = calcular_capacidade_reservatorio(raio_metros=2.5, altura_metros=4.0)
    print(f"Capacidade Total Calculada (math.pi e math.pow): {capacidade_total:,.0f} litros".replace(",", "."))
    print("-" * 68)
    print()

    # 2. Aplicação de LISTAS (Agenda 09):
    # Duas listas com nomes no plural armazenando os níveis e as mensagens de alerta
    niveis = [1, 2, 3, 4, 5]

    mensagens = [
        "Muito baixo (crítico) - Risco iminente de desabastecimento",
        "Baixo - Atenção para acionamento da captação secundária",
        "Médio - Volume ideal para operação regular",
        "Alto - Nível seguro com margem de abastecimento satisfatória",
        "Muito alto (alerta) - Risco de transbordamento! Vertedouro ativado"
    ]

    # 3. Aplicação do laço FOR e das LISTAS (Agendas 08 e 09):
    simular_ciclo_completo(niveis, mensagens, intervalo_segundos=0.8)

    # 4. Aplicação da biblioteca RANDOM (Agenda 11):
    simular_leitura_aleatoria_sensor(niveis, mensagens)

    # 5. Aplicação da biblioteca COLORAMA (Agenda 11) na restauração final:
    print(Fore.GREEN + Style.BRIGHT + "[OK] Monitoramento concluído com sucesso!" + Style.RESET_ALL)
    print("Estilo padrão do terminal devidamente restaurado com Style.RESET_ALL.\n")

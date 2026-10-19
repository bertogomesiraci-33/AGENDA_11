"""
Sistema de Monitoramento de Níveis de Água no Reservatório
Telemetria e Controle de Risco Operacional
"""
import os
import sys
import time
import math
import random
from colorama import Fore, Style, init

# Configuração UTF-8 e inicialização do Colorama
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
init(autoreset=True)

# Lista de cores correspondente aos níveis de 1 a 5
cores_niveis = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]


def limpar_tela():
    """Limpa o console do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_cabecalho():
    """Exibe o cabeçalho formatado do sistema."""
    print(Style.BRIGHT + Fore.CYAN + "=" * 68)
    print(" SISTEMA DE MONITORAMENTO DE NÍVEIS DE ÁGUA - RESERVATÓRIO")
    print(" Telemetria e Controle de Risco Operacional")
    print("=" * 68 + Style.RESET_ALL + "\n")


def calcular_capacidade_reservatorio(raio_m, altura_m):
    """Calcula capacidade em litros usando math.pi e math.pow (1 m³ = 1000L)."""
    return math.pi * math.pow(raio_m, 2) * altura_m * 1000


def definir_cor_mensagem(nivel):
    """Retorna a cor do nível a partir da lista de cores ordenadas."""
    if 1 <= nivel <= len(cores_niveis):
        return cores_niveis[nivel - 1]
    return Fore.WHITE


def exibir_situacao_reservatorio(nivel, situacao):
    """Exibe a situação do reservatório com a respectiva cor."""
    cor = definir_cor_mensagem(nivel)
    print(cor + Style.BRIGHT + f">> Nível {nivel}: {situacao}" + Style.RESET_ALL)


def simular_ciclo_completo(lista_niveis, lista_mensagens, intervalo=0.8):
    """Percorre sequencialmente os níveis e alertas através do laço for."""
    print(Style.BRIGHT + "ETAPA 1: Diagnóstico Sequencial dos 5 Níveis de Água (Laço FOR e Listas)\n" + Style.RESET_ALL)
    print("-" * 68)
    for i in range(len(lista_niveis)):
        exibir_situacao_reservatorio(lista_niveis[i], lista_mensagens[i])
        time.sleep(intervalo)
    print("-" * 68 + "\n")


def simular_leitura_aleatoria_sensor(lista_niveis, lista_mensagens):
    """Simula leitura instantânea oscilatória através de sorteio aleatório."""
    print(Style.BRIGHT + "ETAPA 2: Teste de Telemetria Dinâmica com Sensor Aleatório (Biblioteca RANDOM)\n" + Style.RESET_ALL)
    i = random.randint(0, len(lista_niveis) - 1)
    print("Sensor de campo efetuou uma leitura instantânea:")
    exibir_situacao_reservatorio(lista_niveis[i], f"{lista_mensagens[i]} [Leitura Sorteada via Sensor]\n")


if __name__ == "__main__":
    limpar_tela()
    exibir_cabecalho()
    # Cálculo da capacidade do reservatório cilíndrico (raio=2.5m, altura=4.0m)
    capacidade = calcular_capacidade_reservatorio(raio_m=2.5, altura_m=4.0)
    print(f"Capacidade Total Calculada (math.pi e math.pow): {capacidade:,.0f} litros".replace(",", "."))
    print("-" * 68 + "\n")
    # Listas de telemetria
    niveis = [1, 2, 3, 4, 5]
    mensagens = [
        "Muito baixo (crítico) - Risco iminente de desabastecimento",
        "Baixo - Atenção para acionamento da captação secundária",
        "Médio - Volume ideal para operação regular",
        "Alto - Nível seguro com margem de abastecimento satisfatória",
        "Muito alto (alerta) - Risco de transbordamento! Vertedouro ativado"
    ]
    # Simulações
    simular_ciclo_completo(niveis, mensagens, intervalo=0.8)
    simular_leitura_aleatoria_sensor(niveis, mensagens)
    # Conclusão
    print(Fore.GREEN + Style.BRIGHT + "[OK] Monitoramento concluído com sucesso!" + Style.RESET_ALL)
    print("Estilo padrão do terminal devidamente restaurado com Style.RESET_ALL.\n")

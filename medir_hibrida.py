import time
import random
import csv
import matplotlib.pyplot as plt
from ordenacao_hibrida import ordenacao_rapida, ordenacao_hibrida

TAMANHO = 20000
CORTES = [1, 5, 10, 16, 20, 32, 50, 100, 200]
REPETICOES = 10

def executar_medicoes():
    dados = []
    t_rapida_total = 0
    
    for _ in range(REPETICOES):
        lista_base = [random.randint(-100000, 100000) for _ in range(TAMANHO)]
        inicio = time.perf_counter()
        _ = ordenacao_rapida(lista_base)
        t_rapida_total += time.perf_counter() - inicio
        
    tempo_rapida = t_rapida_total / REPETICOES

    for corte in CORTES:
        t_hibrida_total = 0
        for _ in range(REPETICOES):
            lista_base = [random.randint(-100000, 100000) for _ in range(TAMANHO)]
            inicio = time.perf_counter()
            _ = ordenacao_hibrida(lista_base, corte)
            t_hibrida_total += time.perf_counter() - inicio
            
        dados.append({
            "corte": corte,
            "tempo_hibrida": t_hibrida_total / REPETICOES,
            "tempo_rapida": tempo_rapida
        })

    return dados

def salvar_csv(dados):
    with open("dados_hibrida.csv", "w", newline="", encoding="utf-8") as f:
        campos = ["corte", "tempo_hibrida", "tempo_rapida"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados)

def gerar_grafico(dados):
    cortes = [d["corte"] for d in dados]
    t_hibrida = [d["tempo_hibrida"] for d in dados]
    t_rapida = [d["tempo_rapida"] for d in dados]

    plt.figure(figsize=(9, 5))
    plt.plot(cortes, t_hibrida, marker="o", label="Híbrida (Quick + Insertion)")
    plt.axhline(y=t_rapida[0], color="r", linestyle="--", label="Rápida Pura (Quick)")
    plt.title("Tempo de Execução vs Tamanho do Corte (N = 20.000)")
    plt.xlabel("Tamanho do Corte")
    plt.ylabel("Tempo Médio (segundos)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig("grafico_corte.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    resultados = executar_medicoes()
    salvar_csv(resultados)
    gerar_grafico(resultados)
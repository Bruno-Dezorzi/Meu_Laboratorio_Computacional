from math import sqrt
import matplotlib.pyplot as plt


# Calcula estatísticas descritivas dos dados.
# Serve para resumir os dados e medir sua variabilidade.
def estatisticas(periodos, mostrar: bool = False):
    qtd_dados: int = len(periodos)
    sum_dados: float = sum(periodos)
    avg_dados: float = sum_dados / qtd_dados
    min_dados: float = min(periodos)
    max_dados: float = max(periodos)
    amplitude_dados: float = max_dados - min_dados

    # Diferença entre cada medida e a média.
    # Mostra quanto cada medida se afasta do valor médio.
    desvios: list[float] = [x - avg_dados for x in periodos]

    sum_desvios = sum(desvios)
    avg_desvios = sum_desvios / len(desvios)

    # Usa o módulo dos desvios para evitar que valores positivos
    # e negativos se cancelem.
    desvios_absolutos: list[float] = [abs(x) for x in desvios]

    sum_desvios_absolutos = sum(desvios_absolutos)
    avg_desvios_absolutos = sum_desvios_absolutos / len(desvios_absolutos)

    # Eleva os desvios ao quadrado, dando mais peso a desvios maiores.
    desvios_quadrados = [d**2 for d in desvios]

    sum_desvios_quadrados = sum(desvios_quadrados)

    # Média dos desvios quadrados = variância.
    # Aqui estamos usando N como denominador.
    avg_desvios_quadrados = sum_desvios_quadrados / len(desvios_quadrados)

    # Raiz da variância = desvio padrão.
    # Mede a dispersão típica dos dados em relação à média.
    desvio_padrao = sqrt(avg_desvios_quadrados)

    if mostrar:
        print(f"A quantidade dos dados é de {qtd_dados}")
        print(f"A soma dos dados é de {sum_dados}")
        print(f"A média dos dados é de {avg_dados}")
        print(f"O mínimo dos dados é de {min_dados}")
        print(f"O máximo dos dados é de {max_dados}")
        print(f"A amplitude dos dados é de {amplitude_dados:.2f}")

        print(
            "-------------------------------------------------------------------------------"
        )

        print(f"A soma dos desvios é de {sum_desvios:.2f}")
        print(f"A média dos desvios é de {avg_desvios:.2f}")

        print(
            "-------------------------------------------------------------------------------"
        )

        print("n | xᵢ | x̄ | d_n")
        for i in range(len(periodos)):
            print(f"{i} | {periodos[i]:.2f} | {avg_dados:.2f} | {desvios[i]:+.2f}")

        print(f"A soma dos desvios absolutos é de {sum_desvios_absolutos:.2f}")
        print(f"A média dos desvios absolutos é de {avg_desvios_absolutos:.2f}")

        print("n | xᵢ | x̄ | |d_n|")
        for i in range(len(periodos)):
            print(
                f"{i} | {periodos[i]:.2f} | "
                f"{avg_dados:.2f} | {desvios_absolutos[i]:+.2f}"
            )

        print(
            "-------------------------------------------------------------------------------"
        )

        print(f"A soma dos desvios quadrados é de {sum_desvios_quadrados:.2f}")

        print(
            f"A média dos desvios quadrados (VARIÂNCIA) "
            f"é de {avg_desvios_quadrados:.6f} s²"
        )

        print("n | xᵢ | x̄ | d_n²")
        for i in range(len(periodos)):
            print(
                f"{i} | {periodos[i]:.2f} | "
                f"{avg_dados:.2f} | {desvios_quadrados[i]:+.2f}"
            )

        print(
            "-------------------------------------------------------------------------------"
        )

        print(f"Desvio padrão de {desvio_padrao}")

    return avg_dados, desvio_padrao


# Gráfico das medições.
# Permite visualizar a dispersão dos dados e compará-los
# com a média, o desvio padrão e o valor teórico.
def visualizacao_scatter(periodos, media, desvio_padrao, periodo_teorico):

    qtd_dados: int = len(periodos)
    medicoes: int = range(1, qtd_dados + 1)

    plt.scatter(medicoes, periodos)
    plt.axhline((media + desvio_padrao), color="red", label="Média+DP")
    plt.axhline(media, color="green", label="Média")
    plt.axhline(periodo_teorico, color="purple", label="Teórico")
    plt.axhline((media - desvio_padrao), color="blue", label="Média-DP")

    plt.xlabel("Medições")
    plt.ylabel("Período (s)")
    plt.legend()
    plt.tight_layout()
    plt.grid()
    plt.show()


# Histograma dos dados.
# Mostra como as medições estão distribuídas em diferentes faixas de valores.
def histograma(periodos):
    plt.hist(periodos)
    plt.xlabel("Período (s)")
    plt.ylabel("Frequência")
    plt.tight_layout()
    plt.grid()
    plt.show()


# Executa a análise dos conjuntos de medições.
# Compara a média experimental com um valor teórico.
def analise(periodos_de_teste, periodo_teorico):
    for periodo in periodos_de_teste:

        media, desvio_padrao = estatisticas(periodos=periodo)

        # Diferença entre o valor experimental e o valor teórico.
        discrepancia = media - periodo_teorico

        # Magnitude da discrepância, ignorando o sinal.
        discrepancia_absoluta = abs(discrepancia)

        # Compara a discrepância com o valor teórico.
        erro_relativo = discrepancia_absoluta / abs(periodo_teorico)

        # Expressa o erro relativo em porcentagem.
        erro_relativo_percentual = erro_relativo * 100

        print(
            "-------------------------------------------------------------------------------"
        )
        print(f"Média dos períodos: {media:.2f} s")
        print(f"Desvio padrão dos períodos: {desvio_padrao:.2f} s")
        print(f"Período teórico: {periodo_teorico:.2f} s")
        print(f"Discrepância em relação ao valor teórico: {discrepancia:.6f} s")
        print(f"Discrepância absoluta: {discrepancia_absoluta:.6f} s")
        print(f"Erro relativo: {erro_relativo:.2f}")
        print(f"Erro relativo percentual: {erro_relativo_percentual:.2f} %")

        print(
            "-------------------------------------------------------------------------------"
        )

        visualizacao_scatter(
            periodos=periodo,
            media=media,
            desvio_padrao=desvio_padrao,
            periodo_teorico=periodo_teorico,
        )

        histograma(periodos=periodo)


# Calcula os coeficientes da reta y = ax + b.
# Serve para encontrar uma relação linear que represente os dados.
def regressao_linear(x: list, y: list, mostrar: bool = False):

    media_x = sum(x) / len(x)
    media_y = sum(y) / len(y)

    a_numerador: float = 0
    a_denominador: float = 0

    # Calcula os termos necessários para encontrar a inclinação.
    for i in range(len(x)):
        a_numerador += (x[i] - media_x) * (y[i] - media_y)
        a_denominador += (x[i] - media_x) ** 2

    # a = inclinação da reta.
    # b = valor previsto de y quando x = 0.
    a = a_numerador / a_denominador
    b = media_y - a * media_x

    if mostrar:
        print(f"a = {a:.2f}")
        print(f"b = {b:.2f}")

    return a, b


# Mostra os dados experimentais junto com a reta ajustada.
def visualizar_xy(x, y, a, b):

    # Calcula os valores previstos pelo modelo.
    y_reta = [a * i + b for i in x]

    plt.scatter(x, y)
    plt.plot(x, y_reta)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.tight_layout()
    plt.show()


# Calcula os resíduos do modelo.
# Resíduo = valor observado - valor previsto.
# Serve para verificar onde o modelo erra em cada ponto.
def residuos(x, y, a, b):

    y_reta = [a * i + b for i in x]

    return [y[i] - y_reta[i] for i in range(len(y))]


# Mostra os resíduos em relação a x.
# Resíduos próximos de zero e sem padrão sistemático
# indicam que o modelo pode representar adequadamente os dados.
def visualizar_residuos(x, r):

    plt.scatter(x, r)
    plt.axhline(0)

    plt.xlabel("x")
    plt.ylabel("Resíduo")

    plt.grid()
    plt.tight_layout()
    plt.show()


# Calcula o MSE (Mean Squared Error).
# É a média dos resíduos elevados ao quadrado.
# Mede o erro médio do modelo, dando mais peso a erros maiores.
def erro_quadratico_medio(residuos, mostrar=False):

    soma = sum(r**2 for r in residuos)
    mse = soma / len(residuos)

    if mostrar:
        print(f"MSE = {mse:.6f}")

    return mse


# Calcula o RMSE (Root Mean Squared Error).
# É a raiz quadrada do MSE.
# Permite interpretar o erro na mesma unidade de y.
def raiz_erro_quadratico_medio(residuos, mostrar=False):

    mse = erro_quadratico_medio(residuos)
    rmse = sqrt(mse)

    if mostrar:
        print(f"RMSE = {rmse:.6f}")

    return rmse


def main():

    # Dados experimentais usados na análise estatística.
    periodos_01 = [
        2.01, 1.98, 2.03, 2.00, 1.97,
        2.02, 1.99, 2.04, 2.00, 1.96
    ]

    periodos_02 = [
        2.08, 2.05, 2.07, 2.06, 2.09,
        2.04, 2.07, 2.06, 2.05, 2.08
    ]

    periodo_teorico = 2.00
    periodos_de_teste = [periodos_01, periodos_02]

    # Análise estatística dos períodos.
    # analise(
    #     periodos_de_teste=periodos_de_teste,
    #     periodo_teorico=periodo_teorico
    # )

    # Dados usados para testar a regressão linear.
    x = [1, 2, 3, 4, 5]
    y = [2.1, 4.0, 6.2, 7.9, 10.1]

    # Encontra a reta que melhor representa os dados.
    a, b = regressao_linear(x, y)

    # Visualiza os dados e o modelo linear.
    # visualizar_xy(x, y, a, b)

    # Calcula a diferença entre os valores observados
    # e os valores previstos pela reta.
    r = residuos(x, y, a, b)

    # Visualiza os resíduos.
    # visualizar_residuos(x, r)

    # Mede quantitativamente o erro do modelo.
    mse = erro_quadratico_medio(r)
    rmse = raiz_erro_quadratico_medio(r)

    # Resumo final do modelo.
    print("==============================================")
    print("           RESUMO DO MODELO LINEAR")
    print("==============================================")
    print(f"Equação: y = {a:.3f}x + {b:.3f}")
    print(f"Inclinação (a): {a:.3f}")
    print(f"Intercepto (b): {b:.3f}")
    print(f"MSE: {mse:.6f}")
    print(f"RMSE: {rmse:.6f}")
    print("==============================================")


if __name__ == "__main__":
    main()

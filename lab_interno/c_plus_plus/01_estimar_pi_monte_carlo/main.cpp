#include <iostream>
#include <random>
#include <vector>
#include <cmath>
#include <format>
#include <chrono>
#include <numeric>

/*
    Monte Carlo para estimar PI.

    Um círculo de raio R está inscrito em um quadrado de lado 2R:

        Área círculo  = PI * R²
        Área quadrado = 4 * R²

    Como os pontos são distribuídos uniformemente:

        Ni / N ≈ PI / 4

    Portanto:

        PI ≈ 4 * Ni / N

    O método é estocástico. O erro estatístico típico
    decresce aproximadamente como 1 / sqrt(N).
*/
double number_pi(std::mt19937 &gerador,
                 std::uniform_real_distribution<double> &distribuidor,
                 int pontos_total,
                 double radius_circle)
{
    int Ni = 0;
    double radius_sq = radius_circle * radius_circle;

    for (int i = 0; i < pontos_total; i++)
    {
        // Ponto sorteado uniformemente dentro do quadrado [-R, R].
        double x = distribuidor(gerador);
        double y = distribuidor(gerador);

        // Equação da região interna do círculo: x² + y² <= R².
        if (x * x + y * y <= radius_sq)
        {
            Ni += 1;
        }
    }

    // Estimativa: PI ≈ 4 * (Ni / N).
    // 4.0 garante divisão em ponto flutuante.
    return 4.0 * Ni / pontos_total;
}

int main()
{
    double radius_circle = 2.0;

    // Semente para o gerador pseudoaleatório.
    std::random_device rd;

    // Mersenne Twister: gerador pseudoaleatório utilizado no experimento.
    std::mt19937 gen(rd());

    // Distribuição uniforme das coordenadas no quadrado [-R, R].
    std::uniform_real_distribution<double> distrib(
        -radius_circle, radius_circle);

    // Valor conhecido usado apenas para calcular o erro da estimativa.
    const double PI_REFERENCE = 3.141592653589793;

    // Quantidades de pontos utilizadas nos experimentos.
    std::vector<int> nt = {1000, 10000, 100000, 1000000};

    // Resultados das repetições para cada N.
    std::vector<double> pis;
    std::vector<double> erros;
    std::vector<double> tempos;

    double pi = 0.0;

    // Repetições permitem observar melhor o comportamento estatístico.
    int repeticoes = 10;

    std::cout << "Valor de PI como referencia: "
              << PI_REFERENCE << std::endl;

    std::cout << std::format(
        "{:<12} {:<20} {:<20} {:<20} {:<12}\n",
        "N",
        "PI Medio estimado",
        "Erro Medio",
        "1/raizN",
        "Tempo Medio");

    // Cada N representa uma escala diferente de custo computacional.
    for (size_t i = 0; i < nt.size(); i++)
    {
        for (size_t j = 0; j < repeticoes; j++)
        {
            // Mede somente o custo da execução do Monte Carlo.
            auto start = std::chrono::high_resolution_clock::now();

            pi = number_pi(gen, distrib, nt[i], radius_circle);

            auto end = std::chrono::high_resolution_clock::now();

            pis.push_back(pi);

            // Erro absoluto em relação ao valor de referência.
            erros.push_back(std::abs(pi - PI_REFERENCE));

            std::chrono::duration<double> elapsed = end - start;
            tempos.push_back(elapsed.count());
        }

        // Média das 10 estimativas.
        double pi_medio_estimado =
            std::accumulate(pis.begin(), pis.end(), 0.0) / static_cast<double>(repeticoes);

        // Média dos erros absolutos das 10 execuções.
        double erro_medio =
            std::accumulate(erros.begin(), erros.end(), 0.0) / static_cast<double>(repeticoes);

        // Média dos tempos de execução.
        double tempos_medio =
            std::accumulate(tempos.begin(), tempos.end(), 0.0) / static_cast<double>(repeticoes);

        /*
            Escala teórica do erro de Monte Carlo:

                erro ~ 1 / sqrt(N)

            Não é o erro exato, mas a escala estatística esperada.
        */
        double escala_monte_carlo =
            1.0 / std::sqrt(static_cast<double>(nt[i]));

        std::cout << std::format(
            "{:<12} {:<20.6f} {:<20.6e} {:<20.6e} {:<12.6e}\n",
            nt[i],
            pi_medio_estimado,
            erro_medio,
            escala_monte_carlo,
            tempos_medio);

        // Limpa os resultados antes de iniciar o próximo N.
        pis.clear();
        erros.clear();
        tempos.clear();
    }
}
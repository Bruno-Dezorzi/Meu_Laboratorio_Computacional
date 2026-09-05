# Guia — experimentos.md

## Finalidade

Este documento registra **o que foi testado e em que condições**, antes
de saber o resultado. É o "protocolo experimental" do projeto: define
pergunta, parâmetros e método de cada rodada de testes.

## Diferença entre experimentos.md e resultados.md

- **`experimentos.md`** descreve o *plano*: o que você está testando, com
  quais parâmetros e condições, e o que você espera encontrar.
- **`resultados.md`** descreve o *desfecho*: o que de fato aconteceu,
  com números, gráficos e interpretação física.

Pense em `experimentos.md` como o "antes" e `resultados.md` como o
"depois". Um experimento pode (e deve) ser escrito antes de rodar o
código — isso ajuda a definir claramente o que está sendo testado.

## O que escrever em cada experimento

- Pergunta experimental (o que especificamente está sendo testado?).
- Parâmetros utilizados.
- Condições iniciais.
- Método (qual algoritmo/configuração está sendo usado).
- Hipótese (o que você espera encontrar, e por quê).
- Configuração utilizada (passo de tempo, número de amostras, semente
  aleatória, versão do código, etc. — o que for necessário para
  reproduzir).

## Perguntas que cada experimento deve responder

- O que especificamente estou testando?
- Quais parâmetros estou variando e quais estou mantendo fixos?
- Quais são as condições iniciais?
- Que método estou usando?
- O que eu espero encontrar, e por quê?
- Essa configuração é suficiente para alguém (ou eu mesmo, depois)
  reproduzir o experimento?

## Exemplo genérico

```markdown
## Experimento 1 — Efeito do amortecimento no período

**Pergunta experimental:** como o período de oscilação do pêndulo varia
com o coeficiente de amortecimento $b$?

**Parâmetros:** $L = 1$ m, $g = 9.81$ m/s², $\theta_0 = 15°$,
$b \in \{0, 0.1, 0.5, 1.0\}$ kg/s.

**Condições iniciais:** $\theta(0) = \theta_0$, $\omega(0) = 0$.

**Método:** integração RK4, $\Delta t = 0.001$ s, $T = 20$ s.

**Hipótese:** o período deve aumentar levemente com $b$, e a amplitude
deve decair exponencialmente.

**Configuração utilizada:** `src/main.py`, commit `abc1234`.
```

```markdown
## Experimento 2 — Convergência do Monte Carlo

**Pergunta experimental:** quantas amostras $N$ são necessárias para o
erro da estimativa cair abaixo de 1%?

**Parâmetros:** $N \in \{10^2, 10^3, 10^4, 10^5, 10^6\}$, 20 repetições
por valor de $N$.

**Método:** Monte Carlo simples com amostragem uniforme.

**Hipótese:** o erro deve decair proporcionalmente a $1/\sqrt{N}$.
```

## Quando usar

Sempre que uma rodada de testes tiver um objetivo específico e parâmetros
bem definidos — não é necessário um experimento formal para cada execução
exploratória do código enquanto ele ainda está sendo debugado.

## Quando não é necessário se aprofundar

Durante a fase de "fazer funcionar" (ver PRINCIPIOS.md), testes
exploratórios podem ficar só no diário. Reserve `experimentos.md` para
quando o código já está validado e você está investigando o
comportamento físico do sistema de forma sistemática.

# Guia — algoritmo.md

## Finalidade

Este documento traduz o modelo matemático (`teoria.md`) em uma sequência
de passos computacionais, **antes** de escrever código. É o espaço para
pensar em "como resolver isso" sem ainda se preocupar com sintaxe,
classes ou organização de arquivos.

## O que escrever

- A ideia geral do método (em uma ou duas frases).
- Entradas (parâmetros, condições iniciais) e saídas (o que o código
  produz: números, arrays, gráficos).
- Os passos do algoritmo, em pseudocódigo ou lista numerada.
- O método numérico escolhido e por que ele foi escolhido.
- Critérios de parada, passo de tempo/espaço, tolerâncias, se aplicável.

## Perguntas que este documento deve responder

- Dado o modelo matemático, quais são os passos computacionais para
  resolvê-lo?
- Quais são as entradas e quais são as saídas?
- Que método numérico estou usando (Euler, Runge-Kutta, Monte Carlo,
  diferenças finitas, etc.) e por quê?
- Qual é o critério de parada ou convergência?
- Existe algum caso simples em que eu já sei qual deveria ser o
  resultado, para conferir depois?

## Exemplo genérico (integração de EDO)

```markdown
## Ideia geral

Integrar numericamente o sistema de equações diferenciais do pêndulo
amortecido usando Runge-Kutta de 4ª ordem (RK4).

## Entradas e saídas

**Entradas:** ângulo inicial $\theta_0$, velocidade angular inicial
$\omega_0$, coeficiente de amortecimento $b$, passo de tempo $\Delta t$,
tempo total $T$.

**Saídas:** arrays de tempo, ângulo e velocidade angular ao longo da
simulação.

## Passos

1. Definir o estado do sistema como o vetor $(\theta, \omega)$.
2. Escrever a função que calcula as derivadas $(\dot\theta, \dot\omega)$
   a partir do estado atual.
3. Inicializar o estado com $(\theta_0, \omega_0)$.
4. Para cada passo de tempo, aplicar o método RK4 para avançar o estado.
5. Armazenar o estado a cada passo.
6. Repetir até atingir o tempo total $T$.

## Método numérico utilizado

Runge-Kutta de 4ª ordem, por ter boa precisão para passos de tempo
moderados sem exigir passo adaptativo, adequado para uma primeira versão.
```

## Exemplo genérico (Monte Carlo)

```markdown
## Ideia geral

Estimar a integral de uma função por amostragem aleatória uniforme
(Monte Carlo simples).

## Passos

1. Definir o domínio de integração.
2. Gerar $N$ pontos aleatórios uniformemente distribuídos no domínio.
3. Avaliar a função em cada ponto.
4. Multiplicar a média dos valores pelo volume do domínio.
5. Repetir para diferentes valores de $N$ e observar a convergência.

## Método numérico utilizado

Monte Carlo simples (amostragem uniforme), por ser o ponto de partida
mais direto antes de considerar redução de variância.
```

Este mesmo formato serve para métodos de diferenças finitas (equação do
calor), métodos espectrais, dinâmica molecular, autômatos celulares ou
qualquer outro método — o essencial é sempre: ideia → entradas/saídas →
passos → método escolhido e justificativa.

## Quando usar

Depois de `teoria.md` e antes de abrir o editor de código. Vale a pena
mesmo quando parece "óbvio" — escrever os passos frequentemente revela
detalhes que passariam despercebidos direto no código.

## Quando não é necessário se aprofundar

Para scripts muito simples (ex.: calcular uma grandeza a partir de uma
fórmula fechada, sem iteração), uma frase descrevendo a ideia geral já
basta.

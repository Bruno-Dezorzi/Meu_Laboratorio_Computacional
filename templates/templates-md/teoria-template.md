# Guia — teoria.md

## Finalidade

Este documento registra o **modelo físico e matemático** por trás do
projeto: o que está sendo modelado, quais simplificações foram assumidas e
quais equações descrevem o sistema. É a ponte entre a pergunta física e o
algoritmo.

## O que escrever

- O fenômeno físico sendo modelado, em linguagem simples.
- As hipóteses e simplificações assumidas (e por que são razoáveis).
- As variáveis e parâmetros do sistema, com significado físico e unidades.
- As equações que governam o sistema (dedução breve ou apenas o
  resultado, dependendo da profundidade necessária).
- A solução analítica, quando existir — mesmo que só em um caso limite ou
  regime simplificado.

## Perguntas que este documento deve responder

- O que estou modelando, fisicamente?
- Que suposições estou fazendo para simplificar o problema?
- Quais são as variáveis, parâmetros e suas unidades?
- Qual é a equação (ou sistema de equações) que descreve o fenômeno?
- Existe uma solução analítica ou um caso limite conhecido para comparar?

## Como usar LaTeX neste Markdown

Equações inline usam cifrão simples: `$a = F/m$` produz $a = F/m$.

Equações em bloco usam cifrão duplo, em linha própria:

```markdown
$$
\frac{d^2x}{dt^2} = a(x, t)
$$
```

$$
\frac{d^2x}{dt^2} = a(x, t)
$$

Defina cada variável logo abaixo da equação, por exemplo:

```markdown
onde:

- $x$ — posição (m)
- $t$ — tempo (s)
- $a(x, t)$ — aceleração, possivelmente dependente da posição e do tempo
```

Sistemas de equações usam o ambiente `aligned` ou `cases`:

```markdown
$$
\begin{cases}
\dfrac{dx}{dt} = v \\[4pt]
\dfrac{dv}{dt} = -\dfrac{k}{m}x - \dfrac{b}{m}v
\end{cases}
$$
```

$$
\begin{cases}
\dfrac{dx}{dt} = v \\[4pt]
\dfrac{dv}{dt} = -\dfrac{k}{m}x - \dfrac{b}{m}v
\end{cases}
$$

Matrizes usam `pmatrix` (com parênteses) ou `bmatrix` (com colchetes):

```markdown
$$
\mathbf{M} =
\begin{pmatrix}
m_{11} & m_{12} \\
m_{21} & m_{22}
\end{pmatrix}
$$
```

$$
\mathbf{M} =
\begin{pmatrix}
m_{11} & m_{12} \\
m_{21} & m_{22}
\end{pmatrix}
$$

## Exemplo genérico (Mecânica)

```markdown
## Contexto físico

Corpo de massa $m$ em queda livre com resistência do ar proporcional à
velocidade.

## Hipóteses e simplificações

- Resistência do ar linear em $v$ (válida para baixas velocidades).
- Gravidade $g$ constante.
- Movimento em uma dimensão.

## Modelo matemático

$$
m\frac{dv}{dt} = -mg - bv
$$

onde:

- $v$ — velocidade (m/s)
- $g$ — aceleração da gravidade (m/s²)
- $b$ — coeficiente de arrasto (kg/s)

## Solução analítica

$$
v(t) = -\frac{mg}{b} + \left(v_0 + \frac{mg}{b}\right) e^{-bt/m}
$$
```

## Exemplo genérico (Termodinâmica)

```markdown
## Contexto físico

Difusão de calor em uma barra unidimensional isolada nas extremidades.

## Modelo matemático

$$
\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2}
$$

onde $\alpha$ é a difusividade térmica (m²/s).
```

Esse mesmo formato funciona para Eletromagnetismo (equações de Maxwell em
um caso particular), Física Estatística (uma distribuição ou funcional de
energia), Astrofísica (equação de movimento sob gravidade), Física de
Partículas (uma lagrangiana simplificada) ou Materiais (uma equação
constitutiva) — a estrutura é sempre: contexto → hipóteses → modelo →
solução conhecida, se houver.

## Quando usar

Sempre antes de escrever o algoritmo. Entender o modelo evita implementar
algo que não corresponde à física pretendida.

## Quando não é necessário se aprofundar

Quando o modelo é um resultado padrão e amplamente conhecido (ex.: lei de
Hooke), uma citação da equação com a referência já é suficiente — não é
necessário rededuzir tudo do zero.

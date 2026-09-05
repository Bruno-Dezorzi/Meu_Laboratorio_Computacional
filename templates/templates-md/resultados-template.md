# Guia — resultados.md

## Finalidade

Este documento registra o que foi **de fato obtido** em cada experimento
definido em `experimentos.md`, junto com sua interpretação física. É o
"depois" que fecha o ciclo aberto pelo experimento.

## O que escrever

- Resultados numéricos obtidos.
- Gráficos (referenciados por caminho de arquivo, ex.:
  `![Título](figuras/periodo_vs_amortecimento.png)`).
- Tabelas, quando fizer sentido comparar vários valores.
- Erros/incertezas, quando aplicável (erro numérico, desvio padrão,
  diferença percentual em relação a uma referência).
- Comparação com solução analítica ou fonte de referência.
- Interpretação física: o que esse resultado *significa* em termos do
  fenômeno estudado, não só em termos de números.

## Perguntas que este documento deve responder

- O que eu obtive, especificamente, para o Experimento X?
- Isso bate com a hipótese que eu tinha em `experimentos.md`?
- Como isso se compara com a solução analítica ou com uma referência
  conhecida?
- Qual é a interpretação física deste resultado?
- Esse resultado sugere um próximo experimento ou levanta uma dúvida?

## Exemplo genérico

```markdown
## Resultado — Experimento 1 (efeito do amortecimento no período)

| $b$ (kg/s) | Período medido (s) | Período analítico linear (s) | Diferença |
|---|---|---|---|
| 0.0 | 2.006 | 2.006 | 0.0% |
| 0.1 | 2.011 | — | — |
| 0.5 | 2.089 | — | — |
| 1.0 | 2.312 | — | — |

![Amplitude ao longo do tempo para diferentes valores de b](figuras/amplitude_vs_tempo.png)

**Comparação com referência:** para $b = 0$, o período numérico bate com
a fórmula $T = 2\pi\sqrt{L/g}$ dentro de 0.01%, o que valida a integração
numérica no limite sem amortecimento.

**Interpretação física:** o amortecimento aumenta o período de forma
não linear, mais pronunciada para valores maiores de $b$ — consistente
com o esperado, já que o sistema se aproxima do regime superamortecido.

**Próxima pergunta:** em que valor de $b$ o sistema deixa de oscilar
(amortecimento crítico)?
```

## Quando usar

Após concluir (ou concluir parcialmente) um experimento descrito em
`experimentos.md`. Cada resultado deve, idealmente, referenciar de volta
o experimento que o originou.

## Quando não é necessário se aprofundar

Para execuções puramente exploratórias, sem hipótese definida, um
resultado breve (um gráfico com uma frase) é suficiente — reserve a
análise completa para quando o experimento tiver uma pergunta clara.

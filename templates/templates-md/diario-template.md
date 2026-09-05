# Guia — diario.md

## Finalidade

O diário é o registro pessoal e informal da evolução do projeto, sessão
por sessão. Ele não é um relatório acadêmico — é uma memória externa para
você mesmo, para lembrar o que já foi tentado, o que travou e por que uma
decisão foi tomada.

## O que escrever

Uma entrada nova a cada sessão de trabalho (mesmo que curta), no formato:

```markdown
# DD/MM/AAAA — Título curto da sessão

## Objetivo

## O que fiz

## O que aprendi

## Problemas encontrados

## Hipóteses/dúvidas

## Próximo passo
```

As entradas mais recentes podem ficar no topo do arquivo, para facilitar
a leitura.

## Perguntas que cada entrada deve responder

- O que eu pretendia fazer nesta sessão?
- O que eu de fato fiz?
- O que eu aprendi (sobre a física, a matemática ou o código)?
- O que travou ou deu errado?
- Que dúvidas ou hipóteses ficaram em aberto?
- Qual é o próximo passo concreto?

## Exemplos de entradas

```markdown
# 24/08/2026 — Primeiro modelo

## Objetivo

Escrever a equação de movimento do pêndulo simples sem amortecimento e
implementar uma primeira versão com o método de Euler.

## O que fiz

Deduzi a equação $\ddot\theta = -(g/L)\sin\theta$ e implementei um loop
simples de Euler em Python para integrar no tempo.

## O que aprendi

Com passo de tempo grande (0.1 s), a energia do sistema claramente
aumenta ao longo da simulação — o método de Euler não conserva energia
bem para este problema.

## Problemas encontrados

A amplitude da oscilação cresce artificialmente após algumas dezenas de
ciclos.

## Hipóteses/dúvidas

Talvez um método simplético (ex.: Euler-Cromer) resolva o problema sem
precisar ir direto para RK4.

## Próximo passo

Implementar Euler-Cromer e comparar a energia total ao longo do tempo.
```

```markdown
# 26/08/2026 — Trocando o método de integração

## Objetivo

Testar Euler-Cromer e comparar com Euler simples em termos de conservação
de energia.

## O que fiz

Implementei Euler-Cromer atualizando a velocidade antes da posição.
Plotei a energia total ao longo do tempo para os dois métodos.

## O que aprendi

Euler-Cromer mantém a energia oscilando em torno de um valor constante,
sem a deriva sistemática que Euler simples apresentava. Isso bate com o
que a teoria de integradores simpléticos prevê.

## Problemas encontrados

Nenhum bloqueante. O gráfico de energia ficou um pouco poluído — preciso
melhorar a visualização depois (anotado em ideias-futuras.md).

## Hipóteses/dúvidas

Será que para amplitudes grandes (regime não linear) o comportamento
qualitativo muda?

## Próximo passo

Rodar o mesmo experimento com ângulo inicial grande (> 90°) e comparar.
```

```markdown
# 29/08/2026 — Regime não linear

## Objetivo

Investigar o período de oscilação para amplitudes grandes e comparar com
a aproximação de pequenas oscilações.

## O que fiz

Rodei a simulação para vários ângulos iniciais (10°, 45°, 90°, 150°) e
medi o período numericamente a partir dos cruzamentos por zero.

## O que aprendi

O período cresce visivelmente com a amplitude, divergindo da
aproximação $T \approx 2\pi\sqrt{L/g}$ para ângulos acima de ~30°, como
esperado da teoria.

## Problemas encontrados

A detecção de cruzamento por zero é sensível ao passo de tempo escolhido.

## Hipóteses/dúvidas

Vale comparar com a fórmula do período em termos de integral elíptica
completa, se eu encontrar uma referência acessível.

## Próximo passo

Procurar a expressão do período em função da amplitude na literatura e
registrar em referencias.md.
```

## Quando usar

Em toda sessão de trabalho, por mais curta que seja. Uma entrada de três
linhas ainda é útil — o importante é manter o hábito.

## Quando não é necessário se aprofundar

Sessões de trabalho muito curtas (ex.: só corrigir um erro de digitação)
não precisam preencher todas as seções — "O que fiz" e "Próximo passo"
já bastam.

# Guia — README.md do projeto

## Finalidade

O `README.md` é a **página inicial** do projeto. É o primeiro (e às vezes
único) documento que alguém — inclusive você, seis meses depois — vai ler.
Ele não conta a história completa; ele **orienta** para onde encontrar
cada parte da história.

## O que escrever

- Nome do projeto e uma descrição de 1–3 frases.
- A pergunta física central, em linguagem simples.
- Uma seção "Documentação" com links relativos para os outros arquivos,
  cada um com uma frase dizendo o que encontrar lá.
- O fluxo geral do projeto (pergunta → teoria → algoritmo → implementação
  → validação → experimentos → resultados → próximos passos).
- Status atual do projeto (em andamento, pausado, concluído, etc.).
- Como rodar o código, se já houver algo executável.

## Perguntas que o README deve responder

- Do que se trata este projeto, em uma frase?
- Que pergunta física ele tenta responder?
- Onde encontro a teoria? O algoritmo? Os resultados?
- Como eu rodo isso?
- Em que estado o projeto está agora?

## Modelo de seção "Documentação"

```markdown
## Documentação

- [Teoria](teoria.md) — modelo físico e matemático utilizado.
- [Algoritmo](algoritmo.md) — como o modelo é traduzido em passos computacionais.
- [Diário](diario.md) — registro das sessões de trabalho.
- [Experimentos](experimentos.md) — o que foi testado e em que condições.
- [Resultados](resultados.md) — o que foi obtido e sua interpretação física.
- [Referências](referencias.md) — livros, artigos e fontes utilizadas.
- [Ideias futuras](ideias-futuras.md) — o que foi adiado de propósito.
```

## Exemplo genérico completo

```markdown
# Pêndulo Simples com Amortecimento

> Simulação numérica de um pêndulo simples sujeito a amortecimento viscoso,
> comparando integração numérica com a solução analítica no regime linear.

## Pergunta

Como a amplitude e o período de oscilação de um pêndulo evoluem quando
existe amortecimento proporcional à velocidade, e até que ponto a
aproximação de pequenas oscilações continua válida?

## Fluxo do projeto

pergunta → teoria → algoritmo → implementação → validação → experimentos
→ resultados → próximos passos

## Documentação

- [Teoria](teoria.md) — equação do pêndulo amortecido e sua linearização.
- [Algoritmo](algoritmo.md) — integração via Runge-Kutta de 4ª ordem.
- [Diário](diario.md) — registro das sessões de trabalho.
- [Experimentos](experimentos.md) — variação do coeficiente de amortecimento.
- [Resultados](resultados.md) — comparação numérico vs. analítico.
- [Referências](referencias.md) — bibliografia utilizada.
- [Ideias futuras](ideias-futuras.md) — pêndulo duplo, forçamento externo.

## Como rodar

\`\`\`bash
python src/main.py
\`\`\`

## Status

Em andamento — validação numérica concluída, experimentos em progresso.
```

## Quando usar

Sempre. Todo projeto tem um README, mesmo que ainda esteja no início —
nesse caso, apenas o nome, a pergunta e o status já bastam.

## Quando não é necessário se aprofundar

Nas fases muito iniciais (primeiro dia de um experimento rápido), um
README de três linhas é suficiente. Ele cresce junto com o projeto — não
precisa nascer completo.

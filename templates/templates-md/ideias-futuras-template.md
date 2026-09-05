# Guia — ideias-futuras.md

## Finalidade

Este documento existe para resolver um problema específico: a tentação de
implementar tudo de uma vez assim que uma ideia nova surge. Em vez de
interromper o trabalho atual, a ideia é **anotada aqui e o trabalho
continua** no objetivo em andamento.

## O que escrever

- Uma lista curta de ideias, cada uma com uma ou duas frases.
- Opcionalmente, uma indicação de prioridade ou esforço estimado.
- Nenhum compromisso de implementação — este documento é uma lista de
  possibilidades, não um roadmap obrigatório.

## Perguntas que este documento deve responder

- Que ideia acabou de surgir que não é o foco atual?
- Isso é uma extensão do modelo, uma melhoria de código, ou um novo
  fenômeno a explorar?
- Vale a pena registrar uma frase sobre por que essa ideia é interessante?

## Exemplo genérico

```markdown
## Extensões do modelo

- Adicionar resistência do ar não linear (proporcional a $v^2$).
- Testar o efeito de forçamento periódico externo (pêndulo forçado).

## Métodos

- Comparar RK4 com um integrador simplético de ordem superior.
- Testar passo de tempo adaptativo.

## Código / infraestrutura

- Separar a função de integração em um módulo próprio, se o `main.py`
  crescer demais.
- Portar o núcleo de integração para C++ para comparar desempenho.

## Visualização

- Fazer uma animação da trajetória em vez de só o gráfico estático.
- Adicionar um painel comparando energia cinética e potencial ao vivo.

## Paralelismo / desempenho

- Rodar múltiplas condições iniciais em paralelo para explorar o espaço
  de fase mais rapidamente.
```

## Regra de uso

Quando uma ideia surgir no meio do trabalho:

1. Escreva uma linha aqui.
2. Volte imediatamente para o que você estava fazendo.

Não é necessário decidir agora se a ideia será implementada — só é
necessário garantir que ela não será esquecida nem vai desviar o foco
atual.

## Quando usar

Toda vez que uma ideia "e se eu também..." aparecer durante o trabalho.

## Quando não é necessário se aprofundar

Nunca é necessário detalhar demais uma ideia aqui — se ela virar
prioridade, ela ganha seu próprio espaço em `algoritmo.md`,
`experimentos.md` ou até um novo projeto.

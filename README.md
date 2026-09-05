# Laboratório Computacional Pessoal

Repositório para reunir projetos pessoais de programação científica, Física
Computacional, modelagem matemática, métodos numéricos e simulação,
desenvolvidos ao longo da graduação em Engenharia Física (e, se fizer
sentido, além dela).

Cada pasta dentro de `projetos/` é um pequeno experimento
científico/computacional independente, tratado como se fosse um mini
projeto de pesquisa: tem uma pergunta, um modelo, um código, uma validação
e um registro do processo.

## Estrutura do repositório

```
lab-computacional/
├── README.md              <- este arquivo
├── PRINCIPIOS.md           <- filosofia e regras do laboratório
├── projeto-template/       <- molde vazio para começar um projeto novo
├── templates-md/           <- guias completos de como preencher cada documento
└── projetos/                <- (você cria) onde ficam os projetos reais
    ├── projetil-2d/
    ├── pendulo-simples/
    └── ...
```

> A pasta `projetos/` não vem criada por padrão — você a cria quando iniciar
> seu primeiro projeto, copiando `projeto-template/` para dentro dela.

## Como usar este laboratório

1. Copie `projeto-template/` para `projetos/nome-do-projeto/`.
2. Leia `templates-md/README-template.md` para saber como preencher o
   `README.md` do novo projeto.
3. Siga o fluxo: pergunta → teoria → algoritmo → código → validação →
   experimentos → resultados → refinamento.
4. Use `diario.md` a cada sessão de trabalho, mesmo que seja um parágrafo.
5. Quando surgir uma ideia que não é a prioridade agora, anote em
   `ideias-futuras.md` e continue no que estava fazendo.

## Filosofia

As regras completas estão em [`PRINCIPIOS.md`](PRINCIPIOS.md). Resumo:

> Primeiro fazer funcionar e validar. Depois organizar. Depois abstrair.
> Depois otimizar.

## Os documentos de cada projeto

| Documento | Pergunta que ele responde |
|---|---|
| `README.md` | Do que se trata este projeto e como navegar nele? |
| `teoria.md` | Qual é o modelo físico e matemático? |
| `algoritmo.md` | Como o modelo vira um algoritmo? |
| `diario.md` | O que eu fiz, aprendi e travei em cada sessão? |
| `experimentos.md` | O que eu testei e em que condições? |
| `resultados.md` | O que eu obtive e o que isso significa fisicamente? |
| `referencias.md` | Em que eu me apoiei? |
| `ideias-futuras.md` | O que eu decidi *não* fazer agora? |
| `checklist.md` | Em que etapa do ciclo de vida o projeto está? |

Guias completos de como preencher cada um estão em `templates-md/`.

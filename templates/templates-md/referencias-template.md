# Guia — referencias.md

## Finalidade

Registrar as fontes em que o projeto se apoiou: livros, artigos, notas de
aula, documentação de bibliotecas, vídeos ou qualquer material que tenha
influenciado o modelo, o algoritmo ou a interpretação dos resultados.

## O que escrever

- Referências bibliográficas formais (livros, artigos), quando existirem.
- Fontes informais (posts, vídeos, notas de aula) — sem se preocupar em
  formatá-las como uma bibliografia acadêmica.
- Documentação técnica de bibliotecas ou ferramentas usadas de forma não
  trivial.
- Uma frase sobre *o que* cada fonte contribuiu para o projeto, se não
  for óbvio pelo título.

## Perguntas que este documento deve responder

- Em quais fontes eu me apoiei para o modelo físico?
- Em quais fontes eu me apoiei para o método numérico?
- Existe uma solução de referência (livro, paper) com a qual comparar os
  resultados?
- Se eu precisar revisitar um conceito, onde eu procuraria primeiro?

## Exemplo genérico

```markdown
## Física / modelo

- Marion, J. B.; Thornton, S. T. *Classical Dynamics of Particles and
  Systems*. Capítulo sobre oscilações — dedução da equação do pêndulo e
  do regime de pequenas oscilações.
- Notas de aula de Mecânica Clássica, Semana 4 — amortecimento viscoso.

## Métodos numéricos

- Press, W. H. et al. *Numerical Recipes* — capítulo sobre integração de
  EDOs, usado para entender RK4 e Euler-Cromer.
- Documentação do `scipy.integrate.solve_ivp` — usada para validar a
  implementação manual do RK4.

## Outras

- Vídeo "Simplectic integrators explained" — ajudou a entender por que
  Euler-Cromer conserva energia melhor que Euler simples.
```

## Quando usar

Sempre que uma fonte específica influenciar uma decisão de modelagem,
método ou interpretação — não é necessário citar fontes genéricas de
conhecimento já consolidado (ex.: leis de Newton).

## Quando não é necessário se aprofundar

Projetos de exploração rápida, sem uma fonte específica além de
conhecimento geral, podem deixar este arquivo vazio ou com uma única
linha.

# Guia — checklist.md

## Finalidade

Acompanhar em que etapa do ciclo de vida o projeto está, servindo como
uma bússola rápida: o que já foi feito, o que falta, e o que ainda não é
necessário fazer agora.

## O que escrever

Uma lista de tarefas no formato de checklist do Markdown
(`- [ ]` / `- [x]`), cobrindo as etapas do ciclo de vida do projeto.
Nem toda etapa é obrigatória em todo projeto — as opcionais estão
marcadas como tal no modelo abaixo.

## Modelo completo

```markdown
## Modelo e teoria

- [ ] Definir a pergunta física
- [ ] Definir o modelo (hipóteses e simplificações)
- [ ] Escrever as equações que governam o sistema
- [ ] Identificar as hipóteses assumidas
- [ ] Encontrar solução analítica ou caso limite (opcional — nem todo
      problema tem uma)

## Algoritmo e implementação

- [ ] Escrever o algoritmo (passos, método numérico escolhido)
- [ ] Implementar a versão mínima ("fazer funcionar")
- [ ] Testar com casos simples/conhecidos
- [ ] Validar contra solução analítica ou referência

## Investigação

- [ ] Rodar experimentos (ver experimentos.md)
- [ ] Documentar resultados (ver resultados.md)
- [ ] Interpretar fisicamente os resultados

## Organização e melhoria (depois de validar)

- [ ] Refatorar o código (opcional — só se o código já validado estiver
      difícil de estender)
- [ ] Medir desempenho (opcional — só se desempenho for relevante para o
      projeto)
- [ ] Otimizar (opcional — só depois de medir, e só se necessário)

## Extensões (opcional)

- [ ] Portar núcleo do código para C++ (opcional — só quando desempenho
      em Python for uma limitação real)
- [ ] Registrar lições aprendidas em diario.md
```

## Perguntas que este documento deve responder

- Em que etapa do ciclo de vida o projeto está agora?
- O que já foi validado e o que ainda é só uma primeira versão?
- Existe alguma etapa que estou pulando sem perceber (ex.: indo direto
  para otimização sem ter validado)?

## Quando usar

Atualize sempre que concluir uma etapa relevante, ou no início/fim de uma
sessão de trabalho mais longa.

## Quando não é necessário se aprofundar

Nem todo projeto precisa passar pelas seções "Organização e melhoria" ou
"Extensões" — muitos experimentos pequenos terminam logo depois da
validação e interpretação dos resultados, e está tudo bem.

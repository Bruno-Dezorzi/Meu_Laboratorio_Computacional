# Princípios do Laboratório

Estas regras existem para lembrar, especialmente nos momentos em que a
vontade de construir uma arquitetura sofisticada aparece cedo demais, qual
é o objetivo real deste laboratório: **aprender modelagem computacional**,
não produzir software perfeito desde o primeiro commit.

1. **Não otimizar antes de validar.** Um código lento e correto vale mais
   que um código rápido e errado.
2. **Não adicionar abstração sem necessidade.** Classes, padrões de
   projeto e camadas de indireção só entram quando o código *pede* isso —
   não antes.
3. **Primeiro compreender o modelo físico.** Se a física não está clara,
   nenhuma engenharia de software resolve isso.
4. **Primeiro implementar a versão mínima.** Um script feio que reproduz o
   fenômeno é mais valioso que uma arquitetura vazia.
5. **Comparar com soluções conhecidas sempre que possível.** Solução
   analítica, limites conhecidos, casos particulares, resultados de
   referência.
6. **Usar gráficos para investigar o comportamento.** Antes de confiar em
   um número, olhe para a curva.
7. **Registrar erros e tentativas fracassadas.** Elas fazem parte do
   processo e economizam tempo no futuro (ver `diario.md`).
8. **Melhorar o projeto incrementalmente.** Uma mudança pequena e testada
   por vez.
9. **Aprender novas ferramentas conforme a necessidade**, sem exigir
   domínio prévio de toda a tecnologia antes de começar.
10. **O objetivo principal é aprender modelagem computacional**, não
    produzir software perfeito desde o primeiro commit.

## O processo que este laboratório tenta ensinar

```
pergunta física → modelo → matemática → algoritmo → código
     → validação → experimentos → refinamento → otimização
```

Cada seta é um documento (ou parte de um documento) do projeto:

- **pergunta física → modelo → matemática** → `teoria.md`
- **algoritmo** → `algoritmo.md`
- **código** → `src/`
- **validação e experimentos** → `experimentos.md`
- **refinamento** → `diario.md` e `checklist.md`
- **otimização** → etapa final de `checklist.md`, quando fizer sentido

Nem todo projeto passa por todas as etapas com a mesma profundidade — e
está tudo bem. O ponto é *saber em qual etapa você está* e não pular direto
para código sem entender o modelo, nem travar em arquitetura antes de ter
algo que funciona.

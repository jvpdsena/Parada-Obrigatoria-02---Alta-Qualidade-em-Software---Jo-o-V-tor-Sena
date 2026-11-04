# Relatório final — Bug Hunter & TDD Calculator

## 1. Introdução
A atividade teve como objetivo investigar defeitos em uma calculadora científica escrita em Python, registrar os problemas identificados e aplicar desenvolvimento orientado a testes (TDD) para corrigi-los. O código disponibilizado pelo professor foi preservado em `Calculadora_original.py`, permitindo comparar os comportamentos anterior e posterior.

## 2. Ferramentas e procedimento
Foram utilizados Python, NumPy (para examinar o original), `unittest` (biblioteca padrão), Git como ferramenta prevista de versionamento e arquivos Markdown para documentação. A análise incluiu leitura do código, verificação das operações matemáticas, validação de entradas e inspeção do fluxo do menu. Os defeitos, suas condições de reprodução, impactos e correções estão descritos em `Bugs.md`.

## 3. Resultados da inspeção
Foram registrados **12 defeitos**: adição incorreta; fatorial incorreto; função inexistente para ln; base incorreta para log10; zero aceito em log10; divisão por zero sem tratamento; opção seno ausente; cosseno e tangente indefinidos; entradas inválidas sem tratamento; recursão no menu; e execução automática ao importar o módulo. Os defeitos foram classificados conforme gravidade e impacto. A classificação é uma avaliação técnica para esta atividade.

## 4. Aplicação de TDD — ciclo RED, GREEN, REFACTOR
**RED:** foi formulado o requisito `adicao(2, 3) == 5`. A execução da verificação no arquivo original falhou com `AssertionError: Esperado 5, obtido 7`. A saída da execução está em `evidencias/teste_vermelho.txt`.

**GREEN:** a expressão incorreta `x + np.add(x, y)` foi substituída por `x + y`. Foram criados testes automatizados para operações e casos-limite. Na execução documentada, os **22 testes passaram**. A saída completa está em `evidencias/testes_verdes.txt`.

**REFACTOR:** as operações foram isoladas da interface, a entrada principal foi protegida com `if __name__ == '__main__'`, o menu passou a usar um laço em vez de recursão e foram adicionadas validações de domínio. As operações trigonométricas interpretam ângulos em graus. Após as mudanças, os 22 testes permaneceram aprovados.

A etapa RED demonstrada usa um script de asserção contra o original; a suíte `unittest` valida a implementação corrigida. Não se afirma que todos os 12 bugs tiveram ciclos RED independentes.

## 5. Verificação
O comando `python -m unittest discover -s tests -v` executou 22 testes, todos com resultado `OK` no ambiente utilizado. Há testes para casos normais, valores de fronteira, exceções e opções do menu. Esse resultado não equivale a cobertura integral do programa.

## 6. Reflexão sobre Scrum
Embora a atividade seja individual, o trabalho pode ser organizado de acordo com princípios do Scrum: o relatório de defeitos funciona como backlog; a escolha do bug de adição define um item prioritário; a implementação com testes constitui uma entrega incremental; e a execução dos testes e revisão da documentação funcionam como inspeção e adaptação. Em uma equipe Scrum, as decisões seriam discutidas no Sprint Planning, acompanhadas durante a Sprint e avaliadas na Sprint Review e Retrospective. Nesta atividade, essas cerimônias são apenas uma analogia metodológica, não eventos de equipe efetivamente realizados.

## 7. Conclusão
A inspeção identificou falhas funcionais e problemas de robustez. A aplicação de TDD a um defeito permitiu demonstrar a falha antes da correção e verificar o comportamento esperado depois dela. O projeto está organizado para versionamento e publicação em repositório público, que ainda dependem da ação do aluno em sua conta GitHub.

## Referências
PRESSMAN, Roger S.; MAXIM, Bruce R. *Engenharia de software: uma abordagem profissional*. 9. ed. Porto Alegre: AMGH, 2021.

PYTHON SOFTWARE FOUNDATION. *unittest — Unit testing framework*. Disponível em: https://docs.python.org/3/library/unittest.html.

GITHUB. *GitHub Docs*. Disponível em: https://docs.github.com/pt.

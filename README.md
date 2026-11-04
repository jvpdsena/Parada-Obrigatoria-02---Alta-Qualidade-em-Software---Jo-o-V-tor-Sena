# Bug Hunter & TDD Calculator

Projeto acadêmico de identificação, documentação e correção de defeitos de uma calculadora científica em Python.

## Estrutura
- `Calculadora_original.py`: código original sem modificações.
- `Calculadora.py`: versão corrigida e testável.
- `Bugs.md`: relatório detalhado dos 12 defeitos encontrados.
- `tests/test_calculadora.py`: 22 testes automatizados com `unittest`.
- `evidencias/demonstracao_red.py`: demonstração do teste que falha no código original.
- `evidencias/teste_vermelho.txt`: saída real da etapa RED.
- `evidencias/testes_verdes.txt`: saída real da etapa GREEN.
- `RELATORIO_FINAL.md`: metodologia, resultados e reflexão sobre Scrum.

## Pré-requisitos
Python 3.10+ para o código corrigido. NumPy é necessário apenas para executar o arquivo original.

## Executar
```bash
python Calculadora.py
```

## Executar testes
```bash
python -m unittest discover -s tests -v
```

## Reproduzir o TDD
```bash
pip install -r requirements-original.txt
python evidencias/demonstracao_red.py  # falha intencional: esperado 5, original devolve 7
python -m unittest discover -s tests -v  # versão corrigida: 22 testes passam
```

## Publicação no GitHub
Na pasta do projeto:
```bash
git init
git add .
git commit -m "Documenta bugs e corrige calculadora com TDD"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/bug-hunter-tdd-calculator.git
git push -u origin main
```
Crie primeiro um repositório público vazio com esse nome em sua conta. Substitua `SEU_USUARIO` e não publique credenciais.

## Observação
O repositório remoto ainda precisa ser criado e publicado pelo aluno; os arquivos fornecidos estão prontos para isso.

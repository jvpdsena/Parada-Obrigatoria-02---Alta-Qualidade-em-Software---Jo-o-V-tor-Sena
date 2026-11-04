# Relatório de bugs — Bug Hunter & TDD Calculator

**Fonte:** `Calculadora_original.py`, fornecido na atividade. **Ambiente de verificação:** Python 3, NumPy 2.3.5. **Data de análise:** 04/11/2026. **Status:** corrigidos na versão `Calculadora.py`; o arquivo original foi preservado. A localização usa as linhas do arquivo original.

## BUG-01 — Adição soma o primeiro operando duas vezes
- **Localização:** linha 4, função `adicao`.
- **Descrição/contexto:** `x + np.add(x, y)` equivale a `2*x+y`.
- **Reprodução:** executar `adicao(2, 3)`.
- **Esperado:** `5`. **Obtido no original:** `7`.
- **Consistência:** sempre que `x != 0`. **Severidade:** alta. **Impacto:** resultados matemáticos incorretos.
- **Correção:** retornar `x + y`. **Status:** resolvido. **Evidência:** `evidencias/teste_vermelho.txt` e `evidencias/testes_verdes.txt`.

## BUG-02 — Fatorial retorna zero para inteiros positivos
- **Localização:** linhas 23–27, função `fatorial`.
- **Descrição:** o laço começa em zero e multiplica o acumulador por zero.
- **Reprodução:** `fatorial(5)`. **Esperado:** `120`. **Obtido:** `0`.
- **Consistência:** sempre para inteiros não negativos; para negativos retorna 1 sem validação. **Severidade:** alta.
- **Correção:** usar `math.factorial` e validar inteiro não negativo. **Status:** resolvido.

## BUG-03 — Logaritmo natural usa atributo inexistente
- **Localização:** linha 32, função `logaritmo_natural`.
- **Descrição:** `np.ln` não existe na versão NumPy 2.3.5.
- **Reprodução:** `logaritmo_natural(2.718281828)`. **Esperado:** aproximadamente `1`. **Obtido:** `AttributeError`.
- **Consistência:** para entradas positivas no ambiente testado. **Severidade:** alta.
- **Correção:** `math.log(x)`. **Status:** resolvido.

## BUG-04 — Logaritmo base 10 usa logaritmo natural
- **Localização:** linha 37, função `logaritmo_base10`.
- **Descrição:** `np.log(x)` calcula ln(x), não log10(x).
- **Reprodução:** `logaritmo_base10(100)`. **Esperado:** `2`. **Obtido:** aproximadamente `4.60517`.
- **Consistência:** para valores positivos, exceto 1. **Severidade:** alta.
- **Correção:** `math.log10(x)`. **Status:** resolvido.

## BUG-05 — Logaritmo base 10 aceita zero
- **Localização:** linha 35, função `logaritmo_base10`.
- **Descrição:** a condição `x < 0` não rejeita `x == 0`.
- **Reprodução:** `logaritmo_base10(0)`. **Esperado:** erro controlado. **Obtido:** `-inf` e aviso do NumPy.
- **Consistência:** sempre no ambiente testado. **Severidade:** média.
- **Correção:** rejeitar `x <= 0` com `ValueError`. **Status:** resolvido.

## BUG-06 — Divisão por zero não é tratada
- **Localização:** linha 13, função `divisao`.
- **Reprodução:** `divisao(10, 0)`. **Esperado:** mensagem de erro sem interromper a interface. **Obtido:** `ZeroDivisionError` não tratado.
- **Consistência:** sempre para divisor zero. **Severidade:** alta. **Impacto:** encerramento inesperado.
- **Correção:** validação explícita e tratamento na interface. **Status:** resolvido.

## BUG-07 — Opção seno não implementada
- **Localização:** menu linha 52 e fluxo de escolhas linhas 56–106.
- **Reprodução:** escolher `10` no menu. **Esperado:** solicitar ângulo e calcular seno. **Obtido:** `Operação inválida`.
- **Consistência:** sempre. **Severidade:** média.
- **Correção:** implementar `seno` em graus e vincular à opção 10. **Status:** resolvido.

## BUG-08 — Cosseno não definido
- **Localização:** linha 95, opção `11`.
- **Reprodução:** selecionar `11` e informar `180`. **Esperado:** `-1`. **Obtido:** `NameError`.
- **Consistência:** sempre que a opção é executada. **Severidade:** alta.
- **Correção:** implementar `cosseno` com conversão de graus para radianos. **Status:** resolvido.

## BUG-09 — Tangente não definida
- **Localização:** linha 99, opção `12`.
- **Reprodução:** selecionar `12` e informar `45`. **Esperado:** aproximadamente `1`. **Obtido:** `NameError`.
- **Consistência:** sempre que a opção é executada. **Severidade:** alta.
- **Correção:** implementar `tangente`, conversão de unidades e verificação de pontos indefinidos. **Status:** resolvido.

## BUG-10 — Entrada numérica inválida encerra a execução
- **Localização:** linhas 64–65, 78, 82, 86, 90, 94, 98.
- **Reprodução:** selecionar `1` e digitar `abc` como primeiro número. **Esperado:** erro amigável. **Obtido:** `ValueError` não tratado.
- **Consistência:** sempre com texto não numérico. **Severidade:** média.
- **Correção:** tratar `ValueError` na interface. **Status:** resolvido.

## BUG-11 — Repetição recursiva pode esgotar a pilha
- **Localização:** linhas 104–106.
- **Reprodução:** executar sucessivas operações e responder `s` muitas vezes. **Esperado:** continuar sem acumular chamadas. **Obtido:** crescimento da pilha, potencial `RecursionError` após muitas operações.
- **Consistência:** depende do número de repetições. **Severidade:** média.
- **Correção:** substituir recursão por `while`. **Status:** resolvido.

## BUG-12 — Importar módulo inicia a interface
- **Localização:** linha 108.
- **Reprodução:** executar `import Calculadora` em outro script. **Esperado:** importar funções sem pedir entrada. **Obtido:** menu e chamada de `input()`.
- **Consistência:** sempre. **Severidade:** média. **Impacto:** dificulta testes unitários e reutilização.
- **Correção:** usar `if __name__ == '__main__':`. **Status:** resolvido.

## Observações
- Os comportamentos de raiz quadrada negativa e ln de não positivo já eram tratados com strings no original; a versão corrigida padroniza a sinalização por exceções, sem classificar esses casos como bugs originais.
- Os testes automatizados cobrem as operações e casos-limite principais, mas não demonstram ausência absoluta de defeitos.
- Evidências em texto são saídas reais de execução; capturas de tela podem ser acrescentadas pelo aluno ao executar localmente.

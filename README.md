# 📘 README – Analisador Léxico e Sintático para Linguagem C
## 📌 Visão Geral

Este projeto implementa um analisador léxico e sintático para um subconjunto da linguagem C utilizando Python e a biblioteca PLY (Python Lex-Yacc).
O objetivo é simular as duas primeiras etapas de um compilador — análise léxica e análise sintática — e gerar, ao final, uma Árvore de Sintaxe Abstrata (AST) que representa estruturalmente o código de entrada.

O projeto também inclui um conjunto de testes contendo arquivos válidos e inválidos, permitindo verificar o comportamento do analisador em diferentes cenários.

## 🎯 Objetivos do Projeto

Implementar um lexer capaz de identificar palavras-chave, identificadores, operadores, literais e delimitadores da linguagem C.

Construir um parser capaz de validar a estrutura sintática de programas C simples.

Criar uma Árvore de Sintaxe Abstrata (AST) legível e organizada para representar o programa analisado.

Tratar erros léxicos e sintáticos de forma clara, exibindo linha e coluna do erro.

Disponibilizar exemplos de entrada válidos e inválidos para fins de testes e validação.

## 📂 Estrutura do Projeto

O projeto é organizado em quatro arquivos principais e uma pasta com testes:

**lexer.py** – Implementa o analisador léxico usando regras regulares, classificação de tokens e tratamento de erros.

**parser.py** – Define a gramática sintática utilizando YACC, monta a AST e gerencia erros de análise.

**my_ast.py** – Contém as classes que compõem a Árvore de Sintaxe Abstrata.

**main.py** – Arquivo principal que executa a análise de um arquivo .c e exibe os resultados.

**tests_files/** – Contém programas C divididos entre válidos e inválidos para teste.

## 🧩 Funcionamento do Sistema
### Análise Léxica

O lexer converte o código-fonte em uma sequência de tokens.
Ele reconhece:

- palavras-chave da linguagem C

- identificadores

- literais numéricos, caracteres e strings

- operadores aritméticos, relacionais e lógicos

- símbolos como parênteses, chaves e ponto-e-vírgula

- comentários

Tokens inválidos são detectados e reportados com precisão.

### Análise Sintática

O parser utiliza as regras da gramática para:

- validar a estrutura do programa

- interpretar expressões com precedência correta

- processar comandos como if/else, while, for e return

- analisar declarações e definições de funções

- construir recursivamente a AST

Caso um token inesperado seja encontrado, é gerada uma mensagem de erro com a posição do problema.

### Construção da AST

A AST representa o programa como uma estrutura hierárquica.
Ela é composta por nós como:

- funções

- declarações

- blocos de código

- expressões

- operadores

- comandos de fluxo

Essa árvore é convertida em formato dicionário/JSON para facilitar visualização e depuração.

### ▶️ Como Executar
1. Instale as dependências:
   ```pip install ply```
2. Execute o analisador passando um arquivo C:
```python main.py caminho/do/arquivo.c```

 ## 🧪 Testes
 A pasta tests_files contém arquivos de teste divididos em:
 - **Válidos:** exemplos completos e sintaticamente corretos.
 - **Inválidos:** códigos contendo erros intencionais para validar o tratamento de falhas.
Eles são úteis para demonstrar que o analisador identifica corretamente tanto estruturas válidas quanto inválidas.

 ## 📚 O que este projeto demonstra
- Funcionamento prático das fases iniciais de um compilador.

- Implementação de um lexer e parser reais usando PLY.

- Construção e interpretação de árvores sintáticas.

- Tratamento de erros durante o processo de compilação.

- Modularização limpa entre léxico, sintaxe e AST.

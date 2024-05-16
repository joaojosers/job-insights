# job-insights

## Contexto
- O projeto requer a implementação de análises a partir de um conjunto de dados sobre empregos.

## Habilidades a serem trabalhadas
- Utilizar o terminal interativo do Python.
- Utilizar estruturas condicionais e de repetição e  funções built-in do Python.
- Utilizar tratamento de exceções, manipulação de arquivos e escrever funções.
- Escrever testes com Pytest e desenvolver  módulos e importá-los em outros códigos.
## Crie o ambiente virtual para o projeto
```
python3 -m venv .venv && source .venv/bin/activate
```
## Instalando Dependências
```
python3 -m pip install -r dev-requirements.txt
```
## Executando Testes
* executando todos os testes
 ```
 python3 -m pytest
```
* Caso precise executar apenas um arquivo de testes basta executar o comando:
```
python3 -m pytest tests/nomedoarquivo.py
```
## Arquivos desenvolvidos pela Trybe
* src:
  - dev-requirements.txt
  - requirements.txt
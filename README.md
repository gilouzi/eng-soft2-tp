# eng-soft2-tp
Repositório para o trabalho prático de Engenharia de Software 2

## Integrantes
1. Ana Flavia de Miranda Silva
2. Giovanna Louzi Bellonia
3. Thiago Martin Poppe

## Explicação do sistema
- Foi desenvolvido um sistema de E-Commerce simples, onde o usuário pode cadastrar novos usuários, produtos e fazer compras desses respectivos produtos (de acordo com o estoque da loja).
- Ao final da compra o usuário será enviado para uma página de *checkout* onde ele deverá informar seus dados, como: nome, e-mail, endereço e forma de pagamento.
  - Além disso, o usuário poderá visualizar quais produtos foram adicionados ao carrinho, bem como frete e valor total da compra. 

## Explicação das tecnologias utilizadas
- Para construir o sistema, utilizamos a linguagem de programação Python.
- A interface web foi criada usando o micro framework Flask.
- Para a interface entre o Flask e o banco de dados SQL foi utilizada a extensão Flask-SQLAlchemy.

### Execução do sistema
- Para executar o sistema, execute os seguintes passos:
````bash
python3 -m venv venv # criação de um virtual environment
source venv/bin/activate

pip3 install -e . # instalação das dependências do sistema
python3 main.py # execução do sistema em um servidor local
````
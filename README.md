# Financa - API

API para gerenciador de finanças.

### Arquitetura

* Linguagem: Python
* Framework: Django e Django rest framework

### 📋 Pré-requisitos

Para instalação do software é necessário:
* Python 3.10
* Django 4.1.7
* django cors headers 3.14.0
* djangorestframework 3.14.0
* pytz 2022.7.1
* sqlparse 0.4.3
* tzdata 2022.7
* django filter 22.1


### 🔧 Instalação

1. Clone o repositório:
```
> git clone https://github.com/DCOMP-UFS/2022-2-praticas-projetoinca.git
```

2. Crie um ambiente virtual:
```
> python -m venv venv
```

3. Ative o ambiente virtual:
```
> venv/Scripts/activate
```

4. Instale as dependências:
```
> pip install -r requisitos.txt
```

6. Execute as migrações:
```
> python manage.py makemigrations
> python manage.py migrate
```

5. Execute o servidor:
```
> python manage.py runserver
```

## ⚙️ Executando os testes

Para executar os testes automatizados deste sistema, você pode seguir os seguintes passos:

1. Ative o ambiente virtual:
```
> venv/Scripts/activate
```

2. Execute o seguinte comando para executar todos os testes automatizados:
```
python manage.py test
```

## API

## Visão Geral
Esta API permite aos usuários fazerem CRUD (Create, Retrieve, Update e Delete).

### AUTH

| ENDPOINT | HTTP METHOD | CRUD METHOD | RESULTADO |
|----------|-------------|-------------|-----------|
|`/auth/cadastro/`| POST | CRIAR | criar usário |
|`/auth/login`| POST | CRIAR | autenticação |

Exemplo de corpo da requisição de cadastro:
~~~JSON
{
  "email": "user@example.com",
  "password": "string"
}
~~~

Exemplo de corpo da requisição de login:
~~~JSON
{
  "email": "user@example.com",
  "password": "string"
}
~~~

### DESPESA

| ENDPOINT | HTTP METHOD | CRUD METHOD | RESULTADO |
|----------|-------------|-------------|-----------|
|`despesa/`| GET | LEITURA | listagem de despesa|
|`despesa/`| POST | CRIAR | adiciona uma despesa |
|`despesa/{id}`| GET | LEITURA | listagem de uma despesa|
|`despesa/{id}`| PUT | ATUALIZAR | atualiza uma despesa existente|
|`despesa/{id}`| DELETE | DELETAR | deleta uma despesa existente|

Exemplo de corpo da requisição de despesa:
~~~JSON
}
    "valor": 0,
    "data": "2023-07-27",
    "categoria": "alimentacao",
    "descricao": "string",
    "usuario": 0
}
~~~

### META

| ENDPOINT | HTTP METHOD | CRUD METHOD | RESULTADO |
|----------|-------------|-------------|-----------|
|`meta/`| GET | LEITURA | listagem de meta|
|`meta/`| POST | CRIAR | adiciona uma meta |
|`meta/{id}`| GET | LEITURA | listagem de uma meta|
|`meta/{id}`| PUT | ATUALIZAR | atualiza uma meta existente|
|`meta/{id}`| DELETE | DELETAR | deleta uma meta existente|

Exemplo de corpo da requisição de despesa:
~~~JSON
{
  "nome_meta": "string",
  "valor_alvo": 0,
  "progresso": 0,
  "concluida": true
}
~~~

### RECEITA

| ENDPOINT | HTTP METHOD | CRUD METHOD | RESULTADO |
|----------|-------------|-------------|-----------|
|`receita/`| GET | LEITURA | listagem de receita|
|`receita/`| POST | CRIAR | adiciona uma receita |
|`receita/{id}`| GET | LEITURA | listagem de uma receita|
|`receita/{id}`| PUT | ATUALIZAR | atualiza uma receite existente|
|`receita/{id}`| DELETE | DELETAR | deleta uma receite existente|

Exemplo de corpo da requisição de despesa:
~~~JSON
{
  "valor": 0,
  "categoria": "salario",
  "descricao": "string",
  "data": "2023-07-27"
}
~~~

### RELATORIO

| ENDPOINT | HTTP METHOD | CRUD METHOD | RESULTADO |
|----------|-------------|-------------|-----------|
|`relatorio/porcategoria/`| GET | LEITURA | listagem de dados por categoria |
|`relatorio/pormes`| GET | LEITURA | listagem de dados por mes |


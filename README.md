# Desafio EM

## 💡 Objetivo:

API Para cadastro de aluno realizando o armazenamento, consulta, inserção, atualização e remoção dos mesmos. O banco utilizado para esta função foi PostgreSQL, suas tabelas são geradas automaticamente ao iniciar o sistema.
Como endpoints adicionais foi incluído um segundo cadastro de notas anuais dos alunos, sendo esta tabela conectada à primeira através da chave estrangeira de id do aluno.
Também foram adicionados endpoints de cadastro e autenticação de logins de usuários para ter acesso ao sistema através de um token gerado na rota de login.

## 🛠 Tecnologias:

- [Python](https://www.python.org/)
- [Pytest](https://docs.pytest.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/)
- [Flask-RESTX](https://flask-restx.readthedocs.io/)
- [PostgreSQL](https://www.postgresql.org/)
- [Dotenv](https://pypi.org/project/python-dotenv/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Bcrypt](https://pypi.org/project/bcrypt/)
- [Insomnia](https://insomnia.rest/)

## 🔨 Clonagem, Configurações e Variáveis de Ambiente:

Através do terminal clone o diretório usando a chave SSH, crie o ambiente virtual e instale as dependências utilizando os seguintes comandos:

```bash
git clone git@github.com:wagnerberna/EM.git
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Configure as variáveis de ambiente criando o arquivo **.env** com as configurações, será necessário substituir o XXX pela senha da base local de acesso ao PostgreSQL e o YYY será a chave secreta de geração do token.

```bash
POSTGRES_LOCAL = "postgresql://postgres:XXX@localhost:5432/postgres"
DATABASE_LOCAL = "postgresql://postgres:XXX@localhost:5432/school_test"
APP_PORT = 5000
APP_DEV = "config.DevConfig"
APP_PROD = "config.ProdConfig"
JWT_SECRET_KEY = "YYY"
```

## 📌 Inicialização da API:

No terminal inicialize a API com o seguinte comando:

```bash
python app.py
```

## 🔎 Métodos e Rotas de Requisições:

A URL de base para acesso das rotas é:
**http://localhost:5000**

### Rotas dos Usuários do Sistema:

```python
| Metodo | Rota            | Descricao                    |
|--------|-----------------|------------------------------|
| Get    | /users          | Buscar todos                 |
| Get    | /user/{ID}      | Buscar por ID                |
| Post * | /user           | Adicionar                    |
| Put    | /user/{ID}      | Atualizar por ID e campo     |
| Delete | /user/{ID}      | Deletar por ID               |
| Put    | /user           | Ativar ou desativar por login|
```

**Campos Rotas:**  
Todos os campos exceto os Marcados com \* usam o cabeçalho de autenticação.  
-Header:  
Authorization: Bearer token

Post - /user:

```json
{
  "name": "xxx",
  "login": "xxx",
  "password": "yyy"
}
```

Put - /user/{ID}:  
Define o nome do campo a ser atualizado ("name", "login", "password") e valor.

```json
{
  "field": "xxx",
  "value": "yyy"
}
```

Put - /user:  
Define o nome do login a ser ativado ou desativado e valor (true, false).

```json
{
  "login": "xxx",
  "status": true
}
```

### Rotas de Auteticação:

```python
| Metodo | Rota            | Descricao                    |
|--------|-----------------|------------------------------|
| Post * | /auth/login     | Logar no sistema             |
| Post   | /auth/logout    | Deslogar do sistema          |
```

**Campos Rotas:**  
Todos os campos exceto os Marcados com \* usam o cabeçalho de autenticação.  
-Header:  
Authorization: Bearer token

Post - /auth/login:

```json
{
  "login": "xxx",
  "password": "yyy"
}
```

### Rotas Estudantes:

```python
| Metodo | Rota            | Descricao                    |
|--------|-----------------|------------------------------|
| Get    | /students       | Buscar todos                 |
| Get    | /student/{ID}   | Buscar por ID                |
| Post   | /student        | Adicionar                    |
| Put    | /student/{ID}   | Atualizar por ID             |
| Delete | /student/{ID}   | Deletar por ID               |
| Put    | /student        | Ativar ou desativar por login|
```

**Campos Rotas:**  
Todos os campos exceto os Marcados com \* usam o cabeçalho de autenticação.  
-Header:  
Authorization: Bearer token

Post - /student:  
Adiciona os dados do estudante os campos de string passam por uma normalização onde são colocados em minúsculos, retirados assentos e espaços no início e fim do campo para armazenamento, o CPF passa por um processo de retirada de pontos e traços.
O e-mail é validado.

```json
{
  "name": "xxx",
  "birth_date": "yyyy-mm-dd",
  "address": "xxx",
  "tutor_name": "xxx",
  "cpf_tutor": "100.200.300-00",
  "tutor_email": "xxx@xxx.com"
}
```

Put - /user/{ID}:  
Define o nome do campo a ser atualizado ("name", "birth_date", "address", "tutor_name", "cpf_tutor", "tutor_email") e valor.

```json
{
  "field": "xxx",
  "value": "yyy"
}
```

### Rota de Filtros Estudantes:

```python
| Metodo | Rota            | Descricao                                        |
|--------|-----------------|--------------------------------------------------|
| Get    | /filters        | Filtro por palavra chave e campo a ser filtrado  |
```

**Campos Rotas:**  
Todos os campos exceto os Marcados com \* usam o cabeçalho de autenticação.  
-Header:  
Authorization: Bearer token

Get - /filters:  
Define o nome do campo a ser filtrado ("name", "address", "tutor_name", "tutor_email") e palavra chave da busca.

```json
{
  "field": "xxx",
  "word": "yyy"
}
```

### Rotas da Grade de Notas Anual:

```python
| Metodo | Rota            | Descricao                    |
|--------|-----------------|------------------------------|
| Get    | /grandegridall  | Buscar todos                 |
| Get    | /gradegrid/{ID} | Buscar por ID                |
| Get    | /gradegrid      | Buscar por estudante e ano   |
| Post   | /gradegrid      | Adicionar                    |
| Put    | /gradegrid/{ID} | Atualizar por ID             |
| Put    | /gradegrid      | Atualizar por estudante e ano|
| Delete | /gradegrid/{ID} | Deletar por ID               |
```

**Campos Rotas:**  
Todos os campos exceto os Marcados com \* usam o cabeçalho de autenticação.  
-Header:  
Authorization: Bearer token

Post - /gradegrid:  
Adiciona notas, as quais são arredondadas para uma casa decimal de forma automática.

```json
{
  "student_id": 1,
  "year": 2000,
  "portuguese": 7.5,
  "mathematics": 7.5,
  "biology": 7.5,
  "geography": 7.5,
  "history": 7.5
}
```

Get - /gradegrid:  
Busca de notas do estudante por ano.

```json
{
  "student_id": 1,
  "year": 2000
}
```

Put - /gradegrid/{ID}:  
Define o nome do campo a ser atualizado ("portuguese", "mathematics", "biology", "geography", "history",) e valor da nota.

```json
{
  "subject": "xxx",
  "scored": 2.5
}
```

Put - /gradegrid:  
Define o id do estudante, ano e nome do campo a ser atualizado ("portuguese", "mathematics", "biology", "geography", "history",) e valor da nota.

```json
{
  "student_id": 1,
  "year": 2000,
  "subject": "biology",
  "scored": 2.5
}
```

## 🔒 Testes

Os testes estão localizados no diretório: /tests  
Para rodar os testes é necessário executar o comando:

```bash
pytest
```

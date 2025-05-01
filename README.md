🔐 OAuth2 Practice - FastAPI + Auth + CRUD
==========================================

Este repositório foi criado como uma prática de implementação de autenticação OAuth2 utilizando **FastAPI**, JWT com `python-jose`, e um CRUD simples de usuários. A estrutura do projeto foi inspirada no padrão **MVC**, semelhante ao que é comumente utilizado com _Spring Boot_ em Java, visando escalabilidade e organização de código.

* * *

📁 Estrutura do Projeto
-----------------------

*   `models/` – Contém os modelos de dados (pydantic e SQLAlchemy)
*   `schemas/` – Define os contratos dos dados (DTOs)
*   `controllers/` – Contém os endpoints da API
*   `services/` – Lógica de negócio (ex: autenticação, CRUD)
*   `repositories/` – Implementação dos bancos de dados
*   `utils/` – Funções auxiliares (como geração e verificação de tokens JWT)

* * *

📌 Funcionalidades
------------------

*   ✅ Autenticação de usuário usando **OAuth2 + JWT**
*   ✅ Criação de tokens de acesso (com tempo de expiração)
*   ✅ Validação de tokens protegendo rotas privadas
*   ✅ CRUD de usuários (falta apenas `PUT/PATCH`)

* * *

⚙️ Tecnologias e Bibliotecas
----------------------------

*   **FastAPI** – Framework web rápido e moderno para construção de APIs
*   **SQLAlchemy** – ORM para comunicação com banco de dados
*   **python-jose** – Biblioteca para gerar e verificar tokens JWT
*   **passlib** – Utilizada para hashing de senhas
*   **pydantic** – Validação e tipagem dos dados
*   **uvicorn** – Servidor ASGI para execução da API

* * *

🚀 Como rodar o projeto
-----------------------

1.  Clone o repositório:

    git clone https://github.com/bielsolosos/OAuth2-Pratice.git

3.  Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
    python -m venv venv
    
    source venv/bin/activate  # Linux/macOS
    
    venv\Scripts\activate     # Windows
```

5.  Instale as dependências:
```bash
    pip install -r requirements.txt
```
7.  Execute a aplicação:
```bash
    uvicorn main:app --reload

```
Ou utilizar a cli do fast api
```bash
    fastapi run dev
```

A API estará disponível em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI).

* * *

🔐 Rotas de Autenticação
------------------------

*   `POST /auth/token` – Gera um token JWT
*   `GET /auth/test` – Rota protegida, exige um token válido

* * *

👤 Rotas de Usuário
-------------------

*   `POST /users` – Cria um novo usuário
*   `GET /users` – Lista todos os usuários
*   `GET /users/{id}` – Busca um usuário por ID
*   `DELETE /users/{id}` – Deleta um usuário

* * *

📎 Observações
--------------

*   O projeto foi deployado com sucesso usando o **Railway**.
*   Foi utilizado como base de uma prática durante uma apresentação interna sobre API REST e uso do Insomnia.
*   Ideal para quem deseja aprender FastAPI + JWT com uma estrutura clara e escalável.

* * *

📬 Contato
----------

Feito com ❤️ por Gabriel (bielsolosos). Em caso de dúvidas, entre em contato pelo LinkedIn ou abra uma issue!
[Linkedin](https://www.linkedin.com/in/gabriel-coutinho-0763922a1/)

# Hashflix

Hashflix é uma plataforma web de streaming de filmes e séries, desenvolvida em Django, com autenticação de usuários, sistema de cadastro, pesquisa, exibição de detalhes de filmes, episódios e perfis personalizados.

## Funcionalidades

- **Homepage** com destaques e navegação.
- **Cadastro e Login de Usuário** (com autenticação e edição de perfil).
- **Listagem de Filmes e Séries** com thumbnails, título, descrição, categoria, views e data de criação.
- **Detalhe de Filmes** com episódios associados.
- **Barra de Pesquisa** para encontrar filmes pelo título.
- **Sistema de logout seguro**.
- **Painel administrativo Django** para gerenciamento dos dados.
- **Templates responsivos** com Bootstrap 5 e Crispy Forms.

## Tecnologias Utilizadas

- Python 3.11+
- Django 5.2+
- SQLite (padrão, mas suporta outros bancos)
- Bootstrap 5 (via crispy-bootstrap5)
- HTML, CSS, JavaScript
- WhiteNoise (para servir arquivos estáticos em produção)

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/hashflix.git
   cd hashflix
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure variáveis de ambiente (opcional para produção):**
   - Crie um arquivo `.env` e defina `DATABASE_URL` se for usar outro banco.

5. **Realize as migrações:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crie um superusuário para acessar o admin:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Rode o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

8. **Acesse no navegador:**
   ```
   http://127.0.0.1:8000/
   ```

## Estrutura de Pastas

```
hashflix/
├── filme/
│   ├── migrations/
│   ├── templates/
│   │   ├── navbar.html
│   │   ├── ...
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── hashflix/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── static/
├── media/
├── manage.py
└── requirements.txt
```

## Personalização

- Para adicionar novas categorias de filmes, edite a tupla `LISTA_CATEGORIAS` em `filme/models.py`.
- Para customizar o visual, edite os arquivos em `templates/` e `static/`.

## Créditos

Desenvolvido por Josué e Hashtag Curso Python.

---

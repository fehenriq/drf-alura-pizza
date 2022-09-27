# Django Rest Framework - Alura Pizza

API Rest usada no site Alura Pizza

## 🔨 Funcionalidades do projeto

API Rest que disponibiliza uma lista de pizzas [nome, descricao, preco, imagem]  
Novas pizzas podem ser adicionadas pelo Django Admin  
O armazenamento das imagens são feitas em um bucket na S3  
Deploy da API feita no <a href="https://drf-alura-pizza.herokuapp.com/">Heroku</a>

## ✔️ Técnicas e tecnologias utilizadas

- `Python`
- `Django`
- `Django Rest Framework`
- `Heroku`
- `S3`

## 🛠️ Abrir e rodar o projeto:

- python -m venv venv
- venv/scripts/activate
- pip install -r requirements.txt
- py manage.py makemigrations
- py manage.py migrate
- py manage.py runserver
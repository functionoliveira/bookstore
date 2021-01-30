# Bookstore
Mini Aplicação que realiza CRUD de livros, consumidores e vendas. 

## Pré Requisitos
- docker

## Como Rodar
- Dentro da pasta backend execute o comando <code>docker-compose build</code>.
- Após finalizar o build execute <code>docker-compose up -d</code>.
- Acesse o docker para rodar as migrations <code>docker exec -it bookstore-api bash</code>.
- Na pasta "/app" execute o comando <code>python manage.py db upgrade</code>.
- Execute <code>docker logs -f --tail=100 bookstore-api</code> caso queira ver os logs da aplicação.

Observação: Caso tenha algum tipo de problema com o banco de dados é possível deletar a pasta db-data e migrations.
- Após deletar rode o comando <code>docker-compose up -d</code>.
- Acesse o docker através do comando docker exec -it bookstore-api bash.
- Já dentro do docker na pasta app execute o comando <code>python manage.py db init</code>.
- Logo após execute <code>python manage.py db migrate</code>
- E por fim execute <code>python manage.py db upgrade</code>
O banco de dados estará zerado com as migrations necessárias para a funcionalidade da aplicação. 
## Rotas

#### Books

```
    {
        "title": "Animal Farm",
        "author": "George Orwell",
        "unit_price": 12.90
    }
```
POST /books/ -> Cria um novo livro
GET /books/ -> Lista todos os livros
GET /books/1/ -> Recupera um livro pelo id

#### Customers 
```
    {
        "full_name": "Mike Johnson",
        "email": "mike.johnson@mail.com",
        "document_type": "SSN",
        "document_number": 58101365,
        "address": "4444 Nuzum Court, Cheektowaga - New York."
    }
```
POST /customers/ -> Cria um novo consumidor
GET /customers/ -> Lista todos os consumidores
GET /customers/1/ -> Recupera um consumidor pelo id

#### Sales
```
    {
        "customers_id": 1,
        "items": [
            {
                "books_id": 1,
                "quantity": 1
            },
            {
                "books_id": 3,
                "quantity": 1
            },
            {
                "books_id": 5,
                "quantity": 1
            }
        ]
    }
```
POST /sales/ -> Cria uma nova venda
GET /sales/ -> Lista todas vendas
GET /sales/1/ -> Recupera uma venda pelo id
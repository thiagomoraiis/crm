# 🎮 CRM project with Django and Django Rest Framework

This is the project of a CRM (Customer Relationship Management) system developed with Django and Django Rest Framework

## System Requirements:

Create a CRM mechanism for any type of company, where it will be possible to register/remove/edit products, as well as define quantity in stock and whenever a sale is made, the stock and the total billing of the company must be updated.

Continue the CRM project, now creating your API. Create endpoints for creating an account and logging in. Create endpoints to list/register/edit/remove products and these endpoints can only be accessed if the user is “logged in”. Create an endpoint to list product details as well as inventory. Create an endpoint to list the company's billing, it should only be accessed by the company owner.

## Structuring

The project contains 4 main apps: core, product, cart and customer

### App core

* Criar conta: localhost:8000/user/api/register/
* Fazer login/obter o access token: localhost:8000/user/api/login/token/
* Obter refresh token: localhost:8000/user/api/login/token/refresh/
* Verificar de o token é valido: localhost:8000/user/api/login/token/verify/

* Listar itens do Inventorio: localhost:8000/inventory/api/v1/
* Inserir item do Inventorio: localhost:8000/inventory/api/v1/create/
* Ver detalhe itens: localhost:8000/inventory/api/v1/detail/<int:id>/
* Atualizar item localhost:8000/inventory/api/v1/update/<int:id>/
* Deletar item localhost:8000/inventory/api/v1/delete/<int:id>/

* Endpoint para ver faturamento total da empresa (so pode ser acessado pelo dono) localhost:8000/billing/api/v1/1/

### App product

* Endpoint para listagem de produtos localhost:8000/products/api/v1/
* Endpoint ver detalhe de um produto localhost:8000/products/api/v1/<int:id>/
* Endpoint para inserir um produto: localhost:8000/products/api/v1/create/
* Endpoint atualizar produto localhost:8000/products/api/v1/update/<int:id>/
* Endpoint deletar produto localhost:8000/products/api/v1/delete/<int:id>/

## 🥳 How to run the project: 
```
# Clone the repository
git clone https://github.com/thiagomoraiis/crm.git
cd crm

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
or
venv\Scripts\activate for Windows

# Install the dependencies
pip install -r requirements.txt 

python3 manage.py runserver
```

#### 🎉 Documentation Used: 
- [Django](https://docs.djangoproject.com/en/4.1/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)


#### 🎉 Templates used: 

- [Home page and shopping cart](https://mdbootstrap.com/)
- [System administration area](https://startbootstrap.com/theme/sb-admin-2)
# 🎮 CRM project with Django and Django Rest Framework

This is the project of a CRM (Customer Relationship Management) system developed with Django and Django Rest Framework

## System Requirements:

### Django

Create a CRM mechanism for any type of company, where it will be possible to register/remove/edit products, as well as define quantity in stock and whenever a sale is made, the stock and the total billing of the company must be updated.

Crie um mecanismo de CRM para qualquer tipo de empresa, onde será possível cadastrar/remover/editar produtos, assim como definir quantidade em estoque e sempre que realizado uma venda o estoque e o faturamento total da empresa deve ser atualizado.

### Django Rest Framework

Continue the CRM project, now creating your API. Create endpoints for creating an account and logging in. Create endpoints to list/register/edit/remove products and these endpoints can only be accessed if the user is “logged in”. Create an endpoint to list product details as well as inventory. Create an endpoint to list the company's billing, it should only be accessed by the company owner.

Dê continuidade ao projeto do CRM, agora criando sua API. Crie endpoints para criar conta e realizar login. Crie endpoints para listar/cadastrar/editar/remover produtos e estes endpoints só poderão ser acessados se o usuário estiver “logado”. Crie um endpoint para listar os detalhes do produto assim como seu estoque. Crie um endpoint para listar o faturamento da empresa, ele só deve ser acessado pelo dono da empresa.

## Como está estruturado

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

#### 🎉 Documentações utilizadas: 
- [Django](https://docs.djangoproject.com/en/4.1/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
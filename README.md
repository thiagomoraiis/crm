# Meu projeto

## Endpoints

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


# Saucedemo-Sensedata
Teste realizado durante o processo seletivo para a SenseData com os seguintes objetivos ao acessar o site https://www.saucedemo.com:
- Realizar login;
- Ordenar os produtos pelo valor (low to high);
- Adicionar os seguintes produtos ao carrinho: Sauce Labs Onesie e
Test.allTheThings() T-Shirt (Red);
- Acessar o carrinho e prosseguir para a conclusão da compra.



### Página de login:

**Descrição:** Um usuário válido deve conseguir acessar o site.

**Condição:** O usuário deverá utilizar um usuário e senha válidos.

**Passos do teste:**
1. Navegar até o site https://www.saucedemo.com
2. Adicionar um nome de usuário no campo *username*.
3. Adicionar a senha no campo *password*.
4. Clicar no botão *login*

**Resultado esperado:** O usuário fará o login e a página com todos os itens será mostrada.



### Página dos itens:

**Descrição:** Alterar o filtro da página para menor ao maior preço e adicionar os itens Sauce Labs Onesie e Test.allTheThings() T-Shirt (Red) ao carrinho.

**Condição:** Usuário deve ter feito o login.

**Passos do teste:**
1. Selecionar a caixa de filtros.
2. Selecionar o filtro *Price (low to high)*.
3. Adicionar os itens ao carrinho através da página inicial.

**Resultado esperado:** Os itens serão mostrados do menor preço ao maior e os dois itens deverão ser adicionados ao carrinho.



### Página de Checkout:

**Descrição:** O usuário deverá conseguir acessar seu carrinho e finalizar sua compra.

**Condição:** O usuário tem itens adicionados ao carrinho.

**Passos do teste:**
1. Acessar o carinho através do ícone no topo da página.
2. Seguir para o checkout.
3. Adicionar o primeiro nome no campo *Fisrt Name*.
4. Adicionar o sobrenome no campo *Last Name*.
5. Adicionar o CEP no campo *Zip/Postal Code*.
6. Seguir para o *checkout overview*.
7. Clicar em *Finish* para prosseguir com a compra.

**Resultado esperado:** O usuário terá sua compra realizada.

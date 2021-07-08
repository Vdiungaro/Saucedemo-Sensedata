import time

class Login:
    def __init__(self, page):
        self.page = page
    
    def navigate(self):
        self.page.goto('https://www.saucedemo.com/') # vai para a pagina

    def login_sucess(self):
        # Adiciona as informações de login
        self.page.fill('//*[@id="user-name"]', 'standard_user')
        self.page.fill('//*[@id="password"]', 'secret_sauce')
        self.page.click('#login-button')
        # verifica o titulo da pagina
        title = self.page.title()
        # se o titulo for Swag Labs temos sucesso no login
        if title == 'Swag Labs':
            print('login realizado com sucesso')

    def sort(self):
        # Seleciona o menu de filtrar
        self.page.click('data-test=product_sort_container')
        time.sleep(2)
        # Seleciona a opção menor ao maior valor
        self.page.keyboard.press('ArrowDown')
        self.page.keyboard.press('ArrowDown')
        self.page.keyboard.press('Enter')
        print('Selecionado do menor valor ao maior')

    def add_cart(self):
        # Adiciona os dois itens ao carrinho atraves da pagina inicial
        self.page.click('data-test=add-to-cart-sauce-labs-onesie')
        print('Adicionado sauce labs onesie ao carrinho com sucesso')
        self.page.click('data-test=add-to-cart-test.allthethings()-t-shirt-(red)')
        print('Adicionado test.allthethings() ao carrinho com sucesso')

    def finish_shopping(self):
        # Realiza o acesso ao carrinho
        self.page.click('id=shopping_cart_container')
        print('Carrinho acessado')
        # Realiza o acesso ao checkout
        self.page.click('id=checkout')
        print('Checkout acessado, esperando adicionar informações')
        # Adiciona as informações pessoais
        self.page.fill('//*[@id="first-name"]', 'Vitor')
        self.page.fill('//*[@id="last-name"]', 'Diungaro')
        self.page.fill('//*[@id="postal-code"]', '17360-000')
        print('Informações adicionadas com sucesso')
        # Confirma as informações e continua a compra
        self.page.click('id=continue')
        print('Checkout Overview, aguardando termino')
        # Finaliza a compra
        self.page.click('id=finish')
        print('Compra finalizada')

    
        


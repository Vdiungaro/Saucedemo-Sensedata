from models import Login
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch() #headless=False para ver o browser, slow_mo=1200 para diminuir a velocidade
    page = browser.new_page() #gera nova pagina do browser selecionado
    login_page = Login(page)
    login_page.navigate()
    login_page.login_sucess()
    login_page.sort()
    login_page.add_cart()
    login_page.finish_shopping()
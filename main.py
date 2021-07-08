from models import SauceDemo
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch() #headless=False para ver o browser, slow_mo=1200 para diminuir a velocidade
    page = browser.new_page() #gera nova pagina do browser selecionado
    test_page = SauceDemo(page)
    test_page.navigate()
    test_page.login_sucess()
    test_page.sort()
    test_page.add_cart()
    test_page.finish_shopping()
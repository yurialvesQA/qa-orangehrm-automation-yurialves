# -*- coding: utf-8 -*-
"""
Configuração do ambiente para Behave
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


def before_all(context):
    """Configuração antes de todos os testes"""
    # Configurar Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Verificar se deve rodar em headless
    if os.getenv('HEADLESS', 'false').lower() == 'true':
        chrome_options.add_argument("--headless")
    
    # Criar driver
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def after_all(context):
    """Limpeza após todos os testes"""
    if hasattr(context, 'driver'):
        context.driver.quit()


def before_scenario(context, scenario):
    """Configuração antes de cada cenário"""
    # Limpar cookies
    context.driver.delete_all_cookies()


def after_scenario(context, scenario):
    """Limpeza após cada cenário"""
    # Capturar screenshot em caso de falha
    if scenario.status == "failed":
        screenshot_name = f"failed_{scenario.name.replace(' ', '_')}.png"
        context.driver.save_screenshot(f"results/screenshots/{screenshot_name}")
        print(f"Screenshot salvo: {screenshot_name}")
    
    # Limpar cookies
    context.driver.delete_all_cookies()

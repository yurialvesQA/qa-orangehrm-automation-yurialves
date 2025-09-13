# -*- coding: utf-8 -*-
"""
Page Object Model para a página de Login do OrangeHRM
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LoginPage:
    """Classe que representa a página de login do OrangeHRM"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators
        self.username_field = (By.XPATH, "//input[@name='username']")
        self.password_field = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.error_message = (By.XPATH, "//div[@class='oxd-alert-content oxd-alert-content--error']//p")
        self.login_title = (By.XPATH, "//h5[text()='Login']")
        self.forgot_password_link = (By.XPATH, "//p[text()='Forgot your password?']")
        
    def is_login_page_loaded(self):
        """Verifica se a página de login foi carregada"""
        try:
            self.wait.until(EC.presence_of_element_located(self.login_title))
            return True
        except TimeoutException:
            return False
    
    def enter_username(self, username):
        """Insere o nome de usuário"""
        try:
            username_element = self.wait.until(EC.element_to_be_clickable(self.username_field))
            username_element.clear()
            username_element.send_keys(username)
            return True
        except TimeoutException:
            return False
    
    def enter_password(self, password):
        """Insere a senha"""
        try:
            password_element = self.wait.until(EC.element_to_be_clickable(self.password_field))
            password_element.clear()
            password_element.send_keys(password)
            return True
        except TimeoutException:
            return False
    
    def click_login_button(self):
        """Clica no botão de login"""
        try:
            login_btn = self.wait.until(EC.element_to_be_clickable(self.login_button))
            login_btn.click()
            return True
        except TimeoutException:
            return False
    
    def login(self, username, password):
        """Realiza o login completo"""
        if self.enter_username(username) and self.enter_password(password):
            return self.click_login_button()
        return False
    
    def get_error_message(self):
        """Obtém a mensagem de erro"""
        try:
            error_element = self.wait.until(EC.presence_of_element_located(self.error_message))
            return error_element.text
        except TimeoutException:
            return None
    
    def is_error_message_displayed(self):
        """Verifica se a mensagem de erro está sendo exibida"""
        try:
            self.wait.until(EC.presence_of_element_located(self.error_message))
            return True
        except TimeoutException:
            return False
    
    def click_forgot_password(self):
        """Clica no link 'Forgot your password?'"""
        try:
            forgot_link = self.wait.until(EC.element_to_be_clickable(self.forgot_password_link))
            forgot_link.click()
            return True
        except TimeoutException:
            return False
    
    def get_page_title(self):
        """Obtém o título da página"""
        return self.driver.title
    
    def get_current_url(self):
        """Obtém a URL atual"""
        return self.driver.current_url

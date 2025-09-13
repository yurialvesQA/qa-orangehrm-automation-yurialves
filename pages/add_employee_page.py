# -*- coding: utf-8 -*-
"""
Page Object Model para a página Add Employee do OrangeHRM
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class AddEmployeePage:
    """Classe que representa a página Add Employee do OrangeHRM"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators
        self.page_title = (By.XPATH, "//h6[text()='Add Employee']")
        self.first_name_field = (By.XPATH, "//input[@placeholder='First Name']")
        self.middle_name_field = (By.XPATH, "//input[@placeholder='Middle Name']")
        self.last_name_field = (By.XPATH, "//input[@placeholder='Last Name']")
        self.employee_id_field = (By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//input")
        self.create_login_details_checkbox = (By.XPATH, "//input[@type='checkbox']")
        self.username_field = (By.XPATH, "//div[@class='oxd-form-row']//input[@autocomplete='off']")
        self.password_field = (By.XPATH, "//div[@class='oxd-form-row user-password-row']//input[@type='password']")
        self.confirm_password_field = (By.XPATH, "//div[@class='oxd-form-row user-password-row']//input[@type='password']")
        self.enabled_radio = (By.XPATH, "//input[@value='1']")
        self.disabled_radio = (By.XPATH, "//input[@value='0']")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.cancel_button = (By.XPATH, "//button[@type='button' and text()='Cancel']")
        self.required_field_message = (By.XPATH, "//span[text()='Required']")
        self.success_message = (By.XPATH, "//div[contains(@class,'oxd-toast')]//p[text()='Successfully Saved']")
        self.profile_picture_upload = (By.XPATH, "//input[@type='file']")
        self.profile_picture_button = (By.XPATH, "//button[contains(@class,'employee-image-wrapper')]")
        
    def is_add_employee_page_loaded(self):
        """Verifica se a página Add Employee foi carregada"""
        try:
            self.wait.until(EC.presence_of_element_located(self.page_title))
            return True
        except TimeoutException:
            return False
    
    def get_page_title(self):
        """Obtém o título da página"""
        try:
            title_element = self.wait.until(EC.presence_of_element_located(self.page_title))
            return title_element.text
        except TimeoutException:
            return None
    
    def enter_first_name(self, first_name):
        """Insere o primeiro nome"""
        try:
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.first_name_field))
            first_name_field.clear()
            first_name_field.send_keys(first_name)
            return True
        except TimeoutException:
            return False
    
    def enter_middle_name(self, middle_name):
        """Insere o nome do meio"""
        try:
            middle_name_field = self.wait.until(EC.element_to_be_clickable(self.middle_name_field))
            middle_name_field.clear()
            middle_name_field.send_keys(middle_name)
            return True
        except TimeoutException:
            return False
    
    def enter_last_name(self, last_name):
        """Insere o sobrenome"""
        try:
            last_name_field = self.wait.until(EC.element_to_be_clickable(self.last_name_field))
            last_name_field.clear()
            last_name_field.send_keys(last_name)
            return True
        except TimeoutException:
            return False
    
    def enter_employee_id(self, employee_id):
        """Insere o ID do funcionário"""
        try:
            employee_id_field = self.wait.until(EC.element_to_be_clickable(self.employee_id_field))
            employee_id_field.clear()
            employee_id_field.send_keys(employee_id)
            return True
        except TimeoutException:
            return False
    
    def get_employee_id_value(self):
        """Obtém o valor do campo Employee ID"""
        try:
            employee_id_field = self.wait.until(EC.presence_of_element_located(self.employee_id_field))
            return employee_id_field.get_attribute('value')
        except TimeoutException:
            return None
    
    def check_create_login_details(self):
        """Marca o checkbox para criar detalhes de login"""
        try:
            checkbox = self.wait.until(EC.element_to_be_clickable(self.create_login_details_checkbox))
            if not checkbox.is_selected():
                checkbox.click()
            return True
        except TimeoutException:
            return False
    
    def uncheck_create_login_details(self):
        """Desmarca o checkbox para criar detalhes de login"""
        try:
            checkbox = self.wait.until(EC.element_to_be_clickable(self.create_login_details_checkbox))
            if checkbox.is_selected():
                checkbox.click()
            return True
        except TimeoutException:
            return False
    
    def is_login_details_section_visible(self):
        """Verifica se a seção de detalhes de login está visível"""
        try:
            self.wait.until(EC.presence_of_element_located(self.username_field))
            return True
        except TimeoutException:
            return False
    
    def enter_username(self, username):
        """Insere o nome de usuário"""
        try:
            username_field = self.wait.until(EC.element_to_be_clickable(self.username_field))
            username_field.clear()
            username_field.send_keys(username)
            return True
        except TimeoutException:
            return False
    
    def enter_password(self, password):
        """Insere a senha"""
        try:
            password_field = self.wait.until(EC.element_to_be_clickable(self.password_field))
            password_field.clear()
            password_field.send_keys(password)
            return True
        except TimeoutException:
            return False
    
    def enter_confirm_password(self, password):
        """Insere a confirmação da senha"""
        try:
            confirm_password_field = self.wait.until(EC.element_to_be_clickable(self.confirm_password_field))
            confirm_password_field.clear()
            confirm_password_field.send_keys(password)
            return True
        except TimeoutException:
            return False
    
    def select_enabled_status(self):
        """Seleciona status Enabled"""
        try:
            enabled_radio = self.wait.until(EC.element_to_be_clickable(self.enabled_radio))
            enabled_radio.click()
            return True
        except TimeoutException:
            return False
    
    def select_disabled_status(self):
        """Seleciona status Disabled"""
        try:
            disabled_radio = self.wait.until(EC.element_to_be_clickable(self.disabled_radio))
            disabled_radio.click()
            return True
        except TimeoutException:
            return False
    
    def click_save_button(self):
        """Clica no botão Save"""
        try:
            save_btn = self.wait.until(EC.element_to_be_clickable(self.save_button))
            save_btn.click()
            return True
        except TimeoutException:
            return False
    
    def click_cancel_button(self):
        """Clica no botão Cancel"""
        try:
            cancel_btn = self.wait.until(EC.element_to_be_clickable(self.cancel_button))
            cancel_btn.click()
            return True
        except TimeoutException:
            return False
    
    def add_employee_basic_info(self, first_name, middle_name, last_name, employee_id=None):
        """Adiciona informações básicas do funcionário"""
        success = True
        success &= self.enter_first_name(first_name)
        success &= self.enter_middle_name(middle_name)
        success &= self.enter_last_name(last_name)
        
        if employee_id:
            success &= self.enter_employee_id(employee_id)
        
        return success
    
    def add_employee_with_login(self, first_name, middle_name, last_name, username, password, employee_id=None):
        """Adiciona funcionário com detalhes de login"""
        success = self.add_employee_basic_info(first_name, middle_name, last_name, employee_id)
        if success:
            success &= self.check_create_login_details()
            if self.is_login_details_section_visible():
                success &= self.enter_username(username)
                success &= self.enter_password(password)
                success &= self.enter_confirm_password(password)
                success &= self.select_enabled_status()
        return success
    
    def is_required_field_error_displayed(self):
        """Verifica se a mensagem de campo obrigatório está sendo exibida"""
        try:
            self.wait.until(EC.presence_of_element_located(self.required_field_message))
            return True
        except TimeoutException:
            return False
    
    def get_required_field_errors(self):
        """Obtém todas as mensagens de campo obrigatório"""
        try:
            error_elements = self.driver.find_elements(*self.required_field_message)
            return [element.text for element in error_elements]
        except NoSuchElementException:
            return []
    
    def is_success_message_displayed(self):
        """Verifica se a mensagem de sucesso está sendo exibida"""
        try:
            self.wait.until(EC.presence_of_element_located(self.success_message))
            return True
        except TimeoutException:
            return False
    
    def get_success_message(self):
        """Obtém a mensagem de sucesso"""
        try:
            success_element = self.wait.until(EC.presence_of_element_located(self.success_message))
            return success_element.text
        except TimeoutException:
            return None
    
    def upload_profile_picture(self, file_path):
        """Faz upload da foto de perfil"""
        try:
            file_input = self.wait.until(EC.presence_of_element_located(self.profile_picture_upload))
            file_input.send_keys(file_path)
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """Obtém a URL atual"""
        return self.driver.current_url

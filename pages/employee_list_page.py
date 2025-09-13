# -*- coding: utf-8 -*-
"""
Page Object Model para a página Employee List do OrangeHRM
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class EmployeeListPage:
    """Classe que representa a página Employee List do OrangeHRM"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators
        self.page_title = (By.XPATH, "//h6[text()='PIM']")
        self.add_button = (By.XPATH, "//button[contains(@class,'oxd-button--secondary') and contains(.,'Add')]")
        self.employee_name_field = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.employee_id_field = (By.XPATH, "//label[text()='Employee Id']/following-sibling::div//input")
        self.employment_status_dropdown = (By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
        self.include_dropdown = (By.XPATH, "//div[contains(@class,'oxd-select-text') and contains(text(),'Current Employees Only')]")
        self.supervisor_name_field = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.job_title_dropdown = (By.XPATH, "//div[contains(@class,'oxd-select-text') and contains(text(),'-- Select --')]")
        self.sub_unit_dropdown = (By.XPATH, "//div[contains(@class,'oxd-select-text') and contains(text(),'-- Select --')]")
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.reset_button = (By.XPATH, "//button[@type='reset']")
        
        # Table locators
        self.employee_table = (By.XPATH, "//table")
        self.table_rows = (By.XPATH, "//table//tbody//tr")
        self.employee_id_column = (By.XPATH, "//table//tbody//tr//td[2]")
        self.first_name_column = (By.XPATH, "//table//tbody//tr//td[3]")
        self.last_name_column = (By.XPATH, "//table//tbody//tr//td[4]")
        
        # Action buttons
        self.edit_button = (By.XPATH, "//button[@title='Edit']")
        self.delete_button = (By.XPATH, "//button[@title='Delete']")
        
        # Pagination
        self.pagination_info = (By.XPATH, "//span[@class='oxd-text oxd-text--span']")
        self.next_page_button = (By.XPATH, "//button[@title='Next']")
        self.previous_page_button = (By.XPATH, "//button[@title='Previous']")
        
    def is_employee_list_loaded(self):
        """Verifica se a página Employee List foi carregada"""
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
    
    def click_add_button(self):
        """Clica no botão Add"""
        try:
            add_btn = self.wait.until(EC.element_to_be_clickable(self.add_button))
            add_btn.click()
            return True
        except TimeoutException:
            return False
    
    def search_employee_by_name(self, employee_name):
        """Busca funcionário por nome"""
        try:
            name_field = self.wait.until(EC.element_to_be_clickable(self.employee_name_field))
            name_field.clear()
            name_field.send_keys(employee_name)
            search_btn = self.wait.until(EC.element_to_be_clickable(self.search_button))
            search_btn.click()
            return True
        except TimeoutException:
            return False
    
    def search_employee_by_id(self, employee_id):
        """Busca funcionário por ID"""
        try:
            id_field = self.wait.until(EC.element_to_be_clickable(self.employee_id_field))
            id_field.clear()
            id_field.send_keys(employee_id)
            search_btn = self.wait.until(EC.element_to_be_clickable(self.search_button))
            search_btn.click()
            return True
        except TimeoutException:
            return False
    
    def clear_search_filters(self):
        """Limpa os filtros de busca"""
        try:
            reset_btn = self.wait.until(EC.element_to_be_clickable(self.reset_button))
            reset_btn.click()
            return True
        except TimeoutException:
            return False
    
    def get_employee_count(self):
        """Obtém o número de funcionários encontrados"""
        try:
            pagination_info = self.wait.until(EC.presence_of_element_located(self.pagination_info))
            text = pagination_info.text
            # Extrai o número de registros do texto
            import re
            match = re.search(r'\((\d+)\)', text)
            if match:
                return int(match.group(1))
            return 0
        except TimeoutException:
            return 0
    
    def is_employee_in_table(self, employee_name):
        """Verifica se o funcionário está na tabela"""
        try:
            # Procura por linhas que contenham o nome do funcionário
            employee_elements = self.driver.find_elements(By.XPATH, f"//div[@class='oxd-table-body']//div[@class='oxd-table-card']//div[contains(text(),'{employee_name}')]")
            return len(employee_elements) > 0
        except NoSuchElementException:
            return False
    
    def get_employee_data_from_table(self, row_index=0):
        """Obtém dados do funcionário da tabela"""
        try:
            rows = self.driver.find_elements(*self.table_rows)
            if row_index < len(rows):
                row = rows[row_index]
                employee_id = row.find_element(By.XPATH, ".//div[2]").text
                first_name = row.find_element(By.XPATH, ".//div[3]").text
                last_name = row.find_element(By.XPATH, ".//div[4]").text
                return {
                    'employee_id': employee_id,
                    'first_name': first_name,
                    'last_name': last_name
                }
            return None
        except (NoSuchElementException, IndexError):
            return None
    
    def click_edit_employee(self, row_index=0):
        """Clica no botão de editar funcionário"""
        try:
            rows = self.driver.find_elements(*self.table_rows)
            if row_index < len(rows):
                row = rows[row_index]
                edit_btn = row.find_element(By.XPATH, ".//button[@title='Edit']")
                edit_btn.click()
                return True
            return False
        except (NoSuchElementException, IndexError):
            return False
    
    def click_delete_employee(self, row_index=0):
        """Clica no botão de deletar funcionário"""
        try:
            rows = self.driver.find_elements(*self.table_rows)
            if row_index < len(rows):
                row = rows[row_index]
                delete_btn = row.find_element(By.XPATH, ".//button[@title='Delete']")
                delete_btn.click()
                return True
            return False
        except (NoSuchElementException, IndexError):
            return False
    
    def get_table_data(self):
        """Obtém todos os dados da tabela"""
        try:
            rows = self.driver.find_elements(*self.table_rows)
            table_data = []
            for row in rows:
                try:
                    employee_id = row.find_element(By.XPATH, ".//div[2]").text
                    first_name = row.find_element(By.XPATH, ".//div[3]").text
                    last_name = row.find_element(By.XPATH, ".//div[4]").text
                    table_data.append({
                        'employee_id': employee_id,
                        'first_name': first_name,
                        'last_name': last_name
                    })
                except NoSuchElementException:
                    continue
            return table_data
        except NoSuchElementException:
            return []
    
    def wait_for_table_load(self):
        """Aguarda o carregamento da tabela"""
        try:
            self.wait.until(EC.presence_of_element_located(self.employee_table))
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """Obtém a URL atual"""
        return self.driver.current_url

# -*- coding: utf-8 -*-
"""
Page Object Model para a página Dashboard do OrangeHRM
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class DashboardPage:
    """Classe que representa a página Dashboard do OrangeHRM"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators
        self.dashboard_title = (By.XPATH, "//h6[text()='Dashboard']")
        self.user_dropdown = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        self.logout_link = (By.XPATH, "//a[text()='Logout']")
        self.pim_menu = (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
        self.admin_menu = (By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']")
        self.leave_menu = (By.XPATH, "//a[@href='/web/index.php/leave/viewLeaveModule']")
        self.time_menu = (By.XPATH, "//a[@href='/web/index.php/time/viewTimeModule']")
        self.recruitment_menu = (By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']")
        self.my_info_menu = (By.XPATH, "//a[@href='/web/index.php/pim/viewMyDetails']")
        self.performance_menu = (By.XPATH, "//a[@href='/web/index.php/performance/viewPerformanceModule']")
        self.directory_menu = (By.XPATH, "//a[@href='/web/index.php/directory/viewDirectory']")
        self.maintenance_menu = (By.XPATH, "//a[@href='/web/index.php/maintenance/viewMaintenanceModule']")
        self.claim_menu = (By.XPATH, "//a[@href='/web/index.php/claim/viewClaimModule']")
        self.buzz_menu = (By.XPATH, "//a[@href='/web/index.php/buzz/viewBuzz']")
        
        # Quick Launch locators
        self.assign_leave_btn = (By.XPATH, "//button[@title='Assign Leave']")
        self.leave_list_btn = (By.XPATH, "//button[@title='Leave List']")
        self.timesheets_btn = (By.XPATH, "//button[@title='Timesheets']")
        self.apply_leave_btn = (By.XPATH, "//button[@title='Apply Leave']")
        self.my_leave_btn = (By.XPATH, "//button[@title='My Leave']")
        self.my_timesheet_btn = (By.XPATH, "//button[@title='My Timesheet']")
        
    def is_dashboard_loaded(self):
        """Verifica se a página Dashboard foi carregada"""
        try:
            self.wait.until(EC.presence_of_element_located(self.dashboard_title))
            return True
        except TimeoutException:
            return False
    
    def get_dashboard_title(self):
        """Obtém o título do Dashboard"""
        try:
            title_element = self.wait.until(EC.presence_of_element_located(self.dashboard_title))
            return title_element.text
        except TimeoutException:
            return None
    
    def click_user_dropdown(self):
        """Clica no dropdown do usuário"""
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(self.user_dropdown))
            dropdown.click()
            return True
        except TimeoutException:
            return False
    
    def click_logout(self):
        """Realiza logout do sistema"""
        try:
            if self.click_user_dropdown():
                logout_link = self.wait.until(EC.element_to_be_clickable(self.logout_link))
                logout_link.click()
                return True
            return False
        except TimeoutException:
            return False
    
    def click_pim_menu(self):
        """Clica no menu PIM"""
        try:
            pim_menu = self.wait.until(EC.element_to_be_clickable(self.pim_menu))
            pim_menu.click()
            return True
        except TimeoutException:
            return False
    
    def click_admin_menu(self):
        """Clica no menu Admin"""
        try:
            admin_menu = self.wait.until(EC.element_to_be_clickable(self.admin_menu))
            admin_menu.click()
            return True
        except TimeoutException:
            return False
    
    def click_leave_menu(self):
        """Clica no menu Leave"""
        try:
            leave_menu = self.wait.until(EC.element_to_be_clickable(self.leave_menu))
            leave_menu.click()
            return True
        except TimeoutException:
            return False
    
    def click_time_menu(self):
        """Clica no menu Time"""
        try:
            time_menu = self.wait.until(EC.element_to_be_clickable(self.time_menu))
            time_menu.click()
            return True
        except TimeoutException:
            return False
    
    def click_recruitment_menu(self):
        """Clica no menu Recruitment"""
        try:
            recruitment_menu = self.wait.until(EC.element_to_be_clickable(self.recruitment_menu))
            recruitment_menu.click()
            return True
        except TimeoutException:
            return False
    
    def click_my_info_menu(self):
        """Clica no menu My Info"""
        try:
            my_info_menu = self.wait.until(EC.element_to_be_clickable(self.my_info_menu))
            my_info_menu.click()
            return True
        except TimeoutException:
            return False
    
    def click_performance_menu(self):
        """Clica no menu Performance"""
        try:
            performance_menu = self.wait.until(EC.element_to_be_clickable(self.performance_menu))
            performance_menu.click()
            return True
        except TimeoutException:
            return False
    
    def click_directory_menu(self):
        """Clica no menu Directory"""
        try:
            directory_menu = self.wait.until(EC.element_to_be_clickable(self.directory_menu))
            directory_menu.click()
            return True
        except TimeoutException:
            return False
    
    def click_maintenance_menu(self):
        """Clica no menu Maintenance"""
        try:
            maintenance_menu = self.wait.until(EC.element_to_be_clickable(self.maintenance_menu))
            maintenance_menu.click()
            return True
        except TimeoutException:
            return False
    
    def click_claim_menu(self):
        """Clica no menu Claim"""
        try:
            claim_menu = self.wait.until(EC.element_to_be_clickable(self.claim_menu))
            claim_menu.click()
            return True
        except TimeoutException:
            return False
    
    def click_buzz_menu(self):
        """Clica no menu Buzz"""
        try:
            buzz_menu = self.wait.until(EC.element_to_be_clickable(self.buzz_menu))
            buzz_menu.click()
            return True
        except TimeoutException:
            return False
    
    def get_user_name(self):
        """Obtém o nome do usuário logado"""
        try:
            user_element = self.wait.until(EC.presence_of_element_located(self.user_dropdown))
            return user_element.text
        except TimeoutException:
            return None
    
    def is_quick_launch_visible(self):
        """Verifica se a seção Quick Launch está visível"""
        try:
            self.wait.until(EC.presence_of_element_located(self.assign_leave_btn))
            return True
        except TimeoutException:
            return False
    
    def get_page_title(self):
        """Obtém o título da página"""
        return self.driver.title
    
    def get_current_url(self):
        """Obtém a URL atual"""
        return self.driver.current_url

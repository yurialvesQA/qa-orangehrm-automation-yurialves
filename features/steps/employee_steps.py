# -*- coding: utf-8 -*-
"""
Step definitions para os cenários de funcionários
"""

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.dashboard_page import DashboardPage
from pages.employee_list_page import EmployeeListPage
from pages.add_employee_page import AddEmployeePage


@given('que estou logado no sistema OrangeHRM')
def step_logged_in_to_orangehrm(context):
    """Realiza login no sistema OrangeHRM"""
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    from pages.login_page import LoginPage
    context.login_page = LoginPage(context.driver)
    context.login_page.login("Admin", "admin123")
    context.dashboard_page = DashboardPage(context.driver)
    assert context.dashboard_page.is_dashboard_loaded(), "Dashboard não foi carregado"


@given('que existe um funcionário cadastrado "{employee_name}"')
def step_employee_exists(context, employee_name):
    """Verifica se existe um funcionário cadastrado"""
    # Navegar para PIM
    context.dashboard_page.click_pim_menu()
    context.employee_list_page = EmployeeListPage(context.driver)
    
    # Buscar pelo funcionário
    names = employee_name.split()
    first_name = names[0]
    context.employee_list_page.search_employee_by_name(first_name)
    
    # Verificar se existe
    assert context.employee_list_page.is_employee_in_table(first_name), f"Funcionário '{employee_name}' não encontrado"


@given('que existe um funcionário cadastrado com ID "{employee_id}"')
def step_employee_exists_with_id(context, employee_id):
    """Cria um funcionário com ID específico para teste"""
    # Navegar para PIM
    context.dashboard_page.click_pim_menu()
    context.employee_list_page = EmployeeListPage(context.driver)
    
    # Clicar em Add Employee
    context.employee_list_page.click_add_button()
    context.add_employee_page = AddEmployeePage(context.driver)
    
    # Preencher dados do funcionário
    context.add_employee_page.enter_first_name("Teste")
    context.add_employee_page.enter_last_name("ID")
    context.add_employee_page.enter_employee_id(employee_id)
    
    # Salvar
    context.add_employee_page.click_save_button()
    
    # Aguardar mensagem de sucesso
    import time
    time.sleep(3)
    
    # Armazenar o ID para uso posterior
    context.test_employee_id = employee_id


@when('eu navego para o módulo PIM')
def step_navigate_to_pim(context):
    """Navega para o módulo PIM"""
    context.dashboard_page.click_pim_menu()
    context.employee_list_page = EmployeeListPage(context.driver)
    assert context.employee_list_page.is_employee_list_loaded(), "Página PIM não foi carregada"


@when('eu clico em "Add Employee"')
def step_click_add_employee(context):
    """Clica no botão Add Employee"""
    context.employee_list_page.click_add_button()
    context.add_employee_page = AddEmployeePage(context.driver)
    assert context.add_employee_page.is_add_employee_page_loaded(), "Página Add Employee não foi carregada"


@when('eu clico no botão "Save"')
def step_click_save_button(context):
    """Clica no botão Save"""
    context.add_employee_page.click_save_button()


@when('eu clico no botão "Search"')
def step_click_search_button(context):
    """Clica no botão Search"""
    context.employee_list_page.search_employee_by_name("")  # Busca vazia para executar a busca


@when('eu clico no botão "Reset"')
def step_click_reset_button(context):
    """Clica no botão Reset"""
    context.employee_list_page.clear_search_filters()


@when('eu preencho o campo de busca com "{search_text}"')
def step_fill_search_field(context, search_text):
    """Preenche o campo de busca com texto específico"""
    context.employee_list_page.search_employee_by_name(search_text)


@when('eu preencho o primeiro nome "{first_name}"')
def step_fill_first_name(context, first_name):
    """Preenche o primeiro nome"""
    context.add_employee_page.enter_first_name(first_name)


@when('eu preencho o nome do meio "{middle_name}"')
def step_fill_middle_name(context, middle_name):
    """Preenche o nome do meio"""
    context.add_employee_page.enter_middle_name(middle_name)


@when('eu preencho o sobrenome "{last_name}"')
def step_fill_last_name(context, last_name):
    """Preenche o sobrenome"""
    context.add_employee_page.enter_last_name(last_name)


@when('eu marco o checkbox "{checkbox_text}"')
def step_check_checkbox(context, checkbox_text):
    """Marca checkbox"""
    if checkbox_text == "Create Login Details":
        context.add_employee_page.check_create_login_details()


@when('eu preencho o username "{username}"')
def step_fill_username(context, username):
    """Preenche o username"""
    context.add_employee_page.enter_username(username)


@when('eu preencho a senha "{password}"')
def step_fill_password(context, password):
    """Preenche a senha"""
    context.add_employee_page.enter_password(password)


@when('eu confirmo a senha "{password}"')
def step_confirm_password(context, password):
    """Confirma a senha"""
    context.add_employee_page.enter_confirm_password(password)


@when('eu seleciono o status "{status}"')
def step_select_status(context, status):
    """Seleciona status"""
    if status == "Enabled":
        context.add_employee_page.select_enabled_status()


@when('eu digito "{text}" no campo de busca')
def step_type_in_search_field(context, text):
    """Digita no campo de busca"""
    context.employee_list_page.search_employee_by_name(text)


@when('eu digito "{text}" no campo Employee ID')
def step_type_in_employee_id_field(context, text):
    """Digita no campo Employee ID"""
    context.employee_list_page.search_employee_by_id(text)


@when('eu clico no botão "Save" sem preencher os campos')
def step_click_save_without_fields(context):
    """Clica em Save sem preencher campos"""
    context.add_employee_page.click_save_button()


@then('eu devo ver a mensagem "{message}"')
def step_should_see_message(context, message):
    """Verifica se a mensagem está visível"""
    if message == "Successfully Saved":
        assert context.add_employee_page.is_success_message_displayed(), f"Mensagem '{message}' não está sendo exibida"
    elif message == "Required":
        assert context.add_employee_page.is_required_field_error_displayed(), f"Mensagem '{message}' não está sendo exibida"


@then('eu devo ver os dados do funcionário na página')
def step_should_see_employee_data(context):
    """Verifica se os dados do funcionário estão visíveis"""
    # Verificar se a mensagem de sucesso foi exibida (já validada no step anterior)
    # e se estamos na página correta
    import time
    time.sleep(1)  # Aguardar um pouco para a página carregar
    current_url = context.driver.current_url
    assert "addEmployee" in current_url or "viewEmployeeList" in current_url, "Não está na página correta após salvar"


@then('eu devo ver o funcionário "{employee_name}" nos resultados')
def step_should_see_employee_in_results(context, employee_name):
    """Verifica se o funcionário está nos resultados"""
    names = employee_name.split()
    first_name = names[0]
    assert context.employee_list_page.is_employee_in_table(first_name), f"Funcionário '{employee_name}' não encontrado nos resultados"


@then('eu devo ver o funcionário com ID "{employee_id}" nos resultados')
def step_should_see_employee_with_id(context, employee_id):
    """Verifica se o funcionário com ID está nos resultados"""
    import time
    time.sleep(3)  # Aguardar carregamento dos resultados
    
    # Usar o ID armazenado no contexto se disponível
    search_id = getattr(context, 'test_employee_id', employee_id)
    
    # Verificar se o ID específico está nos resultados
    page_source = context.driver.page_source
    assert search_id in page_source, f"Funcionário com ID '{search_id}' não encontrado nos resultados"


@then('eu devo ver mensagens de erro "{message}"')
def step_should_see_error_messages(context, message):
    """Verifica se as mensagens de erro estão visíveis"""
    assert context.add_employee_page.is_required_field_error_displayed(), f"Mensagens de erro '{message}' não estão sendo exibidas"


@then('eu não devo ver nenhum resultado')
def step_should_not_see_results(context):
    """Verifica se não há resultados"""
    employee_count = context.employee_list_page.get_employee_count()
    assert employee_count == 0, f"Esperado 0 resultados, mas encontrado {employee_count}"


@then('eu devo ver a tabela de funcionários')
def step_should_see_employee_table(context):
    """Verifica se a tabela de funcionários está visível"""
    import time
    time.sleep(2)  # Aguardar carregamento da tabela
    page_source = context.driver.page_source
    assert "table" in page_source, "Tabela de funcionários não está visível"


@then('eu devo ver os cabeçalhos das colunas')
def step_should_see_table_headers(context):
    """Verifica se os cabeçalhos das colunas estão visíveis"""
    page_source = context.driver.page_source
    assert "Id" in page_source, "Cabeçalho 'Id' não encontrado"
    assert "First" in page_source and "Name" in page_source, "Cabeçalho 'First (& Middle) Name' não encontrado"
    assert "Last Name" in page_source, "Cabeçalho 'Last Name' não encontrado"


@then('eu devo ver pelo menos um funcionário na lista')
def step_should_see_at_least_one_employee(context):
    """Verifica se há pelo menos um funcionário na lista"""
    employee_count = context.employee_list_page.get_employee_count()
    assert employee_count > 0, f"Esperado pelo menos 1 funcionário, mas encontrado {employee_count}"


@then('os campos de busca devem estar vazios')
def step_search_fields_should_be_empty(context):
    """Verifica se os campos de busca estão vazios"""
    # Verificar se os campos foram limpos
    name_field = context.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
    id_field = context.driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//input")
    
    assert name_field.get_attribute('value') == "", "Campo de nome não está vazio"
    assert id_field.get_attribute('value') == "", "Campo de ID não está vazio"

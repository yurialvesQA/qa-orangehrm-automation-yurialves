*** Settings ***
Documentation    Recursos comuns para todos os testes
Library          SeleniumLibrary
Library          Collections
Library          String
Library          DateTime

*** Variables ***
${BROWSER}              chrome
${HEADLESS}             False
${WINDOW_WIDTH}         1920
${WINDOW_HEIGHT}        1080
${DEFAULT_TIMEOUT}      10

# URLs
${BASE_URL}             https://opensource-demo.orangehrmlive.com
${LOGIN_URL}            https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${DASHBOARD_URL}        https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index
${PIM_URL}              https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList
${ADD_EMPLOYEE_URL}     https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee

# Credenciais
${VALID_USERNAME}       Admin
${VALID_PASSWORD}       admin123
${INVALID_USERNAME}     usuario_invalido
${INVALID_PASSWORD}     senha_invalida

# Timeouts
${LONG_TIMEOUT}         30
${SHORT_TIMEOUT}        5

# Messages
${INVALID_CREDENTIALS_MESSAGE}    Invalid credentials
${SUCCESS_MESSAGE}                Successfully Saved
${REQUIRED_FIELD_MESSAGE}         Required

# File paths
${SCREENSHOTS_DIR}      results/screenshots
${REPORTS_DIR}          results
${ALLURE_RESULTS_DIR}   results/allure-results

*** Keywords ***
Setup Browser
    [Documentation]    Configura e abre o navegador
    Open Browser    about:blank    ${BROWSER}
    Set Window Size    ${WINDOW_WIDTH}    ${WINDOW_HEIGHT}
    Set Selenium Timeout    ${DEFAULT_TIMEOUT}
    Set Selenium Implicit Wait    ${DEFAULT_TIMEOUT}

Teardown Browser
    [Documentation]    Fecha o navegador e limpa recursos
    Close All Browsers

Take Screenshot On Failure
    [Documentation]    Captura screenshot em caso de falha
    [Arguments]    ${test_name}
    ${timestamp}=    Get Current Date    result_format=%Y%m%d_%H%M%S
    ${screenshot_name}=    Set Variable    ${test_name}_${timestamp}.png
    Capture Page Screenshot    ${SCREENSHOTS_DIR}/${screenshot_name}
    Log    Screenshot capturado: ${screenshot_name}

Navigate To Login Page
    [Documentation]    Navega para a página de login
    Go To    ${LOGIN_URL}
    Wait Until Page Contains Element    name:username    timeout=${DEFAULT_TIMEOUT}

Login With Valid Credentials
    [Documentation]    Realiza login com credenciais válidas
    [Arguments]    ${username}=${VALID_USERNAME}    ${password}=${VALID_PASSWORD}
    Input Text    name:username    ${username}
    Input Text    name:password    ${password}
    Click Button    xpath://button[@type='submit']
    Wait Until Page Contains Element    xpath://h6[text()='Dashboard']    timeout=${DEFAULT_TIMEOUT}

Logout From System
    [Documentation]    Realiza logout do sistema
    Click Element    xpath://span[@class='oxd-userdropdown-tab']
    Click Element    xpath://a[text()='Logout']
    Wait Until Page Contains Element    xpath://h5[text()='Login']    timeout=${DEFAULT_TIMEOUT}

Navigate To PIM Module
    [Documentation]    Navega para o módulo PIM
    Click Element    xpath://a[@href='/web/index.php/pim/viewPimModule']
    Wait Until Page Contains Element    xpath://h6[text()='PIM']    timeout=${DEFAULT_TIMEOUT}

Navigate To Add Employee
    [Documentation]    Navega para a página de adicionar funcionário
    Click Element    xpath://button[contains(@class,'oxd-button--secondary') and contains(text(),'Add')]
    Wait Until Page Contains Element    xpath://h6[text()='Add Employee']    timeout=${DEFAULT_TIMEOUT}

Generate Random Employee Data
    [Documentation]    Gera dados aleatórios para funcionário
    ${timestamp}=    Get Current Date    result_format=%Y%m%d%H%M%S
    ${first_name}=    Set Variable    TestUser${timestamp}
    ${last_name}=    Set Variable    TestLastName${timestamp}
    ${employee_id}=    Set Variable    EMP${timestamp}
    [Return]    ${first_name}    ${last_name}    ${employee_id}

Wait For Page Load
    [Documentation]    Aguarda o carregamento completo da página
    Wait Until Page Does Not Contain Element    xpath://div[@class='oxd-loading-spinner']    timeout=${LONG_TIMEOUT}

Wait And Click Element
    [Documentation]    Aguarda elemento estar visível e clica
    [Arguments]    ${locator}    ${timeout}=10
    Wait Until Element Is Visible    ${locator}    timeout=${timeout}
    Click Element    ${locator}

Wait And Input Text
    [Documentation]    Aguarda elemento estar visível e insere texto
    [Arguments]    ${locator}    ${text}    ${timeout}=10
    Wait Until Element Is Visible    ${locator}    timeout=${timeout}
    Clear Element Text    ${locator}
    Input Text    ${locator}    ${text}

Wait And Get Text
    [Documentation]    Aguarda elemento estar visível e obtém texto
    [Arguments]    ${locator}    ${timeout}=10
    Wait Until Element Is Visible    ${locator}    timeout=${timeout}
    ${text}=    Get Text    ${locator}
    [Return]    ${text}

Verify Element Is Present
    [Documentation]    Verifica se elemento está presente na página
    [Arguments]    ${locator}    ${timeout}=10
    Wait Until Element Is Visible    ${locator}    timeout=${timeout}
    Element Should Be Visible    ${locator}

Verify Element Is Not Present
    [Documentation]    Verifica se elemento não está presente na página
    [Arguments]    ${locator}    ${timeout}=10
    Wait Until Element Is Not Visible    ${locator}    timeout=${timeout}
    Element Should Not Be Visible    ${locator}

Verify Text Is Present
    [Documentation]    Verifica se texto está presente na página
    [Arguments]    ${text}    ${timeout}=10
    Wait Until Page Contains    ${text}    timeout=${timeout}
    Page Should Contain    ${text}

Verify Text Is Not Present
    [Documentation]    Verifica se texto não está presente na página
    [Arguments]    ${text}    ${timeout}=10
    Wait Until Page Does Not Contain    ${text}    timeout=${timeout}
    Page Should Not Contain    ${text}

Scroll To Element
    [Documentation]    Faz scroll até o elemento
    [Arguments]    ${locator}
    Scroll Element Into View    ${locator}

Select Dropdown Option
    [Documentation]    Seleciona opção em dropdown
    [Arguments]    ${dropdown_locator}    ${option_text}
    Click Element    ${dropdown_locator}
    Wait And Click Element    xpath://div[@role='option' and contains(text(),'${option_text}')]

Verify URL Contains
    [Documentation]    Verifica se URL contém texto específico
    [Arguments]    ${expected_text}
    ${current_url}=    Get Location
    Should Contain    ${current_url}    ${expected_text}

Generate Random String
    [Documentation]    Gera string aleatória
    [Arguments]    ${length}=8
    ${random_string}=    Generate Random String    ${length}    [LETTERS][NUMBERS]
    [Return]    ${random_string}

Get Current Timestamp
    [Documentation]    Obtém timestamp atual
    ${timestamp}=    Get Current Date    result_format=%Y%m%d_%H%M%S
    [Return]    ${timestamp}

Clear And Input Text
    [Documentation]    Limpa campo e insere texto
    [Arguments]    ${locator}    ${text}
    Clear Element Text    ${locator}
    Input Text    ${locator}    ${text}

Wait For Element To Be Clickable
    [Documentation]    Aguarda elemento estar clicável
    [Arguments]    ${locator}    ${timeout}=10
    Wait Until Element Is Enabled    ${locator}    timeout=${timeout}
    Element Should Be Enabled    ${locator}

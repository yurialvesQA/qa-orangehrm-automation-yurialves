# OrangeHRM Automation Project

Este projeto implementa automação de testes para o sistema OrangeHRM utilizando Robot Framework com padrão Page Object Model (POM) e relatórios Allure.

## 🎯 Objetivo

Avaliar a capacidade de implementar automações de testes de interface com:
- Cobertura de cenários reais
- Padrão Page Object Model (POM)
- Relatórios Allure
- Cenários negativos
- Integração com GitHub Actions

## 🚀 Cenários Automatizados

### Cenários Positivos
1. **Login bem-sucedido** com as credenciais fornecidas
2. **Logout do sistema** após o login
3. **Cadastro de novo funcionário** através do menu PIM > Add Employee
4. **Busca pelo funcionário** recém-cadastrado em PIM > Employee List

### Cenários Negativos
5. **Login inválido** com mensagem de erro validada
6. **Cadastro de funcionário** com campos obrigatórios vazios
7. **Busca de funcionário** inexistente

## 🛠️ Tecnologias Utilizadas

- **Robot Framework** - Framework de automação
- **Selenium Library** - Automação web
- **Page Object Model** - Padrão de design
- **Allure** - Relatórios de teste
- **Behave** - BDD com Gherkin
- **GitHub Actions** - CI/CD

## 📋 Pré-requisitos

- Python 3.8+
- pip
- Chrome/Chromium browser

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone <repository-url>
cd qa-orangehrm-automation-yduartealvesqa
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Execução dos Testes

### Executar todos os testes:
```bash
robot -d results tests/
```

### Executar testes específicos:
```bash
robot -d results tests/login_tests.robot
robot -d results tests/employee_tests.robot
```

### Executar com Allure:
```bash
robot -d results --listener allure_robotframework:results/allure-results tests/
allure serve results/allure-results
```

### Executar com BDD:
```bash
behave features/
```

## 📊 Relatórios

Os relatórios são gerados na pasta `results/`:
- `log.html` - Log detalhado dos testes
- `report.html` - Relatório de resultados
- `output.xml` - Dados em XML
- `allure-results/` - Dados para Allure

## 🏗️ Estrutura do Projeto

```
qa-orangehrm-automation-yduartealvesqa/
├── features/                    # Arquivos BDD (Gherkin)
│   ├── login.feature
│   ├── employee.feature
│   └── steps/
├── pages/                       # Page Objects
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── employee_list_page.py
│   └── add_employee_page.py
├── tests/                       # Testes Robot Framework
│   ├── login_tests.robot
│   ├── employee_tests.robot
│   └── negative_tests.robot
├── resources/                   # Recursos compartilhados
│   ├── keywords/
│   ├── variables/
│   └── common.robot
├── results/                     # Resultados dos testes
├── .github/workflows/           # GitHub Actions
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔑 Credenciais de Teste

- **URL**: https://opensource-demo.orangehrmlive.com
- **Usuário**: Admin
- **Senha**: admin123

## 🚀 CI/CD

O projeto está configurado com GitHub Actions para execução automática dos testes em:
- Push para branch main
- Pull requests
- Agendamento diário

## 📝 Padrões de Desenvolvimento

- **Page Object Model**: Separação de lógica de teste e elementos da página
- **BDD**: Cenários descritos em linguagem natural
- **Allure**: Relatórios visuais e detalhados
- **Clean Code**: Código limpo e bem documentado


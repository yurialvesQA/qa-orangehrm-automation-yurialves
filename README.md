# OrangeHRM Automation Project

Este projeto implementa automação de testes para o sistema OrangeHRM utilizando Robot Framework com padrão Page Object Model (POM), BDD com Behave/Gherkin e relatórios Allure.

## 🎯 Objetivo

Avaliar a capacidade de implementar automações de testes de interface com:
- Cobertura de cenários reais
- Padrão Page Object Model (POM)
- Relatórios Allure
- Cenários negativos
- Integração com GitHub Actions

## 🚀 Cenários Automatizados (14 CTs)

### Login (CT01-CT06)
- **CT01**: Login bem-sucedido com credenciais válidas
- **CT02**: Login com credenciais inválidas
- **CT03**: Login com usuário vazio
- **CT04**: Login com senha vazia
- **CT05**: Logout do sistema após login
- **CT06**: Verificar link "Forgot your password?"

### Employee Management (CT07-CT14)
- **CT07**: Cadastro de novo funcionário com dados válidos
- **CT08**: Cadastro de funcionário com campos obrigatórios
- **CT09**: Navegação para Employee List
- **CT10**: Busca de funcionário por ID
- **CT11**: Busca de funcionário inexistente
- **CT12**: Reset de filtros de busca
- **CT13**: Visualização da tabela de funcionários
- **CT14**: Verificação de cabeçalhos da tabela

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
git clone https://github.com/yurialvesQA/qa-orangehrm-automation-yurialves.git
cd qa-orangehrm-automation-yurialves
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

### Executar todos os cenários BDD:
```bash
behave features/
```

### Executar cenários específicos:
```bash
# Apenas cenários de login
behave features/login.feature

# Apenas cenários de employee
behave features/employee.feature
```

### Executar com relatório Allure:
```bash
# Executar testes com formatter Allure
behave features/ --format allure_behave.formatter:AllureFormatter -o results/allure-results

# Gerar e visualizar relatório
allure generate results/allure-results --clean -o results/allure-report
allure serve results/allure-results
```

### Executar cenários por tag:
```bash
# Executar apenas CT01 (login bem-sucedido)
behave features/ --tags=@CT01

# Executar todos os cenários de login
behave features/ --tags=@login

# Executar todos os cenários de employee
behave features/ --tags=@employee
```

## 📊 Relatórios

Os relatórios são gerados na pasta `results/`:
- `allure-results/` - Dados para relatórios Allure
- `allure-report/` - Relatório HTML do Allure
- `screenshots/` - Screenshots de falhas
- Logs do Behave no terminal

## 🏗️ Estrutura do Projeto

```
qa-orangehrm-automation-yurialves/
├── features/                    # Arquivos BDD (Gherkin)
│   ├── login.feature           # Cenários de login (CT01-CT06)
│   ├── employee.feature        # Cenários de employee (CT07-CT14)
│   ├── environment.py          # Configuração do ambiente
│   └── steps/                  # Step definitions
│       ├── login_steps.py
│       └── employee_steps.py
├── pages/                       # Page Objects
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── employee_list_page.py
│   └── add_employee_page.py
├── resources/                   # Recursos compartilhados
│   └── common.robot            # Configurações e keywords
├── results/                     # Resultados dos testes
│   ├── allure-results/
│   ├── allure-report/
│   └── screenshots/
├── .github/workflows/           # GitHub Actions
│   └── automation-tests.yml
├── requirements.txt
├── allure.properties
├── .gitignore
└── README.md
```

## 🔑 Credenciais de Teste

- **URL**: https://opensource-demo.orangehrmlive.com
- **Usuário**: Admin
- **Senha**: admin123

## 🚀 CI/CD

O projeto está configurado com GitHub Actions para execução automática dos testes em:
- **Push para branch main** - Execução automática
- **Pull requests** - Validação antes do merge
- **Agendamento diário** - Execução às 2:00 AM UTC
- **Matriz de testes** - Python 3.8, 3.9, 3.10 + Chrome/Firefox
- **Relatórios Allure** - Disponíveis nos artifacts

### 📊 Status do Workflow:
- ✅ **6 jobs de teste** - Matriz Python + Browser
- ✅ **Allure instalado** - Relatórios gerados
- ✅ **Artifacts disponíveis** - Para download
- ⏸️ **GitHub Pages** - Desabilitado temporariamente

## 📝 Padrões de Desenvolvimento

- **Page Object Model**: Separação de lógica de teste e elementos da página
- **BDD**: Cenários descritos em linguagem natural
- **Allure**: Relatórios visuais e detalhados
- **Clean Code**: Código limpo e bem documentado

## 🔗 Links Úteis

- **Repositório**: https://github.com/yurialvesQA/qa-orangehrm-automation-yurialves
- **GitHub Actions**: https://github.com/yurialvesQA/qa-orangehrm-automation-yurialves/actions
- **OrangeHRM Demo**: https://opensource-demo.orangehrmlive.com
- **Behave Documentation**: https://behave.readthedocs.io/
- **Allure Documentation**: https://docs.qameta.io/allure/

## 👨‍💻 Autor

**Yuri Alves QA** - [@yurialvesQA](https://github.com/yurialvesQA)

---

⭐ **Se este projeto foi útil, considere dar uma estrela!**


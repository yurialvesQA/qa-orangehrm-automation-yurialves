Feature: Login do OrangeHRM
  Como um usuário do sistema OrangeHRM
  Eu quero poder fazer login no sistema
  Para acessar as funcionalidades disponíveis

  Background:
    Given que estou na página de login do OrangeHRM

  @smoke @positive @CT01
  Scenario: Login bem-sucedido com credenciais válidas
    When eu insiro o username "Admin"
    And eu insiro a senha "admin123"
    And eu clico no botão de login
    Then eu devo ser redirecionado para o dashboard
    And eu devo ver o título "Dashboard"
    And eu devo ver o menu PIM

  @negative @CT02
  Scenario: Login com credenciais inválidas
    When eu insiro o username "usuario_invalido"
    And eu insiro a senha "senha_invalida"
    And eu clico no botão de login
    Then eu devo ver a mensagem de erro "Invalid credentials"
    And eu devo permanecer na página de login

  @negative @CT03
  Scenario: Login com username válido e senha inválida
    When eu insiro o username "Admin"
    And eu insiro a senha "senha_errada"
    And eu clico no botão de login
    Then eu devo ver a mensagem de erro "Invalid credentials"

  @negative @CT04
  Scenario: Login com campos vazios
    When eu clico no botão de login sem preencher os campos
    Then eu devo permanecer na página de login
    And os campos devem estar vazios

  @positive @CT05
  Scenario: Logout do sistema
    Given que estou logado no sistema
    When eu clico no dropdown do usuário
    And eu clico em "Logout"
    Then eu devo ser redirecionado para a página de login
    And eu devo ver o título "Login"

  @ui @CT06
  Scenario: Verificar elementos da página de login
    Then eu devo ver o campo de username
    And eu devo ver o campo de senha
    And eu devo ver o botão de login
    And eu devo ver o link "Forgot your password?"
    And eu devo ver as credenciais de teste

Feature: Gerenciamento de Funcionários
  Como um administrador do sistema OrangeHRM
  Eu quero poder gerenciar funcionários
  Para manter os dados dos colaboradores atualizados

  Background:
    Given que estou logado no sistema OrangeHRM

  @smoke @positive @CT07
  Scenario: Cadastrar novo funcionário
    When eu navego para o módulo PIM
    And eu clico em "Add Employee"
    And eu preencho o primeiro nome "João"
    And eu preencho o nome do meio "Silva"
    And eu preencho o sobrenome "Santos"
    And eu clico no botão "Save"
    Then eu devo ver a mensagem "Successfully Saved"
    And eu devo ver os dados do funcionário na página

  @positive @CT09
  Scenario: Buscar funcionário por nome
    Given que existe um funcionário cadastrado "João Silva Santos"
    When eu navego para o módulo PIM
    And eu digito "João" no campo de busca
    And eu clico no botão "Search"
    Then eu devo ver o funcionário "João Silva Santos" nos resultados

  @positive @CT10
  Scenario: Buscar funcionário por ID
    Given que estou logado no sistema OrangeHRM
    When eu navego para o módulo PIM
    And eu digito "0367" no campo Employee ID
    And eu clico no botão "Search"
    Then eu devo ver o funcionário com ID "0367" nos resultados

  @negative @CT11
  Scenario: Cadastrar funcionário sem campos obrigatórios
    When eu navego para o módulo PIM
    And eu clico em "Add Employee"
    And eu clico no botão "Save" sem preencher os campos
    Then eu devo ver mensagens de erro "Required"

  @negative @CT12
  Scenario: Buscar funcionário inexistente
    When eu navego para o módulo PIM
    And eu digito "FuncionarioInexistente" no campo de busca
    And eu clico no botão "Search"
    Then eu não devo ver nenhum resultado

  @positive @CT13
  Scenario: Verificar lista de funcionários
    When eu navego para o módulo PIM
    Then eu devo ver a tabela de funcionários
    And eu devo ver os cabeçalhos das colunas
    And eu devo ver pelo menos um funcionário na lista

  @positive @CT14
  Scenario: Limpar filtros de busca
    When eu navego para o módulo PIM
    And eu preencho o campo de busca com "Test"
    And eu clico no botão "Reset"
    Then os campos de busca devem estar vazios

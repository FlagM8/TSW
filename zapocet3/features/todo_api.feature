@api
Feature: ToDo API

  Scenario Outline: Přidání nového úkolu
    When pošlu POST na /api/todos s úkolem "<task>"
    Then odpověď má status 201
    And odpověď obsahuje stav "created"

    Examples:
      | task         |
      | Nakoupit     |
      | Uklidit      |
      | Zalít květiny|
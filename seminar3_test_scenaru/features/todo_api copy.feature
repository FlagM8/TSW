Feature: ToDo API

  Scenario: Získání prázdného seznamu úkolů
    When zavolám GET na /api/todos
    Then odpověď obsahuje prázdný seznam

  Scenario: Přidání nového úkolu
    When pošlu POST na /api/todos s úkolem "Nakoupit"
    Then odpověď má status 201
    And odpověď obsahuje stav "created"

  Scenario: Označení úkolu jako dokončený
    Given přidám úkol "Uklidit" přes API
    When pošlu PUT na /api/todos/0
    Then odpověď obsahuje stav "updated"


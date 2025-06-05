Feature: HTML ToDo web

  Scenario: Titulní stránka obsahuje název aplikace
    Given aplikace běží
    When navštívím domovskou stránku
    Then uvidím nadpis "My Tasks"

  Scenario: Přidání úkolu přes HTML formulář
    Given aplikace běží
    When přidám úkol "Zaplatit chat-gpt" přes formulář
    Then uvidím úkol "Zaplatit chat-gpt" na stránce

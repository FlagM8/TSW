@html
Feature: HTML ToDo web

  Scenario Outline: Přidání úkolu přes HTML formulář
    Given aplikace běží
    When přidám úkol "<task>" přes formulář
    Then uvidím úkol "<task>" na stránce

    Examples:
      | task                |
      | Zaplatit chat-gpt   |
      | Udělat úkol z TSW   |
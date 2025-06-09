@html_splinter
Feature: HTML ToDo web přes Splinter

  Scenario: Zobrazení nadpisu na domovské stránce v prohlížeči
    Given aplikace běží
    When otevřu domovskou stránku v prohlížeči
    Then uvidím nadpis "My Tasks" v prohlížeči

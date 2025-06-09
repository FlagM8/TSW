Feature: Načítání nových článků při scrollování

  Scenario: Scroll načte nové články
    Given otevřu stránku s nekonečným scrollováním
    When scroluji na konec stránky a počkám
    Then se načtou nové články

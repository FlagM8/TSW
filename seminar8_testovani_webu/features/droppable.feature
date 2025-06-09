Feature: Drag and drop prvku

  Scenario: Drag and drop prvku mění text na "Dropped!"
    Given otevřu stránku s drag and drop
    When přetáhnu prvek "Drag me to my target" na target
    Then target obsahuje text "Dropped!"

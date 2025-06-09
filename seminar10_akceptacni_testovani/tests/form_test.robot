*** Settings ***
Documentation     Testy v Robot FW
Resource          keywords.robot
Suite Setup       Open Browser To Home
Suite Teardown    Close Browser

*** Variables ***
${HOST}        http://127.0.0.1:5000
${BROWSER}     Chrome
${NAME}        David
${EMAIL}       david@email.cz

*** Test Cases ***
Zobrazení domovské stránky
    Title Should Be    Robot FW hlavni strana

Vyplnění a odeslání formuláře
    Go To    ${HOST}/form
    Fill And Submit Form
    Verify Entry Exists

Mazání dat
    Go To    ${HOST}/reset
    Page Should Contain    Smazano!

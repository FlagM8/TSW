
*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Browser To Home
    Open Browser    ${HOST}    ${BROWSER}
    Maximize Browser Window

Fill And Submit Form
    Input Text    name    ${NAME}
    Input Text    email   ${EMAIL}
    Click Button    Submit

Verify Entry Exists
    Page Should Contain    ${NAME}
    Page Should Contain    ${EMAIL}

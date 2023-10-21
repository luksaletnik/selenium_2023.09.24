# robotframework.org "Builtln & SeleniumLibrary"

*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Keywords ***


*** Test Cases ***
Log In Wikipedia
    Open Browser    https://pl.wikipedia.org    chrome
    Run Keyword And Ignore Error    Click Element    id:non-existent
    Wait Until Element Is Visible    id:pt-login-2    5
    Click Element    id:pt-login-2
    Input Text    id:wpName1    RobotTests
    Input Password    id:wpPassword1    RobotFramework
    Click Button    id:wpLoginAttempt
    Capture Page Screenshot
    Sleep    10

*** Settings ***
Library    Browser

*** Variables ***

${URL}=    https://automationexercise.com
${USER_EMAIL}=     example@dummy.com
${PASSWORD}=    1
${Search Text}=    jeans

${concent field}=    button[class~="fc-cta-consent"]
${email field}=    input[data-qa="login-email"]
${password field}=    input[data-qa="login-password"]
${login button}=    button[data-qa="login-button"]
${search field}=    input[id=search_product]
${search btn}=    button[id=submit_search]
${products selector}=    div[class=single-products]

*** Test Cases ***
Login and Search
    Browser.New Browser    browser=chromium    headless=${True}
    Browser.New Context    viewport={"width": 1920, "height": 1080}
    Browser.New Page    url=${URL}
    Browser.Click    selector=${concent field}
  
    Browser.Go To   url=${URL}/login

    Browser.Fill Text    selector=${email field}    txt=${USER_EMAIL}
    Browser.Fill Text    selector=${password field}    txt=${PASSWORD}

    Browser.Click    selector=${login button}

    Browser.Go To    url=${URL}/products

    Browser.Fill Text    selector=${search field}    txt=${Search Text}
    Browser.Click    selector=${search btn}

    ${products}=    Browser.Get Elements    ${products selector} >> text=${Search Text}
    Should Not Be Empty    ${products}

    Browser.Go To    url=${URL}/logout

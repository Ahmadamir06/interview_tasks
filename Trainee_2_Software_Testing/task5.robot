 
Library    SeleniumLibrary


${URL}          automationexercise.com
${USEREMAIL}    khizraasaf94@gmail.com
${PASSWORD}     Khizra@123
${VALID_QUERY}  Shirts

 
Login 

    Open Browser    ${URL}    chrome
    Sleep    2s
    Maximize Browser Window
    Wait Until Element Is Visible    id:username    10s
    Input Text      id:username    ${USEREMAIL}
    Input Text      id:password    ${PASSWORD}
    Click Button    id:submit
    Page Should Contain    Logged In Successfully
     


 Search Query  

    Input Text      id=search_box    ${VALID_QUERY}
    Click Button    id=search_button
    Page Should Contain    shirts
    

 Logout 

    Click Log_out Button  id:submit1
    Page Should Contain   Logged Out Successfully

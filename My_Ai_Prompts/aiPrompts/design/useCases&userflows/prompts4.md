# Prompts - [useCases&userflows]

## Prompt 1
* **Description:** User provided prompt
* **Prompt ID:** 1
* **Prompt Text:** check at the use cases are u shure graph is something that can be used with mermaid, what would be the best way to represent use cases ?

look at the documentation 
@https://mermaid.js.org/intro/syntax-reference.html
* **AI Tool:** cursor Composer, cloud-3.5-sonnet
* **Date:** 2024-10-22
* **Result Link:** #result-1

## Prompt 2
* **Description:** User provided prompt
* **Prompt ID:** 2
* **Prompt Text:** did not work, are u really reading the we page of mermaid documentation ? 
PS C:\Users\yagua\AI4Devs\Growgrebuddy_PSA\GrowEbuddy_PSA\docs\design\diagrams\use_cases> mmdc -i user_management.mmd -o user_management.png
Generating single mermaid chart
[@zenuml/core] Store is a function and is not initiated in 1 second.

UnknownDiagramError: No diagram type detected matching given configuration for text: ��---      
title: User Management Use Cases
---
flowchart LR
    User((User))
    Admin((Admin))

    User --> Register[Register Account]
    User --> Login[Login]
    User --> ManageProfile[Manage Profile]
    User --> ResetPassword[Reset Password]

    Admin --> ManageUsers[Manage Users]
    Admin --> ViewAnalytics[View User Analytics]

detectType (C:\Users\yagua\AppData\Roaming\npm\node_modules\@mermaid-js\mermaid-cli\node_modules\mermaid\dist\mermaid.js:1526:15)
    at $eval ($eval at renderMermaid (file:///C:/Users/yagua/AppData/Roaming/npm/node_modules/@mermaid-js/mermaid-cli/src/index.js:250:33), <anonymous>:17:45)
    at ExecutionContext.#evaluate (file:///C:/Users/yagua/AppData/Roaming/npm/node_modules/@mermaid-js/mermaid-cli/node_modules/puppeteer-core/lib/esm/puppeteer/cdp/ExecutionContext.js:385:19)
    at async ExecutionContext.evaluate (file:///C:/Users/yagua/AppData/Roaming/npm/node_modules/@mermaid-js/mermaid-cli/node_modules/puppeteer-core/lib/esm/puppeteer/cdp/ExecutionContext.js:272:16)
    at async IsolatedWorld.evaluate (file:///C:/Users/yagua/AppData/Roaming/npm/node_modules/@mermaid-js/mermaid-cli/node_modules/puppeteer-core/lib/esm/puppeteer/cdp/IsolatedWorld.js:97:16)  
    at async CdpJSHandle.evaluate (file:///C:/Users/yagua/AppData/Roaming/npm/node_modules/@mermaid-js/mermaid-cli/node_modules/puppeteer-core/lib/esm/puppeteer/api/JSHandle.js:141:20)        
    at async CdpElementHandle.evaluate (file:///C:/Users/yagua/AppData/Roaming/npm/node_modules/@mermaid-js/mermaid-cli/node_modules/puppeteer-core/lib/esm/puppeteer/api/ElementHandle.js:335:20)
    at async CdpElementHandle.$eval (file:///C:/Users/yagua/AppData/Roaming/npm/node_modules/@mermaid-js/mermaid-cli/node_modules/puppeteer-core/lib/esm/puppeteer/api/ElementHandle.js:489:24) 
    at async CdpFrame.$eval (file:///C:/Users/yagua/AppData/Roaming/npm/node_modules/@mermaid-js/mermaid-cli/node_modules/puppeteer-core/lib/esm/puppeteer/api/Frame.js:443:20)
    at async CdpPage.$eval (file:///C:/Users/yagua/AppData/Roaming/npm/node_modules/@mermaid-js/mermaid-cli/node_modules/puppeteer-core/lib/esm/puppeteer/api/Page.js:445:20)
    at async renderMermaid (file:///C:/Users/yagua/AppData/Roaming/npm/node_modules/@mermaid-js/mermaid-cli/src/index.js:250:22)
* **AI Tool:** cursor Composer, cloud-3.5-sonnet
* **Date:** 2024-10-22
* **Result Link:** #result-1

## Prompt 3
* **Description:** User provided prompt
* **Prompt ID:** 3
* **Prompt Text:** you are not following this recomendations at all @https://mermaid.js.org/intro/syntax-reference.html
* **AI Tool:** cursor Composer, cloud-3.5-sonnet
* **Date:** 2024-10-22
* **Result Link:** #result-1

## Prompt 4
* **Description:** User provided prompt
* **Prompt ID:** 4
* **Prompt Text:** you are still doing something gron check documentation and examples
* **AI Tool:** cursor Composer, cloud-3.5-sonnet
* **Date:** 2024-10-22
* **Result Link:** #result-1

## Prompt 5
* **Description:** User provided prompt
* **Prompt ID:** 5
* **Prompt Text:** why it doesnt work ?
* **AI Tool:** cursor Composer, cloud-3.5-sonnet
* **Date:** 2024-10-22
* **Result Link:** #result-1

## Prompt 6
* **Description:** User provided prompt
* **Prompt ID:** 6
* **Prompt Text:** explain to me why are you representing the use cases like u do
* **AI Tool:** cursor Composer, cloud-3.5-sonnet
* **Date:** 2024-10-22
* **Result Link:** #result-1

## Prompt 7
* **Description:** User provided prompt
* **Prompt ID:** 7
* **Prompt Text:** then why it does render in @https://mermaid.live/  but it doesnt here using mermaid cli comand
* **AI Tool:** cursor Composer, cloud-3.5-sonnet
* **Date:** 2024-10-22
* **Result Link:** #result-1


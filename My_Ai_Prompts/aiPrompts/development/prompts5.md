# Prompts - [development]

## Prompt 1
* **Description:** User provided prompt
* **Prompt ID:** 1
* **Prompt Text:** now As an expert Backend developer who always works applying the best practices and aplicable principles, i want you to look at Ticket DEV-007-2.
- then explain to me what needs to be done and how.
- look at the existing files in the repository @src 
- list  new or main files, and related files that will need changes
- after that apply the changes that you can by yourself
- guide me step by step on whatever thing you can do yourself
- ask me if you need to make sure of anything
- and once we are finished, update the ticket, marking it as done, and filling the results/changes section.

remeber to allways:
- explain from which part of the reposotory should i run terminal codes, 
- give code for our enviroment, cursor ide on  windows,
- add comments explain the code you create

@Codebase
* **AI Tool:** cursor Composer, cursor-small
* **Date:** 2024-11-17
* **Result Link:** #result-1

## Prompt 2
* **Description:** User provided prompt
* **Prompt ID:** 2
* **Prompt Text:** about step 4 "Update models.py if necessary to ensure the Vpet model is correctly defined.
" i don´t have a models.py, i just have a schema.prisma file
¿what should we do?
* **AI Tool:** cursor Composer, cursor-small
* **Date:** 2024-11-17
* **Result Link:** #result-1

## Prompt 3
* **Description:** User provided prompt
* **Prompt ID:** 3
* **Prompt Text:** what about the main and related fiels with references to the innexisting model.py file sinceh we are using primsa? like 
from .models import Vpet  # Import the Vpet model
* **AI Tool:** cursor Composer, cursor-small
* **Date:** 2024-11-17
* **Result Link:** #result-1

## Prompt 4
* **Description:** User provided prompt
* **Prompt ID:** 4
* **Prompt Text:** why ur updates to vpet_view.py don´t mention serializer ?
* **AI Tool:** cursor Composer, cursor-small
* **Date:** 2024-11-17
* **Result Link:** #result-1

## Prompt 5
* **Description:** User provided prompt
* **Prompt ID:** 5
* **Prompt Text:** why are using VpetSerializer() in the responses returned instead of the previous serializer.data ? @vpet_views.py 

also why are u not using try and except in the async defs ?
* **AI Tool:** cursor Composer, cursor-small
* **Date:** 2024-11-17
* **Result Link:** #result-1

## Prompt 6
* **Description:** User provided prompt
* **Prompt ID:** 6
* **Prompt Text:** look at the current @Codebase  and tell which step we are in now ? then give me the step by step instructions to continue with this solution, including terminal codes to turn on of virtual enviroment, servers prisma migrations etc
* **AI Tool:** cursor Composer, cursor-small
* **Date:** 2024-11-17
* **Result Link:** #result-1

## Prompt 7
* **Description:** User provided prompt
* **Prompt ID:** 7
* **Prompt Text:** ¿?
if there are some terminal code to run, don´t forget to tell me 
- if i should run it inside or outsiede of the virtual enviroment
- and the folder from which i should run it
- we have docker
@Codebase
* **AI Tool:** cursor Composer, cursor-small
* **Date:** 2024-11-17
* **Result Link:** #result-1

## Prompt 8
* **Description:** User provided prompt
* **Prompt ID:** 8
* **Prompt Text:** should i run backend server from terminal while also running docker.

gave me an overview of what needs to be running. (docker, local fronend & backend server, prima server, virtual enviroment, database server)
explain why
then who to do it in my project (windows OS)
* **AI Tool:** cursor Composer, cursor-small
* **Date:** 2024-11-17
* **Result Link:** #result-1

## Prompt 9
* **Description:** User provided prompt
* **Prompt ID:** 9
* **Prompt Text:** Overview of prompts
1. Request for Steps: You asked for step-by-step instructions to continue with the solution, including terminal commands to activate the virtual environment, run the server, and handle Prisma migrations.
2. Docker Issues: You encountered an error when trying to run Docker, specifically related to the Docker Compose file version and connection issues with the PostgreSQL database.
Running the Backend Server: You inquired whether to run the backend server while also running Docker and requested an overview of what needs to be running (Docker, local frontend & backend server, Prisma server, virtual environment, database server).
Prisma Client Import Error: You reported an import error related to the Prisma client in the vpet_views.py file, indicating that the import statement was incorrect.
5. Testing the API Endpoints: You expressed a need to test the API endpoints and ensure everything is functioning correctly.
* **AI Tool:** cursor Composer, cursor-small
* **Date:** 2024-11-17
* **Result Link:** #result-1


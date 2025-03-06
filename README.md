# A RESTful API for Professor Rating

This project is a RESTful web service built using Django and Django REST Framework (DRF), allowing students to rate professors on a scale from 1 to 5 for different modules. The service provides a command-line client application for interacting with the API and is deployed on PythonAnywhere.

The system consists of:
- A Django-based backend that manages professors, modules, module instances, and user-submitted ratings.
- A REST API that enables students to view professor ratings, list available modules, and submit ratings.
- A command-line client that provides an intuitive interface for interacting with the API.

## Using the client
To use the Professor Rating Client, ensure that Python 3.10 is installed, as well as the following libraries using: 
-> pip install requests tabulate. 

Then run the client using: 
-> python client.py

The client runs once and enters a while loop, continuously listening for user input. This allows users to execute multiple commands without restarting the script. The loop is entirely intuitive: it accepts one-line commands with (for some) arguments.

## Available Commands
•	register = Registers a new user, prompting input for a username, email, and password.
•	login <url> = logs in to the API at the inputted url.
•	logout = logs out the current user
•	list = Displays a formatted table of all module instances and their professors
•	view = Shows a list of all professors and their average ratings
•	average <professor_id> <module_code> = retrieves the average rating of a professor for the specified module
•	rate <professor_id> <module_code> <year> <semester> <rating> = Submits a rating (between 1-5) for a professor for a module.
•	exit = closes the application.

## Example Usage
\> `login sc21jg.pythonanywhere.com`

\> `list`

\> `average JM1 COMP3011`

\> `rate JM1 COMP3011 2023 2 5`

\> `logout`

\> `exit`

## PythonAnywhere Domain
My Professor Rating API is hosted at: https://sc21jg.pythonanywhere.com/

## Admin Login
To access the Django Admin site:
URL: https://sc21jg.pythonanywhere.com/admin/
Username: joshuagraham
Password: 1234567890

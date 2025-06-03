# Exercise Microservice

This project is a simple microservice-based architecture in Python for searching and sorting a list of physical exercises using a command-line interface.

It consists of:

- `test.py`: A **command-line client**that stores and serves exercise data over HTTP.
- `microservice_a.py`: A **Flask-based microservice** that sends search and sort requests to the microservice and displays the results.
---

## Features

- Search exercises by name (partial or full match)
- Sort exercises alphabetically (ascending or descending)
- Command-line interface (no browser or JavaScript needed)
- Plain-text communication between services

---

## How to
First start test.py in the terminal. This is done by writing python > test.py and pressing enter in the terminal like the image below.
`test.py` acts as a client that sends HTTP GET requests to http://localhost:5001/exercisesLinks to an external site.. Both the search and sort are optional. When you leave both blank an unsorted list of the exercises in your library is returned in plain text. You can search for partial and complete matches. The program can sort in either ascending or descending order.
![image](https://github.com/user-attachments/assets/75cebeee-9c6f-4caa-903e-8aad691158f6)

Then in a second terminal, start the microservice by typing >python microservice.py and press enter like the image below.
'microservie.py'acts as a server that listens for HTTP GET requests. It then filters the exercise list by checking that the query is in the list.
When request is received the program prints “message received” to the CDL
![image](https://github.com/user-attachments/assets/cc3ed3ed-e8ae-44c9-af70-c86549524c99)

---

## ULM
![ulm_diagram](https://github.com/user-attachments/assets/8a95a157-2686-4dcf-8b5b-d2419310d316)

## Requirements

- Python 3.7+
- Flask
- requests

## Communication 

I am available via discord or text. I can and will respond within 24 hours. Texting me will generally result in the fastest response

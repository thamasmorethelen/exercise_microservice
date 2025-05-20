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

## Files

- : `microservice_a.py` Runs a Flask server on port `5001`, serving `/exercises`.
- `test.py`: CLI tool that sends `GET` requests to the microservice and prints the response.
- `requirements.txt`: Lists required Python libraries.

---

## Requirements

- Python 3.7+
- Flask
- requests

## 
# Flask Stock Data App

This project is a Flask web application that allows users to retrieve stock data and news using the Stock Data API. The app is dockerized for easy deployment and scalability.

## Features

- Retrieve real-time stock quotes.
- Fetch latest stock-related news.
- Interactive form for user input of stock symbols.
- Responsive and user-friendly interface.

## Technologies Used

- Flask (Python)
- Jinja2 for templating
- `requests` library to handle API requests
- Docker for containerization

## Prerequisites

Before you can run the project, make sure you have:

- [Docker](https://www.docker.com/) installed on your machine.
- Stock Data API key from [stockdata.org](https://www.stockdata.org/).

## Getting Started

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/flask-stock-app.git
cd flask-stock-app

### 2. Build the Docker image:
docker build -t flask-stock-app .
```bash

## OR

### Using docker pull:
docker pull rohanskbd/flask-stock-app:latest

### Build docker image:
docker run -p 5000:5000 your-dockerhub-username/flask-stock-app

### Key Sections:
- **Project overview and features.**
- **Technologies used and prerequisites.**
- **Step-by-step instructions on how to build, run, and deploy the Docker container.**
- **Docker commands for building and running the container.**
- **Acknowledgments and license information.**

This README file should help others understand how to set up and run your Flask app using Docker.

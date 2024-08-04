# Web Scraper and Data Processing Service

This project demonstrates a web scraping and data processing service using Python, Selenium, RabbitMQ, Docker, and GitHub Actions for CI/CD. The web scraper collects data from a specified website, sends it to RabbitMQ, and a data processor consumes and processes the data.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Services](#running-the-services)
- [Monitoring](#monitoring)
- [CI/CD with GitHub Actions](#cicd-with-github-actions)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8
- Docker
- Docker Compose
- Git

## Project Structure

web_scraper/
├── scraper.py
├── processor.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .github/
│ └── workflows/
│ └── ci-cd.yml
└── README.md

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/<your-repository>.git
   cd <your-repository>
   ```
2. **Set up a virtual environment::**
  ```bash
  python -m venv web_scraper_env
  source web_scraper_env/bin/activate  # On Windows, use `web_scraper_env\Scripts\activate`
  ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Install Docker (use the instructions)**
5. **Run RabbitMQ:**
   ```bash
   docker-compose up -d rabbitmq
   ```

## Running the Services

1. **Run the Web Scraper:**
   ```bash
   docker-compose up -d scraper
   ```
2. **Run the data processor:**
   ```bash
   docker-compose up -d processor
   ```


## Monitoring
- Access the RabbitMQ management UI at http://localhost:15672 (default credentials: guest/guest).

## CI/CD with GitHub Actions
This project uses GitHub Actions for continuous integration and deployment.

**Add DockerHub credentials to GitHub Secrets:**
Go to your GitHub repository, then go to Settings > Secrets > Actions.
Add the following secrets:
DOCKER_USERNAME: Your DockerHub username.
DOCKER_PASSWORD: Your DockerHub password.

**GitHub Actions Workflow:**
The workflow file is located at .github/workflows/ci-cd.yml and is triggered on push and pull request events to the master branch.

## Contributing
**Contributions are welcome! Please open an issue or submit a pull request for any changes.**

# CI Workflow for URL Shortener

This repository contains the Continuous Integration (CI) workflow for a URL shortener project. The CI pipeline is defined using GitHub Actions and automates the process of building, testing, versioning, and deploying a Docker container for a Flask-based URL shortener service.

## Project Overview

The URL Shortener is a simple Flask web application that allows users to shorten URLs. The primary goal of this CI pipeline is to streamline the process of building, testing, and deploying the application to ensure continuous delivery of updates.

## Workflow Overview

### The GitHub Actions CI workflow is triggered by the following events:

Pushes to the main branch
Pull requests targeting the main branch
Manual triggers via workflow dispatch
Jobs in the Workflow

### Build

- Checks out the code from the repository.
- Builds a Docker image for the Flask application.
- Runs the Docker container to expose the application on port 8000.
- Installs dependencies listed in requirements.txt.
- Runs unit tests using pytest.
- Stops the running Docker container.

### Versioning

- Fetches the latest tag from DockerHub.
- Bumps the version number based on the latest tag.
- Sanitizes the new version number to ensure it’s valid.

### Docker Image Management

- Renames the Docker image with the new version.
- Logs in to DockerHub.
- Pushes the Docker image with the new tag to DockerHub.

### Deployment

- Checks out a target GitOps repository.
- Updates the deployment file (shorten-url-dep.yaml) with the new Docker image version.
- Commits and pushes the changes back to the main branch of the target repository.

# Forecast App

## Overview

The Forecast App is a web application designed to display weather forecasts for the upcoming week. The application is built with Flask for the backend and a modern frontend framework, and it uses CI/CD pipelines to ensure continuous deployment to AWS EKS using Helm charts.

## Features

- **7-Day Weather Forecast**: Displays detailed weather forecasts for a chosen location.
- **Continuous Deployment**: Fully automated deployment pipeline to AWS EKS.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: For containerizing the application.
- **Kubernetes**: A Kubernetes cluster where the application will be deployed.
- **Helm**: For deploying the application on Kubernetes.
- **AWS CLI**: To interact with AWS services.
- **kubectl**: To manage your Kubernetes cluster.
- **Python 3.x**: Required for running the application locally.
- **API KEY**: Weather API key from `visualcrossing`

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/oraharon209/forecast_app.git
    cd forecast_app
    ```

2. **Set up a virtual environment** (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**(optional for running application locallu):

    ```bash
    pip install -r requirements.txt
    ```

4. **Build the Docker image**:

    ```bash
    docker build -t forecastapp/REPO --build-arg API_KEY="YOURAPIKEY"
    ```

5. **Deploy to Kubernetes using Helm**:

   - Ensure your Kubernetes context is set to the desired cluster.
   - Update the Helm chart values in `chartforecast/values.yaml` to point to your Docker image.
   - Deploy the application:

    ```bash
    helm install chartforecast ./chartforecast
    ```

## Usage

Once the application is deployed, you can access it via the URL provided by your Kubernetes service. The application will show the weather forecast for the selected location, with options to choose different cities or regions.

## Configuration

- **Helm Values**: Customize your deployment by modifying the `values.yaml` file within the Helm chart directory.
- **Environment Variables**: Configure API keys, deployment environments, and other settings via environment variables.
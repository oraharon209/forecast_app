# Forecast App ☔️☀️

This application shows the forecast for the next 7 days, deployed on Kubernetes Cluster with Helm charts

## Requirements
- Kubernetes cluster
- Docker
- Helm
- Weather API key

## How to use
- Build and upload a Docker image in `/forecastapp` with `docker build -t forecastapp/REPO --build-arg API_KEY="YOURAPIKEY"`.
- In `/chartforecast/values.yaml` under `myapp` change `image: YOUR IMAGE`, if you have ingress change `host`to your domain name otherwise change `enabled` to false.
- In `/chartforecast` run `helm install chartforecast .`
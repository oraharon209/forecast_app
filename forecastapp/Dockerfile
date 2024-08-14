FROM python:alpine3.19
WORKDIR /forecastapp
COPY . .
ARG API_KEY=""
ENV API_KEY=$API_KEY
RUN pip install --no-cache-dir -r requirements.txt
CMD gunicorn --bind 0.0.0.0:9090 wsgi:app

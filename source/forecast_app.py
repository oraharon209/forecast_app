from app_utils import get_data, StatusCodeException, log_history
from flask import Flask, request, render_template, send_from_directory
import os
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)  # Set log level to INFO
handler = logging.FileHandler('./logs/app.log')  # Log to a file
app.logger.addHandler(handler)
BG_COLOR = os.getenv("BG_COLOR")


@app.route("/", methods=['GET', 'POST'])
def get_weather_data():
    if request.method == 'POST':
        city_name = request.form['location']
        app.logger.info(f"{city_name} was searched")
        log_history(city_name)
        try:
            weather_data = get_data(city_name)
        except StatusCodeException as e:
            app.logger.error('This is an error message')
            return render_template('forecast_app_front.html', error=e, BG_COLOR=BG_COLOR)
        return render_template('forecast_app_front.html', weather_data=weather_data, BG_COLOR=BG_COLOR)
    return render_template('forecast_app_front.html', BG_COLOR=BG_COLOR)


@app.route("/history")
def download_history():
    return send_from_directory('./', 'history.json', as_attachment=True)


@app.errorhandler(404)
def error_handler(e):
    return render_template('forecast_app_front.html', error=e, BG_COLOR=BG_COLOR)


if __name__ == '__main__':
    app.run(debug=True)

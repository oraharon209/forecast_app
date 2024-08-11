# Weather App ☔️☀️

This application shows the forecast for the next 7 days

## Requirements
- Flask
- python-dotenv
- API key(how to hide the key in the next section)

## Environment variable
to hide the API key:
- make an .env file.
- type : API_KEY ='INSERT YOUR KEY HERE'

## How to use
Install requirements.txt
- `pip install -r requirements.txt` 

To use this app you will need to reparse the JSON object generated from the API-key,
in 'app_utils.py' either edit the method "parse_data()" or re-write it.
if you are using visual-crossing's API key you can skip this part, if you
are not using visual-crossing you also need to change the url in get_data() function.


Run the `weather_app.py`.
import requests
import logging


logging.basicConfig(format ='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y :: %H:%M:%S',
                    level = logging.INFO,
                    filename="logs.txt")

logger = logging.getLogger('getting_weather_description')

API_ID = '5a49555877205adc4deaaaee32f26d78'
END_POINT = 'http://api.openweathermap.org/data/2.5/weather?'


def weather_data(query):
    response = requests.get(f'{END_POINT}{query}&APPID={API_ID}&units=metric')
    return response.json()


def print_weather(result, city):
    print(f"Description: {result['weather'][0]['description']}")
    logger.info('Printing the weather description...')

    print(f"{city}'s minimum temperature: {result['main']['temp_min']}°C ")
    logger.info('Printing the minimum temperature...')

    print(f"{city}'s maximum temperature: {result['main']['temp_max']}°C ")
    logger.info('Printing the maximum temperature...')

    print(f"Wind speed: {result['wind']['speed']} m/s")
    logger.info('Printing the wind speed...')

    print(f"{city}'s Timezone: {result['timezone']}")
    logger.info('Printing the time zone...')

    print(f"Humidity: {result['main']['humidity']}")
    logger.info('Printing the humidity...')



if __name__ == '__main__':
    city = input('Enter the city:')
    print()
    try:
        query = 'q=' + city
        w_data = weather_data(query)
        logger.info('Getting the weather information of the entered city...')

        print_weather(w_data, city)
        print()
    except:
        print('City name not found...')
        logger.info('city not found...')




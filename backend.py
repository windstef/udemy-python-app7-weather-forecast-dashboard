import requests

def get_data(place, forecast_days=None):
    API_KEY = "785c76436d5102b49ace6d03adb4574a"
    # use the default (standard) system in temperatures in Kelvin scale
    # url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    # use metric unit, for celcius and language hellenic
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric&lang=el"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    # list of items of every 3 hours
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
import json
import requests

with open("apikey.txt") as f:
    API_key = str(f.read().strip())


def main():
    request = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(request)
        if response.status_code == 200:
            json_response = response.json()
            print(json_response["value"])
    except requests.exceptions.RequestException as e:
        print("Request could not be completed.")


def main2():
    print("\n")
    city_name = input("Enter city name: ")
    print("\n")
    request1 = f"https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_key}"
    try:
        response1 = requests.get(request1)
        if response1.status_code == 200:
            json_response1 = response1.json()
            lat = json_response1[0]["lat"]
            lon = json_response1[0]["lon"]
            request2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
            try:
                response2 = requests.get(request2)
                if response2.status_code == 200:
                    json_response2 = response2.json()
                    print("City:", json_response2["name"])
                    temperature = json_response2["main"]["temp"] - 273.15
                    print(f"Temperature: {temperature:.1f} degrees celsius")
                    print("Weather:", json_response2["weather"][0]["description"])
                    print("Wind speed:", json_response2["wind"]["speed"], "m/s")
                    print("Cloudiness:", json_response2["clouds"]["all"], "%")
            except requests.exceptions.RequestException as e:
                print("Request could not be completed.")
    except requests.exceptions.RequestException as e:
        print("Request could not be completed.")


main()
main2()

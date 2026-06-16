import json
import urllib.parse
import urllib.request


def get_weather_data():
    city_name = input("Enter Municipality Name: ").strip()

    api_key = "7d08b8208483edaa19c754c351989d9f"

    encoded_city = urllib.parse.quote(city_name)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid={api_key}&units=metric"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())


                description = data["weather"][0]["description"]

                temp_celsius = data["main"]["temp"]

                print(f"\nWeather in {city_name.title()}:")
                print(f"Condition: {description.capitalize()}")
                print(f"Temperature: {temp_celsius}°C")
            else:
                print(f"Error: Received status code {response.status}")

    except urllib.error.HTTPError as e:
        if e.code == 401:
            print(
                "Error: Check if your API key is valid or fully activated yet."
            )
        elif e.code == 404:
            print(
                "Error: Municipality Name not found"
            )
        else:
            print(f"HTTP Error: {e.code} - {e.reason}")
    except Exception as e:
        print(f"An unexpected error: {e}")


if __name__ == "__main__":
    get_weather_data()
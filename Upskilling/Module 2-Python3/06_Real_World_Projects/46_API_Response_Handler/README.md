# Exercise 46 - API Response Handler

## Objective

Use requests, JSON handling, classes, and error handling to process API responses.

## Task

Fetch weather data from an API and display temperature and weather conditions safely.

## Instructions

- Install and use the `requests` library.
- Fetch weather data in JSON format.
- Parse the temperature and weather conditions.
- Handle 404 and network errors.
- Format the output neatly.

## Project Structure

- `Exercise_46.py` - Python source code
- `46_output.png` - Program output screenshot

## Requirements

Install the requests library:

```bash
pip install requests
```

## Code

```python
import requests


class WeatherAPI:
    def __init__(self, city):
        self.city = city

    def get_weather(self):
        url = f"https://wttr.in/{self.city}?format=j1"

        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 404:
                print("Error: City not found.")
                return

            response.raise_for_status()

            data = response.json()

            temperature = data["current_condition"][0]["temp_C"]
            condition = data["current_condition"][0]["weatherDesc"][0]["value"]

            print("Weather Report")
            print(f"City: {self.city}")
            print(f"Temperature: {temperature}°C")
            print(f"Condition: {condition}")

        except requests.exceptions.ConnectionError:
            print("Error: Network connection failed.")
        except requests.exceptions.Timeout:
            print("Error: Request timed out.")
        except requests.exceptions.HTTPError:
            print("Error: Unable to retrieve weather data.")
        except KeyError:
            print("Error: Invalid response format.")


weather = WeatherAPI("Chennai")
weather.get_weather()
```

## Expected Output

```
Weather Report
City: Chennai
Temperature: 31°C
Condition: Partly cloudy
```

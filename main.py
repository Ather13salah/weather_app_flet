"""Weather flet app"""
from flet import *
import requests
import datetime

api_key = "06991f5a417d4300814113707251901"
url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=toronto&days=7&aqi=no"
resp = requests.get(url)  # Make a GET request to the URL
data = resp.json()  # Convert the response to JSON
daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def main(page: Page):
    page.theme_mode = "dark"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def topCon():
        top_container = Container(
            width=310,
            height=660 * 0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_left,
                colors=["lightblue600", "lightblue900"]
            ),
            border_radius=35,
            padding=15,
            content=Column(
                alignment='start',
                spacing=10,
                controls=[
                    Row(
                        alignment='center',
                        controls=[
                            Text(
                                "Toronto,CA",
                                size=16,
                                weight='w600'
                            ),
                        ],
                    ),
                    Container(padding=padding.only(bottom=5)),
                    Row(
                        alignment='center',
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=65,
                                        height=65,
                                        content=Image(src='./assets/cloudy.png'),
                                    ),
                                    Column(
                                        controls=[
                                            Text(f"{data['current']['wind_kph']} km/h", size=12, weight='w400'),
                                            Text(f"{data['current']['humidity']} % humidity of air", size=12, weight='w400'),
                                            Text(f"{data['current']['pressure_mb']} mb", size=12, weight='w400'),
                                        ],
                                    ),
                                ],
                            ),
                            Column(
                                spacing=5,
                                horizontal_alignment='center',
                                controls=[
                                    Text(
                                        "Today",
                                        size=16,
                                        text_align='center',
                                    ),
                                    Column(
                                        spacing=0,
                                        alignment='center',
                                        controls=[
                                            Text(
                                                f"{data['current']['temp_c']}°C",
                                                size=40,
                                            ),
                                            Text(
                                                f"{data['current']['temp_f']}°f",
                                                size=40,
                                            ),
                                            Text(f'{data["current"]["condition"]["text"]}', size=12, weight='w400'),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        return top_container

    def bottomData():
        bottomDay = []
        forecast_days = data['forecast']['forecastday']  # Get the forecast data for the next 7 days
        for day in forecast_days:
            date = datetime.datetime.strptime(day['date'], "%Y-%m-%d")  # Convert date string to datetime object
            day_name = daysOfWeek[date.weekday()]  # Get the day name (e.g., Monday)
            avg_temp_c = day['day']['avgtemp_c']  # Get the average temperature in Celsius
            avg_temp_f = day['day']['avgtemp_f']  # Get the average temperature in Fahrenheit
            bottomDay.append(
                Row(
                    alignment='spaceBetween',
                    controls=[
                        Text(
                            day_name,  # Display the day name
                            size=16,
                            color="white",
                            weight="w600",
                        ),
                        Text(
                            f"{avg_temp_c}°C / {avg_temp_f}°F",  # Display the temperature
                            size=16,
                            color="white",
                            weight="w600",
                        ),
                    ],
                ),
            )
        return bottomDay

    def bottomCon():
        BottomColumn = Column(
            alignment='center',
            horizontal_alignment='center',
            spacing=25,
            controls=bottomData(),  # Add the days and temperatures to the column
        )
        bototomCon = Container(
            padding=padding.only(top=20, bottom=20, left=20, right=20),  # Adjust padding
            bgcolor="black",  # Set background color
            content=BottomColumn,
        )
        return bototomCon

    _main_container = Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor="black",
        padding=10,
        content=Column(  # Use Column instead of Stack
            spacing=0,
            controls=[
                topCon(),  # Add the top container
                bottomCon(),  # Add the bottom container
            ],
        ),
    )
    page.add(_main_container)
    page.update()

if __name__ == "__main__":
    app(target=main)
"""Weather flet app"""
from flet import *
import requests
import datetime

api_key = "06991f5a417d4300814113707251901"
url =f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=toronto&aqi=no"
resp = requests.get(url) # make a get request to the url
data = resp.json() # convert the response to json
daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
def main(page:Page):
    page.theme_mode = "dark"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    def bottomCon():
        # bototomCon = Container(
        #     bgcolor='white10',
        #     border_radius=12,
        #     alignment=alignment.center
        # )
        # return bototomCon
        ...
    
    def topCon():
        top_container = Container(
            width=310,
            height=660 *0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_left,
                colors=["lightblue600","lightblue900"]
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
                                            Text(f"{data['current']['wind_kph']} km/h",size=12,weight='w400'),                                         
                                            Text(f"{data['current']['humidity']} % humidity of air",size=12,weight='w400'),
                                            Text(f"{data['current']['pressure_mb']} mb",size=12,weight='w400'),
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
                                            Text(f'{data['current']['condition']['text']}',size=12,weight='w400'),
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
    _main_container = Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor="black",
        padding=10,
        content=Stack(
            width=300,height=550,
            controls=[topCon()]
        )
    )
    page.add(_main_container)
    page.update()
if __name__=="__main__":
    app(target=main)
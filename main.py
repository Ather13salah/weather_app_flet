"""Weather flet app"""
from flet import *
import requests
import datetime

api_key = "06991f5a417d4300814113707251901"

url =f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=toronto&aqi=yes"
resp = requests.get(url)
daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# data = resp.json() # convert the response to json

def main(page:Page):
    page.theme_mode = "dark"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    def expand(e):
        if e.data =="true":
            _main_container.content.controls[0].height = 560
            _main_container.content.controls[0].update()
        else:
            _main_container.content.controls[0].height = 660 *0.40
            _main_container.content.controls[0].update()    
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
            animate=animation.Animation(duration=450,curve="decelerate"),
            on_hover=lambda e : expand(e),
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
                                        width=90,
                                        height=90,
                                        image_src='assests/cloudy.png',
                                    ),
                                ],
                            ),
                            
                        ],
                    ),
                ],
            )
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
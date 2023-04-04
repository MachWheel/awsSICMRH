import PySimpleGUI as sg

from app.certbot_parser import parse_certbot_manual_challenge
from config.default_text import DEFAULT_EMAIL, DEFAULT_DOMAIN

col0 = sg.Col([
    [sg.Frame(
        "1) Input your data exactly as shown",
        [
            [sg.VPush()],
            [
                sg.Text("email", font="Consolas 10 italic"),
                sg.Input(
                    DEFAULT_EMAIL,
                    key="email_input",
                    font="Consolas 12",
                    text_color="white",
                    enable_events=True
                )
            ],
            [sg.VPush()],
            [
                sg.Text("domain", font="Consolas 10 italic"),
                sg.Input(
                    DEFAULT_DOMAIN,
                    key="domain_input",
                    font="Consolas 12",
                    text_color="white",
                    enable_events=True
                )
            ],
            [sg.VPush()]
        ],
        pad=(25, 0),
        title_color='yellow',
        font="Default 12"
    )]
])

col1 = sg.Col([
    [sg.Frame(
        "2) Run the command following the steps",
        [
            [sg.Text(
                "1. Create a folder\n"
                "2. Right click inside it\n"
                "3. Open a linux shell there\n",
                font="Consolas 12",
                text_color="white"
            )],
            [
                sg.Push(), sg.Button('4. Copy command to Clipboard', key='copy_btn_0'), sg.Push()
            ],
            [sg.Text(
                "5. Paste and run the command\n"
                "6. Follow the instructions",
                font="Consolas 12",
                text_color="white"
            )]
        ],
        pad=(25, 0),
        title_color='yellow',
        font="Default 12"
    )]
])

tab0 = sg.Tab('0) run certbot', [
    [sg.VPush()],

    [col0, col1],
    [sg.Text(
        "Resulting command:",
        font="Consolas 10 bold",
        text_color="white",
        pad=((50, 0), (100, 0)),
    )],
    [sg.Multiline(
        parse_certbot_manual_challenge(DEFAULT_EMAIL, DEFAULT_DOMAIN),
        font="Consolas 10 bold",
        text_color="lightgray",
        size=(100, 4),
        pad=(50, 0),
        disabled=True,
        key="resulting_cmd"
    )],
    [sg.VPush()],
])

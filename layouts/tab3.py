import PySimpleGUI as sg

from config.default_text import DEFAULT_KEY

tab3 = sg.Tab(
    '3) paste privkey.pem',
    [
        [sg.VPush()],
        [sg.Text(
            "Enter the new private key exactly as below:",
            font="Default 12 italic",
            text_color="yellow"
        )],
        [
            sg.Multiline(
                size=(100, 30),
                key="key_input",
                font="Consolas 11",
                text_color="white",
                default_text=DEFAULT_KEY
            )
        ]
    ]
)

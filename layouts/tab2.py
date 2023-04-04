import PySimpleGUI as sg

from config.default_text import DEFAULT_CERT

tab2 = sg.Tab('2) paste "cert.pem"', [
    [sg.VPush()],
    [
        sg.Text(
            "Enter the new certificate exactly as below:",
            font="Default 12 italic",
            text_color="yellow"
        )
    ],
    [
        sg.Multiline(
            size=(100, 30),
            key="cert_input",
            font="Consolas 11",
            text_color="white",
            default_text=DEFAULT_CERT
        )
    ]
])

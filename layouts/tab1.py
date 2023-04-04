import PySimpleGUI as sg

from config.default_text import DEFAULT_DOMAIN, COPY_CMD_0, COPY_CMD_1

tab1 = sg.Tab('1) copy SSL data', [
    [sg.VPush()],
    [sg.Frame(
        "Now copy SSL data from the linux shell",
        [
            [sg.VPush()],
            [
                sg.Text(
                    "1. Paste and run the command into linux terminal:",
                    font="Consolas 12",
                    text_color="white"
                )
            ],
            [sg.Multiline(default_text=COPY_CMD_0(DEFAULT_DOMAIN), size=(50, 3), disabled=True, pad=(25, 5),
                          key="copy_cmd_0")],
            [
                sg.Push(), sg.Button('Copy command to Clipboard', key='copy_btn_1'), sg.Push()
            ],
            [sg.VPush()],
            [
                sg.Text(
                    '2. Copy the SSL certificate and paste at tab 2\n'
                    '3. Press Crtl+X to exit nano\n'
                    '4. Paste and run the command:',
                    font="Consolas 12",
                    text_color="white"
                )
            ],
            [sg.Multiline(default_text=COPY_CMD_1, size=(50, 2), disabled=True, pad=(25, 5))],
            [
                sg.Push(), sg.Button('Copy command to Clipboard', key='copy_btn_2'), sg.Push()
            ],
            [sg.VPush()],
            [
                sg.Text(
                    '5. Copy the private key and paste at tab 3\n',
                    font="Consolas 12",
                    text_color="white"
                )
            ]
        ],
        pad=(100, 0),
        title_color='yellow',
        font="Default 12"
    )],
    [sg.VPush()],
])

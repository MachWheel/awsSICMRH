import PySimpleGUI as sg
import pyperclip

from app.cert_replacer import replace_ssl_cert
from app.certbot_parser import parse_certbot_manual_challenge
from config import default_text, msgs
from layouts import main_layout


def main():
    window = sg.Window(
        "AWS Single Instance Manual Certbot Renew Helper",
        main_layout,
        relative_location=(0, -50)
    )

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        elif event == "copy_btn_0":
            pyperclip.copy(
                parse_certbot_manual_challenge(
                    values['email_input'],
                    values['domain_input']
                )
            )
            sg.popup(msgs.CMD_COPIED)

        elif event == "copy_btn_1":
            pyperclip.copy(
                default_text.COPY_CMD_0(values['domain_input'])
            )
            sg.popup(msgs.CMD_COPIED)

        elif event == "copy_btn_2":
            pyperclip.copy(default_text.COPY_CMD_1)
            sg.popup(msgs.CMD_COPIED)

        elif event == "domain_input" or event == "email_input":
            window['resulting_cmd'].update(
                parse_certbot_manual_challenge(
                    values['email_input'], values['domain_input']
                )
            )
            window['copy_cmd_0'].update(
                default_text.COPY_CMD_0(values['domain_input'])
            )

        elif event == "Replace":
            replace_ssl_cert(
                values["cert_input"],
                values["key_input"],
                values["file"]
            )
            sg.popup(msgs.CERT_REPLACED)
            break

    window.close()


if __name__ == "__main__":
    main()

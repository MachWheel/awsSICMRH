import PySimpleGUI as sg

tab4 = sg.Tab(
    '4) update "https-instance.config"',
    [
        [sg.VPush()],
        [sg.Frame(
            'file located under ".ebextensions/https-instance.config"', [
                [
                    sg.Text(
                        "Select a .config file to modify:",
                        font="Default 12 italic"
                    )
                ],
                [sg.Input(default_text="https-instance.config", key="file"), sg.FileBrowse()],
                [sg.Button("Replace"), sg.Button("Cancel")]
            ], pad=100, title_color='yellow'
        )],
        [sg.VPush()]
    ]
)

import PySimpleGUI as sg


sg.theme('DarkBlue')

from .tab0 import tab0
from .tab1 import tab1
from .tab2 import tab2
from .tab3 import tab3
from .tab4 import tab4

main_layout = [
    [sg.TabGroup(
        [[tab0], [tab1], [tab2], [tab3], [tab4]],
        selected_title_color="yellow",
        font="Consolas 10 bold"
    )]
]

# -*- coding: utf-8 -*-

import sys
from cryptomon.common import Colors
if sys.version_info >= (3, 0):
    import io
else:
    import StringIO as io


ascii_title = """

  /$$$$$$                                  /$$               /$$      /$$                    
 /$$__  $$                                | $$              | $$$    /$$$                    
| $$  \__/  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$    /$$$$$$ | $$$$  /$$$$  /$$$$$$  /$$$$$$$ 
| $$       /$$__  $$| $$  | $$ /$$__  $$|_  $$_/   /$$__  $$| $$ $$/$$ $$ /$$__  $$| $$__  $$
| $$      | $$  \__/| $$  | $$| $$  \ $$  | $$    | $$  \ $$| $$  $$$| $$| $$  \ $$| $$  \ $$
| $$    $$| $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$| $$\  $ | $$| $$  | $$| $$  | $$
|  $$$$$$/| $$      |  $$$$$$$| $$$$$$$/  |  $$$$/|  $$$$$$/| $$ \/  | $$|  $$$$$$/| $$  | $$
 \______/ |__/       \____  $$| $$____/    \___/   \______/ |__/     |__/ \______/ |__/  |__/
                     /$$  | $$| $$                                                           
                    |  $$$$$$/| $$                                                           
                     \______/ |__/                                                           

"""


def process_title(title):
    buf = io.StringIO(title)
    lines = buf.readlines()
    lines = lines[1:-1]
    colored_lines = []
    colored_title = ""

    for line in lines:
        colored_lines.append(Colors.BLUE + line[:13] + Colors.YELLOW + line[14:])

    for line in colored_lines:
        colored_title += line

    return colored_title + Colors.ENDLINE

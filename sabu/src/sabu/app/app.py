from rich.console import Console
from pathlib import Path
import sys
import os

from sabu.app.utils.git import is_git

class App:
    def __init__(self) -> None:
        self.console: Console = Console()

    def titlebar(self) -> None:
        self.console.print(
            "[sabu]", 
            justify="center", 
            style="black on white"
        )

    def sabu(self) -> None:
        try:
            self.titlebar()

            while True:
                cwd: str = Path.cwd()

                print(f"\x0A\x1b[96m╭─[{cwd} :: {is_git()}\x1b[96m]\x1b[0m")
                prompt: str = input("\x1b[1 q\x1b[96m╰─➤\x1b[0m ")

                if prompt is None:
                    pass

                if prompt in ["exit", "quit", "bye"]:
                    if prompt == "bye":
                        print("bye, bye!\x0A")
                    sys.exit()

                os.system(prompt)
                print()

        except KeyboardInterrupt:
            sys.exit("bye")

    def run(self) -> None:
        print("\x1b[2J\x1b[H", end="")
        self.sabu()

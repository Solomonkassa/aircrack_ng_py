from interfaces.cli import cli
from interfaces.gui import start_gui
import sys

def main():
    if len(sys.argv) > 1:
        cli()
    else:
        start_gui()

if __name__ == "__main__":
    main()


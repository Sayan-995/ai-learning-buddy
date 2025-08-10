import os
import sys
import streamlit.web.cli as stcli

def main():
    ui_file = os.path.join(os.path.dirname(__file__), "main.py")
    sys.argv = ["streamlit", "run", ui_file]
    sys.exit(stcli.main())

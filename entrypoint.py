import sys
import os
import site

venv_path = "/app/venv"
site_packages = os.path.join(
    venv_path, "lib", f"python3.12", "site-packages"
)
site.addsitedir(site_packages)

import app

from app.app import main

main()
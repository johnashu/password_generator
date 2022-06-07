import os, sys, logging

def create_data_path(pth: str, data_path: str = "logs") -> os.path:
    cwd = os.getcwd()
    p = os.path.join(cwd, data_path, pth)
    if not os.path.exists(p):
        os.mkdir(p)
    return p


create_data_path((""))

import logging

file_handler = logging.FileHandler(filename=os.path.join("logs", "passwords.log"))
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=handlers)

log = logging.getLogger()

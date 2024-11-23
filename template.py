import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format= '[%(asctime)s]: %(message)s')



project_name = " text summarizer"

list_of_files = [ 
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__inint__.py",
    f"src/{project_name}/components/__inint__.py",
    f"src/{project_name}/utils/__inint__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__inint__.py",
    f"src/{project_name}/config/__inint__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__inint__.py",
    f"src/{project_name}/entity/__inint__.py",
    f"src/{project_name}/constants/__inint__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trial.ipynb"

    ]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath )

    if filedir != "":
        os.makedirs(filedir,  exist_ok= True)
        logging.info(f"creating directory: {filedir} for the file {filename}")

    
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            
            logging.info(f"creating empty file:{filepath}") 

    else:
        logging.info(f"{filename} is already exist")
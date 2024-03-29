import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


project_name = "emailTextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init_.py",
    f"src/{project_name}/utils/__init_.py",
    f"src/{project_name}/utils/__init_.py",
    f"src/{project_name}/utils/common/__init_.py",
    f"src/{project_name}/logging/__init_.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entitiy/__init_.py",                
    f"src/{project_name}/constants/__init_.py", 
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "reseach/trials.ipynp",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file :{filepath}")

    else:
        logging.info(f"{filename} already exists")
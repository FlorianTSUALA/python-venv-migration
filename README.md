# Python Environment Migration Script

  This Python script helps to migrate a Python project environment from one location to another. It updates the paths in the `pyenv.cfg` file and all scripts in the `.env\Scripts` directory.
 

## Usage

  
1. Place the `migration_script.py` in the root directory of your project.
  

2. Ensure your project has the following structure:
```
My Project/
│
├── .env/
│ ├── pyenv.cfg
│ └── Scripts/
│ ├── activate
│ └── activate.bat
│ ...
│
└── migration_script.py
```
3. Run the script by executing `python migration_script.py` in the terminal.
4. Follow the prompts:
- The script will ask you to enter the environment file name. Press Enter to use `.env` by default.
- It will then update the `pyenv.cfg` file with the new Python executable path.
- Next, it updates all scripts in the `.env\Scripts` directory with the new project path.

## Acknowledgements
This script was inspired by the solution provided by Imran Said on Stack Overflow: [Stack Overflow Answer](https://stackoverflow.com/a/72999525). We extend our gratitude to Imran for his valuable contribution.

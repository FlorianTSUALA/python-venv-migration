import os
import re
import sys

def get_python_executable():
    # Get the Python executable path
    python_executable = sys.executable
    print("Python executable path obtained:", python_executable)
    return python_executable

def update_pyvenv_cfg(python_executable, pyvenv_cfg_path):
    # Update the pyvenv.cfg file with the new Python executable
    print("Updating", pyvenv_cfg_path, "with the new Python executable...")
    with open(pyvenv_cfg_path, 'r') as file:
        content = file.read()

    # Update the executable path
    # Use a regular expression to extract the home value
    match = re.search(r'home\s*=\s*(.*)', content)
    if match:
        old_home_value = match.group(1)
        print("Old home value:", old_home_value)

        # Replace the old value with the new one
        new_content = content.replace(old_home_value, python_executable)
        with open(pyvenv_cfg_path, 'w') as file:
            file.write(new_content)
    else:
        print("Home value was not found in the provided content.")

    print("File", pyvenv_cfg_path, "updated successfully.")

def update_scripts(old_project_path, new_project_path):
    # Update the scripts in .env\Scripts directory
    print("Updating scripts in .env\\Scripts directory...")
    scripts_dir = os.path.join(os.getcwd(), '.env', 'Scripts')

    for root, _, files in os.walk(scripts_dir):
        for file in files:
            if not file.endswith(".exe"):  # Check the file extension
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    script_content = f.read()

                # Replace the old project path with the new one
                new_script_content = script_content.replace(old_project_path, new_project_path)

                with open(file_path, 'w') as f:
                    f.write(new_script_content)

    print("Scripts updated successfully.")

if __name__ == "__main__":
    print("Starting the migration...")

    # Get the Python executable path
    python_executable = get_python_executable()

    # Ask the user for the environment file name
    env_file_name = input("Enter the environment file name (press Enter to use '.env' by default): ")
    if not env_file_name:
        env_file_name = ".env"

    # Update the pyvenv.cfg file
    pyvenv_cfg_path = os.path.join(os.getcwd(), env_file_name, 'pyvenv.cfg')
    update_pyvenv_cfg(python_executable, pyvenv_cfg_path)

    # Determine the old and new project paths
    with open(pyvenv_cfg_path, 'r') as file:
        pyvenv_cfg_content = file.read()
    old_project_path_match = re.search(r'command\s=\s.*?python.exe\s-m\svenv\s(.*)', pyvenv_cfg_content)
    if old_project_path_match:
        old_project_path = old_project_path_match.group(1)
    new_project_path = os.path.join(os.getcwd(), env_file_name)

    # Update the scripts in .env\Scripts directory
    update_scripts(old_project_path, new_project_path)

    print("Migration completed successfully.")

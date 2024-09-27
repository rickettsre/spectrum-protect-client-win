import subprocess
import os
import platform
import logging

supported_os_list = ['2012Server', '2016Server', '2019Server', '2022Server']
baclient_exe_folder = '../download'
output_folder = '../extract'
log_output_folder = '../logs'
log_file = f'{log_output_folder}/install.log'

# # Set up logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler(log_file),
#         logging.StreamHandler()
#     ]
# )


def create_log():
    os.makedirs(log_output_folder, exist_ok=True)
# Set up logging
    logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()    
        ]
        )

def check_os():
    os_info = platform.uname()
    if os_info.release in supported_os_list:
        logging.info(f"{os_info.release} is in list of supported servers") 
        return True
    else:
        logging.error(f"{os_info.release} not in list of supported servers")

def list_exe_files(folder_path):
    logging.info(f"Listing .exe files in folder: {folder_path}")
    exe_files = [f for f in os.listdir(folder_path) if f.endswith('.exe')]
    logging.info(f"Found {len(exe_files)} .exe files.")
    return exe_files

def extract_self_extracting_zip(exe_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    command = [exe_path, f'-o{output_folder}', '-y']
    logging.info(f"Extracting {exe_path} to {output_folder}")
    try:
        result = subprocess.run(command, check=True)
        logging.info(f"Extraction successful for {exe_path}: {result}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during extraction of {exe_path}: {e}")

def extract_all_exe_files_in_folder(folder_path, output_folder):
    exe_files = list_exe_files(folder_path)
    if not exe_files:
        logging.warning(f"No .exe files found in the folder: {folder_path}")
        return

    for exe_file in exe_files:
        exe_path = os.path.join(folder_path, exe_file)
        extract_self_extracting_zip(exe_path, output_folder)

def install_vcredist_exe_files():
     # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(f'{output_folder}/TSMClient/ISSetupPrerequisites'):
        for file in files:
            if file.lower().endswith('redist.x64.exe'):
                exe_path = os.path.join(root, file)
                try:
                    result = subprocess.run([exe_path, "/install", "/quiet", "/norestart", "/log", "../logs/vcredist_log.txt"], check=True)
                    logging.info(f"{exe_path} Installation succeeded")
                except subprocess.CalledProcessError as e:
                    logging.error(f"Installation of {exe_path} failed with error: {e}")

def install_ibm_jvm_exe_file():
     # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(f'{output_folder}/TSMClient/ISSetupPrerequisites'):
        for file in files:
            if file.lower()=='spinstall.exe':
                exe_path = os.path.join(root, file)
                command = [exe_path,
                           '/s',
                           '/vRebootYesNo="No" Reboot="ReallySuppress" ALLUSERS=1 /qn /l*v "../logs/jre_log.txt"'
                           ]
                try:
                    result = subprocess.run(command, check=True, shell=True)
                    logging.info(f"Installation of {exe_path} Command executed successfully")
                except subprocess.CalledProcessError as e:
                    logging.error(f"Installation of {exe_path} Command failed with error: {e}")
                except Exception as e:
                    logging.error(f"An error occurred: {e}")
            
def get_installed_redistributables():
    try:
        result = subprocess.run(
            ['wmic', 'product', 'get', 'name,version'],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout
        installed_redistributables = []
        for line in output.splitlines():
            if 'Microsoft Visual C++' in line:
                installed_redistributables.append(line.strip().split(' ')[3])
        return installed_redistributables

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while querying installed programs: {e}")
        return []
    

def install_baclient():
    # Change the working directory
    os.chdir(os.path.join(output_folder, 'TSMClient'))

    # Define the MSI file
    msi_file = 'IBM Storage Protect Client.msi'
    log_file = os.path.join('..', 'logs', 'spinstall_log.txt')

    # Construct the command as a single string
    command = (
        f'msiexec /i "{msi_file}" '
        f'RebootYesNo="No" REBOOT="Suppress" ALLUSERS=1 '
        f'INSTALLDIR="C:\\Program Files\\Tivoli\\Tsm" '
        f'ADDLOCAL="BackupArchiveGUI,Api64Runtime" '
        f'TRANSFORMS=1033.mst /qn /l*v "../../logs/spinstall_log.txt"'
    )

    # Run the command using subprocess
    try:
        result = subprocess.run(command, check=True, shell=True)
        print("Command executed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
  
   
def main():
    create_log()
    if check_os():
        print("Passed the OS Check")
        print("Extracting File")
        extract_all_exe_files_in_folder(baclient_exe_folder, output_folder)
        print("Checking prereqs...")
        redistributables = get_installed_redistributables()

        if len(redistributables) > 0:
            lowest_release =  int(min(redistributables))
            if lowest_release >= 2015:
                print(f"C++ Prereq met\nOldest Installed Microsoft Visual C++ Redistributables: {lowest_release}")
            
            else:
                print("Prerq not met.\nInstalling VC C++")
                install_vcredist_exe_files()
    else:
        print("No redistributables found installing Microsoft Visual C++ Redistributables")
        install_vcredist_exe_files()
    
    print("Installing IBM JVM prereq...")
    install_ibm_jvm_exe_file()
    print("Installing Baclient...")
    install_baclient() 
        
if __name__ == "__main__":
    main()
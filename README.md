IBM Spectrum Protect Client Install on Windows Using Python
================================================================

For this automation project I am automating the initial install of the IBM Spectrum Protect aka TSM client on a windows machine.  


1. To do this I'm using python embedded:

https://www.python.org/downloads/windows/
https://www.python.org/ftp/python/3.12.5/python-3.12.5-embed-amd64.zip

2. Extract the python embedded to a folder called python.

3. Create download folder put baclient in this directory e.g:

https://public.dhe.ibm.com/storage/tivoli-storage-management/maintenance/client/v8r1/Windows/x64/v8123/8.1.23.0-TIV-TSMBAC-WinX64.exe

Put 8.1.23.0-TIV-TSMBAC-WinX64.exe into download folder

4. main.py is placed in python portable version

5. At command line navigate to python portable folder

python main.py

5. Logs will be placed in the logs folder

Unattended install information:

Manual Link:
===============

https://www.ibm.com/docs/en/SSEQVQ_8.1.23/pdf/b_ba_guide_win.pdf

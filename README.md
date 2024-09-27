Day 98 - Python Automation
============================

You've learnt about automation with Python and Selenium. It's your turn to get creative and automate some aspect of your life using what you have learnt.

This could be an aspect of your job, your schoolwork, your home, your chores. Think about your week and everything that you do on a regular basis, when do you feel like a robot? Which jobs do you find tedious and boring? Can it be automated?

Here are some stories for inspiration:

Automate an email to your boss to ask for a raise every 3 months. =)

Automate your lights so they switch on when your phone is within the radius of your house.

Automatically organise the files in your downloads folder based on file type.

Automate your gym class bookings.

Automate your library book renewals.

Automate your job.

Automate your home chores.

Personally, I had a job in a hospital where I had to arrange all the doctors' shifts in my department (normal day, long day, night shift). It would depend on when they wanted to take annual leave/vacation and the staffing requirements. It started out in an Excel spreadsheet, by the time I was done with it, it was fully automated with Python and doctors were able to view a live version of the rota to see when they can take time off. The code took an evening to write and it saves me 3 hours per week. (More time to watch Netflix and eat ice cream).

Once you're done with the assignment, let us know what you automated in your life and maybe it will inspire another student!



My Notes
-------------------

For this automation project I am installing the IBM Spectrum Protect aka TSM client on a windows machine.  


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
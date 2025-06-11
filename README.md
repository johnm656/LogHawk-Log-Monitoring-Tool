# LogHawk-Log-Monitoring-Tool
An open source log analysis tool that can be automated to run as often as desired
This preconfigured script will locate and notify of any suspicious activities within log files

To run preconfigured script on a Windows machine 
Python must be installed and to do so;
Open Cmd prompt entering cmd in the task bar search
In the terminal enter "sudo apt-get install python3"
After python3 is installed;
In terminal enter python3 <path/to/file> of the preconfigured script we have provided
This will locate and filter a preset set of potential malicious threats and help to pinpoint source

![Image](https://github.com/user-attachments/assets/b379d22b-60cd-410e-a34d-6294ce1890b3)

![Image](https://github.com/user-attachments/assets/7d0ccce8-0a8d-41ce-87ee-68c12c4f8c8d)


To run the script on Visual Studio Code
Install Visual Studio Code from web browser
Once installed, open Visual Studio Code and click open file
Navigate to where file is located and open
Script will load but need to be edited to locate to the the location of the log files
This will need to be done in four locations of the script, as four logs are scanned in the same script

![Image](https://github.com/user-attachments/assets/0583b29e-c11f-4fa3-8c98-3c13060b9ce0)

After all four file locations have been updated, click run and script will run showing all potential malicious activities

![Image](https://github.com/user-attachments/assets/d447d9fb-b85e-4535-bf72-aa90df6ffec4)

![Image](https://github.com/user-attachments/assets/a5103281-8887-47a2-9383-543d9c7c3c38)

It is suggested to run script once daily through an automated program called crontab
To run crontab, open linux terminal and type crontab -e
This will open scheduling program 

![Image](https://github.com/user-attachments/assets/e93bda06-e6bf-417f-91a8-6afc1658729e)

The time fields (from left to right) Minute, Hour, Day of Month(DOM), Month, Day of Week(DOW)   * means nothing selected and will run at all of times
                                      0-59   0-23       1-31          1-12         0-6       


In Windows a task scheduler will be used to schedule time to run script
In taskbar search type "task scheduler"
Select "create basic task"
Create a name and description for task
In trigger tab, choose when task is to start then select start times and number of recurring days
In action tab, select "start a program"
Add script through browse tab
Select script/program to run
Click next
Then finish and review selected schedule


If an emailed copy of results of script is needed:
Create a new basic task, but in action tab, instead of choosing start a program, select "send and email"
Enter in source and destination email addresses, subject, description, and pick the attachment

![Image](https://github.com/user-attachments/assets/86c1ace9-2930-4f46-ac3d-7d1e72afca96)

![Image](https://github.com/user-attachments/assets/05871cf9-92c5-44ee-9921-a183e10fd2ec)











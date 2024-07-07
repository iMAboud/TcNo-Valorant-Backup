<div align="center">

# TcNo and Valorant Backup | Restore

## Description
This is a simple backup and restore script that saves you a lot of time configuring settings and inserting passwords for Valorant and TcNo Account Switcher.

## Download
[Valorant Backup](https://github.com/iMAboud/TcNo-Valorant-Backup/releases/download/v0.1/Valorant.Backup.exe)
## Usage
- **Backup**: Click Backup, and it will save all necessary files from "TcNo Account Switcher" and "Riot Client/Valorant" into a ZIP folder. Save that ZIP folder somewhere for later to restore.
- **Restore**: Click Restore, select the ZIP file, and it will restore all these files into their paths, now you're ready to use your accounts without re-entering passwords or configuring settings in Valorant for each account.

![](https://i.imgur.com/BJQAFF5.png)


## Dependencies:
``
pip install pillow
``

This script can be reconfigured to be used with any other platform supported by TcNo Account Switcher, edit the python script and configure it to backup any other folder.

## Make it an EXE
If you wish to make it an exe so you can use it on any other device without needing python or installing dependencies then follow these simple steps:

1. Ofc you need python installed and added to path.
2. open powershell and type `pip install pyinstaller`
3. close and relaunch powershell and `cd` to valobackup.py and valorant.ico path then type `pyinstaller --onefile --windowed --icon=valorant.ico --name "Valorant Backup" ValoBackup.py`
4. Wait until finish, then it'll create a "dist" folder where the .exe is inside it. 



</div>

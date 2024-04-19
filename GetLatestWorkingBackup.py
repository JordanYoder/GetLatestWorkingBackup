# This program grabs the latest backup Working file and makes a copy into  ...\Filemaker Upload\Working Programs
# This allows the 'latest' Working file to be available for local hosting.
# Setting this to run daily on my PC as IT doesn't want to create a script that creates backups in multiple places

import os
import shutil
import datetime


def find_latest_backup():
    backup_dir = r'\\EngageFS\Filemaker\Server Backup\EngageDC4'
    daily_backup_dirs = os.listdir(backup_dir)
    daily_backup_dirs.sort(reverse=True)

    for daily_backup_dir in daily_backup_dirs:
        if daily_backup_dir.startswith('Daily Backup_'):
            return os.path.join(backup_dir, daily_backup_dir, 'Databases', 'Working', 'Working.fmp12')


def log_message(message):
    log_dir = r'\\EngageFS\Filemaker\Development\Jordan\Logs\Automation\getlatestworkingbackup'
    log_file = os.path.join(log_dir, 'log.txt')

    with open(log_file, 'a') as f:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f'{timestamp}: {message}\n'
        f.write(log_entry)


def main():
    source_file = find_latest_backup()
    if source_file is None:
        log_message("No backup found.")
        print("No backup found.")
        return

    destination_dir = r'\\Engagefs\File Conversions\Client Files\FileMaker Upload\Working Programs'
    destination_file = os.path.join(destination_dir, 'Working.fmp12')

    try:
        shutil.copyfile(source_file, destination_file)
        log_message(f"Backup copied to {destination_file}")
        print(f"Backup copied to {destination_file}")
    except FileNotFoundError:
        log_message("Source file not found.")
        print("Source file not found.")
    except PermissionError:
        log_message("Permission denied. Make sure you have necessary permissions.")
        print("Permission denied. Make sure you have necessary permissions.")


if __name__ == "__main__":
    main()

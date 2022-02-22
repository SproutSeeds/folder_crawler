# Work on zipping the files and then transferring them

import json
import time
from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect
pretty.install()
from colorama import Fore



def connect(ipv4, username, password, key_file_path, count):
    with open('main_log.txt', 'a') as f:
        f.write(f'#{count}\n')
        f.write(f'IPV4:{ipv4}\n')
        f.write(f'password:{password}\n')
        f.write(f'key_file_path:{key_file_path}\n')
        f.write(f'OUTPUT:\n')
        f.close()

    print(Fore.GREEN + f'\n\n#{count} Attempting to connect to ipv4: {ipv4}')

    # setting up SSH client
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy)

    if password != '':
        client.connect(ipv4, username=username, password=password)
    else:
        client.connect(ipv4, username=username, key_filename=key_file_path)

    print(Fore.WHITE + 'Executing "hostname" command to test ssh connection...')

    stdin, stdout, stderr = client.exec_command('hostname')
    # Will print output of command. Will wait for command to finish.
    print(f'hostname: {stdout.read().decode("utf8")}')

    # Get return code from command (0 is default for success)
    if stdout.channel.recv_exit_status() == 0:
        print(f'Command Return Code: {stdout.channel.recv_exit_status()}')
        print(Fore.BLUE + "Command Execution: Success!" + Fore.WHITE)
        with open('main_log.txt', 'a') as f:
            f.write('Successfully connected.\n')
            f.close()
    else:
        print(f'Command Return Code: {stdout.channel.recv_exit_status()}')
        print(Fore.RED + "Command Execution: Failure!" + Fore.WHITE)
        with open('main_log.txt', 'a') as f:
            f.write('Failed connection.\n')
            f.close()
    stdin.close()
    stdout.close()
    stderr.close()

    # begin file transfer
    file_transfer(client)

def file_transfer(client):
    # transfer files
    sftp = client.open_sftp()
    try:
        sftp.put(localpath='./folder_crawler/requirements.txt', remotepath='/home/ec2-user/requirements.txt')
        sftp.put(localpath='./folder_crawler/create_files_downloads_folder.py', remotepath='/home/ec2-user/create_files_downloads_folder.py')
        sftp.put(localpath='./folder_crawler/delete_files_from_folders.py', remotepath='/home/ec2-user/delete_files_from_folders.py')
        sftp.put(localpath='./folder_crawler/determine_size.py', remotepath='/home/ec2-user/determine_size.py')
        sftp.put(localpath='./folder_crawler/file_organizer.py', remotepath='/home/ec2-user/file_organizer.py')
        sftp.put(localpath='./folder_crawler/main.py', remotepath='/home/ec2-user/main.py')
    except IOError:
        with open('main_log.txt', 'a') as f:
            f.write('IOERROR: Failed to upload python excutables.\n')
            f.close()
    except OSError:
        with open('main_log.txt', 'a') as f:
            f.write('OSERROR: Failed to upload python excutables.\n')
            f.close()

    with open('main_log.txt', 'a') as f:
        f.write('Sftp connection enabled.\n')
        f.write('All python executables successfully transferred.\n')
        f.close()

    create_environment_download_dependencies(client)

def create_environment_download_dependencies(client):
    with open('main_log.txt', 'a') as f:
        f.write('\nEXECUTING COMMANDS IN VIRTUAL MACHINE:\n')
        f.close()

    with open('main_log.txt', 'a') as f:
        # Download python3
        stdin, stdout, stderr = client.exec_command('sudo yum install python3 -y')
        if stdout.channel.recv_exit_status() == 0:
            f.write('sudo yum install python3 -y <---- SUCCESS\n')
        else:
            f.write('sudo yum install python3 -y <---- FAILURE\n')
        time.sleep(5)
        f.close()
    with open('main_log.txt', 'a') as f:
        # Creating a python3 virtual env folder named folder_crawler
        stdin, stdout, stderr = client.exec_command('python3 -m venv folder_crawler/env')
        if stdout.channel.recv_exit_status() == 0:
            f.write('python3 -m venv folder_crawler/env <---- SUCCESS\n')
        else:
            f.write('python3 -m venv folder_crawler/env <---- FAILURE\n')
        time.sleep(5)
        f.close()
    with open('main_log.txt', 'a') as f:
        # Activating the virtual environment, installing pip upgrades, installing all dependencies
        stdin, stdout, stderr = client.exec_command('source ~/folder_crawler/env/bin/activate;pip install pip --upgrade;pip install -r requirements.txt')
        if stdout.channel.recv_exit_status() == 0:
            f.write('source ~/folder_crawler/env/bin/activate;pip install pip --upgrade;pip install -r requirements.txt <---- SUCCESS\n')
        else:
            f.write('source ~/folder_crawler/env/bin/activate;pip install pip --upgrade;pip install -r requirements.txt <---- FAILURE\n')
        time.sleep(5)
        f.close()
    with open('main_log.txt', 'a') as f:
        # Sourcing virtual environment and executing main.py
        stdin, stdout, stderr = client.exec_command('source ~/folder_crawler/env/bin/activate;python main.py')
        stdin.write('2')
        time.sleep(15)
        # if stdout.channel.recv_exit_status() == 0:
        #     f.write('source ~/folder_crawler/env/bin/activate;python main.py <---- SUCCESS\n')
        # else:
        #     f.write('source ~/folder_crawler/env/bin/activate;python main.py <---- FAILURE\n')
        f.write('main.py was executed successfully. Scripting complete.\n\n\n\n')
        f.close()
    time.sleep(5)


    print('Closing stdin, stdout, stderr and client...')
    # close out all file objects
    stdin.close()
    stdout.close()
    stderr.close()
    # close the client itself
    client.close()

    time.sleep(1)

def main():
    IPV4_DNS_ADDRESSES = list()
    count = 1

    with open('IPV4_DNS_ADDRESSES_EXAMPLE.json.json', 'rt') as f:
        IPV4_DNS_ADDRESSES = json.load(f)
        f.close()

    for ip_address in IPV4_DNS_ADDRESSES:
        ipv4 = ip_address['ipv4_DNS']
        username = ip_address['username']
        password = ip_address['password']
        key_file_path = ip_address['key_file_path']
        connect(ipv4, username, password, key_file_path, count)
        count += 1

main()
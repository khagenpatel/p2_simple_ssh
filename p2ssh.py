import subprocess

# Prompt the user to enter the SSH parameters
host = raw_input('Enter the hostname: ')
username = raw_input('Enter the username: ')
password = raw_input('Enter the password: ')

# Define the list of commands
commands = [
    'show run',
    'show ip arp',
    'show mac add',
    'show cdp nei',
    'show lldp nei',
    'show int status',
    'show interface des'
]

# Construct the SSH command prefix
ssh_prefix = ['sshpass', '-p', password, 'ssh', '-o', 'StrictHostKeyChecking=no', '-o', 'UserKnownHostsFile=/dev/null', '-l', username, host]

for command in commands:
    # Construct the full SSH command
    ssh_command = ssh_prefix + [command]

    try:
        # Execute the SSH command and capture the output
        output = subprocess.check_output(ssh_command)

        # Save the output to a file
        filename = command.replace(' ', '_') + '.txt'
        with open(filename, 'w') as f:
            f.write(output)

    except subprocess.CalledProcessError:
        print('Error: Failed to execute SSH command')

    except Exception as e:
        print('Error:', e)

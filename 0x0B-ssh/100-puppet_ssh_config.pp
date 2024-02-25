#This script connect to a server without typing a password.

file_line { 'Turn off password auth':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentification no',
}

file_line {'Declare identity file':
path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/school',
}

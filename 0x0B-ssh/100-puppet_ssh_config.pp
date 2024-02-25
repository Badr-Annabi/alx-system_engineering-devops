#This script connect to a server without typing a password.

file {'/etc/ssh/ssh_config':
ensure => present,
}

file_line { 'Turn off password auth':
path  => '/etc/ssh/ssh_config',
line  => 'PasswordAuthentification no',
match => '^#PasswordAuthentification',
}

file_line {'Declare identity file':
path  => '/etc/ssh/ssh_config',
line  => 'IdentityFile ~/.ssh/school',
match => '^#IdentityFile',
}

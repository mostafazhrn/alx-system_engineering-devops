# chnge config for server to only connect with key no passwd

file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication.*$',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile.*$',
}

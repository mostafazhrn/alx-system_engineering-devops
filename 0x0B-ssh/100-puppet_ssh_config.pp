# chnge config for server to only connect with key no passwd

file_line { 'Turn passwd off':
  ensure => 'present',
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication.*$',
}

file_line { 'Declare id file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile.*$',
}

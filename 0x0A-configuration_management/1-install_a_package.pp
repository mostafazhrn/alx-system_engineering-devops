# Installs puppet-lint

exec { 'install pip3':
  command => '/usr/bin/apt-get install -y python3-pip',
}

exec { 'install flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  require => Exec['install pip3'],
  unless  => '/usr/bin/pip3 show flask | grep -q 2.1.0',
}

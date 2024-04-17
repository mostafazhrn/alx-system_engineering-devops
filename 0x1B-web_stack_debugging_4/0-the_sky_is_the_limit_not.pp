# this script shall change max no of files opened

exec { 'fix-nginx':
  path     => '/etc/local/bin/:/usr/bin:/bin',
  command  => 'sed -i "s/15/5000/" /etc/default/nginx',
  provider => shell
}

exec { 'restart-nginx':
  path     => '/etc/init.d',
  command  => 'nginx restart',
  provider => shell,
  require  => Exec['fix-nginx']
}

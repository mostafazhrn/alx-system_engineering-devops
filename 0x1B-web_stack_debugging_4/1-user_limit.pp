# This script shall change user limits

exec { 'fix-usr-hrdlimit':
  path     => '/etc/local/bin/:/usr/bin:/bin',
  command  => 'sed -i "s/5/5555/" /etc/security/limits.conf',
  provider => shell
}

exec { 'fix-usr-softlimit':
  path     => '/etc/local/bin/:/usr/bin:/bin',
  command  => 'sed -i "s/4/4444/" /etc/security/limits.conf',
  provider => shell
}

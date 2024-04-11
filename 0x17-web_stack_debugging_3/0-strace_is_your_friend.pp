#THis script shall fix typos in wordpress file

exec { 'fix_typo':
  path     => ['/bin', '/usr/bin', '/usr/sbin', '/sbin'],
  command  => 'sed -i s/.phpphp/.php/g /var/www/html/wp-settings.php',
  provider => 'shell',
}

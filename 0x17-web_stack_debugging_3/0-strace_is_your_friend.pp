#THis script shall fix typos in wordpress file

exec { 'fix_wordpress' :
  path     => '/usr/local/bin/:/bin/',
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => 'shell',
}

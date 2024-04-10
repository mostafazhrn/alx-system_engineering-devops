# THis script shall fix typos in wordpress file

exec { 'fix_wordpress_typo':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin:/bin',
    require => File['/var/www/html/wp-settings.php'],
}

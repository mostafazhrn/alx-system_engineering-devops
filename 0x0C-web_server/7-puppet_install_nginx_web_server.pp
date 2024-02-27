# This script shal install nginx on server with 301 error code

include stdlib

$url = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
$in = "\trewrite ^/redirect_me/$ ${url} permanent;"

exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/bin',
  require => Package['nginx'],
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx'],
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update packages'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  require => Package['nginx'],
}

file_line { '301 redirect':
  ensure   => present,
  after    => 'server_name _;',
  path     => '/etc/nginx/sites-available/default',
  line     => $in,
  multiple => true,
  notify   => Exec['restart nginx'],
  require  => File['/var/www/html/index.html'],
}

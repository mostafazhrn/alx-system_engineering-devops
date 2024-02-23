# This script shall kill process killmenow

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}

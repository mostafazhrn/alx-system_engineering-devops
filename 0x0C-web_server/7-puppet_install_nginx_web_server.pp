# This script shal install nginx on server with 301 error code

package { 'nginx':
  ensure => 'present',
}

exec { 'install':
  command  => 'sudo apt-get update && apt-get install -y nginx',
  provider => 'shell',
  }

exec { 'Hello World':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => 'shell',
}

exec { 'sudo sed -i "s/80 default_server;/80 default_server;
  \\n\\tlocation \\/redirect_me {\\n\\t\\treturn 301 \\/;
    \\n\\t}\\n\\t/" /etc/nginx/sites-available/default':
  provider => 'shell',
}

exec { 'run':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}

# install flask and werkzeug

package { 'flask':
  ensure          => 'installed',
  install_options => ['-v', '2.1.0'],
  provider        => 'pip3',
}

package { 'werkzeug':
  ensure          => 'installed',
  provider        => 'pip3',
  install_options => ['v', '2.1.1'],
}

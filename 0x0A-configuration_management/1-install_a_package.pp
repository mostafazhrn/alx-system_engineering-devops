# install flask and werkzeug

package { 'flask':
  ensure          => '2.1.0',
  provider        => 'pip3',
  install_options =>  ['-v', '2.1.0'],
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

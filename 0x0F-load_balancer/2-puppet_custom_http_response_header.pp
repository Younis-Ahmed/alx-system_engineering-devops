# Creating a custom HTTP header response

exec { 'apt':
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx',
  provider => shell,
}

-> exec { 'configuration':
  command => 'sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
  provider => shell,
}

-> exec { 'nginx':
  command => 'sudo service nginx restart',
  provider => shell,
}

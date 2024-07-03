# server configuration with puppet

exec {'install':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx',
  provider => shell,
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

exec {'redirect':
  command  => "sudo sed -i 's/location \/ {/location \/redirect_me { return 301 https:\/\/www.youtube.com\/watch?v=XqZsoesa55w;/' /etc/nginx/sites-available/default",
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx start',
  provider => shell,
}

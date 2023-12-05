# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Define a custom fact to get the hostname
fact { 'custom_hostname':
  setcode => 'hostname',
}

# Define Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "# Custom HTTP header configuration\nserver {\n\tlisten 80 default_server;\n\tserver_name _;\n\n\tlocation / {\n\t\tadd_header X-Served-By $custom_hostname;\n\t\t# Your other configuration goes here...\n\t}\n}\n",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/000-default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

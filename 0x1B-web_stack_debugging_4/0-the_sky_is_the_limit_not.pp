# Puppet manifest to optimize Nginx configuration

# Adjust worker_processes and worker_connections based on server resources
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "
user www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
    worker_connections 1024;
    # multi_accept on;
}

http {
    ##
    # Basic Settings
    ##

    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    ##
    # Logging Settings
    ##

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    ##
    # Gzip Settings
    ##

    gzip on;
}

include /etc/nginx/conf.d/*.conf;
include /etc/nginx/sites-enabled/*;
",
}

# Restart Nginx service after configuration changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}

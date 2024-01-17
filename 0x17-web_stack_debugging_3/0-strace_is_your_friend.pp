file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => '# Add your WordPress settings here',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin/',
  require => File['/var/www/html/wp-settings.php'],
}

# Puppet Manifest for installing Flask with pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'python3-pip':
  ensure => 'latest',
  provider => 'apt',
}

# Puppet manifest to increase the open file limit for the holberton user

# Set the limit of open files for the holberton user
user { 'holberton':
  ensure     => 'present',
  managehome => true,
  shell      => '/bin/bash',
  home       => '/home/holberton',
  comment    => 'Holberton User',
  uid        => '1001',  # Adjust UID as needed
  gid        => '1001',  # Adjust GID as needed
}

# Importing the camptocamp-systemd module
include systemd::sysctl

# Applying sysctl settings to increase the maximum number of open files
class { 'systemd::sysctl':
  values => {
    'fs.file-max' => {
      'value' => '200000'
    },
    'fs.nr_open' => {
      'value' => '200000'
    },
  },
}

# Set the soft and hard limits for open files for the holberton user
# Adjust the values as per your requirements
limits::fragment { 'holberton':
  content => "holberton hard nofile 10240\nholberton soft nofile 8192",
}

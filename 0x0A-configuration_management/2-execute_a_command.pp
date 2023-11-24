# Puppet Manifest for killing a process named "killmenow"

exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  path        => '/usr/bin',
  refreshonly => true,
  subscribe   => File['/tmp/killmenow'],
}

file { '/tmp/killmenow':
  ensure  => file,
  content => '#!/bin/bash\nwhile [[ true ]]; do sleep 2; done',
  mode    => 'ugo+x',
}

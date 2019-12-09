# Using Puppet, create a manifest that kills a process named killmenow
$paths = ['/usr/bin', '/sbin', '/bin', '/usr/sbin']

exec { 'killmenow':
command => 'pkill -e killmenow',
path    => $paths,
}

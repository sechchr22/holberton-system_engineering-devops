# Adjust limit of Open Files by nginx server on the etc/default
$current_limit='ULIMIT="-n 15"'
$new_limit='ULIMIT="-n 500000"'

$replace="'s/${current_limit}/${new_limit}/g'"

$update_limit = "sudo sed -i ${replace} nginx ; sudo service nginx restart"

exec {'Update amount of open files':
    command => $update_limit,
    path    => '/usr/bin',
    cwd     => '/etc/default'
}

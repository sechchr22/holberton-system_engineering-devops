# increase limit of open files that Holberton user can do

$current_upper='holberton hard nofile 5'
$current_lower='holberton soft nofile 4'

$update_upper='holberton hard nofile 50000'
$update_lower='holberton soft nofile 30000'

$switch_upper= "'s/${current_upper}/${update_upper}/g'"
$switch_lower= "'s/${current_lower}/${update_lower}/g'"

$config_file='limits.conf'
$update = "sudo sed -i -e ${switch_upper} -e ${switch_lower} ${config_file}"

exec {'Increace holberton user open files':
    command => $update,
    path    => '/usr/bin',
    cwd     => '/etc/security'
}

# Using puppet to modify wp-settings to fix a bug

exec { 'filefix':
command => '/bin/sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
}

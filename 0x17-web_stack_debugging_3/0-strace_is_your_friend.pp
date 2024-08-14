# Fixes bad `phpp` extensions replacing "phpp" to "php"

exec { 'fix-wordpress':
  command => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin', '/bin'
}

# Fixing the error bad `phpp` extensions in /var/www/html/wp-settings.php'

exec {'replacing':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => shell,
}
# Fixing the error bad `phpp` extensions in /var/www/html/wp-settings.php'
exec { 'replace-phpp-with-php':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  onlyif   => 'grep -q "phpp" /var/www/html/wp-settings.php',
}
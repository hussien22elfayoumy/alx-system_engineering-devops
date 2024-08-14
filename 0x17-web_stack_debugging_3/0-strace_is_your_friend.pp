# Fixing the error bad `phpp` extensions to `php` in the `wp-settings.php`.

exec {'replace':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => shell,
}
# Fixing the error bad `phpp` extensions to `php` in the `wp-settings.php`.

exec {'replacing-fix':
  command  => 'sed -i 's/phpp/php/g' /var/www/html/wp-settings.php',
  provider => shell,
}
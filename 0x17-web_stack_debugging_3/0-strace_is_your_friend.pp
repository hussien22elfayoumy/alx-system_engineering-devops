# Fixing the error bad `phpp` extensions in /var/www/html/wp-settings.php'
exec {'replacing':
	provider => shell,
	command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
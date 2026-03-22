<?php
$root = dirname(__DIR__); // public_html
$v2 = __DIR__; // public_html/v2

// 1. Create backup dir
if (!is_dir("$root/backup_v1")) {
    mkdir("$root/backup_v1", 0755);
}

// 2. Clear root files safely (ignoring important dirs)
$items = scandir($root);
foreach ($items as $item) {
    if ($item === '.' || $item === '..' || $item === 'v2' || $item === 'backup_v1' || $item === '.well-known' || $item === 'cgi-bin' || $item === '.ftpquota') {
        continue;
    }
    rename("$root/$item", "$root/backup_v1/$item");
}

// 3. Update WP options
require_once("$v2/wp-load.php");
update_option('home', 'https://stretch-plus.co.jp');
update_option('siteurl', 'https://stretch-plus.co.jp/v2');
flush_rewrite_rules(); // Ensure permalinks are rebuilt

// 4. Create new index.php in root to point to /v2
$index_php = "<?php\n/**\n * Front to the WordPress application.\n */\ndefine( 'WP_USE_THEMES', true );\nrequire __DIR__ . '/v2/wp-blog-header.php';\n";
file_put_contents("$root/index.php", $index_php);

// 5. Create new .htaccess in root for WordPress routing
$htaccess = "<IfModule mod_rewrite.c>\nRewriteEngine On\nRewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]\nRewriteBase /\nRewriteRule ^index\.php$ - [L]\nRewriteCond %{REQUEST_FILENAME} !-f\nRewriteCond %{REQUEST_FILENAME} !-d\nRewriteRule . /index.php [L]\n</IfModule>";
file_put_contents("$root/.htaccess", $htaccess);

echo "MIGRATION_SUCCESS";
?>

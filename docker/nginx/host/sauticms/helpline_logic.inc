location /helpline/ {
    root /var/www/html;
    index index.php index.html index.htm;
    try_files $uri $uri/ /helpline/api/index.php?$args;
}

location /hh13feb24_2/ {
    root /var/www/html;
    index index.php index.html index.htm;
    try_files $uri $uri/ /hh13feb24_2/api/index.php?$args;
}

location /hh24jul2025/ {
    root /var/www/html;
    index index.php index.html index.htm;
    try_files $uri $uri/ /hh24jul2025/api/index.php?$args;
}

location /wallboard/ {
    root /var/www/html;
    index index.php index.html index.htm;
}

location ~ [^/]\.php(/|$) {
    root /var/www/html;
    fastcgi_split_path_info ^(.+?\.php)(/.*)$;
    if (!-f $document_root$fastcgi_script_name) {
        return 404;
    }
    include fastcgi_params;
    fastcgi_pass unix:/run/php-fpm/www.sock;
    fastcgi_index index.php;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
}

location = /api/ {
    proxy_pass http://unix:/home/helpline/holla.sock;
}

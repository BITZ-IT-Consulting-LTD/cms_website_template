location /sauti/ {
    proxy_pass http://127.0.0.1:8080/sauti/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Host $host;
}

location ^~ /sauti/assets/ {
    proxy_pass http://127.0.0.1:8080/sauti/assets/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
}

location /cms-admin/ {
    proxy_pass http://127.0.0.1:8080/cms-admin/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Host $host;
}

location /cms-django-admin/ {
    proxy_pass http://127.0.0.1:8080/sauti/django-admin/;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
}

location /cms-api/ {
    rewrite ^/cms-api/(.*)$ /sauti/api/$1 break;
    proxy_pass http://127.0.0.1:8080;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}

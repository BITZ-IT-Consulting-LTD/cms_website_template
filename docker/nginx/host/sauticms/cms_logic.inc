# Crawler-facing OG previews for article links (item 10). WhatsApp/Facebook/
# X/LinkedIn/Telegram etc. fetch a shared link and read its <meta> tags
# without running JS, so the client-rendered SPA is invisible to them. For
# requests whose User-Agent matches a known link-preview crawler ONLY, this
# is forwarded (still through the docker prod nginx's own /sauti/api rewrite
# to Django) to the crawler-facing OG HTML instead of the SPA shell below.
# Everyone else keeps hitting the normal /sauti/ location underneath.
# Internal target for the crawler rewrite below. `internal` means it
# cannot be requested from outside, so it is not a second public URL
# for the same article.
location ~ ^/__og_preview/(?<og_slug>.+)$ {
    internal;
    proxy_pass http://127.0.0.1:8080/sauti/api/seo/post/$og_slug/;
    proxy_set_header Host $host;
}

location ~ ^/sauti/blogs/(?<og_slug>[^/]+)/?$ {
    if ($http_user_agent ~* "facebookexternalhit|Facebot|Twitterbot|WhatsApp|LinkedInBot|TelegramBot|Slackbot|Discordbot|SkypeUriPreview|Pinterest|redditbot|Applebot|Googlebot|bingbot|DuckDuckBot") {
        rewrite ^ /__og_preview/$og_slug last;
    }
    proxy_pass http://127.0.0.1:8080/sauti/blogs/$og_slug;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Host $host;
}

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

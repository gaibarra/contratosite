# Deploy: contratosmodelo.site

This folder contains example configs for Nginx and systemd (Gunicorn).

## Paths assumed
- Project root: `/home/gaibarra/contrato`
- Django settings: `contrato.settings.production`
- Collected static: `/home/gaibarra/contrato/contrato/staticfiles/`
- Media: `/home/gaibarra/contrato/contrato/media/`
- Logs: `/home/gaibarra/logs/`

Adjust as needed.

## Gunicorn (systemd)
1. Copy service:
   - sudo cp deploy/systemd/gunicorn.service /etc/systemd/system/gunicorn.service
2. Reload and enable:
   - sudo systemctl daemon-reload
   - sudo systemctl enable --now gunicorn
3. Check status/logs:
   - systemctl status gunicorn
   - journalctl -u gunicorn -f

Note: Ensure venv path if not using system python; e.g., replace `/usr/bin/gunicorn` with `/home/gaibarra/contrato/.venv/bin/gunicorn`.

## Nginx
1. Copy site config:
   - sudo cp deploy/nginx/contratosmodelo.site.conf /etc/nginx/sites-available/contratosmodelo.site
2. Enable:
   - sudo ln -s /etc/nginx/sites-available/contratosmodelo.site /etc/nginx/sites-enabled/
3. Test & reload:
   - sudo nginx -t
   - sudo systemctl reload nginx

## Certbot (already present)
Ensure certificates exist at:
- /etc/letsencrypt/live/contratosmodelo.site/fullchain.pem
- /etc/letsencrypt/live/contratosmodelo.site/privkey.pem

## Static files
Run after code updates:
- source .venv/bin/activate
- python manage.py collectstatic --noinput

## Socket permissions
Gunicorn creates `/run/gunicorn.sock`. Ensure Nginx (group `www-data`) can access it; service sets `Group=www-data`.

## Troubleshooting
- 502 Bad Gateway: check gunicorn running and socket perms.
- Permission denied on socket: verify `Group=www-data` and directory perms.
- Static 404: verify collectstatic path and Nginx `alias`.

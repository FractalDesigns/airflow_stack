mkdir -m 700 /var/lib/pgadmin/storage/elafrit.achraf_gmail.com
mv /tmp/pgpassfile /var/lib/pgadmin/storage/elafrit.achraf_gmail.com/pgpassfile
mv /tmp/servers.json /var/lib/pgadmin/storage/elafrit.achraf_gmail.com/servers.json
chown pgadmin:root /var/lib/pgadmin/storage/elafrit.achraf_gmail.com/pgpassfile
chown pgadmin:root /var/lib/pgadmin/storage/elafrit.achraf_gmail.com/servers.json
chmod 600 /var/lib/pgadmin/storage/elafrit.achraf_gmail.com/pgpassfile
chown pgadmin:root /var/lib/pgadmin/storage/elafrit.achraf_gmail.com/servers.json
/venv/bin/python /pgadmin4/setup.py --load-servers /var/lib/pgadmin/storage/elafrit.achraf_gmail.com/servers.json --user elafrit.achraf@gmail.com
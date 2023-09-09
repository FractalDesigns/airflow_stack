docker-compose up -d
sleep 5
docker cp pgpassfile pgadmin:/tmp/pgpassfile
docker cp servers.json pgadmin:/tmp/servers.json
docker cp import.sh pgadmin:/tmp/import.sh
docker exec -i -u root pgadmin sh -c 'chown pgadmin:root /tmp/import.sh'
docker exec -it -u root pgadmin sh -c 'sh /tmp/import.sh'

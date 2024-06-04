export AIRFLOW_HOME=/root/source/repos/gcp-composer-exploitation
export AIRFLOW_UID=50000
podman-compose up -d
sleep 5
podman cp pgpassfile pgadmin:/tmp/pgpassfile
podman cp servers.json pgadmin:/tmp/servers.json
podman cp import.sh pgadmin:/tmp/import.sh
podman exec -i -u root pgadmin sh -c 'chown pgadmin:root /tmp/import.sh'
podman exec -it -u root pgadmin sh -c 'sh /tmp/import.sh'

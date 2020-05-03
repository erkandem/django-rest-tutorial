#!/bin/sh
# wait-for-postgres.sh
# copied from https://docs.docker.com/compose/startup-order/
# also https://stackoverflow.com/questions/42307008/django-cant-connect-to-postgres-in-docker-setup
set -e

host="$1"
shift
cmd="$@"

sleep_duration=5
echo "sleeping $sleep_duration seconds"
sleep $sleep_duration

until PGPASSWORD=$POSTGRES_INITIAL_PASSWORD psql -h "$host" -U postgres -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done

>&2 echo "Postgres is up - executing command"
exec $cmd

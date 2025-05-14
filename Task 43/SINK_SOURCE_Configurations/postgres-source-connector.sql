{
  "name": "postgres-source-connector",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "localhost",
    "database.port": "5432",
    "database.user": "cdc_user",
    "database.password": "cdc_password",
    "database.dbname": "source_db",
    "database.server.name": "pg_server",
    "topic.prefix": "pg_server",
    "table.include.list": "public.users",
    "plugin.name": "pgoutput",
    "publication.name": "dbz_publication",
    "publication.autocreate.mode": "disabled",
    "slot.name": "debezium_slot",
    "tombstones.on.delete": "true"
  }
}

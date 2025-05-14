{
  "name": "mysql-sink-connector",
  "config": {
    "connector.class": "io.debezium.connector.jdbc.JdbcSinkConnector",
    "tasks.max": "1",
    "connection.url": "jdbc:mysql://localhost:3306/target_db?useSSL=false",
    "connection.username": "cdc_user",
    "connection.password": "cdc_password",
    "topics": "pg_server.public.users",
    "table.name.format": "users",
    "insert.mode": "upsert",
    "primary.key.mode": "record_key",
    "primary.key.fields": "id",
    "auto.create": "false",
    "auto.evolve": "false",
    "delete.enabled": "true"
  }
}

from azure.data.tables import TableServiceClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=mystoragetable98659080;AccountKey=bFRlgjos1qJx+GB86ub9LYrHZQVGvVuZvH65X0OE21UhluBe6NCFKimYk7PEE3HazS7nsMgzrQUF+AStM39MoQ==;EndpointSuffix=core.windows.net"

service = TableServiceClient.from_connection_string(conn_str=connection_string)

table_name = "mytable"
table_client = service.get_table_client(table_name)

entity = {
    "PartitionKey": "Users",
    "RowKey": "3",
    "Name": "Amol",
    "Age": 33
}

table_client.upsert_entity(entity=entity)

print("Entity upserted successfully!")

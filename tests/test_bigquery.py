from citypulse.cloud.bigquery import BigQueryClient

client = BigQueryClient()

client.test_connection()

client.create_complaints_table()



from citypulse.cloud.bigquery import BigQueryClient

client = BigQueryClient()

query = """
SELECT
    DATE(created_at) AS day,
    COUNT(*) AS total
FROM
    `linear-quasar-497618-a9.citypulse.complaints`
GROUP BY day
ORDER BY day
"""

rows = client.client.query(query).result()

print("\nComplaint Distribution\n")

for row in rows:
    print(row.day, row.total)
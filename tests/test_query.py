from citypulse.cloud.bigquery import BigQueryClient

client = BigQueryClient()

query = """
SELECT
    ward,
    COUNT(*) AS total
FROM
    `linear-quasar-497618-a9.citypulse.complaints`
GROUP BY ward
ORDER BY total DESC
"""

rows = client.execute_query(query)

for row in rows:
    print(row)
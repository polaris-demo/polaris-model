import prestodb
import pandas as pd
from pprint import pprint
# https://prestodb.io/docs/current/overview/concepts.html

conn=prestodb.dbapi.connect(
    host='localhost',
    port=7000,
    user='the-user',
    catalog='postgresql', # presto catalog = postgresql database
    schema='public',  # presto schema = postgresql schema
    # auth=prestodb.auth.BasicAuthentication("principal id", "password"),
)
cur = conn.cursor()
cur.execute('SELECT * FROM postgresql.public.wines limit 10')
rows = cur.fetchall()
titles = [col[0] for col in cur.description]
df = pd.DataFrame(rows, columns=titles)
df.to_pickle("data.pkl")

print(df.head())
print(df[["quality", "citric_acid"]])
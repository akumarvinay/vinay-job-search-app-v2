import os

from sqlalchemy import create_engine, text

connectionString = os.environ['MYSQL_CONNECTION_STRING']
engine = create_engine(
    connectionString,
    connect_args={"ssl": {
        "ssl_ca": "/etc/ssl/certs/ca-certificates.crt"
    }})


def retrieve_jobs():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    # print(result.all()) --> this is printing list of row classes

    row_dictionaries = []
    # _mapping is used to convert row into python dictionary
    for every_row in result.all():
      row_dictionaries.append(every_row._mapping)

    return row_dictionaries

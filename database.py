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
    result_all = result.all()

    for every_row in result_all:
      row_dictionaries.append(dict(every_row._mapping))

    return row_dictionaries


def retrieve_job_info(jobid):
  with engine.connect() as con:
    result = con.execute(text("select * from jobs where id = :val"),
                         {"val": jobid})
    jobInfo = result.all()
    if len(jobInfo) == 0:
      return None
    else:
      job_row = jobInfo[0]
      dictobj = dict(job_row._mapping)
      return dictobj

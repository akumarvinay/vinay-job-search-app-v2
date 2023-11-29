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


def add_job_application_into_db(applicant_info, job_id):
  print("Adding job application into database")

  with engine.connect() as con:
    query = text(
        "INSERT INTO job_applicaton(jobid,fullname,emailid,resume_url,linkedin_url, education_qualification,work_experience) values(:job_id, :fullname, :emailid, :resume_url, :linkedin_url, :education_qualification, :work_experience);"
    )
    result = con.execute(
        query, {
            "job_id": job_id,
            "fullname": applicant_info['full_name'],
            "emailid": applicant_info["emailid"],
            "resume_url": applicant_info["resume_url"],
            "linkedin_url": applicant_info["linkedin_url"],
            "education_qualification":
            applicant_info["educational_qualification"],
            "work_experience": applicant_info["work_experience"]
        })


def get_applications_from_db():
  with engine.connect() as con:
    result = con.execute(text("select * from job_applicaton"))
    applications = result.all()
    applications_info = []
    for everyapp in applications:
      applications_info.append(dict(everyapp._mapping))

    return applications_info

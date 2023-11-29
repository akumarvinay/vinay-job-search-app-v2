from flask import Flask, jsonify, render_template, request

from database import add_job_application_into_db, get_applications_from_db, retrieve_job_info, retrieve_jobs

app = Flask(__name__)


@app.route("/")
def sayhello():
  JOBS = retrieve_jobs()
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def listjobs():
  JOBS = retrieve_jobs()
  return jsonify(JOBS)


@app.route("/job/<id>")
def get_job_info(id):
  job_info = retrieve_job_info(id)
  #return jsonify(job_info)
  if job_info is None:
    return 'Not found', 404
  return render_template("job-details.html", job=job_info)


@app.route("/job/<id>/apply", methods=["POST"])
def apply_job(id):
  job_id = id
  applicant_info = request.form  # Arguments sent in input form
  add_job_application_into_db(applicant_info, job_id)
  return render_template("application_submitted.html",
                         userInfo=applicant_info,
                         jobid=job_id)


@app.route("/api/applications")
def get_all_applications():
  applications = get_applications_from_db()
  return jsonify(applications)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

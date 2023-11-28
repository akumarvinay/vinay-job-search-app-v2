from flask import Flask, jsonify, render_template

from database import retrieve_job_info, retrieve_jobs

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


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

from flask import Flask, jsonify, render_template

from database import retrieve_jobs

app = Flask(__name__)

# JOBS = [{
#     "ID": "10012",
#     "Tittle": "Python Developer",
#     "Location": "Bangalore",
#     "Salary": "Rs. 10,00,000",
#     "Experience": "2 Years"
# }, {
#     "ID": "10013",
#     "Tittle": "Java Developer",
#     "Location": "Delhi",
#     "Experience": "3 Years"
# }, {
#     "ID": "10014",
#     "Tittle": "Devops Engineer",
#     "Location": "Mumbai",
#     "Salary": "Rs. 12,00,000",
#     "Experience": "2 Years"
# }, {
#     "ID": "10015",
#     "Tittle": "Cloud Support Engineer",
#     "Location": "Bangalore",
#     "Experience": "3 Years",
#     "Salary": "Rs. 10,00,000"
# }]


@app.route("/")
def sayhello():
  JOBS = retrieve_jobs()
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def listjobs():
  JOBS = retrieve_jobs()
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

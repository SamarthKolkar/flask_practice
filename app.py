from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
    'id' : 1,
    'title' : 'Data analyst',
    'location' : 'Delhi',
    'salary' : 'Rs 15,00,000'
    },

    {
    'id' : 2,
    'title' : 'Cyber security',
    'location' : 'Banglore',
    'salary' : 'Rs 20,00,000'
    },

    {
    'id' : 3,
    'title' : 'Frontend Engineer',
    'location' : 'Pune',
    'salary' : 'Rs 10,00,000'
    },

    {
    'id' : 4,
    'title' : 'Backend engineer',
    'location' : 'Remote',
    'salary' : 'Rs 13,00,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
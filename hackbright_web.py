"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    project_list = hackbright.get_grades_by_github(github)


    html = render_template('student_info.html',
                            first=first,
                            last=last,
                            github = github,
                            project_list=project_list)
    
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching a student."""

    return render_template("student_search.html")


@app.route("/new-student-form")
def show_new_student_form():
    """Show form for adding a new student."""

    return render_template("make_new_student.html")


@app.route("/make-new-student", methods=["POST"])
def add_new_student():
    """Add new student based on input from form."""

    first= request.form.get('first-name')
    last= request.form.get('last-name')
    github= request.form.get('github')


    hackbright.make_new_student(first, last, github)

    return render_template('student_added.html', github=github)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")

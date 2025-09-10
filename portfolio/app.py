from flask import Flask, render_template

app = Flask(__name__)

# Data for dynamic rendering
PROJECTS = [
    {"name": "Airplane Management System", "repo": "Airplane-Management-System"},
    {"name": "CodeProcessor", "repo": "CodeProcessor"},
    {"name": "Book Management Rental System", "repo": "Book-Management-Rental-System"},
    {"name": "University Admission Management", "repo": "University-Admission-Management"},
    {"name": "My Portfolio", "repo": "My-Portfolio"},
    {"name": "E-Commerce Platform", "repo": "E-Commerence-Platform"},
]
GITHUB_BASE = "https://github.com/SahilBhatti09/"

AWARDS = [
    "Medal of Excellence – Formanites Debating Society, FCCU",
    "Torch Bearer Award – Formanites Debating Society, FCCU",
    "10+ National Debating Tournaments",
    "Best Narrator Award – Annual Urdu Play, FCCU",
]

CERTIFICATIONS = [
    "Python & Flask Development – FCCU",
    "Leadership & Public Speaking Workshops",
    "Software Engineering Coursework Projects",
]

EXPERIENCES = [
    "Work-Study Student – Financial Aid & International Education Office, FCCU (2022–25)",
    "Customer Care Agent – OnAir Solutions (2021)",
    "President – Formanites Debating Society, FCCU (2024–25)",
    "Media Manager – FCCU Societies (2023–25)",
    "Youth Service Lead – Rotaract Club, FCCU (2023–24)",
]

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects", projects=PROJECTS, github_base=GITHUB_BASE)

@app.route("/awards")
def awards():
    return render_template("awards.html", title="Awards", awards=AWARDS)

@app.route("/certifications")
def certifications():
    return render_template("certifications.html", title="Certifications", certifications=CERTIFICATIONS)

@app.route("/exp")
def experiences():
    return render_template("exp.html", title="Experiences", experiences=EXPERIENCES)

if __name__ == "__main__":
    app.run(debug=True)

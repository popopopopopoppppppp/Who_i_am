from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        name="Peter",
        skills="Python | HTML | CSS | Flask",
        message="I am a future full stack developer 💻🔥"
    )

@app.route("/projects")
def projects():
    my_projects = [
        {
            "name": "Calculator",
            "desc": "Simple calculator using Python"
        },
        {
            "name": "Who Am I Website",
            "desc": "Personal website using Flask"
        },
        {
            "name": "Temperature Converter",
            "desc": "Convert Celsius to Fahrenheit"
        }
    ]
    return render_template("projects.html", projects=my_projects)

if __name__ == "__main__":
    app.run(debug=True)

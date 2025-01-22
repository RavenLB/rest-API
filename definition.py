from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home2.html")

@app.route("/api/v1/<word>/")
def about(word):
    definition =
    return {"word": word, "definition": definition}

if __name__ == "__main__":
    app.run(debug=True)
   # app.run(debug=True, port=5001)if you have multiple apps running at once you can specify the port here

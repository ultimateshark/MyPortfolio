from flask import Flask,render_template,redirect

app=Flask(__name__)

@app.route("/")
def Home():
	return render_template("home.html")

@app.route("/project1")
def project1():
	return render_template("project1.html")

if __name__ == '__main__':
	app.run(debug=True)

from flask import Flask,render_template,redirect
from blogs import blogs
app=Flask(__name__)



@app.route("/")
def Home():
	return render_template("home.html")

@app.route("/blog-<int:blog_no>")
def Blogs(blog_no):
	return render_template("project1.html",blog_content=blogs[blog_no])

if __name__ == '__main__':
	app.run(debug=True)

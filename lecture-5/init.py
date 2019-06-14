from flask import Flask,render_template,redirect,request
from blogs import blogs
app=Flask(__name__)

@app.route("/")
def Home():
	return render_template("home.html")

@app.route("/blog-<int:blog_no>")
def Blogs(blog_no):
	return render_template("project1.html",blog_content=blogs[blog_no-1])

@app.route("/blog-entry-page")
def blog_entry_page():
	return render_template("blog_entry.html")

@app.route("/blog-entry",methods=["GET","POST"])
def blog_entry():
	global blogs
	heading=request.form["head"]
	content=request.form["content"]
	blogs.append({
	"heading":heading,"img":"blog2.png",
	"content":content
	})
	return redirect("/")

if __name__ == '__main__':
	app.run(debug=True)









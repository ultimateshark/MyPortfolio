from flask import Flask,render_template,redirect,request
from models import *
app=Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:mom0511@localhost/myportfolio"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
db.init_app(app)
db.app=app


@app.route("/")
def Home():
	return render_template("home.html")

@app.route("/blog-<int:blog_no>")
def Blog(blog_no):
	blog_content=Blogs.query.filter_by(bid=blog_no).one()
	#return str(blog_content.content)
	return render_template("project1.html",blog_content=blog_content)

@app.route("/blog-entry-page")
def blog_entry_page():
	return render_template("blog_entry.html")

@app.route("/blog-entry",methods=["GET","POST"])
def blog_entry():
	head=request.form["head"]
	cont=request.form["content"]
	new_blog=Blogs(heading=head,img="blog2.png",content=cont)
	db.session.add(new_blog)
	db.session.commit()
	return redirect("/")

@app.route("/all-blogs")
def all_blogs():
	blog_all=Blogs.query.all()
	return render_template("all_blogs.html",blog_all=blog_all)


if __name__ == '__main__':
	app.run(debug=True,host="0.0.0.0")









from flask import Flask, render_template, request
import requests
import smtplib

EMAIL = 'ekipavronsta@gmail.com'
PASSWORD = 'ecjizsvtezmidght'

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", data=0)
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        if all([name, email, phone, message]):
            print(name, email, phone, message)
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(EMAIL, PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=EMAIL,
                    msg=f"Subject: Login \n\n Successful login attempt\n"
                        f"Name = {name}, Email= {email},"
                        f"Phone = {phone}, Message = {message}"
                )
            return render_template("contact.html", data=1)
        else:
            return "error"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


# @app.route("/form-entry", methods=['POST'])
# def receiving():
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#     if all([name, email, phone, message]):
#         print(name, email, phone, message)
#         return 'Success'
#     else:
#         return "error"


if __name__ == "__main__":
    app.run(debug=True, port=5001)

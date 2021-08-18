from flask import Flask, render_template, jsonify
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditorField
from flask_mail import Mail, Message
import os

# initializing the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
Bootstrap(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TSL'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "nonyeibeanu5@gmail.com"
app.config['MAIL_PASSWORD'] = "wwaecglcdiilwvun"
mail = Mail(app)


# creating a "contact me" form class
class ContactMeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    message = CKEditorField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")


# creating a home route
@app.route('/', methods=["GET", "POST"])
def home():
    form = ContactMeForm()
    if form.validate_on_submit():

        message = Message(f"Message from {form.email.data}    {form.message.data}", sender="nonyeibeanu5@gmail.com",
                          recipients=['nonyeibeanu@gmail.com'])
        mail.send(message)
        return jsonify(f"Hello {form.name.data}, thank you for contacting me")
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

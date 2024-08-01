from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import ContactForm
from flask_mail import Mail, Message
from config import EMAIL_PASSWORD, EMAIL_ADDRESS
import os
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False').lower() in ('true', '1', 't')
app.config['EMAIL_ADDRESS'] = os.getenv('EMAIL_ADDRESS')
app.config['EMAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
app.config['ADMIN_PASSWORD'] = os.getenv('ADMIN_PASSWORD')

db = SQLAlchemy(app)

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = EMAIL_ADDRESS
app.config["MAIL_PASSWORD"] = EMAIL_PASSWORD
mail.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender=EMAIL_ADDRESS, recipients=[EMAIL_ADDRESS])
      msg.body = """ 
        This message was sent from the portfolio contact form.

        From: %s <%s> 
        %s 
        """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('contact.html', success=True)
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@app.route('/coffee')
def coffee():
    return render_template('coffee.html')

@app.route('/coffee_menu')
def coffee_menu():
    return render_template('coffee_menu.html')

@app.route('/coffee_specials')
def coffee_specials():
    return render_template('coffee_specials.html')

@app.route('/coffee_today')
def coffee_today():
    return render_template('coffee_today.html')

@app.route('/asimov')
def asimov():
    return render_template('asimov.html')

@app.route('/roshambo', methods=['GET', 'POST'])
def roshambo():
    result = ""
    if request.method == 'POST':
        one = request.form.get('player1').lower()
        two = request.form.get('player2').lower()

        if one == "r":
            if two == "r":
                result = "It's a tie, throw again."
            elif two == "p":
                result = "Paper covers Rock, Player 2 wins!"
            elif two == "s":
                result = "Rock smashes Scissors, Player 1 wins!"
            else: 
                result = "Invalid move from Player 2."
        elif one == "p":
            if two == "r":
                result = "Paper covers Rock, Player 1 wins!"
            elif two == "p":
                result = "It's a tie, throw again."
            elif two == "s":
                result = "Scissors cut Paper, Player 2 wins!"
            else: 
                result = "Invalid move from Player 2."
        elif one == "s":
            if two == "r":
                result = "Rock smashes Scissors, Player 2 wins!"
            elif two == "p":
                result = "Scissors cut Paper, player 1 wins!"
            elif two == "s":
                result = "It's a tie, please throw again."
            else: 
                result = "Invalid move from Player 2."
        else:
            result = "Invalid move from Player 1."

    return render_template('roshambo.html', result=result)

@app.route('/technical')
def technical():
    return render_template('technical.html')

@app.route('/expenses')
def expenses():
    return render_template('expenses.html')


@app.route('/validate', methods=['POST'])
def validate():
    # Extract form data
    form_data = {
        'summary': request.form.get('summary', ''),
        'accID': request.form.get('accID', ''),
        'lname': request.form.get('lname', ''),
        'fname': request.form.get('fname', ''),
        'init': request.form.get('init', ''),
        'deptID': request.form.get('deptID', ''),
        'ssn': request.form.get('ssn', ''),
        'projID': request.form.get('projID', ''),
    }

    # Initialize an empty dictionary to keep track of errors
    errors = {}

    # Check for empty fields and add errors as needed
    for field, value in form_data.items():
        if not value:
            errors[field] = f'{field} is required.'

    # Additional pattern checks
    if form_data['accID'] and not form_data['accID'].startswith('ACC'):
        errors['accID'] = 'Account ID must start with ACC and follow the pattern ACCnnnn.'
    
    if form_data['deptID'] and not form_data['deptID'].startswith('DEPT'):
        errors['deptID'] = 'Department ID must start with DEPT and follow the pattern DEPTnnnn.'

    if form_data['ssn'] and not request.form['ssn'].replace('-', '').isdigit():
        errors['ssn'] = 'Social Security Number must be numeric and follow the pattern nnn-nn-nnnn.'

    if form_data['projID'] and not form_data['projID'].startswith('PROJ-'):
        errors['projID'] = 'Project ID must start with PROJ- and follow the pattern PROJ-nnnn.'

    # Check if there are any errors
    if errors:
        # If there are errors, render the validation template with error messages
        return render_template('validate.html', errors=errors, form_data=form_data)
    else:
        # If there are no errors, process the form data as needed (e.g., save to a database)
        # Then render the validation template with a success message
        return render_template('validate.html', success=True)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), unique=True, nullable=False)
    slug = db.Column(db.String(140), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<BlogPost {self.title}>'

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

# Define routes
@app.route('/blog')
def blog():
    posts = BlogPost.query.order_by(BlogPost.timestamp.desc()).all()
    return render_template('blog.html', posts=posts)

@app.route('/post/<slug>')
def post(slug):
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    return render_template('post.html', post=post)

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        password = request.form['password']
        if password == app.config['ADMIN_PASSWORD']:
            title = request.form['title']
            content = request.form['content']
            slug = title.lower().replace(' ', '-')
            new_post = BlogPost(title=title, content=content, slug=slug)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('blog'))
        else:
            flash('Invalid password')
    return render_template('add_post.html')

if __name__ == '__main__':
    app.run(debug=True)
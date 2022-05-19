from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'a27ec479f46d91d5c46f2ec8'

posts = [
    {
    
      'author':'Oscar Kamau',
      'title': 'First gig',
      'content': 'one',
      'date_posted': 'May 18, 2022' #dict
    },
        
    {
    
      'author':'Sekani Kamau',
      'title': 'My son',
      'content': 'To dad ',
      'date_posted': 'May 19, 2022'
    }
]         

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route('/register')
def register():
    
    form = RegistrationForm()
    return render_template('register.html',title= 'Register',form=form)

@app.route('/login')
def login():
    
    form = LoginForm()
    return render_template('login.html',title= 'Login',form=form)





if __name__ =='__main__':
    app.run(debug=True)
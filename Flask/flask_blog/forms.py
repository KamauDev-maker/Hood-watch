from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username'
                           ,validators=[DataRequired(),Length(min=2, max=10)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    Password = PasswordField('confirm password',validators=[DataRequired()])
    confirm_Password = PasswordField('password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('sign up')
    
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    Password = PasswordField('confirm password',validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')    
    
    
    
    
    
    
    
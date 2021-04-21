from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

"""
This is what creates the fields for what the user can interact with.
It creates fields for an author, a message, and a button that will send
them over.
"""
class MessageForm(FlaskForm):
    # add
    # author (string) validator should make this textbox required
    author = StringField('Author', validators = [DataRequired()])
    # message (string) validator should make this textbox required
    message = StringField('Message', validators = [DataRequired()])    
    # submit (button) text should say 'Send' 
    submit = SubmitField('Send')

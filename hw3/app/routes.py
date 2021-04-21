from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route("/", methods=['POST', 'GET'])
def home():
    form=MessageForm()
    if form.validate_on_submit():
        # check if user exits in database
        # if not create user and add to database
        # create row in Message table with user (created/found) add to ta database
        user = User.query.filter_by(author=form.author.data).first()
        if user is None:
            newuser = User(author=form.author.data)
            db.session.add(newuser)
        row = Messages(message=form.message.data, user_id=User.query.filter_by(author=form.author.data).first().id)
        db.session.add(row)
        db.session.commit()
    
    # output all messages
    # create a list of dictionaries with the following structure
    # [{'author':'carlos', 'message':'Yo! Where you at?!'},
    #  {'author':'Jerry', 'message':'Home. You?'}]
    posts = [
        {
            'author' : 'Carlos',
            'message' : 'Yo! Where you at?!'
        },
        {
            'author' : 'Jerry',
            'message' : 'Home. You?'
        }
    ]

    allmessages =  Messages.query.all()
    if allmessages is not None:
        for newmessage in allmessages:   
            posts = posts + [
                { 
                    'author' : f'{User.query.filter_by(id=newmessage.user_id).first().author}',
                    'message' : f'{newmessage.message}'
                }
            ]    
                  
    return render_template('home.html', posts=posts, form=form)

from flask import render_template,abort
from . import blog
from flask_login import login_required,current_user
from ..models import User

# Views
@blog.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')


@blog.route('/profile/<username>')
@login_required
def profile(username):

    '''
    View profile page function that returns the profile details of the current user logged in
    '''
    user = User.query.filter_by(username = username).first()
    
    if user is None:
        abort(404)
 
    return render_template("profile/profile.html", user = user)      


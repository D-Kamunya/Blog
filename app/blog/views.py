from flask import render_template
from . import blog
from flask_login import login_required


# Views
@blog.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')


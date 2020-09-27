from flask import render_template
from . import blog


# Views
@blog.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')


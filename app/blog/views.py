from flask import render_template,abort,request,redirect,url_for
from . import blog
from flask_login import login_required,current_user
from ..models import User,Article
from .forms import UpdateProfile
from .. import db,photos
from ..requests import get_quotes
# Views
@blog.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quotes=get_quotes()
    return render_template('index.html',quotes=quotes)


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
    

@blog.route('/profile/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('blog.profile',username=user.username))

    return render_template('profile/update.html',user=user,form =form)    

@blog.route('/profile/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('blog.update_profile',username=username))  



@blog.route('/article/new',methods= ['GET','POST'])
@login_required
def new_article():
    if request.method=='POST':
        article_title=request.form['title']
        article_body=request.form['body']
        article_tag=request.form['tag']
        filename = photos.save(request.files['photo'])
        article_cover_path=f'photos/{filename}'
        
        new_article=Article(article_title=article_title,article_body=article_body,article_tag=article_tag,article_cover_path=article_cover_path,user=current_user)
        new_article.save_article()
        return redirect(url_for('blog.index'))

    return render_template('new_article.html')  
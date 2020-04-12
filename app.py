from flask import Flask, render_template, request, send_file, redirect
from flask import session, Response
from flask_sqlalchemy_session import flask_scoped_session
from utils.base import session_factory
from utils.api import *
from utils.googleapi import *
from base64 import b64encode
from CAS import CAS, login
from CAS import login_required
from s3 import list_files, upload_file, check_file_bytes
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'bdfa8a83f16eb4f95dc2473fe4a50820b14e74cc70cef6ae'
sess = flask_scoped_session(session_factory, app)

########## CAS AUTHENTICATION ###########
cas = CAS(app)
app.config['CAS_SERVER'] = "https://fed.princeton.edu/cas/login"
app.config['CAS_AFTER_LOGIN'] = 'caslogin'
app.config['CAS_AFTER_LOGOUT'] = 'http://localhost:8000/caslogout'
app.config['CAS_LOGIN_ROUTE'] = '/cas'
################# AWS ####################
UPLOAD_FOLDER = "uploads"
BUCKET = "iw-spring"

def isLoggedIn():
    if 'username' in session:
        return True
    return False

@app.route('/')
@app.route('/signin')
def signin():
    if isLoggedIn():
      return render_template("index.html")
    return render_template("signin.html")

@app.route('/caslogin')
def caslogin():
   print(app.config['CAS_USERNAME_SESSION_KEY'])
   if cas.username is not None:
      print("user:", cas.username)
      session['username'] = cas.username
      print("confirming user logged into session", session['username'])
      session.modified = True
      add_get_user(cas.username)
   return redirect('/')

@app.route('/caslogout')
def caslogout():
   if isLoggedIn():
      session.pop('username')
      if 'admin' in session:
          session.pop('admin')
      session.modified = True
   return render_template("signin.html")

@app.route('/index')
def index():
  if isLoggedIn():
      albums = get_all_albums(session['username'])
      return render_template("index.html", albums=albums)
  return render_template("signin.html")

# add images
@app.route('/success', methods = ['POST'])
def success():
    if isLoggedIn():
        # netid = "jyxu"
        print(session['username'])
        user_obj = add_get_user(session['username'])
        non_valid = []
        if request.method == 'POST':
            album = request.form['a_name']
            album_obj= add_get_album(album, user_obj)

            files = request.files.getlist("file")
            file_tag = {}

            for f in files:
                # upload file to aws
                f.save(f.filename)
                if check_file_bytes(f.filename) == 0:
                    continue
                upload_file(f"{f.filename}", BUCKET)
                link = "https://iw-spring.s3.amazonaws.com/uploads/%s" % f.filename

                f.seek(0)
                content = f.read()
                tags, d_types = annotate_img_bytestream(content)
                img_obj = add_image(album_obj, link, tags, d_types)

                type_tags = img_tags_all_category(img_obj)
                file_tag[f] = type_tags

                os.remove(f.filename)
            return render_template("success.html", album = album, file_tag = file_tag, non_valid = non_valid)
    return render_template("signin.html")

@app.route('/all_tags')
def all_tags():
    if isLoggedIn():
        tags = get_all_tags(session['username'])
        return render_template("all_tags.html", tags = tags)
    return render_template("signin.html")

@app.route('/search', methods = ['POST'])
def search():
    if isLoggedIn():
        if request.method == 'POST':
            search = request.form['search']
            if search is '':
                return render_template("index.html")
            input = search.split(',')
            tags = {}
            albums = []
            reject = []
            for i in input:
                i = i.strip()
                t = False
                a = False
                if is_tag(i):
                    tags[i] = tag_num_img(i)
                    t = True
                if is_album(i):
                    albums.append(i)
                    a = True
                if not a and not t:
                    reject.append(i)
            return render_template("search.html", search=search, tags=tags,
                                              albums=albums, reject=reject)
    return render_template("signin.html")

@app.route('/image')
def image():
    if isLoggedIn():
        id = request.args.get('img')
        img_obj = img_obj_id(id)
        album = album_obj_id(img_obj.album_id)
        type_tags = img_tags_all_category(img_obj)
        print(img_obj.url)
        return render_template("image.html", image = img_obj.url, album = album, type_tags = type_tags)
    return render_template("signin.html")

@app.route('/tag')
def tag():
    if isLoggedIn():
        tag_name = request.args.get('tag_name')
        images = search_by_tag(tag_name, session['username'])
        return render_template("tag.html", search = tag_name, images = images)
    return render_template("signin.html")
#
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug = True)

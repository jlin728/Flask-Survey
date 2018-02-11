from flask import Flask, render_template, request, redirect, session, flash

# import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
 
app = Flask(__name__)
app.secret_key="SecretKeyPassword"

@app.route('/')
def index():
  return render_template("index.html")

# @app.route('/', methods=['GET'])
# def index():
#   return render_template("index.html")

@app.route('/process', methods=['post'])
def process():
  name = request.form['name']
  # email = request.form['email']
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']

  if len(request.form['name']) < 1:
    flash('Name cannot be empty')
  elif len(request.form['comment']) > 120:
    flash('Comments too long')
  else:
    flash('Why hello {}'.format(request.form['name']))
    
    return render_template("return.html", name=name, location=location, language=language, comment=comment)
  # orange = name between {{}}, = location is the value underneath the function

# def submit():
#   if len(request.form['email']) < 1:
#     flash('Email cannot be empty')
#   elif not EMAIL_REGEX.match(request.form['email']):
#     flash('Invalid Email')
#   else:
#     flash('Success')
#   return redirect ('/')
  print request.form #put print before return
  return redirect('/')  
  
app.run(debug=True) # run our server
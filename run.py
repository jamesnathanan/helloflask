from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config.update(
	
	SECRET_KEY = 'topsecret',
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:topsecret@localhost/catalog_db',
	SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)

class Publication(db.Model):
	__tablename__ = 'publication'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	
	def __init__(self, id, name):
		self.id = id
		self.name = name
	
	def __repr__(self):
		return 'The ID is {} , The Name is {} '.format(self.id, self.name)

class Book(db.Model):
	__tabel_name = 'book'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(500), nullable=False, index=True)
	author = db.Column(db.String(350))
	avg_rating = db.Column(db.Float)
	format = db.Column(db.String(50))
	image = db.Column(db.String(100), unique=True)
	num_pages = db.Column(db.Integer)
	pub_date = db.Column(db.DateTime, default=datetime.utcnow())

	# Relationship
	pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))
	
	def __init__(self, title, author, avg_rating, book_format, image, num_pages,  pub_id):
		self.title = title
		self.author = author
		self.avg_rating = avg_rating
		self.format = book_format
		self.image = image
		self.num_pages = num_pages
		self.pub_id = pub_id

	def __repr__(self):
		return '{} by {}'.format(self.title, self.author)

@app.route('/index')
@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/new/')
def query_strings(greeting = 'Hello'):
	query_val = request.args.get('greeting', greeting)
	return '<h1> the Greeting is : {0} </h1>'.format(query_val)

@app.route('/user')
@app.route('/user/<name>')
def do_something(name='mina'):
	return '<h1> hello there ! {} </h1>'.format(name)

@app.route('/numbers')
@app.route('/numbers/<int:num>')
def work_with_numbers(num=0):
	return '<h1> You pick the number {} </h1>'.format(num)

# USING TEMPLATE
@app.route('/temp')
def using_templates():
	return render_template('hello.html') 

# JINJA TEMPLATE
@app.route('/watch')
def top_movies():
	movie_list = ['autopsy of Jane Doe', 'neon demon', 'ghost in a shell', 'kong: skull island', 'john wick 2', 'spiderman - homecoming']
	
	return render_template('movies.html', movies=movie_list, name='Harry')

@app.route('/tables')
def movies_plus():
	movies_dict = {'autopsy of jane doe': 82.14,
			'neon demon': 63.20,
			'ghost in a shell': 71.5,
			'kong: skull island': 53.50,
			'john wick 2': 82.52,
			'spiderman - homecoming': 111.48}
	return render_template('table_data.html', movies=movies_dict, name='Sally')

@app.route('/filters')
def filter_data():
	movies_dict = {'autopsy of jane doe': 82.14,
			'neon demon': 63.20,
			'ghost in a shell': 71.5,
			'kong: skull island': 53.50,
			'john wick 2': 82.52,
			'spiderman - homecoming': 111.48}
	return render_template('filter_data.html', movies=movies_dict, name=None, film='a christmas carol')	

@app.route('/macros')
def jinja_macros():
	movies_dict = {'autopsy of jane doe': 82.14,
			'neon demon': 63.20,
			'ghost in a shell': 71.5,
			'kong: skull island': 53.50,
			'john wick 2': 82.52,
			'spiderman - homecoming': 111.48}
	return render_template('using_macros.html', movies=movies_dict)

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)






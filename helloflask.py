from flask import Flask, request, render_template

app = Flask(__name__)

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
	app.run(debug=True)

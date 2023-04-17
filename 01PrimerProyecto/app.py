from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
	nombre = None
	if request.method == 'POST' and 'nombre' in request.form:
		nombre = request.form['nombre']
	return render_template('user.html', nombre=nombre)

if __name__ == '__main__':
	app.run(debug=True)
from flask import Flask, render_template ,request,url_for,escape,session,redirect,abort
app = Flask(__name__)
app.secret_key = 'any random string'
@app.route('/')
def index():
	if 'username' in session:
		username = session['username']
		return 'logged in as'+ username+'<br>'+render_template('result.html')
	return render_template('hello.html')
@app.route('/login', methods =['GET','POST'] )
def login():
	if request.method == 'POST':
		if request.form['username'] == 'admin':
			return redirect(url_for('logout'))
		else:
			abort(401)
	else:
		session['username']=request.args.get('username')
		return redirect(url_for('index'))

@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('index'))
if(__name__ == "__main__"):
	app.run(debug = True)

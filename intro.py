from flask import Flask, render_template ,request,url_for,escape,session,redirect,abort
import sqlite3 as sql
app = Flask(__name__)
app.secret_key = 'any random string'
#initial route
@app.route('/')
def index():
	return render_template('login.html')
#to register as a new user
@app.route('/register', methods = ['GET','POST'])
def register():
	if request.method == 'POST':
		name = request.form['new_username']
		password = request.form['new_password']
		with sql.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("select * from users where username =?",[request.form['new_username']])
			name=cur.fetchall()
			if name:
				ms2="already existing username"
				return render_template("login.html",ms2=ms2)
			cur.execute("INSERT INTO users (username,password) VALUES (?,?)",(name,password))
			msg = "registered successfully now login"
			con.commit()
		con.close()
		return render_template('login.html',msg=msg)
#login as a user
@app.route('/login', methods =['GET','POST'] )
def login():
	if request.method == 'POST':
		con = sql.connect("database.db")
		con.row_factory = sql.Row
		cur = con.cursor()
		cur.execute("select * from users where username =?",[request.form['username']])
		name=cur.fetchall()
		if name:
			session['username'] = request.form['username']
			cur.execute("select * from users")
			lis=cur.fetchall()
			return render_template('front.html',lis=lis)
		else:
			alr="not registered yet"
			return render_template('login.html',alr=alr)
	else:
		session['username']=request.args.get('username')
		return render_template('front.html')
	con.close()
#logout as a user
@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('index'))
if(__name__ == "__main__"):
	app.run(debug = True)

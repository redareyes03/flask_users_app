from flask import Flask, request, render_template, redirect, url_for
from dbconf import execQuery, fetchUsers

app = Flask(__name__)

def fetchUserById(user_id):
    result = execQuery("SELECT * FROM users WHERE id = %s;", (user_id,))
    print(result)
    return result[0] if result else None

@app.get('/')
def index():
    users = fetchUsers()
    return render_template('home.html', users=users)

@app.post('/users')
def createUser():
    name = request.form['name']
    email = request.form['email']
    execQuery("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
    return redirect(url_for('index')) 

@app.get('/users/update/<int:user_id>')
def updateUserPage(user_id):
    user = fetchUserById(user_id)
    print(user)
    return render_template('update_user.html', user=user)

@app.post('/users/update/<int:user_id>')
def updateUser(user_id):
    name = request.form['name']
    email = request.form['email']
    execQuery("UPDATE users SET name = %s, email = %s WHERE id = %s;", (name, email, user_id))
    return redirect('/')

@app.post('/users/delete/<int:user_id>')
def deleteUser(user_id):
    execQuery("DELETE FROM users WHERE id = %s;", (user_id,))
    return redirect('/')
from flask import Flask,  render_template, request
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://postgres:123@localhost/innovativedb'


content = {"Iphone6": '1', "Nokia": '2'}

 

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')
@app.route('/products', methods=['GET'])
def products():
    return render_template('products.html', content = content )

@app.route('/delete')
def delete():
   
    return render_template('delete.html', content = content)

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/userprofile')
def userprofile():
    return render_template('userprofile.html')

@app.route('/manageuser')
def manageuser():
    return render_template('manageuser.html')

class RegisterForm():
    username = StringField('inputusername', [validators.Length(min=1, max=50)])
    email = StringField('inputEmail', [validators.Length(min=6, max=50)])
    password = PasswordField('inputPassword', [ validators.data_required(), 
    validators.EqualTo('inputconfirmpass', message='Oops! passwords do not match')])
    confirm = PasswordField('inputconfirmpass')
    
    @app.route('/register')
    def register():
        
             return render_template('register.html')
        


    @app.route('/Login')
    def Login():
        return render_template('Login.html')








if __name__ == '__main__':
    app.run(debug=True)

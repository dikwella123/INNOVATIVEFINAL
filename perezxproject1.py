from flask import Flask,  render_template  
app = Flask(__name__)



 

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Login')

def Login():
    return render_template('Login.html')

@app.route('/create')
def create():
    return render_template('create.html')
@app.route('/delete')
def delete():
    return render_template('delete.html')
@app.route('/edit')
def edit():
    return render_template('edit.html')
@app.route('/products')
def products():
    content = ['Iphone 6', 'Nokia', 'Techno']
    return render_template('products.html', content = content )

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/userprofile')
def userprofile():
    return render_template('userprofile.html')

@app.route('/manageuser')
def manageuser():
    return render_template('manageuser.html')






if __name__ == '__main__':
    app.run(debug=True)

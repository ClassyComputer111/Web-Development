# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Treven" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Vicktor" # write your name
    age = "40" # write your age

    return render_template('father.html' , name = name , age = age)


# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Erica" # write your name
    age = "37" # write your age

    return render_template('mother.html' , name = name , age = age)


# define the route to friends webpage
@app.route("/friend")
def friend():

    name = "Peter" # write your name
    age = "15" # write your age

    return render_template('friend.html' , name = name , age = age)

# add other routes, if you want
@app.route("/grandpa")
def grandpa():

    name = "Rupert" # write your name
    age = "62" # write your age

    return render_template('grandpa.html' , name = name , age = age)

@app.route("/grandma")
def grandma():

    name = "Jessica" # write your name
    age = "60" # write your age

    return render_template('grandma.html' , name = name , age = age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)

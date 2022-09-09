# start of falsk
# 1
from flask import Flask

app = Flask(__name__)


@app.route('/reza')
@app.route('/aboutme')
def say_hello():
    return "reza amin is here "


@app.route('/rezadeve')
def aboutme():
    return '''
    my name is reza <b>amin</b>
    and 22 years old
    '''


# _______________________________________________________

# templates
# create dirctory templates\
# 2
from flask import render_template


@app.route('/rezaamin1')
def aboutreza():
    return render_template('about_reza.html', name="reza")


@app.route('/mahdimirzaei')
def mahdi_mirzaei():
    return render_template('about_mahdi.html')


# _____________________________________________
# 3
# jinja
# crate base.html


@app.route('/aboutgroup')
def about_g():
    return render_template('about_group.html')


# _____________________________________________________

# 4

# include in jinja

# craete navbar
# create home.html

@app.route("/home")
def home():
    return render_template('home.html')


# _____________________________________________________________

# 5
# development server

if __name__ == "__main__":
    app.run(debug=True)

# write in terminal : python filename.py  --> python app.py


#_____________________________________________________________________

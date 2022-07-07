from flask import Flask, render_template

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')


@app.route('1')
def enemy():
    return render_template('c:\Users\Eusou\Documents\GitHub\appgame\enemy')

@app.route('2')
def font():
    return render_template('c:\Users\Eusou\Documents\GitHub\appgame\font')

@app.route('3')
def game():
    return render_template('c:\Users\Eusou\Documents\GitHub\appgame\games')


@app.route('3')
def img():
    return render_template('c:\Users\Eusou\Documents\GitHub\appgame\img')


@app.route('3')
def nave():
    return render_template('c:\Users\Eusou\Documents\GitHub\appgame\navei')

@app.route('3')
def sound():
    return render_template('c:\Users\Eusou\Documents\GitHub\appgame\sounds')


if __name__ == "__main__":
    app.run(debug=True)

#git push heroku main 
# heroku login




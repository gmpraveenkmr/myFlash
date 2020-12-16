from flask import Flask,render_template

newflask = Flask(__name__)

@newflask.route('/')

def index():
    list_example=['praveen','robini','barathi','vidhun']
    return render_template('index.html', list_example=list_example)

if __name__ == "__main__":
    newflask.run(debug=True)
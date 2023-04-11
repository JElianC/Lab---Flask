from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/user/<name>')
def greet(name):
    return f"<p> hello, {name}!</p>"


def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]


@app.route("/")
def homePage():
    name = "Jesus Cantu"
    # details = ['this', 'this', 'this']
    details = readDetails('static/details.txt')
    return render_template("base.html", name=name, aboutMe=details)


@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        # if request.form['name']:
        #     name = request.form['name']
        if request.form['message']:
            writeToFile('static/comments.txt', request.form['message'])
        # return render_template('base.html', name=name, aboutMe=[])

    return render_template('form.html', name=name)


def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message)


# When running this file directly...
if __name__ == "__main__":
    app.run(debug=True, port=2000)

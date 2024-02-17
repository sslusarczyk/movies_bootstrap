from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies_no = 20
    movies = ['Film ' + str(i+1) for i in range(movies_no)]
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
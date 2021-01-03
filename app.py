from flask import Flask, render_template, request
import pickle
import database_init

conn, cur = database_init.get_connection()

def sentiment_review(review):
    if review is None or review == "":
        return "Try again"
    with open("model.pickle",'rb') as f:
        pkl = pickle._Unpickler(f)
        pkl.encoding = 'latin1'
        model = pkl.load()
        cv = pkl.load()
    pred = model.predict(cv.fit_transform([review]))
    if pred[0] == 0:
        return "Negative"
    else:
        return "Positive"


def insert_into_db(movie_review,pred):
    cur.execute("INSERT INTO movieReview (Review, Prediction) VALUES (?, ?)",(movie_review,pred))
    conn.commit()

app = Flask(__name__)

@app.route("/")
@app.route("/home.html")
def home():
    return render_template('home.html')

@app.route('/results.html',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        print(request.form['result'])
        prediction = sentiment_review(request.form['result'])
        insert_into_db(request.form['result'],prediction)
        return render_template('results.html', value=prediction)

@app.route('/data.html')
def data():
    movieReview = conn.execute('SELECT * FROM movieReview').fetchall()
    return render_template('data.html', posts=movieReview)

if __name__ == "_main_":
    app.run(debug=True)

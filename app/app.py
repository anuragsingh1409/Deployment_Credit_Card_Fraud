from flask import Flask , render_template , request
import fraud as f
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello():
   
        return render_template("index.html")


@app.route('/sub', methods = ['POST'])
def submit():
     if request.method == "POST":
      amount = request.form['amount']
      num = f.fraud_prediction(amount)

    
   
     return render_template("sub.html", n = num )


if __name__ == '__main__':
    app.run(debug=True)
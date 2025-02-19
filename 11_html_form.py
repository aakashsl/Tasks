from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("11.html")

@app.route('/submit', methods=['post'])
def submit():
   name=request.form['name']
   email=request.form['email']
   message=request.form['message']
   text=f"Your Name: {name}<br>Your Email: {email}<br>Message: {message}"
   return text

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
app = Flask(__name__)

@app.route('/1/<num>')
def hello(num):
   n=num
   str1=""
   for i in n:
      str1=i+str1
   return str1

if __name__ == '__main__':
    app.run(debug=True)
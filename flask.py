from flask import Flask

app = Flask(__name__)
@app.route("/")
def homepage():
    return "<h1>Devops RCT<h1>"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)

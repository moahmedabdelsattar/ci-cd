from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Project 01 - Application is Running! and created by mohamed1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

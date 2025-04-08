# user-service/main.py
from flask import Flask
app = Flask(__name__)

@app.route("/users")
def get_users():
    return {"users": ["Alice", "Bob"]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

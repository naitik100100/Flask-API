# import objects from the flask model
from flask import Flask, jsonify, request
import json

# Create an instance of class, first argument is name of application
app = Flask(__name__)

UserList = []

class UserManagement:
    def __init__(self, email, username):
        self.email = email
        self.username = username

@app.route("/adduser", methods=["POST"])
def adduser():
    getUserData = request.get_json()
    userObject = UserManagement(getUserData["email"], getUserData["username"])
    UserList.append(userObject)
    # To check whether user is added to the list or not.
    print(json.dumps({'Users': [ob.__dict__ for ob in UserList]}))
    return jsonify({'message': "User created successfully..."})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

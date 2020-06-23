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
def addUser():
    getUserData = request.get_json()
    userObject = UserManagement(getUserData["email"], getUserData["username"])
    UserList.append(userObject)
    # To check whether user is added to the list or not.
    return jsonify({'message': "User created successfully..."})

@app.route("/getAllUsers", methods=["GET"])
def getAllUsers():
    return json.dumps({'Users': [ob.__dict__ for ob in UserList]})
    
 
@app.route("/getUser" , methods=["GET"])
def getUserByUsername():
    getUserData = request.get_json()
    temp=[]
    temp.append({'Users': [ob.__dict__ for ob in UserList]})
    for user in range(len(temp[0].get('Users'))):
        if( temp[0].get('Users')[user].get('username') == getUserData["username"]):
            jsonData = json.dumps(temp[0].get('Users')[user])
            return jsonData
    return {'Message' : 'No data found'}


@app.route("/moduser", methods=["PUT"])
def moduser():
    getUserData = request.get_json()
    userObject = UserManagement(getUserData["email"], getUserData["username"])    
    UserList[0] = userObject
    print(json.dumps({'Users': [ob.__dict__ for ob in UserList]}))
    return jsonify({'message': "User modified successfully."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Sohail", "age": 22},
    2: {"name": "Ahmed", "age": 25}
}

@app.route('/')
def home():
    return "Flask REST API is running"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    
    new_id = max(users.keys()) + 1 if users else 1
    
    users[new_id] = {
        "name": data.get("name"),
        "age": data.get("age")
    }
    
    return jsonify({
        "message": "User added",
        "user": users[new_id]
    }), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["age"] = data.get("age", users[user_id]["age"])
    
    return jsonify({
        "message": "User updated",
        "user": users[user_id]
    })

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    deleted_user = users.pop(user_id)
    
    return jsonify({
        "message": "User deleted",
        "user": deleted_user
    })

if __name__ == '__main__':
    app.run(debug=True)

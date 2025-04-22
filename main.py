from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'users.json'

# Load users from file
def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save users to file
def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# Start with existing users
users = load_users()

@app.route('/')
def home():
    return jsonify({"message": "Backend is working!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')

    if not email or not data.get('password'):
        return jsonify({"error": "Missing email or password"}), 400

    if email in users:
        return jsonify({"message": "Logged in", "email": email})
    else:
        users[email] = {
            "roblox_username": data.get("roblox_username"),
            "discord_username": data.get("discord_username"),
            "email": email,
            "password": data.get("password"),
            "points": 0
        }
        save_users(users)
        return jsonify({"message": "User created", "email": email})

@app.route('/points/<email>', methods=['GET'])
def get_points(email):
    user = users.get(email)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"email": email, "points": user["points"]})

@app.route('/rewards', methods=['GET'])
def get_rewards():
    return jsonify([
        {"id": 1, "name": "Free Item", "cost": 10},
        {"id": 2, "name": "Discount Code", "cost": 25}
    ])

if __name__ == '__main__':
    app.run(debug=True)

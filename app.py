from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database (in-memory dictionary)
users = {}
rewards = [
    {"id": 1, "name": "Free Item", "cost": 10},
    {"id": 2, "name": "Discount Code", "cost": 25}
]

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the backend API!"})

# Sign up or login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('roblox_username')
    discord = data.get('discord_username')
    email = data.get('email')
    password = data.get('password')

    if not all([username, discord, email, password]):
        return jsonify({"error": "Missing fields"}), 400

    if email in users:
        return jsonify({"message": "User logged in", "email": email})
    else:
        users[email] = {
            "roblox_username": username,
            "discord_username": discord,
            "email": email,
            "password": password,
            "points": 0
        }
        return jsonify({"message": "User signed up", "email": email})

# Get points for a user
@app.route('/points/<email>', methods=['GET'])
def get_points(email):
    user = users.get(email)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"email": email, "points": user['points']})

# Get available rewards
@app.route('/rewards', methods=['GET'])
def get_rewards():
    return jsonify(rewards)

# Update account info
@app.route('/account/<email>', methods=['PUT'])
def update_account(email):
    user = users.get(email)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    for key in ['roblox_username', 'discord_username', 'password']:
        if key in data:
            user[key] = data[key]

    return jsonify({"message": "Account updated", "user": user})

if __name__ == '__main__':
    app.run(debug=True)

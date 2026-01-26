import os
import json
import uuid
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

DATA_FILE = 'data/lost-items.json'
SEED_FILE = 'data/lost-items.seed.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        if os.path.exists(SEED_FILE):
            with open(SEED_FILE, 'r') as f:
                data = json.load(f)
            save_data(data)
            return data
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    items = load_data()
    # Sorting: newest dateLost first by default
    items.sort(key=lambda x: x['dateLost'], reverse=True)
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.json
    items = load_data()
    
    # Generate ID: LI-YYYY-XXXX
    year = datetime.now().year
    count = len(items) + 1
    new_id = f"LI-{year}-{count:04d}"
    
    new_entry = {
        "id": new_id,
        "itemName": data.get('itemName'),
        "category": data.get('category'),
        "brand": data.get('brand', ''),
        "color": data.get('color', ''),
        "locationLost": data.get('locationLost'),
        "dateLost": data.get('dateLost'),
        "timeLost": data.get('timeLost', ''),
        "description": data.get('description', ''),
        "identifyingMarks": data.get('identifyingMarks', ''),
        "rewardOffered": data.get('rewardOffered', False),
        "rewardAmountPKR": int(data.get('rewardAmountPKR', 0)) if data.get('rewardOffered') else 0,
        "contactName": data.get('contactName'),
        "contactPhone": data.get('contactPhone'),
        "contactEmail": data.get('contactEmail', ''),
        "preferredContactMethod": data.get('preferredContactMethod'),
        "status": "Open",
        "createdAt": datetime.utcnow().isoformat() + "Z",
        "source": "user"
    }
    
    items.append(new_entry)
    save_data(items)
    return jsonify({"success": True, "item": new_entry}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)

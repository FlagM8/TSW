# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)
items = {}

@app.route("/api/items", methods=["POST"])
def create_item():
    data = request.json
    item_id = str(len(items) + 1)
    items[item_id] = data
    return jsonify({"id": item_id, **data}), 201

@app.route("/api/items/<item_id>", methods=["GET"])
def get_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"id": item_id, **item})

@app.route("/api/items/<item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.json
    if item_id not in items:
        return jsonify({"error": "Not found"}), 404
    items[item_id] = data
    return jsonify({"id": item_id, **data})

@app.route("/api/items/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Not found"}), 404
    del items[item_id]
    return jsonify({"status": "deleted"})

if __name__ == "__main__":
    app.run(debug=True)

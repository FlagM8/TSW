from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)
todos = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("task")
    if text:
        todos.append({"task": text, "done": False})
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete(task_id):
    if 0 <= task_id < len(todos):
        todos[task_id]["done"] = True
    return redirect(url_for("index"))

@app.route("/api/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/api/todos", methods=["POST"])
def create_todo():
    data = request.json
    task = data.get("task")
    if task:
        todos.append({"task": task, "done": False})
        return jsonify({"status": "created"}), 201
    return jsonify({"error": "Invalid task"}), 400

@app.route("/api/todos/<int:task_id>", methods=["PUT"])
def complete_todo_api(task_id):
    if 0 <= task_id < len(todos):
        todos[task_id]["done"] = True
        return jsonify({"status": "updated"})
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

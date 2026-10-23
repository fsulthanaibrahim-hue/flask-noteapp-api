from flask import Flask, jsonify, request

app = Flask(__name__)

notes = []
next_id = 1

@app.route("/", methods = ["GET"])
def home():
    return jsonify({
        "message to Notes API",
    }), 200

@app.route("/notes/", methods=["POST"])
def create_note():
    global next_id
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({
            "error": "Request body must be a JSON body object"
        }), 400
    title = data.get("title")
    content = data.get("content", "")
    if not isinstance(title, str) or not title.strip():
        return jsonify({
            "error": "Title is required"
        }), 400
    if not isinstance(content, str):
        return jsonify({
            "error": "Content must be a string"
        }), 400
    note = {
        "id": next_id,
        "title": title.strip(),
        "content": content.strip()
    }
    notes.append(note)
    next_id += 1
    return jsonify({
        "message": "Note created successfully",
        "note": note
    }), 201

@app.route("/notes", methods=["GET"])
def get_all_notes():
    return jsonify({
        "count": len(notes),
        "notes": notes
    }), 200

# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

notes = []          # Memoria, se borra al reiniciar
next_id = 1

@app.route("/api/notes", methods=["GET", "POST"])
def notes_collection():
    global next_id
    if request.method == "GET":
        return jsonify(notes)
    data = request.get_json() or {}
    note = {
        "id": next_id,
        "title": data.get("title", ""),
        "body": data.get("body", ""),
        "priority": data.get("priority", "medium"),
    }
    notes.append(note)
    next_id += 1
    return jsonify(note), 201

@app.route("/api/notes/<int:note_id>", methods=["GET", "PUT", "DELETE"])
def note_item(note_id):
    for note in notes:
        if note["id"] == note_id:

            # ───── me devuekve una nota  ─────
            if request.method == "GET":
                return jsonify(note)          # 200 OK

            if request.method == "PUT":
                data = request.get_json() or {}
                note.update(
                    title=data.get("title", note["title"]),
                    body=data.get("body", note["body"]),
                    priority=data.get("priority", note["priority"]),
                )
                return jsonify(note)

            # DELETE
            notes.remove(note)
            return "", 204
    return {"error": "Nota no encontrada"}, 404 # en caso de Nota no encontrada

if __name__ == "__main__":
    app.run(debug=True)   # http://localhost:5000

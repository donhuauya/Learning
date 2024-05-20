from flask import Flask, jsonify, request

app = Flask(__name__)

#Example route that accepts query parameters
app.route('/users', methods=['GET'])
def get_users():
    name = request.args.get("name")
    age = request.range.get("age")
    return jsonify({
        "name": name,
        "age": age
    })

if __name__ == "__main__":
    app.run(debug=True)

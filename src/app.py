#cabecera
from flask import Flask, jsonify
from flask import request
from flask import Flask
app = Flask(__name__)



#variable
todos = [ { "label": "My first task", "done": False } ]

#GET
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

#POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

#DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    return 'something'

#final
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
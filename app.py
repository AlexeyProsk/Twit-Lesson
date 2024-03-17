import json
from flask import Flask, jsonify, request
from twit import Twit

twits = []
app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})


next_id = 1
@app.route('/twit', methods=['POST'])
def create_twit():
    """{"body": "My twit", "author": "Username"}
    """
    global next_id
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'], id=next_id)
    twits.append(twit)
    next_id += 1
    return jsonify({'status': 'success'})


@app.route('/twit', methods=['GET'])
def read_twits():
    serialized_twits = [twit.to_dict() for twit in twits]
    return jsonify(serialized_twits)


@app.route('/twit/<int:twit_id>', methods=['PUT'])
def update_twit(twit_id):
    """{"body": "UPDATED", "author": "Username"}
    """
    twit_json = request.get_json()
    for twit in twits:
        if twit.id == twit_id:
            twit.body = twit_json.get('body', twit.body)
            twit.author = twit_json.get('author', twit.author)
            return jsonify({'status': 'success'})
    return jsonify({'error': 'Twit not found'}), 404


@app.route('/twit/<int:twit_id>', methods=['DELETE'])
def delete_twit(twit_id):
    for twit in twits:
        if twit.id == twit_id:
            twits.remove(twit)
            return jsonify({'status': 'success'})
    return jsonify({'error': 'Twit not found'}), 404


if __name__ == "__main__":
    app.run(debug=True)

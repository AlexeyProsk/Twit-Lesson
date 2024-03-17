import json
from flask import Flask, jsonify, request
from twit import Twit

twits = []
app = Flask(__name__)


class CustomJSONEnoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Twit):
            return {'body': obj.body, 'author': obj.author}
        else:
            return super().default(obj)


app.json_encoder = CustomJSONEnoder


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})


@app.route('/twit', methods=['POST'])
def create_twit():
    """{"body": "My twit", "author": "Username"}
    """
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'])
    twits.append(twit)
    return jsonify({'status': 'success'})


@app.route('/twit', methods=['GET'])
def read_twits():
    serialized_twits = [app.json_encoder.default(None, twit) for twit in twits]
    return jsonify(serialized_twits)


if __name__ == "__main__":
    app.run(debug=True)

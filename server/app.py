import os
import uuid

import stripe
from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

TODO = [
    {
        'id': uuid.uuid4().hex,
        'todo': 'Test Correction',
        'assignee': '5BHITM',
        'done': False
    },
    {
        'id': uuid.uuid4().hex,
        'todo': 'Projects',
        'assignee': '5BHITM',
        'done': False
    },
    {
        'id': uuid.uuid4().hex,
        'todo': 'Test Correction',
        'assignee': '5BHITM',
        'done': False
    }
]


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/todo', methods=['GET', 'POST'])
def all_todos():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TODO.append({
            'id': uuid.uuid4().hex,
            'todo': post_data.get('todo'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
            'price': post_data.get('price')
        })
        response_object['message'] = 'Todo added!'
    else:
        response_object['todos'] = TODO
    return jsonify(response_object)


@app.route('/todo/<todo_id>', methods=['GET', 'PUT', 'DELETE'])
def single_todo(todo_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        # TODO: refactor to a lambda and filter
        return_todo = ''
        for todo in TODO:
            if todo['id'] == todo_id:
                return_todo = todo
        response_object['todo'] = return_todo
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_todo(todo_id)
        TODO.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'assignee': post_data.get('assignee'),
            'done': post_data.get('done')
        })
        response_object['message'] = 'Todo updated!'
    if request.method == 'DELETE':
        remove_todo(todo_id)
        response_object['message'] = 'Todo removed!'
    return jsonify(response_object)


@app.route('/charge', methods=['POST'])
def create_charge():
    post_data = request.get_json()
    amount = round(float(post_data.get('todo')['price']) * 100)
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    charge = stripe.Charge.create(
        amount=amount,
        currency='usd',
        card=post_data.get('token'),
        description=post_data.get('todo')['title']
    )
    response_object = {
        'status': 'success',
        'charge': charge
    }
    return jsonify(response_object), 200


@app.route('/charge/<charge_id>')
def get_charge(charge_id):
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    response_object = {
        'status': 'success',
        'charge': stripe.Charge.retrieve(charge_id)
    }
    return jsonify(response_object), 200


def remove_todo(todo_id):
    for todo in TODO:
        if todo['id'] == todo_id:
            TODO.remove(todo)
            return True
    return False


if __name__ == '__main__':
    app.run(port=80)

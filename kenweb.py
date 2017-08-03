import os
from flask import Flask
from flask import request
from board import Board
from kakuro import Kakuro
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/add/', methods=['GET'])
def add():
    board_size = request.args.get('size')
    target = request.args.get('target')
    occurs = request.args.get('nums')
    repeats = request.args.get('repeats')
    b = Board(board_size)
    result = b.add(int(target), int(occurs), int(repeats))
    return str(result)
    
@app.route('/multiply/', methods=['GET'])
def multiply():
    board_size = request.args.get('size')
    target = request.args.get('target')
    occurs = request.args.get('nums')
    repeats = request.args.get('repeats')
    b = Board(board_size)
    result = b.multiply(int(target), int(occurs), int(repeats))
    return str(result)
    
@app.route('/subtract/', methods=['GET'])
def subtract():
    board_size = request.args.get('size')
    target = request.args.get('target')
    b = Board(board_size)
    result = b.subtract(int(target))
    return str(result)
    
@app.route('/divide/', methods=['GET'])
def divide():
    board_size = request.args.get('size')
    target = request.args.get('target')
    b = Board(board_size)
    result = b.divide(int(target))
    return str(result)
    
@app.route('/kakuro/', methods=['GET'])
def kakuro_combinations():
    target = int(request.args.get('target'))
    nums = int(request.args.get('nums'))
    #disallowed = list(request.args.get('disallowed'))
    k = Kakuro()
    result = k.get_combinations(target, nums)
    return str(result)
    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
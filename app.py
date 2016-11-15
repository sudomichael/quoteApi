#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

quotes = [
    {
        'id': 1, 
        'quote':u'In order to understand recursion, you must first understand recursion.',
        'author':u'Unknown'
    }, 
    {
        'id': 2,
        'quote':u'Man surprises me most about humanity. Because he sacrifices his health in order to make money. Then he sacrifices money to recuperate his health. And then he is so anxious about the future that he does not enjoy the present; the result being that he does not live in the present or the future; he lives as if he is never going to die, and then dies having never really lived.',
        'author':u'Dalai Lama'
    }
]
'''
@app.route('/')
def index():
    return "Hello, World!"'''

@app.route('/api/v1.0/quotes', methods=['GET'])
def get_quotes():
    return jsonify({'quotes': quotes})

from flask import abort

@app.route('/api/v1.0/quotes/<int:quote_id>', methods=['GET'])
def get_quote(quote_id):
    quote = [quote for quote in quotes if quote['id'] == quote_id]
    if len(quote) == 0:
        abort(404)
    return jsonify({'quote':quote[0]})

from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

from flask import request

@app.route('/api/v1.0/quotes', methods=['POST'])
def create_quote():
    if not request.json or not 'quote' in request.json:
        abort(400)
    quote = {
        'id': quotes[-1]['id'] + 1,
        'quote': request.json['quote'],
        'author': request.json.get('author', "")
    }
    quotes.append(quote)
    return jsonify({'quote': quote}), 201

if __name__ == '__main__':
    app.run(debug=True)


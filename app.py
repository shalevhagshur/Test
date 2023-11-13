from flask import Flask, jsonify, render_template, request, session
from tools.col import zip_it
from tools.numbers.comp import sum_digits, ispal
from tools.numbers.simp import subtract_simp, add_simp

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secret key for session

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/zip_it', methods=['POST'])
def zip_it_route():
    data = request.get_json()
    collection1 = data.get('collection1', [])
    collection2 = data.get('collection2', [])

    # Perform the zip operation
    result = zip_it(collection1, collection2)

    return jsonify(result)

@app.route('/sum_digits/<int:number>')
def sum_digits_route(number):
    if all(func in session.get('functions_used', []) for func in ['add', 'subtract']):
        result = sum_digits(number)
        return jsonify({'result': result})  # Return result as JSON
    else:
        return jsonify({'error': 'Both add and subtract must be used before using this feature'})

@app.route('/ispal/<int:number>')
def ispal_route(number):
    if all(func in session.get('functions_used', []) for func in ['add', 'subtract']):
        result = ispal(number)
        return jsonify({'result': result})  # Return result as JSON
    else:
        return jsonify({'error': 'Both add and subtract must be used before using this feature'})

@app.route('/subtract/<int:x>/<int:y>')
def subtract_route(x, y):
    session['simp_called'] = True  # Set simp function called to True
    session.setdefault('functions_used', []).append('subtract')  # Add subtract to functions_used
    result = subtract_simp(x, y)
    return jsonify({'result': result})  # Return result as JSON

@app.route('/add/<int:x>/<int:y>')
def add_route(x, y):
    session['simp_called'] = True  # Set simp function called to True
    session.setdefault('functions_used', []).append('add')  # Add add to functions_used
    result = add_simp(x, y)
    return jsonify({'result': result})  # Return result as JSON

if __name__ == '__main__':
    app.run(debug=True)

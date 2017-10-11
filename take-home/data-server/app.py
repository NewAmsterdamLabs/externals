#!flask/bin/python
from  invoice import Invoice
from flask import abort, Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data_file = 'data/invoices.json'
_invoices = Invoice(data_file)

@app.route('/id/<int:id>', methods=['GET'])
def get(id):
    invoice = _invoices.get(id)
    if len(invoice) == 0:
        return error_response("Cannot find invoice with id " + str(id))
    return jsonify({'invoice': invoice[0]})
    

@app.route('/', methods=['POST'])
def create():
    response = validate_post_params(request.json)
    if response is not None:
        return response

    return jsonify(_invoices.create(request.json['po_number'], request.json['invoice_date'], request.json['due_date'], request.json['amount_cents']))

@app.route('/id/<int:id>', methods=['PUT'])
def update(id):
    response = validate_post_params(request.json)
    if response is not None:
        return response

    return jsonify(_invoices.update(id, request.json['po_number'], request.json['invoice_date'], request.json['due_date'], request.json['amount_cents']))

@app.route('/id/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(_invoices.delete(id))

@app.route('/list', methods=['GET'])
def list():
    params = {'offset': 0, 'limit': 10}

    if request.args.get('offset'):
        params['offset'] = int(request.args.get('offset'))

    if request.args.get('limit'):
        params['limit'] = int(request.args.get('limit'))

    if request.args.get('po_number'):
        params['po_number'] = request.args.get('po_number')

    return jsonify(_invoices.list(params))

def error_response(message):
    response = jsonify({'error_message': message})
    response.status_code = 500
    return response

def validate_post_params(json):
    if not json:
        return error_response("Missing required post json.")
  
    if not 'po_number' in json:
        return error_response("Missing po number.")

    if not 'invoice_date' in json:
        return error_response("Missing invoice date.")

    if not 'due_date' in json:
        return error_response("Missing due date.")

    if not 'amount_cents' in json:
        return error_response("Missing amount_cents.")

    if json['po_number'] == "Z0000000000":
        return error_response("PO Number Z000000000 is not allowed")

    return None

if __name__ == '__main__':
    app.run(debug=True)

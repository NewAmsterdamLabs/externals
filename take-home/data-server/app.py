#!flask/bin/python
from  invoice import Invoice
from flask import abort, Flask, jsonify, request

app = Flask(__name__)

data_file = 'data/invoices.json'
_invoices = Invoice(data_file)

@app.route('/id/<int:id>', methods=['GET'])
def get(id):
    invoice = _invoices.get(id)
    if len(invoice) == 0:
        abort(404)
    return jsonify({'invoice': invoice[0]})
    

@app.route('/', methods=['POST'])
def create():
    if not request.json or not 'po_number' or not 'invoice_date' or not 'due_date' or not 'amount_cents' in request.json:
        abort(400)

    return jsonify(_invoices.create(request.json['po_number'], request.json['invoice_date'], request.json['due_date'], request.json['amount_cents']))

@app.route('/id/<int:id>', methods=['PUT'])
def update(id):
    if not request.json or not 'po_number' or not 'invoice_date' or not 'due_date' or not 'amount_cents' in request.json:
        abort(400)

    return jsonify(_invoices.update(id, request.json['po_number'], request.json['invoice_date'], request.json['due_date'], request.json['amount_cents']))

@app.route('/id/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(_invoices.delete(id))

@app.route('/list', methods=['GET'])
def list():
    return jsonify(_invoices.list())

if __name__ == '__main__':
    app.run(debug=True)

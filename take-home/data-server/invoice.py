import json
from datetime import datetime

class Invoice:

    def __init__(self, data_file):
        self._data = []
        with open(data_file) as data:    
            self._data = json.load(data) 

    def list(self):
        return self._data

    def get(self, id):
        return [invoice for invoice in self._data if invoice['id'] == id]

    def delete(self, id):
        for invoice in self._data:
            if invoice['id'] == id: 
                self._data.remove(invoice)
                return invoice

    def create(self, po_number, invoice_date, due_date, amount_cents):
        ids = [invoice['id'] for invoice in self._data]
        invoice = {
            'id': max(ids) + 1,
            'po_number': po_number,
            'due_date': due_date,
            'amount_cents': amount_cents,
            'created_at': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        self._data.append(invoice)
        return invoice

    def update(self, id, po_number, invoice_date, due_date, amount_cents):
        invoice = self.get(id)
        if len(invoice) == 0:
            return [];
        invoice[0]['po_number'] = po_number
        invoice[0]['invoice_date'] = invoice_date
        invoice[0]['due_date'] = due_date
        invoice[0]['amount_cents'] = amount_cents 
        self.delete(id)
        self._data.append(invoice[0])
        return invoice[0]

This is a simple python REST API server, build on the Flask framework, that will allow you to access a sample set of invoice data.
The data is stored in a file under data/invoices.json and is read into in memory on start of the application. Therefore each execution
will reset the data to it's original values.  The server can be started by running the following command:

  `bin/start.sh`

This will run the server in the foreground.  If you want to stop the server, press ctrl-c

The available endpoints are as follows:

<ul>
  <li>GET localhost:5000/id/<id>
    <ul style='list-style-type: none'>
      <li><i>Description</i>: Returns an invoice record with the specified id</li>
      <li><i>Request Params</i>: None</li>
      <li><i>Response Payload</i>: {"amount_cents": 15000, "created_at": "2017-04-15T01:02:03Z", "due_date": "2017-03-15", "id": 10, "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"}</li>
    </ul>
  </li>
  <li>GET localhost:5000/list        - <i>Description</i>: Lists all invoices in server
                                 <i>Request Params</i>: None
                                 response payload: [{"amount_cents": 15000, "created_at": "2017-04-15T01:02:03Z", "due_date": "2017-03-15", "id": 10, "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"}, {"amount_cents": 15000, "created_at": "2017-04-15T01:02:03Z", "due_date": "2017-03-15", "id": 11, "invoice_date": "2017-03-01","po_number": "7BYBP3K6W4"}]
  </li>
  <li>POST localhost:5000            - <i>Description</i>: Saves an invoice that is in the request payload. The invoice must be in json format with the following fields: po_number, invoice_date, due_date, amount_cents 
                                 <i>Request Params (body)</i> : {"amount_cents": 15000, "due_date": "2017-03-15", "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"} 
                                 <i>Response Payload</i>: {"amount_cents": 15000, "created_at": "2017-04-15T01:02:03Z", "due_date": "2017-03-15", "id": 10, "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"}
  </li>
  <li>PUT localhost:5000/id/<id>     - <i>Description</i>: Updates an invoice with specific id with the invoice in the request payload. The invoice must be in json format with the following fields: po_number, invoice_date, due_date, amount_cents 
                                 <i>Request Params (body)</i>: {"amount_cents": 15000, "due_date": "2017-03-15", "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"} 
                                 <i>Response Payload</i>: {"amount_cents": 15000, "created_at": "2017-04-15T01:02:03Z", "due_date": "2017-03-15", "id": 10, "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"}
  </li>
  <li>DELETE localhost:5000/id/<id>  - <i>Description</i>: Removes an invoice with he specific id
                                 <i>Request Params</i>: None
                                 <i>Response Payload</i>: {"amount_cents": 15000, "created_at": "2017-04-15T01:02:03Z", "due_date": "2017-03-15", "id": 10, "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"}
  </li>
</ul>

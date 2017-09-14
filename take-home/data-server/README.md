This is a simple python REST API server, build on the Flask framework, that will allow you to access a sample set of invoice data.

You can download the packaged server under downloads/data-server.zip.

To begin, you will need to have python 2.7 installed in your system. You can check your version of python with `python -V`. If you do not have python installed in your system, it can be obtained at:

  `https://www.python.org/downloads/release/python-2713/`

Next install virtualenv. This will nicely install all the libraries you need within your app without polluting the system lib. You can install virtualenv with pip:

  `$ [sudo] pip install virtualenv`

Once Virtualenv is installed, unzip the data-server.zip and navigate to the directory data-server.  We can go ahead and setup your virtual environment in there.

  `$ virtualenv flask`

Next, activate your virtual environment:

  `$ source flask/bin/activate`

Finally install Flask (from within your virtual environment):

  `$ pip install Flask`

Once completed, you should be able to start the server.  The data is stored in a file under data/invoices.json and is read into in memory on start of the application. Therefore each execution
will reset the data to it's original values.  The server can be started by running the following command:

  `bin/start.sh`

This will run the server in the foreground.  If you want to stop the server, press ctrl-c. To exit the virtual environment, type `deactivate`.

The available endpoints are as follows:

* **GET localhost:5000/id/[ID]**

   *Description*: Returns an invoice record with the specified id  
   *Request Params*: None  
   *Response Payload*: {"amount_cents": 15000, "created_at": "2017-04-15T01:02:03Z", "due_date": "2017-03-15", "id": 10, "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"}

* **GET localhost:5000/list**

   *Description*: Lists all invoices in server  
   *Request Params*: None  
   *Response Payload*: [{"amount_cents": 15000, "created_at": "2017-04-15T01:02:03Z", "due_date": "2017-03-15", "id": 10, "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"}, {"amount_cents": 15000, "created_at": "2017-04-15T01:02:03Z", "due_date": "2017-03-15", "id": 11, "invoice_date": "2017-03-01","po_number": "7BYBP3K6W4"}]

* **POST localhost:5000**

   *Description*: Saves an invoice that is in the request payload. The invoice must be in json format with the following fields: po_number, invoice_date, due_date, amount_cents  
   *Request Params (body)* : {"amount_cents": 15000, "due_date": "2017-03-15", "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"}  
   *Response Payload*: {"amount_cents": 15000, "created_at": "2017-04-15T01:02:03Z", "due_date": "2017-03-15", "id": 10, "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"}

* **PUT localhost:5000/id/[ID]**

   *Description*: Updates an invoice with specific id with the invoice in the request payload. The invoice must be in json format with the following fields: po_number, invoice_date, due_date, amount_cents  
   *Request Params (body)*: {"amount_cents": 15000, "due_date": "2017-03-15", "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"}  
   *Response Payload*: {"amount_cents": 15000, "created_at": "2017-04-15T01:02:03Z", "due_date": "2017-03-15", "id": 10, "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"}

* **DELETE localhost:5000/id/[ID]**

   *Description*: Removes an invoice with he specific id  
   *Request Params*: None  
   *Response Payload*: {"amount_cents": 15000, "created_at": "2017-04-15T01:02:03Z", "due_date": "2017-03-15", "id": 10, "invoice_date": "2017-03-01", "po_number": "8LQ0VER5R0"}

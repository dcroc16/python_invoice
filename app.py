from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')


################## START OF CUSTOMERS ########################

@app.route('/customers')
def view_all_customers():
	conn = sqlite3.connect('py_erp')
	c = conn.cursor()
	c.execute('''SELECT * FROM customers''')
	payload = c.fetchall() 
	conn.close()
	return render_template('customers.html', msg=payload)


@app.route('/deleteCustomer/<arg1>', methods=['POST'])
def delete_customer(arg1 = None):
	conn = sqlite3.connect('py_erp')
	c = conn.cursor()
	c.execute("""DELETE FROM customers WHERE customer = '%s';""" % (arg1))
	conn.commit()
	c.execute('''SELECT * FROM customers''')
	payload = c.fetchall()
	print(payload)
	conn.close()
	return render_template('customers.html', msg=payload)


@app.route('/<arg1>')
def view_customer(arg1 = None):
	conn = sqlite3.connect('py_erp')
	c = conn.cursor()
	c.execute('''SELECT * FROM customers, materials WHERE customer = %s;''' % (arg1))
	payload = c.fetchall() 
	conn.close()
	return render_template('customers.html', msg=payload)

@app.route('/add_customer', methods=['POST'])
def add_customer():
	new_customer = request.form['customer']
	new_name = request.form['customer_name']
	print(new_customer)
	print(new_name)
	conn = sqlite3.connect('py_erp')
	c = conn.cursor()
	c.execute('''INSERT INTO customers values ('%s','%s');''' % (new_customer, new_name))
	conn.commit()
	c.execute('''SELECT * FROM customers''')
	payload = c.fetchall() 
	conn.close()
	return render_template('customers.html', msg=payload)

############ START OF MATERIALS ################

@app.route('/materials')
def view_all_materials():
	conn = sqlite3.connect('py_erp')
	c = conn.cursor()
	c.execute('''SELECT * FROM materials ORDER BY material DESC;''')
	payload = c.fetchall() 
	conn.close()
	return render_template('materials.html', msg=payload)

@app.route('/deleteMaterial/<arg1>', methods=['POST'])
def delete_material(arg1 = None):
	conn = sqlite3.connect('py_erp')
	c = conn.cursor()
	c.execute("""DELETE FROM materials WHERE material = '%s';""" % (arg1))
	conn.commit()
	c.execute('''SELECT * FROM materials ORDER BY material DESC''')
	payload = c.fetchall()
	print(payload)
	conn.close()
	return render_template('materials.html', msg=payload)


@app.route('/materials/<arg1>')
def view_material(arg1 = None):
	conn = sqlite3.connect('py_erp')
	c = conn.cursor()
	c.execute('''SELECT * FROM materials WHERE customer = %s;''' % (arg1))
	payload = c.fetchall()
	conn.close()
	return render_template('materials.html', msg=payload)

@app.route('/add_material', methods=['POST'])
def add_material():
	new_material = request.form['material']
	new_name = request.form['material_name']
	print(new_material)
	print(new_name)
	conn = sqlite3.connect('py_erp')
	c = conn.cursor()
	c.execute('''INSERT INTO materials values ('%s','%s');''' % (new_material, new_name))
	conn.commit()
	c.execute('''SELECT * FROM materials ORDER BY material DESC''')
	payload = c.fetchall() 
	conn.close()
	return render_template('materials.html', msg=payload)


################### START OF INVOICES ###########################

@app.route('/invoices')
def view_all_invoices():
	conn = sqlite3.connect('py_erp')
	c = conn.cursor()
	c.execute('''SELECT * FROM invoices''')
	payload = c.fetchall() 

	c.execute('''SELECT * FROM invoices''')

	NextInvoice = c.fetchone()[0] + 1

	c.execute('''SELECT * FROM materials ORDER BY description''')
	items = c.fetchall()
 
	c.execute('''SELECT * FROM customers ORDER BY name''')
	names = c.fetchall()
	conn.close()
	return render_template('invoices.html', msg=payload, item=items, cust_names=names, next=NextInvoice)


@app.route('/invoices/<arg1>')
def view_invoice(arg1 = None):
	conn = sqlite3.connect('py_erp')
	c = conn.cursor()
	c.execute('''SELECT * FROM invoice WHERE customer = %s;''' % (arg1))
	payload = c.fetchall()
	conn.close()
	return render_template('invoices.html', msg=payload)

@app.route('/add_invoice', methods=['POST'])
def add_invoice():
	new_invoice = request.form['invoice']
	customer = request.form['customer']
	customer = request.form['customer']
	customer = request.form['customer']
	customer = request.form['customer']
	customer = request.form['customer']
	customer = request.form['customer']

	conn = sqlite3.connect('py_erp')
	c = conn.cursor()
	c.execute('''INSERT INTO invoices values ('%s','%s','%s','%s','%s','%s','%s','%s');''' % (new_inovice, customer))
	conn.commit()
	c.execute('''SELECT * FROM invoices''')
	payload = c.fetchall() 
	conn.close()
	return render_template('invoices.html', msg=payload)



app.run(port=3000)

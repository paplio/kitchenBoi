import sqlite3
conn = sqlite3.connect('kitchen.db')

c = conn.cursor()

c.execute('''CREATE TABLE menu 
	(item_id INTEGER PRIMARY KEY, 
	item_name text, 
	item price int, 
	item_status int)''')

c.execute('''CREATE TABLE order_store
	(order_id INTEGER PRIMARY KEY,
	customer_name text, 
	customer_phone text)''')


c.execute('''
	CREATE TABLE order_details
	(order_id INTEGER, 
	item_id int, 
	FOREIGN KEY(order_id) references order_store(order_id), 
	FOREIGN KEY (item_id) references menu(item_id))
	''')

conn.commit()
conn.close()
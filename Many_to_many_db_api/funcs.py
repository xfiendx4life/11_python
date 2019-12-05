def addParent(conn, name, lastname):
	cursor = conn.cursor()
	cursor.execute("INSERT INTO Parent (Name, lastname) VALUES (?, ?)", (name, lastname))
	conn.commit()
	return True


def addChild(conn, name, lastname):
	cursor = conn.cursor()
	cursor.execute("INSERT INTO Child (Name, lastname) VALUES (?, ?)", (name, lastname))
	conn.commit()
	return True

def addConnection(conn, parent_name, parent_lastname, child_name, child_lastname):
	cursor = conn.cursor()
	child_id = cursor.execute('SELECT * FROM Child where name = ? and lastname = ?', (child_name, child_lastname)).fetchone()
	parent_id = cursor.execute('SELECT * FROM Parent where name = ? and lastname = ?', (parent_name, parent_lastname)).fetchone()
	if child_id and parent_id:
		pach_connection = cursor.execute('''SELECT * FROM Parent_child_table 
										where child_id = ? and parent_id = ?''', 
										(child_id[0], parent_id[0])).fetchone()
		if not pach_connection:
			cursor.execute("INSERT INTO Parent_child_table (parent_id, child_id) VALUES (?, ?)", (parent_id[0], child_id[0]))
			conn.commit()
			return True
	return False

def getAllChildren(conn, parent_name, parent_lastname):
	cursor = conn.cursor()
	parent_id = cursor.execute('SELECT * FROM Parent where name = ? and lastname = ?', (parent_name, parent_lastname)).fetchone()
	if parent_id:
		return cursor.execute('''SELECT id, name, lastname FROM Child, Parent_child_table 
								where Child.id = child_id and parent_id = %d'''% (parent_id[0])).fetchall()
	return None

def getAllParents(conn, child_name, child_lastname):
	cursor = conn.cursor()
	child_id = cursor.execute('SELECT * FROM Child where name = ? and lastname = ?', (child_name, child_lastname)).fetchone()
	if child_id:
		return cursor.execute('''SELECT id, name, lastname FROM Parent, Parent_child_table 
								where child_id = %d and parent_id = Parent.id'''% (child_id[0])).fetchall()
	return None

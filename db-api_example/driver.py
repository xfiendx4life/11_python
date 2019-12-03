def add(conn, name, lastname):
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM Student where name = ? and lastname = ?', (name, lastname))
	if not cursor.fetchone():
		cursor.execute("INSERT INTO Student (Name, lastname) VALUES (?, ?)", (name, lastname))
		conn.commit()
		return True
	return False

def addMark(conn, name, lastname, **kwargs): # {'math':5, 'physics':3, 'russian':5 }
	cursor = conn.cursor()
	subject = ','.join([key for key, value in kwargs.items()])
	marks = ','.join([str(value) for key, value in kwargs.items()])
	stu_id = cursor.execute("SELECT id FROM Student where name = ? and lastname = ?", (name, lastname)).fetchone()[0]
	if stu_id:
		cursor.execute("INSERT INTO Marks (%s, student_id) VALUES (%s, %s)"% (subject, marks, stu_id))
		conn.commit()
		return True
	return False

def getMark(conn, name, lastname, subject):
	cursor = conn.cursor()
	cursor.execute('SELECT ? FROM Student, Marks WHERE student_id = Student.id and name = ? and lastname = ?', 
					(subject, name, lastname))
	return cursor.fetchall()




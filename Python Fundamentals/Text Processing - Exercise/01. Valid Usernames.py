import sqlite3, datetime
def runSQL(sql):
	conn = sqlite3.connect(r'C:\Users\hristo.grudev\Projects\recipes\recipes.db')
	cursor = conn.cursor()
	cursor.execute(sql)
	data = cursor.fetchall()
	cursor.close()
	conn.close()
	return data

birthday_sql = '''select name, date from holidays
where strftime('%d.%m', date) = strftime('%d.%m', date('now', '6 day'))'''
birthdays = runSQL(birthday_sql)
for birthday in birthdays:
	name, date = [*birthday]
	today = datetime.datetime.now().strftime('%Y')
	years = int(today) - int(date[:4])

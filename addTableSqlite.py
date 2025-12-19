import sqlite3

def create_content(title, content, idcard, idmenu, author, date):
    conn = sqlite3.connect('db.sqlite3')
    querry = conn.cursor()
    querry.execute('INSERT INTO webApp_content (title, content, idcard, idmenu, author, date) VALUES (?, ?, ?, ?, ?, ?)', (title, content, idcard, idmenu, author, date))
    conn.commit()
    conn.close()

create_content('Name table1', 'table1 will be here', 'Card', 'Info', '-', '-')
create_content('Name article1', 'article1 will be here', 'Card', 'Info', '-', '-')
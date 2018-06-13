
import pypyodbc


def list_contacts(server, database, username, password):
    conn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=" + server + ";"
                            "Database=" + database + ";"
                            "uid=" + username + ";"
                            "pwd=" + password)

    cur = conn.cursor()
    cur.execute('select NAME, POSITION, DPT from CONTACTS')

    contacts = []

    for row in cur.fetchall():
        contact = {
            'name': row[0],
            'position': row[1],
            'department': row[2]}
        contacts.append(contact)

    cur.close()
    conn.close()

    return contacts


def find_contact(server, database, username, password, name):
    conn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=" + server + ";"
                            "Database=" + database + ";"
                            "uid=" + username + ";"
                            "pwd=" + password)

    cur = conn.cursor()

    request = "select NAME, POSITION, DPT from CONTACTS where NAME='" + name + "'"

    cur.execute(request)

    contacts = []

    for row in cur.fetchall():
        contact = {
            'name': row[0],
            'position': row[1],
            'department': row[2]}
        contacts.append(contact)

    cur.close()
    conn.close()

    return contacts



"""
Author: Alek Brown
Program: Borrow My Tools
Date: 2021-05-03

This function creates a database connection utilizing sqlite for local persistence
"""

import sqlite3
from sqlite3 import Error

from model.person import *
from model.tool import *


def create_connection(db_file):
    """ Create a database connection to a sqlite database
    :param db_file: database file
    :return: connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ Create a table from the create_table_sql statement
    :param conn: connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def define_tables():
    database = r"../Content/pythonsqlite.db"

    sql_create_tools_table = """ CREATE TABLE IF NOT EXISTS tools (
                                    id integer PRIMARY KEY,
                                    sn text,
                                    type text,
                                    description text,
                                    brand text,
                                    price real,
                                    purchase_date text,
                                    borrowed boolean
                                );"""

    sql_create_persons_table = """ CREATE TABLE IF NOT EXISTS persons (
                                    id integer PRIMARY KEY,
                                    first_name text NOT NULL,
                                    last_name text,
                                    phone text,
                                    email text
                                );"""

    # TODO add table to hold list of rented tools for single person

    # create connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create tools table
        create_table(conn, sql_create_tools_table)

        # create person table
        create_table(conn, sql_create_persons_table)
    else:
        print("Error cannot create the database connection.")


def create_tool(conn, tool: Tool):
    """ Create a new tool in the tools table
    :param conn: connection object
    :param tool: Tool object
    :return: tool id
    """

    sql = "INSERT INTO tools(sn, type, description, brand, price, purchase_date, borrowed) \n" \
          "VALUES(:p1,:p2,:p3,:p4,:p5,:p6,:p7)"

    t1 = {
        'p1': tool.serial_number,
        'p2': tool.tool_type,
        'p3': tool.description,
        'p4': tool.brand,
        'p5': tool.price,
        'p6': tool.purchase_date,
        'p7': tool.borrowed
            }

    cur = conn.cursor()
    cur.execute(sql, t1)
    conn.commit()
    return cur.lastrowid


def get_tools(conn, id=-1):
    """
    Query all rows in tools table
    :param id:
    :param conn: Connection to SQLite database
    :return: dictionary of tool objects
    """
    cur = conn.cursor()
    if not id == -1:
        cur.execute("SELECT * FROM tools WHERE id=" + str(id))
    else:
        cur.execute("SELECT * FROM tools")

    rows = cur.fetchall()
    tools =  dict()

    for row in rows:
        # TODO capture in dict of objects
        tools[str(row[0])] = (Tool(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[0]))

    return tools


def update_tool(conn, tool: Tool):
    """ Update tool properties
    :param conn: database connection from create_connection(db)
    :param tool: tool object to update
    :return : tool id
    """
    sql = ''' UPDATE tools
            SET sn = :t1,
                type = :t2,
                description = :t3,
                brand = :t4,
                price = :t5,
                purchase_date = :t6,
                borrowed = :t7
            WHERE id = :t8
            '''

    tool1 = {
        't1': tool.serial_number,
        't2': tool.tool_type,
        't3': tool.description,
        't4': tool.brand,
        't5': tool.price,
        't6': tool.purchase_date,
        't7': tool.borrowed,
        't8': tool.tool_id
            }

    cur = conn.cursor()
    cur.execute(sql, tool1)
    conn.commit()
    conn.close()
    return cur.lastrowid


def delete_all_tools(conn):
    """
    Delete all rows in tools table
    :param conn: Connection to SQLite db
    :return:
    """
    sql = "DELETE FROM tools"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def delete_tool_by_id(conn, id):
    """
    Delete tool by tool id
    :param conn: Connection to SQLite database
    :param id: id of the tool
    :return:
    """
    sql = "DELETE FROM tools WHERE id=?"
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def create_person(conn, person: Person):
    """ Create a new person in the persons table
    :param conn: connection object
    :param person: Person object
    :return: person id
    """

    sql = "INSERT INTO persons( first_name, last_name, phone, email)\n" \
          "VALUES(:p1,:p2,:p3,:p4)"
    per1 = {
        'p1': person.first_name,
        'p2': person.last_name,
        'p3': person.phone_number,
        'p4': person.email
          }
    cur = conn.cursor()
    cur.execute(sql, per1)
    conn.commit()
    conn.close()
    return cur.lastrowid


def get_persons(conn, id=-1):
    """
    Query all rows in persons table
    :param id:
    :param conn: Connection to SQLite database
    :return: dictionary of person objects
    """
    cur = conn.cursor()
    if not id == -1:
        cur.execute("SELECT * FROM persons WHERE id=" + str(id))
    else:
        cur.execute("SELECT * FROM persons")

    rows = cur.fetchall()
    persons =  dict()

    for row in rows:
        # TODO capture in dict of objects
        persons[str(row[0])] = (Person(row[1],row[2],row[3],row[4],row[0]))

    return persons


def update_person(conn, person: Person):
    """ Update person properties
    :param conn: database connection from create_connecction(db)
    :param person: person object to update
    :return: person id
    """
    sql = ''' UPDATE persons
            SET first_name = :t1,
                last_name = :t2,
                phone = :t3,
                email = :t4
            WHERE id = :t8
            '''

    person1 = {
        'p1': person.first_name,
        'p2': person.last_name,
        'p3': person.phone_number,
        'p4': person.email,
        'p8': person.id
            }

    cur = conn.cursor()
    cur.execute(sql, person1)
    conn.commit()
    conn.close()
    return cur.lastrowid


def delete_person_by_id(conn, id):
    """
    Delete person by id
    :param conn: Connection to SQLite database
    :param id: id of the person
    :return:
    """
    sql = "DELETE FROM persons WHERE id=?"
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_persons(conn):
    """
    Delete all rows from persons table
    :param conn: Connection to SQLite databse
    :return:
    """
    sql = "DELETE FROM persons"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


if __name__ == '__main__':
    # test define tables
    # define_tables()

    db = r"../Content/pythonsqlite.db"
    conn = create_connection(db)
    tool = Tool('A123', 'hand', '3/8 ratchet', 'Mac', 25.87, datetime.datetime.now(), False)
    person = Person('Ali', 'Brown', '515-771-5940', 'alekjbrown@live.com')

    # test inserting a tool
    # create_tool(conn, tool)

    # test inserting a person
    # create_person(conn, person)

    # test updating a tool
    # tools = get_tools(conn,1)
    # tools["1"].price = 5.00
    # tools["1"].borrowed = True
    # update_tool(conn, tools["1"])

    # test delete all tools
    # delete_all_tools(conn)

    # test get all tools
    # tools = get_tools(conn)
    # print(tools)

    # test get persons
    # persons = get_persons(conn)
    # print(persons)

    # close conn
    conn.close()

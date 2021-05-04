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


# if __name__ == '__main__':
    # test define tables
    # define_tables()

    # test inserting a tool
    # db = r"../Content/pythonsqlite.db"
    # conn = create_connection(db)
    # tool = Tool('A123', 'hand', '3/8 ratchet', 'Mac', 25.87, datetime.datetime.now(), False)
    # create_tool(conn, tool)

    # test inserting a person
    # db = r"../Content/pythonsqlite.db"
    # conn = create_connection(db)
    # person = Person('Ali', 'Brown', '515-771-5940', 'alekjbrown@live.com')
    # create_person(conn, person)
    # conn.close()

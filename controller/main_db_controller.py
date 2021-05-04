"""
Author: Alek Brown
Program: Borrow My Tools
Date: 2021-05-03

This function creates a database connection utilizing sqlite for local persistance
"""

import sqlite3
from sqlite3 import Error
from model.tool import Tool
from model.person import Person


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
                                    price long,
                                    purchase_date text,
                                    borrowed integer
                                );"""

    sql_create_persons_table = """ CREATE TABLE IF NOT EXISTS peoples (
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

    sql = ''' INSERT INTO tools(sn, type, description, brand, price, purchase_date, borrowed)
                VALUES(?,?,?,?,?,?,?)'''

    cur = conn.cursor()
    cur.execute(sql, tool)
    conn.commit()
    return cur.lastrowid


def create_person(conn, person: Person):
    """ Create a new person in the persons table
    :param conn: connection object
    :param person: Person object
    :return: person id
    """

    sql = ''' INSERT INTO persons( first_name, last_name, phone, email)
            VALUES(?,?,?,?)'''

    cur = conn.cursor()
    cur.execute(sql, person)
    conn.commit()
    return cur.lastrowid





if __name__ == '__main__':
    define_tables()


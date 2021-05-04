Borrow My Tools

Base descriptions of packages and their contents

controller:
    main_db_controller: the heart of persistence for this program, it will set up the connection and create tables
        using SQLite3 to persist locally where the program is installed

model:
    Tool: object to represent a tool
        - tid: identifying id for persistence
        - sn: serial number of physical tool
        - tool_type: type of tool
            - hand
            - power
            - diagnostic
            - specialty
            - air
            - electrical
            - oversize equipment
        - description: description of tool (i.e. '3/8 drive 10mm deep socket')
        - brand: brand of tool
        - price: price you paid for the tool
        - purchase_date: date tool was purchased for warranty purposes
        - borrowed: boolean, True if tool is lent out right now

    Person: object to represent a person
        - first_name: first name of person
        - last_name: last name of person
        - phone: phone number to reach person
        - email: email to reach person

view:

tests:
    test_person: Unit test for person object
    test_tool: Unit test for tool object

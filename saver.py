#!/bin/env python3

def this_is_record(score):
    """if this is score is new, is saving"""
    score = int(score)
    try:
        database = open(".record",'r')
        record = database.read()
    except:
        file = open(".record" , "w")
        file.write("0")
        file.close()
        database = open(".record",'r')
        record = database.read()


    try:
        record = int(record)
    except:
        file = open('.record','w')
        file.write('0')
        file.close()

        file = open('.record' , 'r')
        record = file.read() ; record = int(record)

    database.close()
    if score >= record:
        return True
    return False


def saving_record(score):
    """i saving record for player"""
    if this_is_record(score):
        database = open('.record','w')
        database.write(str(score))


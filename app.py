from flask import Flask
from flask_restful import  Api,Resource
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import psycopg2
import psycopg2.extras
from collections import OrderedDict
import json
import requests
from flask import jsonify

#=====================================================================DATABASE CONNECTION PURPOSE=============================================================================
Host = "localhost"
Port = "5432"
Dbname = "BanksData"
User = "postgres"
pwd = "sYam@123"



#=============================================================================FLASK============================================================================================

app = Flask(__name__)
api = Api(app)
#=================================================================================BASE-URL=====================================================================================
@app.route('/')
def index():
    try:
        Host = "localhost"
        Port = "5432"
        Dbname = "BanksData"
        User = "postgres"
        pwd = "sYam@123"
        #db_conn = psycopg2.connect(host=Host, port=Port, dbname=Dbname, user=User, password=pwd)
        db_conn = '''postgres: // ujysnxslsapccb: 76
        a7fdb108585830118a05cc1a0a0d79106ae0bfc145118a74c82d9dced39eb6 @ ec2 - 18 - 215 - 111 - 67.
        compute - 1.
        amazonaws.com: 5432 / dtqen6muhpr11'''
        db = db_conn.cursor()
        statement = "SELECT DISTINCT city FROM bankbranches where city LIKE 'BANG%' order by city LIMIT 5 "
        db.execute(statement)
        cityList = db.fetchall()
        k = []
        for i in range(len(cityList)):
            k.append(cityList[i][0].replace("'", "", 4))
        s = "SELECT name FROM banks"
        db.execute(s)
        bankList = db.fetchall()
        l = []
        for i in range(len(bankList)):
            l.append(bankList[i][0].replace("'", "", 2))

        s = "SELECT ifsc,bank_id,branch,address,city,district,state,bank_name FROM bankbranches where city LIKE 'B%' ORDER By ifsc LIMIT 1000"
        db.execute(s)
        details = db.fetchall()

        db.close()
        db_conn.close()
    except Exception as e:
        handle_error(e)
    return render_template("index.html",details = details,cityList = k, details_length = len(details))


#==============================================================================AUTOCOMPLETE-URL================================================================================

@app.route("/api/branches/autocomplete/<string:branch>/<string:limit>/<string:offset>",methods = ['GET'])
def get(branch,limit,offset):
    try:
        Host = "localhost"
        Port = "5432"
        Dbname = "BanksData"
        User = "postgres"
        pwd = "sYam@123"
        # db_conn = psycopg2.connect(host=Host, port=Port, dbname=Dbname, user=User, password=pwd)
        db_conn = '''postgres: // ujysnxslsapccb: 76
                a7fdb108585830118a05cc1a0a0d79106ae0bfc145118a74c82d9dced39eb6 @ ec2 - 18 - 215 - 111 - 67.
                compute - 1.
                amazonaws.com: 5432 / dtqen6muhpr11'''
        #db = db_conn.cursor()
        with db_conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as db:
            s = f"SELECT * FROM branches WHERE city = '{branch}' ORDER BY ifsc LIMIT {limit} OFFSET {offset}"
            db.execute(s)
            column_names = [desc[0] for desc in db.description]
            list_users = db.fetchall()
            d = {}
            print(list_users)
            for row in range(len(list_users)):
                h = {}
                for col in range(len(column_names)):
                    h[column_names[col]] = list_users[row][col]
                d["branch" + f"{row+1}"] = h

            db.close()
            db_conn.close()
    except Exception as e:
        handle_error(e)


    return json.dumps(d,sort_keys=False)





#==============================================================================SEARCH ALL FILEDS================================================================================
@app.route("/api/branches/<string:search_element>/<string:limit>/<string:offset>",methods = ['GET'])
def get_details(search_element,limit,offset):
    Host = "localhost"
    Port = "5432"
    Dbname = "BanksData"
    User = "postgres"
    pwd = "sYam@123"
    try:
        # db_conn = psycopg2.connect(host=Host, port=Port, dbname=Dbname, user=User, password=pwd)
        db_conn = '''postgres: // ujysnxslsapccb: 76
                a7fdb108585830118a05cc1a0a0d79106ae0bfc145118a74c82d9dced39eb6 @ ec2 - 18 - 215 - 111 - 67.
                compute - 1.
                amazonaws.com: 5432 / dtqen6muhpr11'''

        with db_conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as db:
            s = f'''SELECT * FROM branches as b 
                    WHERE b.ifsc = '{search_element}'
                          OR b.city = '{search_element}'
                          OR b.district = '{search_element}'
                          OR b.state = '{search_element}'
                          OR b.bank_name = '{search_element}' LIMIT {limit} OFFSET {offset} '''
            db.execute(s)
            column_names = [desc[0] for desc in db.description]
            list_details = db.fetchall()
            d = {}
            for row in range(len(list_details)):
                h = {}
                for col in range(len(column_names)):
                    h[column_names[col]] = list_details[row][col]
                d["branch" + f"{row + 1}"] = h
            db.close()
            db_conn.close()
    except Exception as e:
        handle_error(e)

    return json.dumps(d,sort_keys=False)



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++HANDLING EXCEPTIONS++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, requests.HTTPError):
        code = e.code
    print(code)
    return jsonify(error=str(e)), code
#==============================================================================MAIN FUNCTION===================================================================================
if __name__ == "__main__":
    app.run()


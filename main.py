import json
import requests
from flask import Flask, request,jsonify

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def hello_world():
    #need to change file name
    return app.send_static_file("hw6.html")


#search request is an endpoint
@app.route("/login_request",methods=["GET"])
def login():
    parameter = request.args
    parameter_dict = parameter.to_dict()

    email = parameter_dict["email"]
    password = parameter_dict["password"]
    print("login email:", email," password:",password)

    #insert the data into database

    #return the json data to front end
    return 

@app.route("/comment_request",methods=["GET"])
def comment():
    parameter = request.args
    parameter_dict = parameter.to_dict()

    email = parameter_dict["email"]
    comment = parameter_dict["comment"]

    #insert data into database


    #return the json data to the front end
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route("/star_request",methods=["GET"])
def star():
    parameter = request.args
    parameter_dict = parameter.to_dict()

    email = parameter_dict["email"]
    star = parameter_dict["star"]

    #insert data into database

    #return the json data to the front end
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/venue_detail",methods=["GET"])
def search_venue():
    ticketmaster_url_front = "https://app.ticketmaster.com/discovery/v2/venues?apikey=4cQfTQ4MajUnHtGsM1vezXLAsAaWT18U&keyword="
    parameter = request.args
    parameter_dict = parameter.to_dict()

    ticketmaster_url_front += parameter_dict["keyword"]

    print("TM_Venue_URL:",ticketmaster_url_front)

    ticketmaster_response = requests.get(ticketmaster_url_front).json()
    #print(ticketmaster_response)

    ticketmaster_response = jsonify(ticketmaster_response)
    ticketmaster_response.headers['Access-Control-Allow-Origin'] = '*'

    return ticketmaster_response

if __name__ == "__main__":
    app.run(debug=True)


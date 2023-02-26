import json
import requests
from flask import Flask, request,jsonify

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def hello_world():
    #need to change file name
    return app.send_static_file("newuserform.html")


#search request is an endpoint
@app.route("/login_request",methods=["GET"])
def login():
    parameter = request.args
    parameter_dict = parameter.to_dict()
    
    user_key=email.replace("@","").replace(".","")

    email = parameter_dict["email"]
    password = parameter_dict["password"]
    print("login email:", email," password:",password)

    #insert the data into database
    response = requests.patch('https://athenahacks-1ad60-default-rtdb.firebaseio.com/users/'+str(user_key)+'/login_info/.json',json=star_json)
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

#get average star rating
def Average(lst):
    return sum(lst) / len(lst)

def avg_star(category):
    response = requests.get('https://athenahacks-1ad60-default-rtdb.firebaseio.com/reviews/'+str(category)+'/star/.json?orderBy="$key"').json()
    star_list=response.values()

    return round(Average(star_list),2)

#upload reviews for beginner_friendly, networking, speakers, workshops, overall_experience
#star ratings
def post_star_review(email,category,stars):
  star_json={str(email): int(stars)}
  #output_star=json.dumps(star_json, indent=4)
  response = requests.patch('https://athenahacks-1ad60-default-rtdb.firebaseio.com/reviews/'+str(category)+'/star/.json',\
                            json=star_json)
  return response

#written feedback
def post_written_review(email,category,written_review):
  written_json={str(email): str(written_review)}
  #output_written=json.dumps(written_json, indent=4)
  response = requests.patch('https://athenahacks-1ad60-default-rtdb.firebaseio.com/reviews/'+str(category)+'/written/.json',\
                            json=written_json)
  return response

#print out  num reviews
def get_reviews(category,num):
  try:
      response = requests.get('https://athenahacks-1ad60-default-rtdb.firebaseio.com/reviews/'+str(category)+'/written/.json?orderBy="$key"').json()
      reviews=[]
      for values in response.values():
          reviews.append(values)

      res=[]
      for i in reviews:
          if i not in res:
              res.append(i)
      leng=len(res)
      #st.write(res)
      try:
          randomlist = random.sample(range(0, leng), num)
          
          for count,i in enumerate(randomlist):
              count_disp=count+1
              print(str(count_disp)+'. '+str(res[i]))
      except:
          print('Not enough info available!')
  except:
      print('Not enough info available!')
        
 # print out contact info
def get_contact_info(person):
  response = requests.get('https://athenahacks-1ad60-default-rtdb.firebaseio.com/users/'+str(person)+'/information/.json')
  response_dict=response.json()
  name=response_dict['name']
  email=response_dict['email']
  phone_number=response_dict['phone_number']
  linkedin=response_dict['linkedin_url']
  bio=response_dict['bio']

  print('Get connected with ',str(name))
  print('email: ',str(email))
  print('phone number: ',str(phone_number))
  print('Linkedin: ',str(linkedin))
  print('About ',str(name),':\n',str(bio))
    

#compute similarities
def flatten(l):
    return [item for sublist in l for item in sublist]

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union


if __name__ == "__main__":
    app.run(debug=True)


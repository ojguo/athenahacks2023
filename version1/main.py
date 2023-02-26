import json
import requests
from flask import Flask, request,jsonify

#post user information data to firebase
def store_user_info(user_dict):
    print("INSIDE STORE USER INFO!")
    user_key=user_dict['email'].replace("@","").replace(".","")
    print("user key:",user_key)
    comment_key = ["beginner", "workshop","speaker","networking","overallexp"]
    for k,v in user_dict.items():
        user_json={str(k):v}
        # if str(k) in  comment_key:
        #     response = requests.patch('https://athenahacks-1ad60-default-rtdb.firebaseio.com/users/'+str(user_key)+'/information/.json',\
        #                     json=user_json)

        response = requests.patch('https://athenahacks-1ad60-default-rtdb.firebaseio.com/users/'+str(user_key)+'/information/.json',\
                            json=user_json)
    return user_key

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
  name=response_dict['fullname']
  email=response_dict['email']
#   phone_number=response_dict['phone_number']
#   linkedin=response_dict['linkedin_url']
#   bio=response_dict['bio']

  print('Get connected with ',str(name))
  print('email: ',str(email))
#   print('phone number: ',str(phone_number))
#   print('Linkedin: ',str(linkedin))
#   print('About ',str(name),':\n',str(bio))

  return response_dict
    

#compute similarities
def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return len(final_list)

def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = Union(list1,list2)
    return float(intersection) / union

#return a list of top_n similar users based on Jaccard similarity
def get_similar_people(user_key,top_n):
  response = requests.get('https://athenahacks-1ad60-default-rtdb.firebaseio.com/users/'+str(user_key)+'/information/.json')
  user_dict=response.json()
  user_list=[]
  for k,v in user_dict.items():
    if k in ['industry','major','interests']:
      user_list.append(v)
  user_list=flatten(user_list)

  similarities=[]
  response2=requests.get('https://athenahacks-1ad60-default-rtdb.firebaseio.com/users/.json').json()

  for k,v in response2.items():
    list_loop=[]
    for k2,v2 in v['information'].items():
      if k2 in ['industry','major','interests']:
        list_loop.append(v2)

    jac_sim=jaccard(user_list,list_loop)
    similarities.append((jac_sim,k))
  similarities=sorted(similarities)

  return_val=[]
  try:
    for i in range(top_n):
      return_val.append(similarities[i][1])
    return return_val
  except:
    for i in range(len(similarities)):
      if similarities[i][1] not in return_val:
        return_val.append(similarities[i][1])
    return return_val

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
    #response.headers['Access-Control-Allow-Origin'] = '*'
    return response



@app.route("/new_user_request",methods=["GET"])
def new_user():
    parameter = request.args
    parameter_dict = parameter.to_dict()

    print("param new user:", parameter_dict)
    new_user_key = store_user_info(parameter_dict)

    print("new user key:", new_user_key)

    similar_people = get_similar_people(new_user_key,2)
    print("similar people:",similar_people)

    result_list = []
    for person in similar_people:
        result_list.append(get_contact_info(person))
    
    response = json.dumps(result_list)







    

    # fullname = parameter_dict["fullname"]
    # email = parameter_dict["email"]
    # gradyear = parameter_dict["gradyear"]
    # gender = parameter_dict["gender"]
    # school = parameter_dict["school"]
    # major = parameter_dict["major"]
    # attended = parameter_dict["attended"]
    # industry = parameter_dict["industry"]
    # interest = parameter_dict["interest"]


    # beginner = str()
    # workshop = str()
    # speaker = str()
    # networking = str()
    # overallexp = str()
    
    # try{
    #     beginner = parameter_dict["beginner"]
    # }except{
    #     pass
    # }

    # try{
    #     workshop = parameter_dict["workshop"]
    # }except{
    #     pass
    # }

    # try{
    #     speaker = parameter_dict["speaker"]
    # }except{
    #     pass
    # }

    # try{
    #     networking = parameter_dict["networking"]
    # }except{
    #     pass
    # }

    # try{
    #     overallexp = parameter_dict["overallexp"]
    # }except{
    #     pass
    # }

    #insert data into database

    #return the json data to the front end
    #response.headers['Access-Control-Allow-Origin'] = '*'
    print("responsetype:",type(response))
    print("response:",response)
    return response

@app.route("/new_user_comment",methods=["GET"])
def new_user_comment():
    parameter = request.args
    parameter_dict = parameter.to_dict()


# @app.route("/venue_detail",methods=["GET"])
# def search_venue():
#     ticketmaster_url_front = "https://app.ticketmaster.com/discovery/v2/venues?apikey=4cQfTQ4MajUnHtGsM1vezXLAsAaWT18U&keyword="
#     parameter = request.args
#     parameter_dict = parameter.to_dict()

#     ticketmaster_url_front += parameter_dict["keyword"]

#     print("TM_Venue_URL:",ticketmaster_url_front)

#     ticketmaster_response = requests.get(ticketmaster_url_front).json()
#     #print(ticketmaster_response)

#     ticketmaster_response = jsonify(ticketmaster_response)
#     ticketmaster_response.headers['Access-Control-Allow-Origin'] = '*'

#     return ticketmaster_response

if __name__ == "__main__":
    app.run(debug=True)


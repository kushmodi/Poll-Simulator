from flask import *
from flask_cors import CORS
  
app = Flask(__name__) #creating the Flask class object   
CORS(app)

candidatesArray = []
votersArray = []

@app.route('/') #decorator drfines the   
def home():
    return "This is poll-simulator app server";

@app.route('/add',methods = ['POST'])
def add():
      data = request.get_json()
      candidatesArray.append({"name" : data['name'], "votes" : 0})
      return {"Message":"data added.", "status":200}

@app.route('/vote',methods = ['POST'])
def vote():
      resdata = request.get_json()

      if (202012120 - int(resdata['voterId']) < 0 or 202012120 - int(resdata['voterId']) > 120):
            return {"message" : "voterID Invalid.", "response" : 202}
      
      if (resdata['selectedCandidate'] == 0):
            return {"message" : "Please select any candidate to vote", "response" : 203}


      for voter in votersArray:
            if voter == (int(resdata['voterId'])):
                  return {"message" : "This voterID already voted.", "response" : 204}
      # print(voterfile)
      
      votersArray.append(int(resdata['voterId']))
      
      for candidate in candidatesArray:
            if(candidate['name'] == resdata['selectedCandidate']):
                  candidate['votes'] = candidate['votes'] + 1;
      
      return {"message" : "Your vote is sucessfully added, Thanks for voting", "response" : 200}

@app.route('/winner',methods = ['GET'])
def winner():
      winner = 0
      setArray  = []
      for candidate in candidatesArray:
            if (candidate['votes'] == winner and winner != 0):
                  return {"message" : "It's Tie", "response" : 201}
            elif(candidate['votes'] > winner):
                  winner = candidate['votes']
                  if len(setArray) > 0:
                        setArray.pop()
                  setArray.append(candidate)
      if(winner == 0):
            return {"message" : "no winner", "response" : 201}
      return jsonify(setArray)

@app.route('/voteSummary',methods = ['GET'])
def voteSummary():  
      return jsonify(candidatesArray)

if __name__ =='__main__':
    app.run(debug = True)
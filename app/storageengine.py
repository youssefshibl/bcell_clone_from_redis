import re
import json
class QueryEngine:
  # AllPattern
  PingPattern = re.compile(r"^PING$", re.IGNORECASE)
  EchoPattern = re.compile(r"^ECHO$", re.IGNORECASE)
  SetPattern = re.compile(r"^SET$", re.IGNORECASE)
  GetPattern = re.compile(r"^GET$", re.IGNORECASE)
  FlushPattern = re.compile(r"^FLUSH$", re.IGNORECASE)
  SavePattern = re.compile(r"^SAVE$", re.IGNORECASE)
  DeletePattern = re.compile(r"^DELETE$", re.IGNORECASE)
  ExistsPattern = re.compile(r"^EXIST$", re.IGNORECASE)
  # Data
  SnapshotFilePath = "./data/data.json"
  Data = {}


  def __init__(self, name, port):
    self.name = name
    self.port = port

  def query(self, query):
    queryArray = query.split()
    print(queryArray)
    PatterNumber = self.checkPatternNumber(queryArray[0])
    if(PatterNumber == 1):
      return self.pingresponse(queryArray)
    elif(PatterNumber == 2):
      return self.echoresponse(queryArray)
    elif(PatterNumber == 3):
      return self.setresponse(queryArray)
    elif(PatterNumber == 4):
      return self.getresponse(queryArray)
    elif(PatterNumber == 5):
      return self.flushresponse(queryArray)
    elif(PatterNumber == 6):
      return self.saveresponse(queryArray)
    elif(PatterNumber == 7):
      return self.deleteresponse(queryArray)
    elif(PatterNumber == 8):
      return self.existsresponse(queryArray)
    else:
      return "ERROR IN QUERY"
    
  def checkPatternNumber(self, queryKey):
    if(self.PingPattern.match(queryKey)):
      # PING query
      return 1
    elif(self.EchoPattern.match(queryKey)):
      # ECHO query
      return 2
    elif(self.SetPattern.match(queryKey)):
      # SET query
      return 3
    elif(self.GetPattern.match(queryKey)):
      # GET query
      return 4
    elif(self.FlushPattern.match(queryKey)):
      # FLUSH query
      return 5
    elif(self.SavePattern.match(queryKey)):
      # SAVE query
      return 6
    elif(self.DeletePattern.match(queryKey)):
      # DELETE query
      return 7
    elif(self.ExistsPattern.match(queryKey)):
      # EXISTS query
      return 8
    else:
      return 0
      
  def pingresponse(self, queryArray):
    if(len(queryArray) >= 3):
      return "ERROR : PING expected 1 argument"
    if(len(queryArray) == 2):
      return queryArray[1]
    return "PONG"
  def echoresponse(self, queryArray):
    if(len(queryArray) >= 3):
      return "ERROR : ECHO expected 1 argument"
    return queryArray[1]
  def setresponse(self,queryArray):
    if(len(queryArray) != 3):
      return "ERROR : SET expected 2 arguments"
    self.Data[queryArray[1]] = queryArray[2]
    print(self.Data)
    return "OK"
  def getresponse(self,queryArray):
    if(len(queryArray) != 2):
      return "ERROR : GET expected 1 argument"
    if(queryArray[1] not in self.Data):
      return "ERROR : Key not found"
    return self.Data[queryArray[1]]
  def flushresponse(self , queryArray):
    if(len(queryArray) >= 3):
      return "ERROR : FLUSH expected 1 argument"
    self.Data = {}
    return "OK"
  def saveresponse(self , queryArray):
    if(len(queryArray) >= 2):
      return "ERROR : SAVE no expected any argument"
    # save all data in file
    self.SaveDataInFile()
    return "OK"
  def deleteresponse(self , queryArray):
    if(len(queryArray) != 2):
      return "ERROR : DELETE expected 1 argument"
    if(queryArray[1] not in self.Data):
      return "ERROR : Key not found"
    del self.Data[queryArray[1]]
    return "OK"
  def existsresponse(self , queryArray):
    if(len(queryArray) != 2):
      return "ERROR : EXISTS expected 1 argument"
    if(queryArray[1] not in self.Data):
      return "False"
    return "True"

  def SaveDataInFile(self):
    with open(self.SnapshotFilePath, "w+") as outfile:
      json.dump(self.Data, outfile)
         
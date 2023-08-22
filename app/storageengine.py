import re
class QueryEngine:
  PingPattern = re.compile(r"^PING$", re.IGNORECASE)
  EchoPattern = re.compile(r"^ECHO$", re.IGNORECASE)
  SetPattern = re.compile(r"^SET$", re.IGNORECASE)
  GetPattern = re.compile(r"^GET$", re.IGNORECASE)
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





        
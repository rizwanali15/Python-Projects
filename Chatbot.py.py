name = input("Naam likh: ")
import datetime
import time

presenthour = datetime.datetime.now().hour

if 5 <= presenthour <= 11:
    print("Good morning", name)
elif 11 <= presenthour <= 17:
    print("Good afternoon", name)
elif 17 <= presenthour <= 20:
    print("Good evening", name)
else:
    print("Good night", name)


print("hello welcome to our chatbot")


responses={
    "salam alikum":"walikum salam",
    "tumhara name kia hai":"mera name chatbot hai",
    "tum kha sy ho":"me a.i ki duniya sy ho"
}

def getResponse(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
            
    # return "Teri maa ka bhrosa"
      
while True:
    userInput = input("Iddhr likh: ")
    reply= getResponse(userInput)
    print("Jawab: ", reply)
    
    if "bye" in userInput.lower():
        break

  








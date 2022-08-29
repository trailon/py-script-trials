import json
import nltk

words = []
labels = []
docs_x = []
docs_y = []

'''with open(r"Yapay Zeka.json") as file:
    data = json.load(file)
    
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        with open('patterns.txt', 'a') as the_file:
            the_file.write(pattern+"\n")
    for response in intent["responses"]:
        with open('responses.txt', 'a') as the_file:
            the_file.write(response+"\n")
            '''
file1 = open('patterns.json', 'r')
file2 = open('responses.json', 'r')          
lines1 = file1.readlines()
lines2 = file2.readlines()
for i in range(len(lines1)):
    # a Python object (dict):
    x = {
      "tag": "","patterns": lines1[i],"responses": lines2[i],"context_set": ""
    }
    
    # convert into JSON:
    y = json.dumps(x,indent=2)


    with open('outputjson.json', 'a') as the_file:
            the_file.write(y)
            the_file.write(',')


print(len(lines1))
print(len(lines2))
    


'''

'''
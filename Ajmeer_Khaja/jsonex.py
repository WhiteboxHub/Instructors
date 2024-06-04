import json
dictData = {
    "name":"kakashi Hatake",
    "role":"ninja Tutor",
    "assignedTeam":"Team 7",
    "TeamMembers": ["naruto","susuke","sakura"],
    "first Assignment":"escorting a bridge builder",
    "Nickname":"The Copy ninja",
    "experties":"awakened mangekeyo sharingan",
    "chakraNature":"lightning"
}

#Converting to json 
x=json.dumps(dictData,indent=5);
print(x)
jsondata = json.dumps(dictData);
#json to dict
y = json.loads(x);
print(y["Nickname"])
print(y)

x2=json.dumps(dictData,indent=5,sort_keys=True);
print(x2)
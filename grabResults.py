import urllib.request, json, pprint

class VoterGroup:
    def __init__(self,VoteValues):
        self.VoterDict=VoteValues

    def printValues(self):
        print('**********************')
        for value in self.VoterDict:
            print(value+ " : "+ str(self.VoterDict[value]))
        print('**********************')

VoteStatsStore={}
with urllib.request.urlopen("https://js.cardiffstudents.com/elections/msl_json.php?e=1446&g=6,2,7,5,8&v=1") as url:

    data = json.loads(url.read().decode())
    for item in data:
        print(item)
        if item=="Groups":
            for group in data[item]:
                name=group['Name']
                for groupValue in group['Items']:
                   # name=groupValue['Name']
                   # print(groupValue)
                    #print(name.upper())
                    VoteStatsStore[name]=VoterGroup(groupValue)
                    VoteStatsStore[name].printValues()
        else:
            print(data[item])
        print("----------------------------")
import urllib.request, json, pprint
with urllib.request.urlopen("https://js.cardiffstudents.com/elections/msl_json.php?e=1446&g=6,2,7,5,8&v=1") as url:

    data = json.loads(url.read().decode())
    pprint.pprint(data)
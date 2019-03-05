# ElectionStats
Cardiff University's Student Union sabattical officers election featured a really interesting demographics breakdown.I wanted to practise, so thought it might be interesting to have a go at making my own. Since the election ended they closed the demographics section, so this might be the only version available. The data was grabbed using the following JS commands (taken from the demographics page source code):

* getJSON('//js.cardiffstudents.com/elections/msl_json.php?e='+election_id+'&g=6,2,7,5,8&v=1&callback=?'
* getJSON('//js.cardiffstudents.com/elections/student_type_dems.php?e='+election_id
* getJSON('//js.cardiffstudents.com/elections/msl_json.php?v=1&e='+election_id+'&t=membershipstats&g=1,2&sort=Turnout&dir=Descending&callback=?'
* getJSON('//js.cardiffstudents.com/elections/votes.php?v=2&e=' + election_id + '&callback=?'

Two election_id of "1027" and "1446"were given, with '1446' likely overiding the first. There looks like there might be the option of getting data from previous year's elections too.

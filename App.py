import urllib.request as ur
import urllib.parse
import json
from Database import Dbase
from bson.code import Code
from pprint import pprint


def fetch_json_data(url_func):
    url = url_func

    values = {'name': 'Michael Foord',
              'location': 'Northampton',
              'anguage': 'Python'}
    headers = {'User-Agent': 'Mozilla/5.0'}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    the_page = response.read().decode('utf-8')

    return the_page


def main():
    Dbase_Obj = Dbase()
    conn = Dbase_Obj.setupConnection()

####fetching team details:
    url = 'http://www.fantasyfootballnerd.com/service/nfl-teams/json/test/'
    team_detl = fetch_json_data(url)
    team_data = json.loads(team_detl)

####creating a new collection and inserting data
    collectionTeamDetl = conn['TeamDetails']
    for teamdetl in team_data['NFLTeams']:
        collectionTeamDetl.insert(teamdetl)

####creating a new team
    result = collectionTeamDetl.insert_one(
        {
            "code": "NEW",
            "fullName": "Its a new team",
            "shortName": "New Team"
        }
    )

####selecting the new inserted team
    print(collectionTeamDetl.find_one({"_id": {"$eq": result.inserted_id}}))

####fetching player details:
    url = 'https://www.fantasyfootballnerd.com/service/players/json/test/'
    player_detl = fetch_json_data(url)
    player_data = json.loads(player_detl)

####creating a new collection and 'bulk' inserting data
    collectionPlayerDetl = conn['PlayerDetails']
    collectionPlayerDetl.insert_many(player_data['Players'])

####Deleting all players D.O.B is '0000-00-00'
    count = collectionPlayerDetl.delete_many({"dob": "0000-00-00"})
    print('the number of documents deleted is :' + str(count.deleted_count))

####Count remaining documents in PlayerDetails
    count = collectionPlayerDetl.count()
    print('the count of players details is :' + str(count))

####select query using Join on both Player and Team details
    combined_player_detl = collectionPlayerDetl.aggregate([
    {
    "$lookup": {
    "from":'TeamDetails',
    "localField": 'team',
    "foreignField": 'code',
    "as":'CombinedDetails'
    }
    }])

    for documents in combined_player_detl:
        pprint(documents)

####selecting with group by
    result = collectionPlayerDetl.aggregate(
    [{
        "$group": {"_id": "$position", "count": {"$sum": 1}}
    }])

    for item in result:
        print(item)

####querying the heaviest players in the collections
    weight = collectionPlayerDetl.aggregate([
        {"$sort": {"weight": 1}},
        {"$limit": 5},
    ])

    for docs in weight:
        print(docs['displayName'], docs['weight'], docs['team'])

####querying the number of player in each team using MapReduce
    mapper = Code("""
                    function(){
                            var key = this.team;
                            var value = 1;
                            emit(key, value);
                        };
                 """)

    reducer = Code("""
                    function(KeyTeam, Val){
                        return Array.sum(Val);
                    }
                    """)

    count_by_team1 = collectionPlayerDetl.map_reduce(mapper, reducer, "count_by_team")
    for document in count_by_team1.find():
        pprint(document)


if __name__ == '__main__': main()

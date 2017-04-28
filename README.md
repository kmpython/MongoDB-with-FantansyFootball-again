# MongoDB-with-FantansyFootball-again

A hands on project to learn the fundamentals of NoSQL database - MongoDB using pymongo. I used the data available from Fantasy Football nerd API and performed several operations on them. 

we have used 
MongoDB version = 3.4.4
Pymongo version = 3.4.0
Python version = 3.5.2

We have two Collections (tables in terms of SQL):
1.  Player Details  - (https://www.fantasyfootballnerd.com/service/players/json/test/) 

```json
{'_id': ObjectId('5903881f05488b5f544c5ba8'),
 'active': '1',
 'college': 'Youngstown State',
 'displayName': 'Jamaine Cook',
 'dob': '0000-00-00',
 'fname': 'Jamaine',
 'height': '5-9',
 'jersey': '36',
 'lname': 'Cook',
 'playerId': '2429',
 'position': 'RB',
 'team': 'CLE',
 'weight': '215'}
{'_id': ObjectId('5903881f05488b5f544c5ba9'),
 'active': '1',
 'college': 'Pittsburgh',
 'displayName': 'Maurice Williams',
 'dob': '0000-00-00',
 'fname': 'Maurice',
 'height': '6-1',
 'jersey': '11',
 'lname': 'Williams',
 'playerId': '2430',
 'position': 'WR',
 'team': 'IND',
 'weight': '190'}
 ```

2.  Team Details  - (http://www.fantasyfootballnerd.com/service/nfl-teams/json/test/)

```json
{'_id': ObjectId('5903879b05488b59e0edbc36'),
 'code': 'ARI',
 'fullName': 'Arizona Cardinals',
 'shortName': 'Arizona'}
{'_id': ObjectId('5903879b05488b59e0edbc37'),
 'code': 'ATL',
 'fullName': 'Atlanta Falcons',
 'shortName': 'Atlanta'}
```
I have performed CURD, Aggregations(Joins), Group, sort, count and even MongoDB map-reduce to gain some insights into the data and lay a strong foundation to delve further into the field of NoSQL databases.

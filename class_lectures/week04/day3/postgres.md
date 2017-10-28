## PostgreSQL setup and loading data


### Install PostgreSQL

(Mostly following the [Ubuntu directions](https://help.ubuntu.com/community/PostgreSQL).)

```bash
sudo apt-get install postgresql postgresql-contrib
```

This will install _and start up_ Postgres. You can check:

```bash
ps awx | grep post
```

On Ubuntu, servers are started and stopped mostly with [upstart](http://upstart.ubuntu.com/). Try:

```bash
sudo service postgresql status
sudo service postgresql stop
sudo service postgresql start
```

Installing Postgres also created a `postgres` user on your computer. But we want to be able to log in as ourselves. So:

```bash
sudo -u postgres createuser --superuser my_user_name
sudo -u postgres psql
# now in psql...
\password my_user_name
# exit out of psql with Ctrl+D
# Create a database for your user
sudo -u postgres createdb my_user_name
```

Now you can go to town with just `psql`! Explore a little with `help`, `\?`, `\l`, and `\d`.


### Make a database

Check what databases you have so far with `\l`.

You can create a new database with `CREATE DATABASE database_name;`.

Case doesn't matter, but to make it clear what's a SQL word and what's chosen by us I'll follow the ugly SQL convention of capitalizing like a crazy person.

Let's make a database called `pokemon`.

```sql
CREATE DATABASE pokemon;
```

From within `psql`, use `\c pokedex` to switch to that database.

Use `\d` to see that there are not yet any tables (relations) in the database. So let's create one.


### Make a table

We have to specify the schema of our table, with detail about [data types](http://www.postgresql.org/docs/9.3/static/datatype.html). There are a bunch of data types, but a few are used most commonly.

```sql
CREATE TABLE pokemon (
    id INTEGER NOT NULL, 
	name VARCHAR(30) NOT NULL,
    species_id INTEGER, 
    height INTEGER NOT NULL, 
    weight INTEGER NOT NULL, 
    base_experience INTEGER NOT NULL, 
    "order" INTEGER NOT NULL, 
    is_default INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    CHECK (is_default IN (0, 1))
);
```

Now you can see that you have a table with `\d`. And you can see what's in it like this:

```sql
SELECT * FROM pokemon;
```


### Manual data loading / removing

You can load data from inside `psql`:

```sql
INSERT INTO pokemon (id,name, species_id, height, weight, base_experience, "order", is_default) VALUES (0,'Missingno', 0, 1, .1, 100, 0, 0);
```

Now `SELECT` to see that your data is there.

Run the `INSERT` again to see what happens.

You can also delete:

```sql
DELETE FROM pokemon WHERE id=0;
```

And finally, you can drop a whole table:

```sql
DROP TABLE pokemon;
```


### Loading data from a file

Make the same `pokemon` table again.

Make a file `pokemon.csv`:

```text
id,name,species_id,height,weight,base_experience,order,is_default
1,bulbasaur,1,7,69,64,1,1
2,ivysaur,2,10,130,142,2,1
3,venusaur,3,20,1000,236,3,1
4,charmander,4,6,85,62,5,1
5,charmeleon,5,11,190,142,6,1
6,charizard,6,17,905,240,7,1
7,squirtle,7,5,90,63,10,1
8,wartortle,8,10,225,142,11,1
9,blastoise,9,16,855,239,12,1
10,caterpie,10,3,29,39,14,1
11,metapod,11,7,99,72,15,1
12,butterfree,12,11,320,178,16,1
13,weedle,13,3,32,39,17,1
14,kakuna,14,6,100,72,18,1
15,beedrill,15,10,295,178,19,1
16,pidgey,16,3,18,50,21,1
17,pidgeotto,17,11,300,122,22,1
18,pidgeot,18,15,395,216,23,1
19,rattata,19,3,35,51,25,1
20,raticate,20,7,185,145,26,1
21,spearow,21,3,20,52,27,1
22,fearow,22,12,380,155,28,1
23,ekans,23,20,69,58,29,1
24,arbok,24,35,650,153,30,1
25,pikachu,25,4,60,112,32,1
26,raichu,26,8,300,218,39,1
27,sandshrew,27,6,120,60,40,1
28,sandslash,28,10,295,158,41,1
29,nidoran-f,29,4,70,55,42,1
30,nidorina,30,8,200,128,43,1
31,nidoqueen,31,13,600,227,44,1
32,nidoran-m,32,5,90,55,45,1
33,nidorino,33,9,195,128,46,1
34,nidoking,34,14,620,227,47,1
35,clefairy,35,6,75,113,49,1
36,clefable,36,13,400,217,50,1
37,vulpix,37,6,99,60,51,1
38,ninetales,38,11,199,177,52,1
39,jigglypuff,39,5,55,95,54,1
40,wigglytuff,40,10,120,196,55,1
41,zubat,41,8,75,49,56,1
42,golbat,42,16,550,159,57,1
43,oddish,43,5,54,64,59,1
44,gloom,44,8,86,138,60,1
45,vileplume,45,12,186,221,61,1
46,paras,46,3,54,57,63,1
47,parasect,47,10,295,142,64,1
48,venonat,48,10,300,61,65,1
49,venomoth,49,15,125,158,66,1
50,diglett,50,2,8,53,67,1
51,dugtrio,51,7,333,142,68,1
52,meowth,52,4,42,58,69,1
53,persian,53,10,320,154,70,1
54,psyduck,54,8,196,64,71,1
55,golduck,55,17,766,175,72,1
56,mankey,56,5,280,61,73,1
57,primeape,57,10,320,159,74,1
58,growlithe,58,7,190,70,75,1
59,arcanine,59,19,1550,194,76,1
60,poliwag,60,6,124,60,77,1
61,poliwhirl,61,10,200,135,78,1
62,poliwrath,62,13,540,230,79,1
63,abra,63,9,195,62,81,1
64,kadabra,64,13,565,140,82,1
65,alakazam,65,15,480,225,83,1
66,machop,66,8,195,61,85,1
67,machoke,67,15,705,142,86,1
68,machamp,68,16,1300,227,87,1
69,bellsprout,69,7,40,60,88,1
70,weepinbell,70,10,64,137,89,1
71,victreebel,71,17,155,221,90,1
72,tentacool,72,9,455,67,91,1
73,tentacruel,73,16,550,180,92,1
74,geodude,74,4,200,60,93,1
75,graveler,75,10,1050,137,94,1
76,golem,76,14,3000,223,95,1
77,ponyta,77,10,300,82,96,1
78,rapidash,78,17,950,175,97,1
79,slowpoke,79,12,360,63,98,1
80,slowbro,80,16,785,172,99,1
81,magnemite,81,3,60,65,102,1
82,magneton,82,10,600,163,103,1
83,farfetchd,83,8,150,123,105,1
84,doduo,84,14,392,62,106,1
85,dodrio,85,18,852,161,107,1
86,seel,86,11,900,65,108,1
87,dewgong,87,17,1200,166,109,1
88,grimer,88,9,300,65,110,1
89,muk,89,12,300,175,111,1
90,shellder,90,3,40,61,112,1
91,cloyster,91,15,1325,184,113,1
92,gastly,92,13,1,62,114,1
93,haunter,93,16,1,142,115,1
94,gengar,94,15,405,225,116,1
95,onix,95,88,2100,77,118,1
96,drowzee,96,10,324,66,121,1
97,hypno,97,16,756,169,122,1
98,krabby,98,4,65,65,123,1
99,kingler,99,13,600,166,124,1
100,voltorb,100,5,104,66,125,1
101,electrode,101,12,666,168,126,1
102,exeggcute,102,4,25,65,127,1
103,exeggutor,103,20,1200,182,128,1
104,cubone,104,4,65,64,129,1
105,marowak,105,10,450,149,130,1
106,hitmonlee,106,15,498,159,132,1
107,hitmonchan,107,14,502,159,133,1
108,lickitung,108,12,655,77,135,1
109,koffing,109,6,10,68,137,1
110,weezing,110,12,95,172,138,1
111,rhyhorn,111,10,1150,69,139,1
112,rhydon,112,19,1200,170,140,1
113,chansey,113,11,346,395,143,1
114,tangela,114,10,350,87,145,1
115,kangaskhan,115,22,800,172,147,1
116,horsea,116,4,80,59,149,1
117,seadra,117,12,250,154,150,1
118,goldeen,118,6,150,64,152,1
119,seaking,119,13,390,158,153,1
120,staryu,120,8,345,68,154,1
121,starmie,121,11,800,182,155,1
122,mr-mime,122,13,545,161,157,1
123,scyther,123,15,560,100,158,1
124,jynx,124,14,406,159,162,1
125,electabuzz,125,11,300,172,164,1
126,magmar,126,13,445,173,167,1
127,pinsir,127,15,550,175,169,1
128,tauros,128,14,884,172,171,1
129,magikarp,129,9,100,40,172,1
130,gyarados,130,65,2350,189,173,1
131,lapras,131,25,2200,187,175,1
132,ditto,132,3,40,101,176,1
133,eevee,133,3,65,65,177,1
134,vaporeon,134,10,290,184,178,1
135,jolteon,135,8,245,184,179,1
136,flareon,136,9,250,184,180,1
137,porygon,137,8,365,79,186,1
138,omanyte,138,4,75,71,189,1
139,omastar,139,10,350,173,190,1
140,kabuto,140,5,115,71,191,1
141,kabutops,141,13,405,173,192,1
142,aerodactyl,142,18,590,180,193,1
143,snorlax,143,21,4600,189,196,1
144,articuno,144,17,554,261,197,1
145,zapdos,145,16,526,261,198,1
146,moltres,146,20,600,261,199,1
147,dratini,147,18,33,60,200,1
148,dragonair,148,40,165,147,201,1
149,dragonite,149,22,2100,270,202,1
150,mewtwo,150,20,1220,306,203,1
151,mew,151,4,40,270,206,1
```

Postgres can handle CSV input. To load it:

```sql
COPY pokemon FROM '/path/to/pokemon.csv' DELIMITER ',' CSV HEADER;
```

Verify success with `SELECT`.

Check out what happens if you try to run that command a second time.

### Get more data!

Load in some more tables from [here](https://github.com/veekun/pokedex/tree/master/pokedex/data/csv)



you can find sql schemas for these csvs [here](https://github.com/danmane/PokemonSQLTutorial/blob/master/schema.sql)

### Python bindings for Postgres

How can you access data in Postgres from Python? Using the `psycopg2` module, you can execute any query and get the results in python to do whatever you want to them (put it in `pandas`, throw it into `sklearn` algorithms, etc.)

Here again it will be easier to `apt-get install` than `pip install`:

```bash
sudo apt-get install python-psycopg2
```

Then, in Python:

```python
import psycopg2

db = psycopg2.connect(database='pokedex')
cursor = db.cursor()

cursor.execute("select * from pokemon;")

for row in cursor.fetchall():
    print row
```

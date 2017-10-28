##Lahman Baseball Dataset


Download and set up MySQL server Open-source SQL DB:

* [MySQL Download](http://dev.mysql.com/downloads/mysql/)

* [MySQL Installation](http://dev.mysql.com/doc/refman/5.6/en/installing.html)

Download and set up MySQL Workbench:

* [MySQL Workbench Download](http://dev.mysql.com/downloads/workbench/)

Download the Baseball DB and import the schema:

* Download and unzip [this script](https://github.com/pburkard88/DS_BOS_06/raw/master/Lessons/Lesson02/BDB-sql-2009-11-25.sql.zip)

* Open MySQL Workbench and connect your local DB (localhost)

* File -> Run SQL Script...

* Select the BDB-sql-2009-11-25.sql file you unzipped, and enter 'baseball' as the Default Schema Name.

* Click Run

* Once the script is done running, click on the small refresh icon next to SCHEMAS on the left sidebar of MySQL Workbench.  You should now see the baseball schema (database), complete with all its tables.

##Queries
Use the appropriate SQL queries to find answers to the following questions:

1. Find all of the Triple Crown (Award) winners ever in Major League Baseball, with their complete batting stats for the given year.  Order the results in descending order first by batting average, then by RBIs, and lastly by home runs.
2. Calculate the number of MVPs and Triple Crown winners by position ever in major league baseball.
3. Calculate the number of MVPs and Triple Crown winners by team ever in major league baseball.
4. Calculate the average batting average, RBIs, and home runs by position ever in major league baseball.  Only consider seasons where a player had at least 300 at-bats (AB).
5. Return all player info for all players that won an MVP and a Gold Glove during their careers, along with the number of times they won each.
6. Calculate the number of world series, division titles, and league championships for all teams.
7. Calculate the average salary (as a percentage of yearly average) of all MVPs ever in major league baseball.
8. Use the statistics available at [Baseball-Reference](http://www.baseball-reference.com/players/c/cabremi01.shtml) to add Miguel Cabrera's 2012 Triple Crown season to your Database.  Make sure to add the appropriate information to all relevant tables.

Try to solve as many of these problems as you can.  Some might be quite complex, feel free to stop if you feel that you have a good handle on SQL.

**Submit:**  
1. Your queries  
2. Your results (truncated is fine for large resultsets)  
3. A screenshot of your DB tables on either the command line or in MySQL Workbench

Requirement: Design a datawarehouse to store data about all the songs being played by different users. The idea is to make the data avilable for analysis.

Solution:

1. Create a datawarehouse with 4 dimension tables and a fact table:
    users - user dimension and its attributes
    songs - song dimension and its attributes
    artists - artist dimension and its attributes
    time - time dimension and its attributes
    songplays - fact table with all songs played on the system along with links to the different dimensions
    
2. Insert data into the datawarehouse

The solution contain the following files:

1. sql_queries.py: contains all the sql queries required to drop and create the database objects and the insert queries to insert data into the tables.
2. create_tables.py: contains functions to create the 'sparkify' database and create the fact and dimension tables.
3. etl.py: Parse the json files and insert data into the tables in the datawarehouse.
4. test.py: Connect the database and query the tables have been populated as expected.

Steps:

1. Open a new jupyter notebook file.
2. execute the below statement to create the database objects:
    %run create_tables.py
2. execute the below statment to populate the data warehouse:
    %run etl.py
3. Finally, confirm that the data has been populated as required by running the different statements in 'test.ipynb'

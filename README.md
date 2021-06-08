# BanksInfo
Fyle Project
In this web App,Information of Banks from different cities all over the India will be given.

I have used PostgreSQL to store the data,which is addon in clevercloud 

The interface will look like this.


We have to select City and No.Of rows to Display.


After selecting these,Available banks will display.



If we want to search any bank among the obtained list,we can search in search bar.




If there are no banks are in the selected city,then it will show  a popup.


In the data base I have used one Schema with attributes ifsc,Bank Id,Branch,	Address,	City,	District,State,Bank Name.

Going to Apis,Created a REST Api using python flask.

# Part1:

Endpoints:https://fyle-banks-info-syam.herokuapp.com/api/branches/autocomplete?q=<>
Example1:https://fyle-banks-info-syam.herokuapp.com/api/branches/autocomplete/KAMAVARAPUKOTA/3/0

This Autocomplete API returns possible matches based on the branch name ordered by IFSC code (ascending order) with limit and offset.


This Search API returns possible matches across all columns and all rows, **ordered by IFSC code** (ascending order) with limit and offset.

1. Endpoint: https://fyle-banks-info-syam.herokuapp.com/api/branches?q=<>**
2. Example: https://fyle-banks-info-syam.herokuapp.com/api/branches/KAMAVARAPUKOTA/3/0

# Part2:
Using above apis,Data wil be displayed in web App as described above.


# BanksInfo
Fyle Project
In this web App,Information of Banks from different cities all over the India will be given.

I have used PostgreSQL to store the data,which is addon in clevercloud 

The interface will look like this.

![Screenshot (379)](https://user-images.githubusercontent.com/56387441/121138175-1250e980-c855-11eb-947a-3a8bf43f23d1.png)




We have to select City and No.Of rows to Display.

![Screenshot (380)](https://user-images.githubusercontent.com/56387441/121138189-15e47080-c855-11eb-894a-948695d0c6b5.png)
![Screenshot (381)](https://user-images.githubusercontent.com/56387441/121138216-1bda5180-c855-11eb-89bd-48e6fc51cf35.png)
After selecting these,Available banks will display.

![Screenshot (382)](https://user-images.githubusercontent.com/56387441/121138227-1da41500-c855-11eb-9d24-3792777b0292.png)

If we want to search any bank among the obtained list,we can search in search bar.


![Screenshot (383)](https://user-images.githubusercontent.com/56387441/121138255-21379c00-c855-11eb-945b-56921d6dcfdc.png)

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


# BanksInfo
Fyle Project
In this web App,Information of Banks from different cities all over the India will be given.

I have used PostgreSQL to store the data,which is addon in clevercloud 

The interface will look like this.

![Screenshot (379)](https://user-images.githubusercontent.com/56387441/121132913-5b05a400-c84f-11eb-9e7c-412d6c4216bc.png)
We have to select City and No.Of rows to Display.
![Screenshot (380)](https://user-images.githubusercontent.com/56387441/121132969-69ec5680-c84f-11eb-9028-90a48d497379.png)
![Screenshot (383)](https://user-images.githubusercontent.com/56387441/121133100-9011f680-c84f-11eb-81b8-11704a5c81bc.png)


After selecting these,Available banks will display.

![Screenshot (382)](https://user-images.githubusercontent.com/56387441/121133075-87212500-c84f-11eb-813e-9dfda0c678ab.png)

If we want to search any bank among the obtained list,we can search in search bar.
![Screenshot (381)](https://user-images.githubusercontent.com/56387441/121133021-7a043600-c84f-11eb-9176-0a4ab223e760.png)




If there are no banks are in the selected city,then it will show  a popup.
![Screenshot (386)](https://user-images.githubusercontent.com/56387441/121133192-acae2e80-c84f-11eb-9bcd-5f758ff0bea5.png)

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


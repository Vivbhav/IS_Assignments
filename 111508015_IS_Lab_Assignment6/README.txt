For installation :

1) Import the database.sql:
    mysql -uroot -ppassword < database.sql

2) Enter your database username and password in connection.php file

3) Run 127.0.0.1/sqlinject/index.html in your browser

Test Cases :

1) Correct Username and password :
    Username = vivek
    Password = bhave
    Output - login successful

2) Incorrect Username or password :
    Username = chinmay
    Password = bahu
    Output - login failed! Incorrect username or password

3) Sql injection attack where in one gives wrong username and password but still is able to login:
    Username = xxx@xxx.xxx' OR 1 = 1 LIMIT 1 -- ' ]
    Password = 12345
    Output - Login successful

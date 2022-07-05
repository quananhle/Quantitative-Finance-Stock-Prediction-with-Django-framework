# Import Records to Database

## Table of Contents

* [Getting Spreadsheet from Wall Street Journal](#getting-spreadsheet-from-wall-street-journal)
* [Connect Excel to PostgreSQL in DBeaver](#connect-excel-to-postgresql-in-dbeaver)
  * [Create CSV Database Connection](#create-csv-database-connection)
  * [Data Export](#data-export)

## Getting Spreadsheet from Wall Street Journal

[<img src="https://user-images.githubusercontent.com/35042430/177369081-9f049753-d198-45ab-94f5-135b826d082e.png">](https://www.wsj.com/market-data/quotes/AAPL/historical-prices)

Select the date range and click on DOWNLOAD A SPREADSHEET

![image](https://user-images.githubusercontent.com/35042430/177370774-31b3a909-7cab-4e57-af28-62402eb0c5d0.png)

Format the cells to match datatype in table

![image](https://user-images.githubusercontent.com/35042430/177371235-55ace394-4ea7-4fa4-bb18-a60cb39c2b91.png)
![image](https://user-images.githubusercontent.com/35042430/177371397-2ba63b90-c80a-4b55-b8c7-afeb5cd6ab5a.png)
![image](https://user-images.githubusercontent.com/35042430/177371315-ccbd95a4-a51f-499e-a439-1e77875d9038.png)

## Connect Excel to PostgreSQL in DBeaver

### Create CSV Database Connection

Select _Connect to a database_ and type _CSV_

![image](https://user-images.githubusercontent.com/35042430/177372681-0bd1c76c-60bb-4010-81b9-0c80a8f1130d.png)

Select _PATH_ to the folder where the spreadsheets located the press _FINISH_ button

![image](https://user-images.githubusercontent.com/35042430/177372862-b5dd955b-c4a6-4f04-b270-e031aaaaba11.png)

After the connection has been created, check the records

![image](https://user-images.githubusercontent.com/35042430/177373131-687a04dc-b1ac-458e-84f2-6d423fdfd696.png)

### Data Export

![image](https://lh5.googleusercontent.com/mlBgUjczKXWQfYkBJozDJrGj2DBQ0_TP4rvWZCZGQD7gfNArenz2d_CeHqyV7lfAOGhA08L9VrwMI1ogaWxPZY17flGbn3_rXL2oTumqWHfyBsF9qTg4z-KxQF7uWYeXBmur7kJV)

Select database and press _Next_

![image](https://user-images.githubusercontent.com/35042430/177373998-a6d4c8e2-e384-443e-9ec2-ca3bba354342.png)

Press _Choose ..._ to select the database, and press _Browse ..._ to select the table to export the data

![image](https://user-images.githubusercontent.com/35042430/177374112-3ced9fe1-fdf5-4bd0-a86d-ea938b7fab4b.png)

![image](https://user-images.githubusercontent.com/35042430/177374433-9df58ea2-5a17-4cd0-8e38-7bd466133b79.png)

Change Target Type to match the datatype of the destination table

![image](https://user-images.githubusercontent.com/35042430/177374933-8ba93945-b9f7-4fbf-be5c-38deb1ccf17f.png)

![image](https://user-images.githubusercontent.com/35042430/177371094-453c4781-8bc4-436d-aea9-10f837d2c7f2.png)

Press _Next_. Deselect the option for truncating the target table if you only want to add data to the table rather than rewriting it and press _Proceed_

![image](https://user-images.githubusercontent.com/35042430/177374608-3b79a76b-82ec-498b-8560-f90e7a0224f5.png)




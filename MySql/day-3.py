mysql> create table employee(
    -> empid char(5),
    -> fname varchar(100),
    -> lname varchar(70),
    -> age int,
    -> doj date,
    -> address tinytext,
    -> dept varchar(20)
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql> show tables;
+----------------+
| Tables_in_pfs6 |
+----------------+
| employee       |
+----------------+
1 row in set (0.00 sec)

mysql> desc employees;
ERROR 1146 (42S02): Table 'pfs6.employees' doesn't exist
mysql> desc employee;
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| empid   | char(5)      | YES  |     | NULL    |       |
| fname   | varchar(100) | YES  |     | NULL    |       |
| lname   | varchar(70)  | YES  |     | NULL    |       |
| age     | int          | YES  |     | NULL    |       |
| doj     | date         | YES  |     | NULL    |       |
| address | tinytext     | YES  |     | NULL    |       |
| dept    | varchar(20)  | YES  |     | NULL    |       |
+---------+--------------+------+-----+---------+-------+
7 rows in set (0.00 sec)

mysql> show columns from employees;
ERROR 1146 (42S02): Table 'pfs6.employees' doesn't exist
mysql> show columns from employee;
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| empid   | char(5)      | YES  |     | NULL    |       |
| fname   | varchar(100) | YES  |     | NULL    |       |
| lname   | varchar(70)  | YES  |     | NULL    |       |
| age     | int          | YES  |     | NULL    |       |
| doj     | date         | YES  |     | NULL    |       |
| address | tinytext     | YES  |     | NULL    |       |
| dept    | varchar(20)  | YES  |     | NULL    |       |
+---------+--------------+------+-----+---------+-------+
7 rows in set (0.00 sec)

mysql> -- modify the fname column in employees table to varchar(70)
mysql> --syntax: alter table table_name modify column_name datatype size
    -> ^C
mysql> alter table employee modify fname varchar(70);
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> show columns from employee;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| empid   | char(5)     | YES  |     | NULL    |       |
| fname   | varchar(70) | YES  |     | NULL    |       |
| lname   | varchar(70) | YES  |     | NULL    |       |
| age     | int         | YES  |     | NULL    |       |
| doj     | date        | YES  |     | NULL    |       |
| address | tinytext    | YES  |     | NULL    |       |
| dept    | varchar(20) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
7 rows in set (0.00 sec)

mysql> -- add a new column names with location to employees table
mysql> -- syntax: alter table table-name add acolumn-name datatype(size);
mysql> alter table employee add location tinytext;
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> show columns from employee;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| empid    | char(5)     | YES  |     | NULL    |       |
| fname    | varchar(70) | YES  |     | NULL    |       |
| lname    | varchar(70) | YES  |     | NULL    |       |
| age      | int         | YES  |     | NULL    |       |
| doj      | date        | YES  |     | NULL    |       |
| address  | tinytext    | YES  |     | NULL    |       |
| dept     | varchar(20) | YES  |     | NULL    |       |
| location | tinytext    | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
8 rows in set (0.00 sec)

mysql> alter table employee add location tinytext after lname;
ERROR 1060 (42S21): Duplicate column name 'location'
mysql> alter table employee modify column location tinytext after lname;
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> show columns from employee;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| empid    | char(5)     | YES  |     | NULL    |       |
| fname    | varchar(70) | YES  |     | NULL    |       |
| lname    | varchar(70) | YES  |     | NULL    |       |
| location | tinytext    | YES  |     | NULL    |       |
| age      | int         | YES  |     | NULL    |       |
| doj      | date        | YES  |     | NULL    |       |
| address  | tinytext    | YES  |     | NULL    |       |
| dept     | varchar(20) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
8 rows in set (0.00 sec)

mysql> alter table employee add pfid int after address;
Query OK, 0 rows affected (0.03 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> show columns from employee;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| empid    | char(5)     | YES  |     | NULL    |       |
| fname    | varchar(70) | YES  |     | NULL    |       |
| lname    | varchar(70) | YES  |     | NULL    |       |
| location | tinytext    | YES  |     | NULL    |       |
| age      | int         | YES  |     | NULL    |       |
| doj      | date        | YES  |     | NULL    |       |
| address  | tinytext    | YES  |     | NULL    |       |
| pfid     | int         | YES  |     | NULL    |       |
| dept     | varchar(20) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
9 rows in set (0.00 sec)

mysql> -- how to rename the column name
mysql> -- syntax : alter table table-name change existing colunm-name new column-name datatyp(size);
mysql> alter table employee change fname firstnam varchar(50);
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> show columns from employee;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| empid    | char(5)     | YES  |     | NULL    |       |
| firstnam | varchar(50) | YES  |     | NULL    |       |
| lname    | varchar(70) | YES  |     | NULL    |       |
| location | tinytext    | YES  |     | NULL    |       |
| age      | int         | YES  |     | NULL    |       |
| doj      | date        | YES  |     | NULL    |       |
| address  | tinytext    | YES  |     | NULL    |       |
| pfid     | int         | YES  |     | NULL    |       |
| dept     | varchar(20) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
9 rows in set (0.00 sec)

mysql> alter table employee change lname lastname varchar(30);
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> show columns from employee;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| empid    | char(5)     | YES  |     | NULL    |       |
| firstnam | varchar(50) | YES  |     | NULL    |       |
| lastname | varchar(30) | YES  |     | NULL    |       |
| location | tinytext    | YES  |     | NULL    |       |
| age      | int         | YES  |     | NULL    |       |
| doj      | date        | YES  |     | NULL    |       |
| address  | tinytext    | YES  |     | NULL    |       |
| pfid     | int         | YES  |     | NULL    |       |
| dept     | varchar(20) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
9 rows in set (0.00 sec)

mysql> desc employee;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| empid    | char(5)     | YES  |     | NULL    |       |
| firstnam | varchar(50) | YES  |     | NULL    |       |
| lastname | varchar(30) | YES  |     | NULL    |       |
| location | tinytext    | YES  |     | NULL    |       |
| age      | int         | YES  |     | NULL    |       |
| doj      | date        | YES  |     | NULL    |       |
| address  | tinytext    | YES  |     | NULL    |       |
| pfid     | int         | YES  |     | NULL    |       |
| dept     | varchar(20) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
9 rows in set (0.00 sec)

mysql> alter table employee change doj date_of_joining data;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'data' at line 1
mysql> alter table employee change doj date_of_joining date;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc employee;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| empid           | char(5)     | YES  |     | NULL    |       |
| firstnam        | varchar(50) | YES  |     | NULL    |       |
| lastname        | varchar(30) | YES  |     | NULL    |       |
| location        | tinytext    | YES  |     | NULL    |       |
| age             | int         | YES  |     | NULL    |       |
| date_of_joining | date        | YES  |     | NULL    |       |
| address         | tinytext    | YES  |     | NULL    |       |
| pfid            | int         | YES  |     | NULL    |       |
| dept            | varchar(20) | YES  |     | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
9 rows in set (0.00 sec)

mysql> -- how to drop column
mysql> -- syntax: alter table table-name drop column-name column-name
mysql> alter table employee drop column location;
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc employee;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| empid           | char(5)     | YES  |     | NULL    |       |
| firstnam        | varchar(50) | YES  |     | NULL    |       |
| lastname        | varchar(30) | YES  |     | NULL    |       |
| age             | int         | YES  |     | NULL    |       |
| date_of_joining | date        | YES  |     | NULL    |       |
| address         | tinytext    | YES  |     | NULL    |       |
| pfid            | int         | YES  |     | NULL    |       |
| dept            | varchar(20) | YES  |     | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
8 rows in set (0.00 sec)

mysql> alter table employee drop column pfid;
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc employee;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| empid           | char(5)     | YES  |     | NULL    |       |
| firstnam        | varchar(50) | YES  |     | NULL    |       |
| lastname        | varchar(30) | YES  |     | NULL    |       |
| age             | int         | YES  |     | NULL    |       |
| date_of_joining | date        | YES  |     | NULL    |       |
| address         | tinytext    | YES  |     | NULL    |       |
| dept            | varchar(20) | YES  |     | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
7 rows in set (0.00 sec)

mysql> desc employee;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| firstnam        | varchar(50) | YES  |     | NULL    |       |
| lastname        | varchar(30) | YES  |     | NULL    |       |
| age             | int         | YES  |     | NULL    |       |
| date_of_joining | date        | YES  |     | NULL    |       |
| address         | tinytext    | YES  |     | NULL    |       |
| dept            | varchar(20) | YES  |     | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
6 rows in set (0.00 sec)

mysql> -- HOW TO CHANGE TABLE-NAME
mysql> -- SYNTAX: ALTER TABLE -NAME RENAME TO NEW-TABLE-NAME
mysql> ALTER TABLE EMPLOYEE RENAME CODEGNAN_EMP;
Query OK, 0 rows affected (0.02 sec)

mysql> desc employee;
ERROR 1146 (42S02): Table 'pfs6.employee' doesn't exist
mysql> USE PFS6;
Database changed
mysql> desc employee;
ERROR 1146 (42S02): Table 'pfs6.employee' doesn't exist
mysql> desc codegnan_emp;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| firstnam        | varchar(50) | YES  |     | NULL    |       |
| lastname        | varchar(30) | YES  |     | NULL    |       |
| age             | int         | YES  |     | NULL    |       |
| date_of_joining | date        | YES  |     | NULL    |       |
| address         | tinytext    | YES  |     | NULL    |       |
| dept            | varchar(20) | YES  |     | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
6 rows in set (0.00 sec)

mysql> alter table codegnan_emp rename to employee;
Query OK, 0 rows affected (0.02 sec)

mysql> desc employee;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| firstnam        | varchar(50) | YES  |     | NULL    |       |
| lastname        | varchar(30) | YES  |     | NULL    |       |
| age             | int         | YES  |     | NULL    |       |
| date_of_joining | date        | YES  |     | NULL    |       |
| address         | tinytext    | YES  |     | NULL    |       |
| dept            | varchar(20) | YES  |     | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
6 rows in set (0.00 sec)

mysql> show tables;
+----------------+
| Tables_in_pfs6 |
+----------------+
| employee       |
+----------------+
1 row in set (0.00 sec)

mysql> drop table employee;
Query OK, 0 rows affected (0.02 sec)

mysql> show tables;
Empty set (0.00 sec)


# Data project

## High level architecture of the application :

![architecture](https://lh3.googleusercontent.com/-uCArmETipy8/YB3oJmxnzZI/AAAAAAAACGg/Qhz2f8wmlEEai1bZHskCknrGHz5Wld-KgCK8BGAsYHg/s0/2021-02-05.jpg)

## Data engineering : 
### Clone Repository
Open a terminal window and run :
```bash
git clone https://github.com/idwy/csv2sql.git
cd csv2sql
```
### Build/Run Docker : 
```bash
docker-compose build
docker-compose up mysql
```
In a second terminal, run inside the repo directory the following command :
```bash
docker-compose up app
```
In a third terminal we can access the mysql container and explore the data stored or in the process of being stored while app container is running :
```bash
docker exec -it csv2sql_mysql_1 bash
mysql -u root -pRootPassword 
```
Our database is named GDC, so we can explore data as following :
```bash
USE GDC;
```
```bash
SHOW TABLES;
```
```bash
Select * from ads limit 10 ;
```
```bash
Select count(*) from users ;
```
, and so on ...

## Data Analysis :
Brief data analysis is provided in `plots.ipynb` file. 
## Enhancements :  
- Unit tests 
- Integration test 
- Scaling to big data infrastructure in case of big files 
- Chunk size tuning for optimal throughput 



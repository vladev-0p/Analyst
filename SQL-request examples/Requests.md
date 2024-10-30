## SQL REQUESTS
![db](DB_scheme.png)
## 1 Task 


#### Display sorted by number of flights (descending) 
#### and name (in ascending order) a list of passengers who have completed at least 1 flight

#### Вывести отсортированный по количеству перелетов (по убыванию)
#### и имени (по возрастанию) список пассажиров, совершивших хотя бы 1 полет. 

SELECT name , COUNT(trip) as count  from Passenger <br>
INNER JOIN Pass_in_trip on <br>
   Passenger.id=Pass_in_trip.passenger <br>
GROUP by name <br>
HAVING COUNT(trip)>0 <br>
ORDER by count DESC, name ASC    <br>

## 2 Task
#### Display the names of people who have a full namesake among the passengers <br>
#### Вывести имена людей, у которых есть полный тёзка среди пассажиров <br>

SELECT name  from Passenger <br>
GROUP BY name <br>
HAVING COUNT(*)>1 <br>

## 3 Task

#### Display the passengers with the longest name. Spaces, hyphens, and periods are considered part of the name. <br>
#### Выведите пассажиров с самым длинным ФИО. Пробелы, дефисы и точки считаются частью имени. <br>
SELECT  name <br>
FROM Passenger <br>
WHERE LENGTH(name) = ( <br>
    SELECT MAX(LENGTH(name))  <br>
    FROM Passenger <br>
) <br>
## 4 Task


#### Display flights made from 10 a.m. to 2 p.m. January 1, 1900<br>
#### Вывести вылеты, совершенные с 10 ч. по 14 ч. 1 января 1900 г<br>

SELECT * from Trip <br>
WHERE time_OUT BETWEEN STR_TO_DATE('1900-01-01 10:00:00','%Y-%m-%d %H:%i:%s') <br>
                       AND  <br>
                       STR_TO_DATE('1900-01-01 14:00:00','%Y-%m-%d %H:%i:%s') <br>

## 5 Task

##### 2 Tables:
1.	projects — с информацией о проектах: project_id, project_name, client_id.
2.	clients — с информацией о клиентах: client_id, client_name, country.
<br>
#### Display all projects that belong to clients from the country CANADA <br>
#### Вывести все проекты  , которые принадлежать клиентам из страны CANADA <br>



| WHERE IN                                                                                                   | JOIN ON                                                                                                                  |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| SELECT * FROM projects <br> WHERE client_id IN <br>( SELECT client_id FROM clients WHERE country="Canada") | SELECT * FROM projects <br> JOIN clients ON projects.client_id = clients.client_id <br> WHERE clients.country = "Canada" |


/* terminal commandes
docker cp /Users/ayumikatsuya/Desktop/cleaned_traffic_data.csv 

some-postgres:/data.csv

docker exec -it some-postgres psql -U postgres*/

-- Creating a table
CREATE TABLE traffic_data (
	Junction VARCHAR(50), 
	Left_Speed VARCHAR(255), 
	Left_Comment VARCHAR(255),
	Right_Speed VARCHAR(255),
	Right_Comment VARCHAR(255),
	Date DATE, Time TIME,
	Day_of_Week VARCHAR(15),
	Stratum VARCHAR(10),
	Left_Speed_Clean VARCHAR(255),
	Right_Speed_Clean VARCHAR(255),
	Left_Speed_Numeric DECIMAL,
	Right_Speed_Numeric DECIMAL
);

/* 
\copy traffic_data FROM '/cleaned_traffic_data.csv' DELIMITER ',' CSV HEADER;
*/

-- Verifying the data
SELECT * FROM traffic_data LIMIT 10;
# Hadoop Data Analysis using Python
_NYC Vehicular Data is analyzed using Python mapper and reducer scripts in Hadoop._

### AIM:
To display statistical summary of each vehicle type that is involved in an incident reported in NYC. 
This data is retreived from NYPD motor vehicle collisions provided by the data published by Public Security department of the New York City.

### STEPS:

#### *Downloading the data onto the local system:*

```
$hadoop fs -get /data/nyc/nyc-traffic.csv ./Data
```

#### *Mapper script:*
```
$vi mapper.py

#!/usr/bin/env python

import sys
import csv

with sys.stdin as data:
	reader = csv.reader(data, delimiter=',')
	reader.next()
	for row in reader:
		row = filter(None,row[-5:])
		for items in row:
   			print(items+"\t"+str(1))
```

#### *Reducer script:*
```
$vi reducer.py

#!/usr/bin/env python

import sys
import csv

count_word = 0
current_word = None
word = None

for line in sys.stdin:
	line = line.strip()
	word, count = line.split('\t', 1)

        count = int(count)
	if current_word == word:
		count_word += count
    	else:
        	if current_word:
            		print(current_word+"\t"+str(count_word))
        	count_word = count
        	current_word = word

if current_word == word:
    print(current_word+"\t"+str(count_word))
```

#### *Adding executable permissions to mapper and reducer scripts*
```
$chmod +x reducer.py mapper.py
```

#### *Testing on local system:*
```
$cat Data/nyc-traffic.csv | python mapper.py | sort -k1,1 | python reducer.py
```

#### *Running Hadoop job with mapper and reducer:*
```
$`hadoop jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.3.0-235.jar -file /home/bundeyyn/HW4_Hadoop_DataAnalysis/mapper.py -mapper /home/bundeyyn/HW4_Hadoop_DataAnalysis/mapper.py -file /home/bundeyyn/HW4_Hadoop_DataAnalysis/reducer.py -reducer /home/bundeyyn/HW4_Hadoop_DataAnalysis/reducer.py -input /data/nyc/nyc-traffic.csv -output /user/bundeyyn/out`
```

#### *Copying output to local folder*
```
$hadoop fs -get /user/bundeyyn/out/* /home/bundeyyn/HW4_Hadoop_DataAnalysis/Hadoop_Output
```

#### *Statistical Summary Output:*
```
$cat part-00000

AMBULANCE	3713
BICYCLE	24153
BUS	25871
FIRE TRUCK	1333
LARGE COM VEH(6 OR MORE TIRES)	27981
LIVERY VEHICLE	17775
MOTORCYCLE	10029
OTHER	51360
PASSENGER VEHICLE	1005162
PEDICAB	123
PICK-UP TRUCK	26281
SCOOTER	534
SMALL COM VEH(4 TIRES)	30048
SPORT UTILITY / STATION WAGON	363209
TAXI	63892
UNKNOWN	105481
VAN	51666
```

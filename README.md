# 2021 Spring finals
Title: Strategy of Pit stops on race result of Formula one
<br>
Project Type: Type II Projects <br>
Team Member: Ko-Mei Lin, Yi-Shiuan Ho
![](https://i.imgur.com/NQQ9SNx.jpg)

## Overview & Background
Pit stops are one of the most tense and exciting features of formula one race. During F1 races, cars stop in pit stalls for maintenance and adjustments. In this project, we would like to find out how different strategies affect results in Formula One. 

## Data Source
All information on the Formula 1 races, drivers, constructors, qualifying, circuits, lap times, pit stops, championships from 1950 - 2020
* https://www.kaggle.com/rohanrao/formula-1-world-championship-1950-2020
* https://ergast.com/mrd/

## Hypothesis1
### Less pit stops gives the driver better rank in each race
The following boxplot shows race result of different amount of pit stop. For taking pitstops between 1 to 3, we can see that taking more stops usually brings driver a lower position. However, if we look at results for taking over 3 pit stops, there are no evidence supporing lower pitstops gives driver better position.<br>
![](https://i.imgur.com/3y3dbGK.png)<br>
The below plot shows the number of times of positions for taking 1, 2 and 3 pit stops. In this plot, we can see there are more drivers ending in higher positions when taking two pit stops, however this is because we are using the number of times instead of percentage of position. Since there are more records for taking two pit stops, the number of times for each position could be higher too. <br>
If we look at the lines in this plot seperately, we can see that drivers choosing to take 1 pit stop (blue line) are more likely to end up with a higher position. This observation can also be made if we look at data for taking two pit stops (orange line). However, if we look at drivers taking 3 pit stops (green line), there are no strong relationship between position and pit stops.<br> 
![](https://i.imgur.com/Ta9c6J1.png)<br>
With the two diagrams, there are no sufficient evidence to support our hypothesis. Therefore, we reject hypothesis1.

## Hypothesis2
### Laps of the each pit stop times should be similar for better tire usage.
(1) 1 pit stop
![](https://i.imgur.com/tVylgvX.png)

From the plot above, we could see that if the team chooses only pit stop once in the total race, then they tend to pit during the half the race. 

(2) 2 pit stops
![](https://i.imgur.com/60EDwaN.png)
From the plot above, we could see that if the team chooses to pit stop twice in the total race, most of the teams will choose to pit during the 0.2~0.3 total race laps at the first time, which is pretty close to 1/3. Furthermore, the second time pit tends to be happened aroung 0.6 of total race laps, which is also very close to 2/3.

(3) 3 and 4 pit stops
![](https://i.imgur.com/Eyi7nFY.png)
![](https://i.imgur.com/nyP031l.png)

If we see the plot 3 and 4 pit stops, they both have a peak in the beginning of the race. This might because in the beginning of the race, drivers will fight for the leading position and there might be some collisions between them. But since these data are already filtered as finished race. It means, even they have collision, they just need to pit and back to the race again. But we don’t think we could say they have significant difference when they need to pit stop. 

We don't have strong evidence to reject the hypothesis 2 when the team pit stop times smaller than 3 times, since the plots show that most of the pit stop timing are average based on total pit times.
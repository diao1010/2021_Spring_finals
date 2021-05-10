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
The following boxplot shows race result of different amount of pit stop. As we can see, taking 1 pit stop usually gives the driver a position around 7, and it goes around 9, 11, 10, 9 when the pit stop gets more. For taking pitstops between 1 to 3, we can see that taking more stops usually brings driver a lower position. However, if we look at results for taking over 3 pit stops, there are no evidence supporting lower pitstops gives driver better position.<br>
![](https://i.imgur.com/3y3dbGK.png)<br>
The next three bar charts show the count of positions in history records when taking 1, 2 or 3 pit stops:
![](https://i.imgur.com/qMNwRYD.png)
In these three bar charts, we can see drivers choosing to take 1 pit stop are more likely to end up with a higher position. This observation can also be made if we look at data for taking 2 and 3 pit stops.
<br> 
Although this result supports our hypothesis, we still want to rule out other facts that may affect race positions such as circuits. In the following table, we can see the count of positions in a given pit stop amount and circuit. These circuits that are chosen to hold f1 races every year during the past decade.
![](https://i.imgur.com/Z3jyBY8.png)<br>
In this table, we can see that it is more likely that a driver gets a higher position if he takes less pit stop. Therfore, there is sufficient evidence to support hypothesis1.

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

Result for Hypothesis2:
When pit stop times <=2: We don't have strong evidence to reject the hypothesis 2, since the plots show that most of the pit stop timing are average based on total pit times. 
But for pit stop times >= 3, we could reject it since there’s no significant evidence showed the result we expected

# Further analysis
Get the tire data, everytime the team using different types of tires. 
For example, hard tyre could run for more laps during the race so the team could use hard tyre for one pit stop, but we don’t have the dataset about tire so we couldn’t test our hypothesis. 
And the pit stop time data could also help us to see if the time significantly affect the result.

# Contribution
* Ko-Mei Lin<br>
complete functions, doctests and plot for hypothesis2
* Yi-Shiuan Ho<br>
complete functions, doctests and plot for hypothesis1

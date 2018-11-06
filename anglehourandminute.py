#this program calculates the angle between the hour hand and the minute hand for a given time


def angle(time):
    mark=0
    l = len(time)
    for i in range (len(time)):
        if time[i] == ":":
            mark=i
            break
    mins_t = int(time[mark+1:l])
    hour_t = int(time[0:mark])%12
        
    mins = 360/60* mins_t
    hour= 30* (hour_t + mins_t/60)
    
    return min(abs(hour-mins), (360-abs(hour-mins)))


print(angle("3:10"))
    

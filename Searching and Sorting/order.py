def minTime(machines, goal):
    day=1
    count=0
    d={}
    for i in machines:
        d[i]=d.get(i,0)+1
    print(d)
    while goal>0:
        production=0
        for key in d:
            if day%key==0:
                production=production+d[key]
                print(day,production)
        day=day+1
        count=count+production
        #print(day,count)
        goal=goal-production
    return day-1

machines=[2,3]
goal=5
print(minTime(machines,goal))

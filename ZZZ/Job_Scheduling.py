def maxProfit(ar):
	n=len(ar)
	total_jobs=0
	max_profit=0
	ar=sorted(ar,key=lambda x:x[1])
	m=0
	for i in range(n):
	    m=max(m,ar[i][0])
	ar=ar[::-1]
	#print(ar)
	t=[0]*m
	
	i=0
	while i<n:
		ind=ar[i][0]-1
		while ind>=0:
			if t[ind]==0:
				t[ind]=max(t[ind],ar[i][1])
				i=i+1
				break
			else:
				ind=ind-1
		if ind<0:
			i=i+1

	for i in t:
		if i!=0:
			max_profit+=i
			total_jobs+=1

	return [total_jobs,max_profit]


ar=[[1,100],[1,25],[2,27],[3,19],[3,15]]
ans=maxProfit(ar)
print(ans)
#############
'''class Job:
	def __init__(self, start, finish, profit):
		self.start = start
		self.finish = finish
		self.profit = profit

def binarySearch(job, start_index):
	lo = 0
	hi = start_index - 1
	while lo <= hi:
		mid = (lo + hi) // 2
		if job[mid].finish <= job[start_index].start:
			if job[mid + 1].finish <= job[start_index].start:
				lo = mid + 1
			else:
				return mid
		else:
			hi = mid - 1
	return -1

def schedule(job):
	job = sorted(job, key = lambda j: j.finish)
	n = len(job)
	table = [0 for i in range(n)]
	table[0] = job[0].profit;

    #rem[0]=True
	for i in range(1, n):
		inclProf = job[i].profit
		l = binarySearch(job, i)
		if (l != -1):
			inclProf += table[l];

		# Store maximum of including and excluding
		table[i] = max(inclProf, table[i - 1])

	return table[n-1]

def LeftProfit(start_time,end_time,cost):
    job=[]
    for i in range(0,len(start_time)):
        job.append(Job(start_time[i],end_time[i],cost[i]))
    profit=schedule(job)
    print(profit)
    rem_profit=sum(cost)-profit
    #return [2,rem_profit]
    return rem_profit



###############################################
start_time=[1,3,6,2]
end_time=[2,5,19,100]
cost=[50,20,100,200]

print(LeftProfit(start_time,end_time,cost))
#job = [Job(1, 2, 50), Job(3, 5, 20),
#	Job(6, 19, 100), Job(2, 100, 200)]'''

def FCFS(arrival_time,burst_time):
    n=len(arrival_time)
    d={}
    for i in range(len(arrival_time)):
        d[i]=[arrival_time[i],burst_time[i]]
            
    d = dict(sorted(d.items(), key=lambda item: item[1][0]))
    CT=0
    TAT=0
    WT=0
    for i in d:
        CT += d[i][1]
        TAT += CT-d[i][0]
        WT = TAT-CT
    order=list(d.keys())
    return (WT/n,TAT/n,order)


def SJS(arrival_time, burst_time):
    WT = [0] * len(arrival_time)
    TAT = [0] * len(arrival_time)
    n = len(arrival_time)
    completed = [False] * n
    total_time = 0
    remaining_bt = burst_time.copy()
    order=[]
    while True:
        min_bt = float('inf')
        shortest = -1
        for i in range(n):
            if not completed[i] and arrival_time[i] <= total_time and remaining_bt[i] < min_bt:
                min_bt = remaining_bt[i]
                shortest = i
        if shortest == -1:
            break
        completed[shortest] = True
        total_time += burst_time[shortest]
        WT[shortest] = total_time - arrival_time[shortest] - burst_time[shortest]
        TAT[shortest] = WT[shortest] + burst_time[shortest]
        order.append(shortest)
    return (sum(WT)/n, sum(TAT)/n,order)


def PS(arrival_time, burst_time, priority):
    n = len(arrival_time)
    WT = [0] * n
    TAT = [0] * n
    order=[]
    processes = [(i, arrival_time[i], burst_time[i], priority[i]) for i in range(n)]
    processes.sort(key=lambda x: x[3],reverse=True)
    total_time = 0
    for i in range(n):
        process_id, at, bt, _ = processes[i]
        if at > total_time:
            total_time = at
        WT[process_id] = total_time - at
        total_time += bt
        TAT[process_id] = WT[process_id] + bt
        order.append(process_id)
    return (sum(WT)/n, sum(TAT)/n, order)


def RR(arrival_time, burst_time, quantum):
    order=[]
    n = len(arrival_time)
    WT = [0] * n
    TAT = [0] * n
    remaining_bt = burst_time.copy()
    time = 0
    while any(remaining_bt):
        for i in range(n):
            if remaining_bt[i] > 0:
                if remaining_bt[i] <= quantum:
                    time += remaining_bt[i]
                    WT[i] = time - arrival_time[i] - burst_time[i]
                    remaining_bt[i] = 0
                else:
                    time += quantum
                    remaining_bt[i] -= quantum
                TAT[i] = WT[i] + burst_time[i]
                order.append(i)
    return (sum(WT)/n,sum(TAT)/n,order)


arrival_time = [0,10,15,20]
burst_time = [30,20,40,15]
priority = [3,5,2,4]

print(FCFS(arrival_time,burst_time))
print(SJS(arrival_time,burst_time))
print(PS(arrival_time,burst_time,priority))
print(RR(arrival_time,burst_time,4))
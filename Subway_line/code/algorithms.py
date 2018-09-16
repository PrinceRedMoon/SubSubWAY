def shortestdistance_path(station_net,start,end,lc_list):                       #dijkstra
    dis={}
    INFINITE=1000000
    visited=[start,]
    path=[start,]
    current_distance=0
    current_station=start
    judge_station=""
    judge_path=[]
    for a in station_net.station_list.keys():
        if(a==start):
            dis.update({a:[0,[]]})
        else:
            dis.update({a:[INFINITE,[]]})
    if lc_list!=0:
        for a in station_net.station_list.keys():
            flag = 0
            for b in station_net.station_list[a].s_line:
                if b in lc_list:
                    flag=1
            if flag==0:
                visited.append(a)

    while visited.__len__()!=station_net.station_list.keys().__len__():
        for station in station_net.station_list[current_station].get_neighbor():
            if station in visited:
                continue
            else:
                distance=int(station_net.station_list[current_station].adj[station][-2])
                if (current_distance+distance)<dis[station][-2]:
                    dis[station][-2]=current_distance+distance
                    t_path=path.copy()
                    t_path.append(station)
                    dis[station][-1]=t_path
        judge_distance=INFINITE
        for station in dis.keys():
            if station not in visited:
                if judge_distance>dis[station][-2]:
                    judge_distance=dis[station][-2]
                    judge_station=station
                    judge_path=dis[station][-1]
        path=judge_path
        current_distance=judge_distance
        current_station=judge_station
        visited.append(current_station)
    result=dis[end][-1].copy()
    result.append(dis[end][-2])
    return result

def otherONE_path(station_net,start,end):
    if start==end :
        return False
    visited=[start,]
    list1=[[start,"",-1,1]]
    while list1:
        path1 = list1.pop(0)
        current=path1[-4]
        current_line=path1[-3]
        changetimes=path1[-2]
        current_stationcount=path1[-1]
        if current == end:
            return path1
        for station in station_net.station_list[current].get_neighbor():
            next_line=station_net.station_list[current].adj[station][-1]
            if station not in visited:
                stationcount = current_stationcount
                stationcount += 1
                if (current=="四惠东"and station=="四惠")or (current=="四惠" and station=="四惠东"):
                    changecount = changetimes
                    path2 = path1[:-3] + [station, current_line, changecount,stationcount]
                else:
                    changecount = changetimes
                    if  current_line != next_line:
                        changecount+=1
                        path2 = path1[:-3] + [station,next_line, changecount,stationcount]
                    else:
                        path2=path1[:-3]+[station, current_line, changecount,stationcount]
                list1.append(path2)
                list1.sort(key=lambda path:path[-1])
                list1.sort(key=lambda path:path[-2])
                visited.append(station)
    return



def otherTWO_path(station_net,start,end):
    if start==end :
        return False
    visited=[start,]
    list1=[[start,1]]
    while list1:
        path1 = list1.pop(0)
        current=path1[-2]
        current_stationcount=path1[-1]
        if current == end:
            return path1
        for station  in station_net.station_list[current].get_neighbor():
            if station not in visited:
                stationcount=current_stationcount
                stationcount+=1
                path2 = path1[:-1] + [station,stationcount]
                list1.append(path2)
                list1.sort(key=lambda path:path[-1])
                visited.append(station)
    return

def fifth_path(station_net,start,end):
    if start==end :
        return False
    visited=[start,]
    list1=[[start,"",-1,1]]
    list2=[]
    countsum=0
    countbreak=0

    while list1:
        path1 = list1.pop(0)
        current=path1[-4]
        current_line=path1[-3]
        changetimes=path1[-2]
        current_stationcount=path1[-1]

        visited=path1.copy()
        dl=visited[-1]
        visited.remove(dl)
        dl=visited[-1]
        visited.remove(dl)

        if current == end:
            list2.append(path1)
            countsum+=1
            if countsum==3:
                return list2
        if countbreak==400:
            return False
        for station in station_net.station_list[current].get_neighbor():
            next_line=station_net.station_list[current].adj[station][-1]
            if station not in visited:
                stationcount = current_stationcount
                stationcount += 1
                if (current=="四惠东"and station=="四惠")or (current=="四惠" and station=="四惠东"):
                    changecount = changetimes
                    path2 = path1[:-3] + [station, current_line, changecount,stationcount]
                else:
                    changecount = changetimes
                    if  current_line != next_line:
                        changecount+=1
                        path2 = path1[:-3] + [station,next_line, changecount,stationcount]
                    else:
                        path2=path1[:-3]+[station, current_line, changecount,stationcount]
                list1.append(path2)
                list1.sort(key=lambda path:path[-1])
                list1.sort(key=lambda path:path[-2])
        countbreak+=1
    return

def sixth_path(station_net,start,end):
    visited=[]
    list1=[[start,]]
    while list1:
        current_path = list1.pop(0)
        current=current_path[-1]
        for station in station_net.station_list[current].get_neighbor():
            if station not in visited:
                new_path = current_path+ [station]
                if station== end:
                    return new_path+[1]
                else:
                    list1.append(new_path)
        visited.append(current)



def otherTHREE_path(station_net,start,end):
    if  fifth_path(station_net,start,end) is False:
        return sixth_path(station_net,start,end)
    else:
        return fifth_path(station_net,start,end)

def find_line(line_list,l_start,l_end):
    if l_start==l_end :
        return [[l_start,-1]]
    visited=[l_start,]
    list1=[[l_start,0]]
    list2=[]
    flag=0
    while list1:
        path1 = list1.pop(0)
        current=path1[-2]
        changetimes=path1[-1]
        visited=path1.copy()
        dl=visited[-1]
        visited.remove(dl)
        if current == l_end:
            if flag==0:
                list2.append(path1)
                flag=changetimes
                continue
            else:
                if changetimes==flag:
                    if path1 not in list2:
                        list2.append(path1)
                        continue
                else:
                    return list2
        for line in line_list[current].get_neighbor():
            if line not in visited:
                changecount=changetimes
                changecount+=1
                path2 = path1[:-1] + [line,changecount]
                list1.append(path2)
        list1.sort(key=lambda path:path[-1])
    return list2

def linechange_list(station_net,line_list,start,end):
    r_list=[]
    if station_net.station_list[start].s_line.__len__()==1:
        l_start=station_net.station_list[start].s_line[0]
        if station_net.station_list[end].s_line.__len__()==1:
            l_end=station_net.station_list[end].s_line[0]
            for a in find_line(line_list, l_start, l_end):
                r_list.append(a)
        else:
            for l_end in station_net.station_list[end].s_line:
                for a in find_line(line_list,l_start,l_end):
                    r_list.append(a)
    else:
        if station_net.station_list[end].s_line.__len__()==1:
            l_end=station_net.station_list[end].s_line[0]
            for l_start in station_net.station_list[start].s_line:
                for a in find_line(line_list, l_start, l_end):
                    r_list.append(a)
        else:
            for l_start in station_net.station_list[start].s_line:
                for l_end in station_net.station_list[end].s_line:
                    for a in find_line(line_list, l_start, l_end):
                        r_list.append(a)
    r_list.sort(key=lambda path:path[-1])
    changetime=r_list[0][-1]
    g_list=[]
    for a in r_list:
        if a[-1]==changetime:
            g_list.append(a[:-1])
    return g_list

def shortestchange_path(station_net,start,end,line_list):
    lc_list=linechange_list(station_net,line_list,start,end)
    result_list=[]
    for a in lc_list:
        result_list.append(shortestdistance_path(station_net,start,end,a))
    result_list.sort(key=lambda path: path[-1])
    result=result_list.pop(0)
    return result









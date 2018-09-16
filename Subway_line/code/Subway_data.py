
from code.station import StaNet,Line

subway_net=StaNet()
line_list={}
pos={}
pos_label={}

def txt_in(txtname,linename):
    with open(txtname, 'r') as f:
        for data in f.readlines():
            tmp = data.strip("\n")
            s_data = data.split()
            subway_net.add_edge(s_data[0], linename, s_data[1],linename, s_data[2])

def add_station(station, adj, weight, line, x, y, label_x, label_y):
    if adj!="":
        subway_net.add_edge(station, line, adj, line, int(weight))
    else:
        subway_net.add_sta(station,line)
        adj="NULL"
        weight="NULL"
    if x!="NULL":
        pos[station]=(int(x),int(y))
        pos_label[station]=(int(label_x),int(label_y))
    with open("new_add.txt","a") as f:
        f.write(station+" "+adj+" "+weight+" "+line+" "+x+" "+y+" "+label_x+" "+label_y+"\n")

def delete_station(station):
    del subway_net.station_list[station]
    subway_net.size=subway_net.size-1
    for s in subway_net.station_list.keys():
        if station in subway_net.station_list[s].adj.keys():
            del subway_net.station_list[s].adj[station]
    with open("new_add.txt", "r") as f:
        lines = f.readlines()
    with open("new_add.txt", "w") as f_w:
        for line in lines:
            if station in line:
                continue
            f_w.write(line)

def create_linelist(subway_net,line_list):
    for station in subway_net.station_list.keys():
        line1=subway_net.station_list[station].s_line[0]
        if subway_net.station_list[station].s_line.__len__()>1:
            for line in subway_net.station_list[station].s_line:
                llist = subway_net.station_list[station].s_line.copy()
                if line not in line_list.keys():
                    line_list[line]=Line(line)
                llist.remove(line)
                for nb_line in llist:
                    if nb_line not in line_list[line].adj.keys():
                        line_list[line].add_neighbor(nb_line)
        else:
             if subway_net.station_list[station].s_line[0] not in line_list.keys():
                line_list[subway_net.station_list[station].s_line[0]]=Line(subway_net.station_list[station].s_line[0])

# def update_linelist(line_list,station,adj,line):

#坐标导入
with open("pos.txt","r") as f:
    for data in f.readlines():
        tmp=data.strip("\n")
        s_data=data.split()
        if s_data.__len__()>0:
           a=int((int(s_data[1])/600)*1000)
           b=int(600-int(s_data[2])/600*700)
           pos[s_data[0]]=(a,b)
with open("pos_label.txt","r") as f:
    for data in f.readlines():
        tmp=data.strip("\n")
        s_data=data.split()
        if s_data.__len__()>0:
           a=int((int(s_data[1])/600)*1000)
           b=int(600-int(s_data[2])/600*700)
           pos_label[s_data[0]]=(a,b)
txt_in("subwayline_one.txt","一号线")
txt_in("subwayline_two.txt","二号线")
#txt_in("subwayline_four.txt","四号线")
txt_in("subwayline_five.txt","五号线")
txt_in("subwayline_six.txt","六号线")
#txt_in("subwayline_seven.txt","七号线")
#txt_in("subwayline_eight.txt","八号线")
#txt_in("subwayline_nine.txt","九号线")
txt_in("subwayline_ten.txt","十号线")
#txt_in("subwayline_thirteen.txt","十三号线")
#txt_in("subwayline_fourteen.txt","十四号线")
#txt_in("subwayline_fifteen.txt","十五号线")
#txt_in("subwayline_batong.txt","八通线")
#txt_in("subwayline_changping.txt","昌平线")
#txt_in("subwayline_daxing.txt","大兴线")
#txt_in("subwayline_fangshan.txt","房山线")
#txt_in("subwayline_yizhuang.txt","亦庄线")
with open("new_add.txt", 'r') as f:
    for data in f.readlines():
        tmp = data.strip("\n")
        s_data = data.split()
        if s_data[0]=="新添加的站点" :
            continue
        if s_data[4]=="NULL":
            subway_net.add_edge(s_data[0], s_data[3], s_data[1], s_data[3], s_data[2])
            continue
        if s_data[1]=="NULL":
            subway_net.add_sta(s_data[0],s_data[3])
        else:
            subway_net.add_edge(s_data[0],s_data[3], s_data[1],s_data[3], s_data[2])
        pos[s_data[0]]=(int(s_data[4]),int(s_data[5]))
        pos_label[s_data[0]]=(int(s_data[6]),int(s_data[7]))

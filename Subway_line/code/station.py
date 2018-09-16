class Station:
    def __init__(self,name):
        self.s_name=name
        self.s_line=[]
        self.adj={}

    def add_neighbor(self,nbrname,weight,line):
        self.adj[nbrname]=(weight,line)

    def add_line(self,line):
        self.s_line.append(line)

    def get_neighbor(self):
        return self.adj.keys()

    def get_name(self):
        return self.s_name

    def get_weight(self,nbr):
        return self.adj[nbr][0]

    def get_line(self):
        return self.s_line

class Line:
    def __init__(self,name):
        self.L_name=name
        self.adj={}

    def add_neighbor(self,nbrname):
        self.adj[nbrname]=nbrname

    def get_neighbor(self):
        return self.adj.keys()

class StaNet:
    def __init__(self):
        self.station_list={}
        self.size=0

    def add_sta(self,name,line):
        a=Station(name)
        a.add_line(line)
        self.station_list[name]=a
        self.size+=1

    def __contains__(self, name):
        if name in self.station_list:
            return True
        else:
            return False

    def add_edge(self,name1,line1,name2,line2,weight):
        if name1 not in self.station_list:
            self.add_sta(name1,line1)
        else:
            if line1 not in self.station_list[name1].get_line():
                self.station_list[name1].add_line(line1)
        if name2 not in self.station_list:
            self.add_sta(name2, line2)
        else:
            if line2 not in self.station_list[name2].get_line():
                self.station_list[name2].add_line(line2)
        self.station_list[name1].add_neighbor(name2,weight,line2)
        self.station_list[name2].add_neighbor(name1,weight,line1)

    def get_sta_list(self):
        return self.station_list.keys()
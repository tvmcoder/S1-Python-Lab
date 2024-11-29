class time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,other):
        totalsecond=self.__second+other.__second
        totalminute=self.__minute+other.__minute+(totalsecond//60)
        totalhour=self.__hour+other.__hour+(totalminute//60)
        return time(totalhour, totalminute % 60,totalsecond %60)
    def display(self):
        print(f"sum of time is {self.__hour:02}:{self.__minute:02}:{self.__second:02}")
        
time1=time(10,32,45)
time2=time(14,46,24)
sum=time1+time2
sum.display()
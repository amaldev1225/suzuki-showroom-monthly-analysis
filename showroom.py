import matplotlib.pyplot as plt
import pandas as p
v={}
vehicle=("alto","swift","baleno","ertiga","brezza")
def show_vehicle():
    print("available vehicles in showroom")
    for car in vehicle:
        print(car)
def buy_vehicle():
    b=input("enter the vechile you wanted to buy: ")   
    if b in vehicle:
        v[b]=v.get(b,0)+1
        print(b,"your purchase succesfull")
    else:
        print("this item is not in suzuki showroom")
def show_purchase():
    print("your purchase",v)  
def most_sold():
    if v:
        mostsold=max(v,key=v.get)  
        print("most sold vehicle this month: ",mostsold ,"-",v[mostsold])
        labels=list(v.keys())  
        size=list(v.values())
        plt.pie(size,labels=labels)
        plt.title("vechile sales ")
        plt.show()
    else:
        print("no vehicle sold yet")
def exit_showroom():
    print("THANK YOU FOR VISITING MARUTI SUZUKI SHOWROOM")
    if v:
        b=p.DataFrame(list(v.items()),columns=[' car',"sold"])
        b.to_csv("showroom.csv",index=False,mode="a")
        c=p.read_csv("showroom.csv")
        print(c)         
    exit()
def main():
    print("----WELCOME TO MARUTI SUZUKI----")
    while True:
        print('''    1.show the vehicle 
    2. to buy vehicle
    3.show the vehicle you buyed
    4. most vehicle saled on this month
    5. exit
    ''')
        try:
            optn=int(input("enter your option: "))
            if optn==1:
                show_vehicle()
            elif optn==2:
                buy_vehicle()
            elif optn==3:
                show_purchase()
            elif optn==4:
                most_sold()
            elif optn==5:
                exit_showroom()
            else:
                print("invalid option.try again")
        except ValueError:
            print("plz enter valid number")        
main() 


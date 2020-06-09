op=''
os=""
x=0
z=0
size=0
save=""
verify=""
name=""
slot=""
serial=""
state=""
day=""
month=""
year=""
ID=""
ok="again"
done=""
sname=""
slot1=""
serial2=""
year2=""
day2=""
month2=""
search=""
gap=""
goku=1
i=1
go=1
gohan=1
bat=""
cat=""
dash=""
car=0
saleyear=""
salemonth=""
fer=""
per=""
sale=""
soup=1
infinite=1
final=""
chop=1
rat=""
pat=""
NAME=[]
SLOT=[]
SERIAL=[]
STATE=[]
DAY=[]
MONTH=[]
YEAR=[]
ID_NO=[]
RCODE=[]
baitB="back"
baitA="again"
import mysql.connector
m=mysql.connector.connect(user='root', password='tiger', auth_plugin='mysql_native_password')
c=m.cursor()
try:
    c.execute("create database vdata")
except mysql.connector.errors.DatabaseError:
    pass
c.execute("use vdata")
try:
    c.execute("create table registry(R_CODE char(15) primary key,NAME char(50) not null,STATE char(50) not null,D_O_R date not null,I_D char(50) not null,SERIAL_N_O int not null,SLOT int not null);")
except:
    pass
#rcode-name-state-dor-id-slot-serial
def fname():
    fname=input("enter your first name")
    if(fname=="back"):
        return baitB
    elif(fname=="again"):
        return baitA
    elif(fname.isalpha()==False):
        print("value should not be numeric")
        raise ValueError
    else:
        return fname
def sname():
    sname=input("enter your first name")
    if(sname=="back"):
        return baitB
    elif(fname=="again"):
        return baitA
    elif(sname.isalpha()==False):
        print("value should not be numeric")
        raise ValueError
    else:
        return sname
def state():
    state=input("enter your state")
    if(state=="back"):
        return baitB
    elif(fname=="again"):
        return baitA
    elif(state.isalpha()==False):
        print("value should not be numeric")
        raise ValueError
    else:
        return state
def month():
    month=input("enter your first name")
    if(month=="back"):
        return baitB
    elif(month=="again"):
        return baitA
    elif(month.isnumeric()==False):
        print("value should be numeric")
        raise ValueError
    elif(int(month)<1):
        print("oops! month does not exist")
        raise AssertionError
    elif(int(month)>12):
        print("month doesn't exist! ENTER AGAIN!!!")
        raise AssertionError
    else:
        return month
def day():
    day=input("enter the day of the month")
    day2=int(day)
    if(day=="back"):
        return baitB
    elif(day=="again"):
        return baitA
    elif(day.isnumeric()==False):
        print("value should be numeric")
        raise ValueError
    elif(day2<0):
        print("day doesn't exist! ENTER AGAIN!!")
        raise AssertionError
    elif(int(year)%4!=0 and month=="2" and day2>28):
        print("day doesn't exist! ENTER AGAIN!!")
        raise AssertionError
    elif(int(year)%4==0 and month=="2" and int(day)>29):
        print("day doesni't exst! ENTER AGAIN!!")
        raise AssertionError
    elif(int(month)==8 and day2>31):
        print("day doesn't exist! ENTER AGAIN!!")
        raise AssertionError
    elif(int(month)%2!=0 and day2>30):
        print("day doesn't exist! ENTER AGAIN!!")
        raise AssertionError
    elif(day2>31):
        print("day doesn't exist! ENTER AGAIN!!")
        raise AssertionError
    elif(day=="0"):
        print("day doesn't exist! ENTER AGAIN!!")
        raise AssertionError
    else:
        return day
def year():
    year=input("enter year")
    if(year=="back"):
        return baitB
    elif(year=="again"):
        return baitA
    elif(year.isnumeric()==False):
        print("value should be numeric")
        raise ValueError
    else:
        return year
def slot():
    slot=input("enter slot number")
    if(slot=="back"):
        return baitB
    elif(slot=="again"):
        return baitA
    elif(slot.isnumeric()==False):
            print("value should be numeric")
            raise AssertionError
    elif(int(slot)<1):
            print("value cant be 0.ENTER AGAIN!!")
            raise AssertionError
    elif(int(slot)>999):
            print("slot no. cannot be more than 999!!! ENTER AGAIN!!!!")
            raise AssertionError
    else:
        length=len(slot)
        while(length!=3):
            length=len(slot)
            slot="0"+slot
        
        return slot
def serial():
    serial=input("enter slot number")
    if(serial=="back"):
        return baitB
    elif(serial=="again"):
        return baitA
    elif(serial.isnumeric()==False):
        print("value should be numeric")
        raise AssertionError
    elif(int(serial)<10000):
        print("oops!! serial no. cannot be more than 9999! ENTER AGAIN!! ")
        raise AssertionError
    else:
        size=len(serial)
        if(size!=4):
            while(size!=4):
                serial="0"+serial
                size=len(serial)
        return serial
   
while(x!="bye"):
    
    car=0
    
    print("1. REGISTER VEHICLE \n2. GET CUSTOMER DETAILS(REGISTRATION NO. REQUIRED) \n3. CHECK REGISTRATION NO.(CUSTOMER DETAILS REQUIRED) \n4. MODIFY DATA \n5. SALE OF CARS \n6. HELP")
    
    x=input("choose from option enter 'bye' to exit")
    
    if(x=="1"):
        
        while(save!="back"):
            
            print("IMPORTANT COMMANDS")
            
            print("*"*95)
            
            print("1. ENTER 'back' AT ANY POINT TO QUIT TO MAIN MENU")
            
            print("2. ENTER 'again' AT ANY POINT TO ENTER AGaIN")
            
            print("*"*95)
            
            
            #fname
            
            while(ok=="again"):
                
                try:
                    fname=fname()
                    
                    ok=input("press any key ")
                    
                    if(fname=="back"):
                        break
                
                except AssertionError:
                    continue
                
                except ValueError:
                    continue
            
            if(fname=="back"):
                        break
            
            
            #sname
            
            ok="again"
            
            while(ok=="again"):
                
                sname=sname()
                
                ok=input("press any key ")
            
            if(sname=="back"):
                break
            
            name=fname+" "+sname
            
            
            #state
            
            ok="again"
            
            while(ok=="again"):
                
                state=state()
                
                if(state=="back"):
                    break
                
                ok=input("press any key to continue ")
            
            if(state=="back"): 
                
                break
            
            state=state.upper()
            
            
            #slot
            
            ok="again"
            
            while(ok=="again"):
                
                try:
                    
                    slot=slot()
                    
                    slot2=int(slot)
                    
                    if(slot=="back"):
                        
                        break
                
                except ValueError:
                    
                    print("OOPS! ERROR!,TRY AGAIN! AVOID USE OF SPECIAL CHARACTER ")
                    
                    continue
                
                except AssertionError:
                    
                    continue
                
                ok=input("press any key to continue")
            
            if(slot=="back"):
                
                break
            
            
            #serial
            
            ok="again"
            
            while(ok=="again"):
                
                try:
                    
                    serial=input("ENTER SERIAL NO. (not more than 4): ")
                    
                    serial2=int(serial)
                    
                    if(serial=="back"):
                        
                        break
                    
                    ok=input("press any key to continue ")
                
                except ValueError:
                    
                    print("OOPS! ERROR!,TRY AGAIN! AVOID USE OF SPECIAL CHARACTER ")
                    
                    continue
                
                except AssertionError:
                    
                    continue
            
            if(serial=="back"):
                
                break
            
            
            #year
            
            ok="again"
            
            while(ok=="again"):
                
                try:
                    
                    year=input("ENTER YEAR: ")
                    
                    if(year=="back"):
                        
                        break
                
                except ValueError:
                    
                    print("OOPS! ERROR!,TRY AGAIN! AVOID USE OF SPECIAL CHARACTER ")
                    
                    continue
                
                except AssertionError:
                    
                    continue
                
                ok=input("press any key to continue ")
            
            if(year=="back"):
                
                break
            
            
            #month
            
            ok="again"
            
            while(ok=="again"):
                
                try:
                    
                    month=input("ENTER MONTH NO.: ")
                    
                    if(month=="back"):
                        
                        break
                
                except ValueError:
                    
                    print("OOPS! ERROR!,TRY AGAIN! AVOID USE OF SPECIAL CHARACTER ")
                    
                    continue
                
                except AssertionError:
                    
                    continue
                
                ok=input("press any key to continue ")
            
            if(month=="back"):
                
                break
            
            
            #day
            
            ok="again"
            
            while(ok=="again"):
                
                day=input("ENTER DAY OF THE MONTH: ")
                
                day2=int(day)
                
                try:
                    if(day=="back"):
                        
                        break
                    else:
                        
                        ok=input("press any key to continue ")
                
                except ValueError:
                    
                    print("OOPS! ERROR!,TRY AGAIN! AVOID USE OF SPECIAL CHARACTER ")
                    
                    continue
                
                except AssertionError:
                    
                    continue
                    
                    print("OOPS! ERROR!,TRY AGAIN! AVOID USE OF SPECIAL CHARACTER ")
                    
                    continue
            if(day=="back"):
                
                break
            
            date=year+"-"+month+"-"+day
            
            
            #id
            
            ok="again"
            
            while(ok=="again"):
                
                try:
                    
                    ID=input("ENTER ID NO.(adhaar card or voter id card no.): ")
                    
                    if(ID=="back"):
                        break
                
                except ValueError:
                    print("OOPS! ERROR!,TRY AGAIN! AVOID USE OF SPECIAL CHARACTER ")
                    
                    continue
                
                except AssertionError:
                    
                    continue
                
                ok=input("press any key to continue ")
            
            if(ID=="back"):
                
                break
            
            print("="*95)
            
            print("STATE:",state,"\nNAME:",name,"\nSLOT NO.:",slot,"\nSERIAL NO.:",serial,"\nDATE:",date,"\nID NO.:",ID,"\nCHECK ALL THE INFORMATION!!!!!!!")
            
            print("1.ENTER 'reenter' TO ENTER AGIN \n2. ENTER 'back' TO QUIT TO MAIN MENU")
            
            print("="*95)
            
            while(True):
                
                save=input("do you want to save data?? yes/no: ")
                
                save=save.lower()
                
                if(save=="yes" or save=="no" or save=="back" or save=="reenter"):
                    
                    break
                
                else:
                    
                    print("enter from the available option only!!")
                    
            save=save.lower()
            
            if(save=="yes"):
                
                print("data registered!!!")
                
                
                #rcode-name-state-dor-id-slot-serial
                
                code=(state[0]+state[2]+slot+chr(64+int(month))+serial+year)
                
                c.execute("INSERT INTO registry VALUES(%s,%s,%s,%s,%s,%s,%s);",(code,name,state,date,ID,slot,serial))
                
                m.commit()
                
                print("your registration code is ",code)
                
                press=input("press any key to continue")
                
                break
                
            
            elif(save=="back"):
                break
            
            elif(save=="reenter"):
                continue
            
            elif(save=="no"):
                print("not saved")
                continue
        
        print("quiting to main menu!!!")
    
    elif(x=="2"):
        
        while(done!="no"):
            
            search=input("ENTER REGISTRATION CODE TO GET INFO or enter 'back' to go back to main menu: ")
            
            if(search==""):
                
                print("empty feild!!enter again!!")
                
                continue
            
            elif(search=="back"):
                break
            else:
                print("REGISTRATION CODE:",search)
            
            check=input("check registration code and press any key to continue or enter 'again' to enter again ")
            
            check=check.lower()
            
            if(check=="again"):
                
                continue
            
            c.execute("select * from registry where R_CODE=%s;",(search,))
            record=c.fetchall()    
            if(record==[]):
                
                print("registration no. not found!! try again!!")
                
                
            else:    
                name=record[0][1]
                
                slot=record[0][5]
                
                serial=record[0][6]
                
                state=record[0][2]
                 
                ID=record[0][4]
                
                date=record[0][3]
                
                print("="*95)
                    
                print("NAME:",name,"\nSLOT:",slot,"\nSERIAL:",serial,"\nSTATE:",state,"\nID NUMBER:",ID,"\nDATE OF REGISTRATION:",date)
                    
                print("="*95)
            while(soup>0):
                
                done=input("do you want to continue? yes/no ")
                
                if(done=="yes" or done=="no"):
                    
                    break
                
                else:
                     print("choose from the given option only")
                   
    elif(x=="3"):
        
        while(final!="no"):
            
            details=input("ENTER YOUR ID NO. TO CHECK REGISTRATION NO.")
            
            if(details==""):
                
                print("empty feild!!enter again!!")
            
            elif(details=="back"):
                
                break
            print("ID NUMBER:",details)
            
            check=input("check ID NUMBER and press any key to continue or enter 'again' to enter again ")
            
            check=check.lower()
            
            if(check=="again"):
                continue
            
            for os in ID_NO:
                
                if(os==details):
                    
                    index=ID_NO.index(os)
                    
                    print("your registration code is:",RCODE[index])
                    
                    break
            
            if(os!=details):
                
                print("registration no. not found!! try again!!")
            
            while(True):
                final=input("do you want to continue? yes/no")
                if(final=="yes" or final=="no"):
                    break
                else:
                    print("choose from the given option only")
                    continue
            
    elif(x=="4"):
        ok=""
        while(ok!=n):
            rcode=input("enter registrtaion code")
            c.exexute("select * from registry where R_CODE=%s",(rcode,) )
            checkdata=c.featchall()
            if(checkdata=[]):
                print("code doesn't exist")
                continue
            else:
                print("="*95
                print("1.NAME \n2.STATE \n what you want to update")
                print("="*95) 
                update=input("choose a option no.")
                if(update="1"):
                      while(check=="again")
                      new_name=input("enter new name")
                      check=input("press any key to continue")
                      c.execute("update registry set name=%s where R_CODE=%s;",(new_name,rcode))
                elif(update="2"):
                      pass
                      while(check=="again")
                      new_name=input("enter new name")
                      check=input("press any key to continue")
                      c.execute("update registry set name=%s where R_CODE=%s;",(new_name,rcode))
    
    elif(x=="5"):
        
        while(sale!="back"):
            
            saleyear=""
            
            salemonth=""
            
            print("Filter by: \n1. MONTH  \n2. YEAR \n3. MONTH and YEAR \nENTER back to quit to main menue")
            
            sale=input("choose from option")
            
            try:
                
                if(sale=="1"):
                    
                    while(bat!="no"):
                        
                        car=0
                        
                        salemonth=input("sale of which month(enter month no.)")
                        
                        for per in MONTH:
                            
                            if(per==salemonth):
                                
                                car=car+1
                        
                        if(salemonth==""):
                            
                            print("empty")
                        
                        elif(per!=salemonth):
                            
                            print("month doesnt exist")
                        
                        print("your sale for this month is",car)
                        
                        while(1>0):
                            
                            bat=input("do yo want to surf more in this filter yes/no")
                            
                            if(bat=="yes" or bat=="no"):
                                break
                            
                            else:
                                continue
                        
                        if(bat=="yes"):
                            continue
                        
                        else:
                            break
                
                elif(sale=="2"):
                    
                    car=0
                    
                    while(cat!="no"):
                        
                        saleyear=input("sale of which year(enter year no.)")
                        
                        for fer in YEAR:
                            
                            if(fer==saleyear):
                                
                                car=car+1
                        
                        if(sale==""):
                            
                            print("empty")
                        
                        elif(car==0):
                            print("sale for year doesnt exist")
                        
                        print("your sale for this year is",car)
                        
                        while(go>0):
                            
                            cat=input("do yo want to surf more yes/no")
                            
                            if(cat=="yes" or cat=="no"):
                                break
                            
                            else:
                                continue
                        
                        if(cat=="yes"):
                            continue
                        
                        else:
                            break
                
                elif(sale=="3"):
                    
                    car=0
                    
                    chop=1
                    
                    while(rat!="no"):
                        
                        saleyear=input("year ")
                        
                        salemonth=input("month")
                        
                        for dash in YEAR:
                            
                            if(dash==saleyear):
                                
                                van=YEAR.index(dash)
                                
                                MONTH[van]==salemonth
                                
                                car=car+1
                        
                        if(car==0):
                            
                            print("sale for this month and year doesn't exist")
                        
                        print("sale for this month and year is",car)
                        
                        while(chop>0):
                            
                            rat=input("do yo want to surf more under this filter yes/no")
                            
                            if(rat=="yes" or rat=="no"):
                                break
                            
                            else:
                                continue
                        if(rat=="yes"):
                            continue
                        
                        else:
                            break
                
                elif(sale=="back"):
                    
                    break
                
                elif(sale=="again"):
                    continue
                
                else:
                    continue
            
            except:
                print("oops error occured")
                    
                    
                            
    elif(x=="6"):
        print("="*95)
        
        print("FOR HELP CONTACT US ON \nEMAIL: anything@example.com \nCUSTOMER CARE: 110-XX-XX-XXX")
        
        print("="*95)                
    else:
        
        continue
        
print("BYE!!HAVE A NICE DAY :]")
    


print("░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗")
print("░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝")
print("░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░")
print("░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░")
print("░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗")
print("░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝")
#---------------------------------------------------------VARIABLES-------------------------------------------------------------

os=""
x=0
z=0
datu="" 
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
#---------------------------------------------CONNECTING TO mysQL----------------------------------------------------------------------
import mysql.connector
import datetime
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
#_______________________________________________________FUNCTION DEFINE______________________________________________________________
def spac():
    print()
    print()
    print()
def orderby(something):
    c.execute("order by %s",(something,))
    odata=c.fetchall()
    if(odata==[]):
        print("feild doesnt exist")
        raise AssertionError
    for hjy in odata:
        print(hjy)
def fnamee():
    fname=input("ENTER YOUR FIRST NAME:")
    if(fname=="back"):
        return baitB
    elif(fname=="again"):
        return baitA
    elif(fname.isalpha()==False):
        print("VALUE SHOULD NOT BE NUMERIC!!!!!")
        raise ValueError
    else:
        return fname
def snamee():
    sname=input("ENTER YOUR FAMILY NAME:")
    if(sname=="back"):
        return baitB
    elif(fname=="again"):
        return baitA
    elif(sname.isalpha()==False):
        print("VALUE SHOULD NOT BE NUMERIC!!!!!")
        raise ValueError
    else:
        return sname
def statee():
    state=input("ENTER THE STATE:")
    
    if(state=="back"):
        return baitB
    elif(fname=="again"):
        return baitA
    elif(state.isalpha()==False):
        print("VALUE SHOULD NOT BE NUMERIC!!!!!!!")
        raise ValueError
    else:
        return state
def datte():
    libra=['0','1','2','3','4','5','6','7','8','9']
    lib=[5,8]
    while True:
      global datu
      datu=input("ENTER THE DATE OF REGISTRATION[DATE FORMAT-- (YYYY-MM-DD)]-")
      
      datu=datu.strip()
      
      if(len(datu)==10):
          
          hey=0
          k=1
          for i in datu:
              if i=='-' and k in lib:
                  pass
              
              elif i in libra:
                  pass
              
              else:
                  hey=1
                  print("ENTER NUMBERS AND CORRECT FORMAT ONLY!!!!!!!!")
                  spac()
                  break
              k+=1
          if hey==0:
               try:
                 dattte=datetime.date(int(datu[0:4]),int(datu[5:7]),int(datu[8:10]))

                 if dattte>datetime.date.today():
                     print("THIS DATE DOESN'T EXIST YET! |PLEASE ENTER A VALID DATE!!!")
                     spac()    

                 elif dattte<datetime.date(1900,12,31):
                     print("PLEASE ENTER A VALID DATE!!!!!")
                     spac()

                 else:
                     

                     return dattte
                     
                     break
               except Exception as er:

                   if str(er)=="month must be in 1..12":
                                   print("ERROR:MONTH MUST BE BETWEEN 1-12|[IT CAN'T BE-",datu[5:7],"]|!!!!")
                                   spac()

                   elif str(er)=="day is out of range for month":
                                   print("ERROR:THE DAY IS OUT OF RANGE FOR MONTH!!!!!")
                                   spac()
               except KeyboardInterrupt:
                   print("don't use random keys")
                   continue
                   
      
      else:
          print("CORRECT FORMAT ONLY!!!!!!!!")
          spac()




def slote():
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
        while(length<3):
            
            slot="0"+slot
            length=len(slot)
        
        return slot
def seriale():
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
#_____________________________________________________EXECUTION_of-data_________________________________________________________________
while(x!="bye"):
    
    car=0
    
    print("1. REGISTER VEHICLE \n2. GET CUSTOMER DETAILS(REGISTRATION NO. REQUIRED) \n3. CHECK REGISTRATION NO.(ID DETAILS REQUIRED) \n4. MODIFY DATA \n5. SALE OF CARS \n6. SORT \n7. HELP")
    
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
                    fname=fnamee()
                    
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
                
                sname=snamee()
                
                ok=input("press any key ")
            
            if(sname=="back"):
                break
            
            name=fname+" "+sname
            
            
            #state
            
            ok="again"
            
            while(ok=="again"):
                
                state=statee()
                
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
                    
                    slot=slote()
                    
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
            
            
            #date
            
            ok="again"
            
            while(ok=="again"):
                
                
                    date=datte()

                    ok=input("press any key to continue ")
            
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
                print("datu",datu)
                
                code=(state[0]+state[2]+slot+chr(64+int(datu[5:7])) +serial+datu[0:4])
                
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
            
            c.execute("select R_CODE from registry where I_D=%s;",(details,))
            rc=c.fetchall()
            print("your code is",rc[0][0])
            if(rc==[]):
                
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
        while(ok!='n'):
            rcode=input("enter registrtaion code")
            c.execute("select * from registry where R_CODE=%s",(rcode,) )
            checkdata=c.fetchall()
            if(checkdata==[]):
                print("code doesn't exist")
                continue
            else:
                print("="*95)
                print("1.NAME \n2.STATE \n what you want to update")
                print("="*95) 
                update=input("choose a option no.")
                if(update=="1"):
                    check="again"
                    while(check=="again"):
                      new_name=input("enter new name")
                      check=input("press any key to continue")
                      c.execute("update registry set name=%s where R_CODE=%s;",(new_name,rcode))
                elif(update=="2"):
                      pass
                      while(check=="again"):
                        new_name=input("enter new name")
                        check=input("press any key to continue")
                        c.execute("update registry set name=%s where R_CODE=%s;",(new_name,rcode))
    

                ok='n'
    elif(x=="5"):
        
        while(sale!="back"):
            
            saleyear=""
            
            salemonth=""
            
            print("Filter by: \n1. MONTH  \n2. YEAR \n3. MONTH and YEAR \nENTER back to quit to main menue")
            
            sale=input("choose from option")
            
            try:
                
                if(sale=="1"):
                    
                    while(bat!="no"):
                        
                        
                        salemonth=input("sale of which month(enter month no.)")
                        salemonth=salemonth.zfill(2)
                        slm = "%"+"-"+salemonth+"-"+"%"
                        if(salemonth==""):
                            
                            print("empty")

                        c.execute("select count(*) from registry where D_O_R like %s;",(slm,))
                        print("yes")
                        car=c.fetchall()
                        if(car[0][0]==0):
                                  print("no sale in this month")
                        c.execute("select * from registry group by D_O_R having D_O_R like %s",(slm,))
                        dcar=c.fetchall()
                        print("rcode | name |state |date of registration| id | slot| serial |")
                        for alldata in dcar:
                            print(alldata)
                        
                        print("your sale for this month is",car[0][0])
                        
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
                        print("empty")
                        c.execute("select count(*) from registry where D_O_R like '%-%s-%';",(saleyear,))
                        
                        car=c.fetchall()
                        c.execute("select * from registry group by name having D_O_R like '%s-%';",(saleyear,))
                        dcar=c.fetchall()
                        print("|-REGISTRATION CODE-|-NAME-|-STATE-|-DATE OF REGISTRATION-|-ID-|-SLOT-|-SERIAL-|")
                        i=""
                        for alldata in dcar:
                            for sdata in alldata:
                                sdata="|-"+sdata+"-|"
                                i=i+sdata
                            print(i)

                        for alldata in dcar:
                            print(alldata)
                        if(car[0][0]==0):
                            print("no sale in this year")
                        
                        print("your sale for this year",car[0][0])
                        
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
            
            except Exception as haha :
                print(haha)
                    
                    
                            
    elif(x=="6"):
        ok="again"
        while(ok=="y"):
            check="again"
            try:
                print("SORT BY: \n1. NAME \n2 STATE \n2 DATE")
                sort=input("choose a option no.")
                check=input("check and press any key to continue \nenter 'again' to reenter")
                if(sort=="back"):
                    break
                elif(check=="back"):
                    break
                elif(check=="again"):
                    continue
                if(sort=="1"):
                    sorted=orderby(NAME)
                elif(sort=="2"):
                    sorted=orderby(STATE)
                elif(sort=="3"):
                    sorted=orderby(D_O_R)
                else:
                    print("choose from the given option")
                    continue
                while(1>0):
                            
                            ok=input("do you which to continue(y/n)")
                            
                            if(ok=="y" or bat=="n"):
                                break
                            
                            else:
                                continue
                        
                if(ok=="y"):
                    continue
                        
                else:
                    break
            except:
                print("error")
                continue
    elif(x=="7"):
        print("="*95)
        
        print("FOR HELP CONTACT US ON \nEMAIL: anything@example.com \nCUSTOMER CARE: 110-XX-XX-XXX")
        
        print("="*95)
    else:
        
        continue
        
print("BYE!!HAVE A NICE DAY :]")
#_____________________________________________________THE-END_____________________________________________________________________________    

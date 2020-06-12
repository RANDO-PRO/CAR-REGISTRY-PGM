#-----------------------------------------------------------IMPORTS-------------------------------------------------------------
import mysql.connector
import datetime
import time

#-------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------SPECIAL--------------------------------------------------------

def spac():
    print()
    print()
    print()


def spac2():
    print()
    print()

def spac3():
    print()
    
def linecr(mo,rep=1,spa=2,dis=0,cdis="",term=0,spaceremo=0):
    namingsa=['REGISTERING',"CUSTOMER DETAILS","SEARCH REGESTRATION NUMBER(R_CODE)","MODIFY DATA","SALE","INF FROM SORTED TABLE","HELP INFO"]
    k=rep+dis
    if cdis=="":
        ja=namingsa[(dis-1)]
    else:
        ja=cdis
    if dis!=0:
        for hoho in range(k):
            if hoho==0 or (hoho==(k-1) and spaceremo==0):
                 print(mo*98)
            elif(hoho==dis and cdis==""):
                 print(" "*47+ja)
            elif(cdis!="" and hoho==dis):
                if term==0:
                     print(ja)
                else:
                    print(" "*47+ja)
    else:           
        for hoho in range(k):
            print(mo*98)
    
    if spaceremo!=0:
        pass
    elif spa==1:
        spac3()
    
    elif spa==2:
        spac2()
    elif(spa==3):
          spac()
#================================================================================================================================


#----------------------------------------------------------WELCOME---------------------------------------------------------------
print("░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗")
print("░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝")
print("░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░")
print("░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░")
print("░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗")
print("░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝")
time.sleep(0.56)
spac2()
linecr("-")
#-------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------VARIABLES-------------------------------------------------------------

os = ""
x = 0
z = 0
datu = ""
size = 0
save = ""
verify = ""
name = ""
slot = ""
serial = ""
state = ""
day = ""
month = ""
year = ""
ID = ""
ok = "again"
done = ""
sname = ""
slot1 = ""
serial2 = ""
year2 = ""
day2 = ""
month2 = ""
search = ""
gap = ""
goku = 1
i = 1
go = 1
gohan = 1
bat = ""
cat = ""
dash = ""
car = 0
saleyear = ""
salemonth = ""
fer = ""
per = ""
sale = ""
soup = 1
infinite = 1
final = ""
chop = 1
rat = ""
pat = ""
NAME = []
SLOT = []
SERIAL = []
STATE = []
DAY = []
MONTH = []
YEAR = []
ID_NO = []
RCODE = []
baitB = "back"
baitA = "again"
huff = ['1', '2', '3', '4', '5']
#---------------------------------------------CONNECTING TO mysQL----------------------------------------------------------------------

m = mysql.connector.connect(
    user='root', password='tiger', auth_plugin='mysql_native_password')
c = m.cursor()
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





def prip(listt):

    a = len(listt)
    dig = 0
    while(a > 0):
         a = a//10
         dig += 1
    
    #stop
    time.sleep(0.666)
    #box
    
    print("", ("_"*13), "_"*13)
    print("|__T.ENTERIES_|"+"____"+str(len(listt))+"_"*(9-dig)+"|")

    #table
    print("", "_"*163)

    print("|_R_CODE___________|_NAME", "_"*45+"_|_STATE", "_"*24 +
          "|_D_O_R________|_I_D________________|_SERIAL_N_O __|_SLOT___|")

    for i in range(len(listt)):

        print("|", listt[i][0], " "*(15-len(listt[i][0])), "|", listt[i][1], " "*(49-len(listt[i][1])), "|", listt[i][2], " "*(28-len(listt[i][2])), "|", listt[i]
              [3], "  |", listt[i][4], " "*(17-len(listt[i][4])), "|", listt[i][5], " "*(11-len(str(listt[i][5]))), "|", listt[i][6], " "*(5-len(str(listt[i][6]))), "|")
        if i == (len(listt)-1):
            print("╹"+"─"*163+"╹")
    spac2()


def infpri(L=[], rp=''):  # r_code,NAME,STATE,D_O_R,I_D,SERIAL_N_O,SLOT
        start = 'SELECT * FROM registry WHERE '
        if rp == 'AND' or rp == 'and':
            rp = ' AND '
        elif rp == 'OR' or rp == 'or':
             rp = ' OR '

        hop = ' LIKE '

        K = ['R_CODE', 'NAME', 'STATE', 'D_O_R', 'I_D', 'SERIAL_N_O', 'SLOT']
        ho = []
        a = 0
        for i in L:
            if(i != ''):
                 ho.append([i, a])
            a += 1
        a = ho

        for he in ho:

                start += K[he[1]]+hop+"'"
                start += he[0]+"'"
                if(he != ho[-1]):
                     start += rp
                else:
                     start += ';'

        c.execute(start)

        pop = c.fetchall()

        return pop


def orderby(something,descending=""):
    if descending=="":
          c.execute("SELECT * FROM REGISTRY ORDER BY "+something+";")
    else:
        c.execute("SELECT * FROM REGISTRY ORDER BY "+something+" DESC;")
    odata = c.fetchall()
    if(odata ==[]):
        print("NO ENTERY EXISTS")
        raise AssertionError
    prip(odata)


def fnamee():
    fname = input("ENTER FIRST NAME:")
    spac()
    if(fname =="back"):
        return baitB
    elif(fname =="again"):
        return baitA
    elif(fname.isalpha() ==False):
        print("VALUE SHOULD NOT BE NUMERIC!!!!!")
        spac()
        raise ValueError
    else:

        return fname


def snamee():
    sname = input("ENTER YOUR FAMILY NAME:")
    spac()
    if(sname =="back"):
        return baitB
    elif(fname =="again"):
        return baitA
    elif(sname.isalpha() ==False):
        print("VALUE SHOULD NOT BE NUMERIC!!!!!")
        spac()
        raise ValueError
    else:
        return sname


def statee():
    state = input("ENTER THE STATE:")
    spac()
    if(state =="back"):
        return baitB
    elif(fname =="again"):
        return baitA
    elif(state.isalpha() ==False):
        print("STATE NAME SHOULD NOT BE NUMERIC!!!!!!!")
        spac()
        raise ValueError
    else:
        return state


def datte():
    libra = ['0','1','2','3','4','5','6','7','8','9']
    lib = [5,8]
    while True:
      global datu
      datu = input("ENTER THE DATE OF REGISTRATION[DATE FORMAT- YYYY-MM-DD] :")
      spac()
      datu = datu.strip()

      if(len(datu) ==10):

          hey = 0
          k = 1
          for i in datu:
              if i =='-' and k in lib:
                  pass

              elif i in libra:
                  pass

              else:
                  hey = 1
                  print("ENTER NUMBERS AND CORRECT FORMAT ONLY!!!!!!!!")
                  spac()
                  break
              k += 1
          if hey ==0:
              try:
                 dattte = datetime.date(int(datu[0:4]),int(datu[5:7]),int(datu[8:10]))

                 if dattte >datetime.date.today():
                     print(
                         "THIS DATE DOESN'T EXIST YET! |PLEASE ENTER A VALID DATE!!!")
                     spac()

                 elif dattte <datetime.date(1900,12,31):
                     print("PLEASE ENTER A VALID DATE!!!!!")
                     spac()

                 else:

                     return dattte

                     break

              except Exception as er:

                   if str(er) =="month must be in 1..12":
                                   print("ERROR:MONTH MUST BE BETWEEN 1-12|[IT CAN'T BE-", datu[5:7],"]|!!!!")
                                   spac()

                   elif str(er) =="day is out of range for month":
                                  print("ERROR:THE DAY IS OUT OF RANGE FOR MONTH!!!!!")
                                  spac()
              except KeyboardInterrupt:
                   print("UNEXPECTED ERROR")
                   spac()
                   continue


      else:
          print("CORRECT FORMAT ONLY!!!!!!!!")
          spac()


def slote():
    slot = input("ENTER SLOT NUMBER:")
    slot = slot.lower()
    spac()
    if(slot =="back"):
        return baitB
    elif(slot =="again"):
        return baitA
    elif(slot.isnumeric() ==False):
            print("SLOT NUMBER CAN ONLY BE NUMERIC!!!!!!")
            spac()
            raise AssertionError

    elif(int(slot) <1):
            print("SLOT NUMBER CAN'T BE LESS THAN 0!!!!!")
            spac()
            raise AssertionError
    elif(int(slot) >999):
            print("SLOT NUMBER CAN'T BE MORE THAN 999!!!!!")
            spac()
            raise AssertionError
    else:
        length = len(slot)
        while(length <3):

            slot = "0"+slot
            length = len(slot)

        return slot


def seriale():
    serial = input("ENTER SERIAL NUMBER:")
    spac()
    if(serial =="back"):
        return baitB
    elif(serial =="again"):
        return baitA
    elif(serial.isnumeric() ==False):
        print("SERIAL NUMBER CAN ONLY BE NUMERIC!!!!!!!")
        spac()
        raise AssertionError
    elif(int(serial) >10000):
        print("SERIAL NUMBER CAN'T BE MORE THAN 10000!!!!!!!")
        spac()
        raise AssertionError
    else:
        size = len(serial)
        if(size !=4):
            while(size !=4):
                serial = "0"+serial
                size = len(serial)
        return serial


def monoga(choice):
    pass
    va=["NAME","STATE","D_O_R","SERIAL_N_O","SLOT"]
    
    if len(choice)==1:
        so=va[(int(choice)-1)]
        orderby(so)
    else:
        so=va[(int(choice[0])-1)]
        orderby(so,"DESC")

def endin(a=0):
   if a==0:
      print("QUITTING TO MAIN MENU.........")
      time.sleep(1.6)
      spac2()       
      linecr("-")
   else:
       print("QUITTING THE PROGRAM...........")
       time.sleep(1.72)
       spac()
       linecr("-")
#_____________________________________________________EXECUTION_of-data_________________________________________________________________



while(x !="bye"):
    
    linecr(" ",2,0,8,"MENU",1,1)
    car = 0

    print("● 1 REGISTER VEHICLE \n\n● 2 GET CUSTOMER DETAILS(REGISTRATION NO. REQUIRED) \n\n● 3 CHECK REGISTRATION NO.(ID DETAILS REQUIRED) \n\n● 4 MODIFY DATA \n\n● 5 SALE OF CARS \n\n● 6 SORT \n\n● 7 HELP \n"+("_"*98)+"\n")
    x=input("CHOOSE[ENTER 'BYE' TO EXIT] :")
    time.sleep(0.44)
    spac2()
    
    
    x=x.upper()
    if(x =="1"):
        
        linecr("=",2,2,int(x))    
        while(save !="back"):
            
            ok='again'
            
            print("IMPORTANT COMMANDS")

            linecr("#",2,2,int(x),"●ENTER 'back' AT ANY POINT TO QUIT TO MAIN MENU\n\n●ENTER 'again' AT ANY POINT TO ENTER AGAIN")

           #fname

            while(ok =="again"):

                try:
                    fname = fnamee()

                    ok = input("press any key ")

                    if(fname =="back"):
                        break

                except AssertionError:
                    continue

                except ValueError:
                    continue

            if(fname =="back"):
                        spac()
                        break

            else:
                fname = fname.upper()
                spac2()
            #sname

            ok = "again"

            while(ok =="again"):

                try:
                    sname = snamee()

                    ok = input("press any key ")

                    if(sname =="back"):
                        break

                except AssertionError:
                    continue

                except ValueError:
                    continue


            if(sname =="back"):
                    spac()
                    break

            else:
                 sname = sname.upper()
                 name = fname+" "+sname
                 spac2()

            if len(name) >45:
                name = name[0:46]

            #state

            ok = "again"

            while(ok =="again"):
               try:
                    state = statee()

                    if(state =="back"):
                        break

                    ok = input("press any key to continue ")
               except ValueError:
                     continue


            if(state =="back"): 
                spac()
                break
            else:
                 state = state.upper()
                 spac2()

            if len(state) >22:
                state = state[0:23]

            #slot

            ok = "again"

            while(ok =="again"):

                try:

                    slot = slote()

                    slot2 = int(slot)

                    if(slot =="back"):

                        break
                    ok = input("press any key to continue")

                except ValueError:

                    print("ERROR:AVOID USE OF SPECIAL CHARACTER!!!!!!!!")
                    spac()
                    continue

                except AssertionError:

                    continue


            if(slot =="back"):
                spac()
                break

            else:
                spac2()

            #serial

            ok = "again"

            while(ok =="again"):

                try:

                    serial = seriale()

                    if(serial =="back"):

                        break

                    ok = input("press any key to continue ")

                except ValueError:

                    print("OOPS! ERROR!,TRY AGAIN! AVOID USE OF SPECIAL CHARACTER ")

                    continue

                except AssertionError:

                    continue

            if(serial =="back"):
                spac()
                break
            else:
                spac2()

            #date

            ok = "again"

            while(ok =="again"):



                    date = datte()

                    ok = input("press any key to continue ")
                    time.sleep(0.57)
                    spac2()
            #id

            ok = "again"

            while(ok =="again"):

                try:

                    ID = input("ENTER ID NUMBER(ADHAAR CARD NO./VOTER ID CARD NO.) :")
                    spac()
                    if(ID =="back"):
                        break


                    elif ID.isnumeric() ==False:
                                 print("THE ADHAAR CARD NUMBER IS FALSE!!!![IT CAN ONLY BE NUMBERIC]")
                                 spac2()
                    elif len(ID) ==12 or len(ID)==10:
                                  decider = infpri(["","","","",ID,"",""],"and")
                                  if decider ==[]:
                                      ok = input("press any key to continue ")
                                  else:
                                       print("AN ID SIMILAR TO THIS ALREADY EXISTS!!!!!!PLEASE CHECK IF REGISTRATION HAS ALREADY BE DONE OR ENTER A CORRECT ID!!!!!!!!!!!!!!!!!!!")
                                       spac2()
                                       prip(decider)
                    else:
                        print(
                            "THE NUMBER ENTERED IS INCORRECT....ADHAAR CARD-12(DIGITS)|VOTERID-10(DIGITS)")
                        spac2()
                except ValueError:
                    print("OOPS! ERROR!TRY AGAIN! AVOID USE OF SPECIAL CHARACTER ")

                    continue

                except AssertionError:

                    continue




            if(ID =="back"):
                spac()
                break
            else:
                spac2()

            print("="*95)

            print("STATE:", state,"\nNAME:",name,"\nSLOT NO.:",slot,"\nSERIAL NO.:",serial,"\nDATE:",date,"\nID NO.:",ID,"\nCHECK ALL THE INFORMATION!!!!!!!\n")
            spac2()
            print("+"*95)
            time.sleep(0.23)
            print(
                "1.ENTER 'reenter' TO ENTER AGAIN \n2. ENTER 'back' TO QUIT TO MAIN MENU")
            print("+"*95)
            print()
            spac2()
            print("="*95)
            time.sleep(0.67)
            while(True):

                save = input("DO YOU WANT TO SAVE THE DATA??[y/n/yes/no] :")
                spac2()
                save = save.lower()

                if(save =="yes" or save=="no" or save=='y' or save=='n' or save=="back" or save=="reenter"):
                    time.sleep(0.12)
                    spac2()
                    break

                else:

                    print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!")
                    spac2()

            try:
                if(save =="yes" or save=='y'):

                    #rcode-name-state-dor-id-slot-serial


                          code = (state[0]+state[2]+slot+chr(64+int(datu[5:7])) + serial+datu[0:4])
                          checker = infpri([code,"","","","","",""],'and')



                          c.execute("INSERT INTO registry VALUES(%s,%s,%s,%s,%s,%s,%s);", (code,name,state,date,ID,serial,slot))

                          m.commit()
                          time.sleep(0.15)
                          print("REGESTRATION CODE IS:", code)
                          print()
                          press = input("press any key to continue")
                          spac2()
                          time.sleep(0.22)
                          print("REGESTRATION COMPLETE!!!!!!!!!!")
                          spac2()
                          endin()
                          break

                elif(save =="back"):
                       endin()
                       break
                elif(save =="reenter"):
                        linecr("-")
                        continue

                elif(save =="no" or save=='n'):
                           print("CANCELLED!!!!!!!!")
                           spac2()
                           endin()
                           break

            except Exception as hmmm:

                         print("UNEXPECTED ERROR:", hmmm)
                         spac2()
                         print("THERE ALREADY EXISTS A REGISTRATION WITH THE SAME INFO!!!!IF YOU ARE TRYING TO CHANGE THE NAME THEN GO TO MODIFY DATA OR ELSE RE-ENTER CORRECT DATA!!!!!!!!!!!!!!!!!!!!")
                         spac2()
                         prip(checker)
                         time.sleep(0.15)
                         print("CANCELLED")
                         spac2()
                         endin()
                         break
            break


    elif(x =="2"):
        linecr("=",2,2,int(x))
        while(done !="no"):
            linecr("*",2,2,int(x))
            search = input("ENTER REGISTRATION CODE TO GET INFO or enter 'back' to go back to main menu: ")

            if(search ==""):

                print("empty feild!!enter again!!")

                continue

            elif(search =="back"):
                break
            else:
                print("REGISTRATION CODE:", search)

            check = input("check registration code and press any key to continue or enter 'again' to enter again ")

            check = check.lower()

            if(check =="again"):

                continue

            c.execute("select * from registry where R_CODE=%s;", (search,))
            record = c.fetchall()    
            if(record ==[]):

                print("registration no. not found!! try again!!")


            else:
                name = record[0][1]

                slot = record[0][5]

                serial = record[0][6]

                state = record[0][2]

                ID = record[0][4]

                date = record[0][3]

                print("="*95)

                print("NAME:", name,"\nSLOT:",slot,"\nSERIAL:",serial,"\nSTATE:",state,"\nID NUMBER:",ID,"\nDATE OF REGISTRATION:",date)

                print("="*95)
            while(soup >0):

                done = input("do you want to continue? yes/no ")

                if(done =="yes" or done=="no"):

                    break

                else:
                    print("choose from the given option only")

    elif(x =="3"):
        linecr("=",2,2,int(x))
        while(final !="no"):
            
            details = input("ENTER YOUR ID NO. TO CHECK REGISTRATION NO.")

            if(details ==""):

                print("empty feild!!enter again!!")

            elif(details =="back"):

                break
            print("ID NUMBER:", details)

            check = input("check ID NUMBER and press any key to continue or enter 'again' to enter again ")

            check = check.lower()

            if(check =="again"):
                continue

            c.execute("select R_CODE from registry where I_D=%s;", (details,))
            rc = c.fetchall()
            print("your code is", rc[0][0])
            if(rc ==[]):

                print("registration no. not found!! try again!!")

            while(True):
                final = input("do you want to continue? yes/no")
                if(final =="yes" or final=="no"):
                    break
                else:
                    print("choose from the given option only")
                    continue

    elif(x =="4"):
        ok = ""
        linecr("=",2,2,int(x))
        while(ok !='n'):
           try: 
            rcode = input("REGISTRATION CODE :")
            spac2()
            if len(rcode)==14:
                if rcode.isnumeric()==False and rcode.isalpha()==False: 
                      c.execute("select * from registry where R_CODE=%s", (rcode,) )
                      checkdata = c.fetchall()
                      if(checkdata ==[]):
                            print("NO SUCH CODE EXISTS")
                            spac2()
                            continue
                      else:
                          
                          while True: 
                              linecr("=",2,2,int(x),"● 1 NAME \n● 2 STATE")
                                                         
                              update = input("CHOOSE :")
                              spac2()
                              check='again'
                              if(update =="1"):
                                 while(check=='again'):  
                                     new_name = input("ENTER NEW NAME :")
                                     spac3()
                                     check = input("press any key to continue")
                                     spac2()  
                                 c.execute("update registry set NAME='"+new_name+"' where R_CODE='"+rcode+"';")
                                 m.commit()
                                 print("NAME CHANGE COMPLETED!!!!!!!!!!!!!!!!!!!!")
                                 spac2()
                                 endin()
                                 break
                                            
                              elif(update =="2"):
                                       while check=='again':                                
                                             new_name = input("ENTER STATE :")
                                             spac()
                                             check = input("press any key to continue")
                                             spac2()
                                       c.execute(c.execute("update registry set STATE='"+new_name+"' where R_CODE='"+rcode+"';"))
                                       m.commit()
                                       print("STATE CHANGE COMPLETED!!!!!!!!!!!!!!!!!!!!")
                                       spac2()
                                       endin()
                                       break
                              elif update=='back':
                                  break
                              
                              else:
                                   print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!")
                                   spac2()
                                   continue
                else:                       
                
                    print("REGISTRATION CODE CONTAINS BOTH NUMBERS AND ALPHABETS!!!!!!!!!!!!!!!")
                    spac2()
                    continue
            elif(rcode=='back'):
                linecr("-")
                break
            
            
            else:
                print("REGISTRATION CODE HAS ONLY 14 CHARACTERS!!!!!!!!!!!!!!")
                continue
           except Exception as jojo:
                  print("UNEXPECTED ERROR:",jojo)
                  spac2()
           ok = 'n'
    
    
    elif(x =="5"):
        linecr("=",2,2,int(x))
        while(sale !="back"):
            
            saleyear = ""

            salemonth = ""

            print(
                "Filter by: \n1. MONTH  \n2. YEAR \n3. MONTH and YEAR \nENTER back to quit to main menu")

            sale = input("choose from option")

            try:

                if(sale =="1"):

                    while(bat !="no"):


                        salemonth = input("sale of which month(enter month no.)")
                        salemonth = salemonth.zfill(2)
                        slm = "%"+"-"+salemonth+"-"+"%"
                        if(salemonth ==""):

                            print("empty")

                        c.execute("select count(*) from registry where D_O_R like %s;", (slm,))
                        print("yes")
                        car = c.fetchall()
                        if(car[0][0] ==0):
                                 print("no sale in this month")
                        c.execute("select * from registry group by D_O_R having D_O_R like %s", (slm,))
                        dcar = c.fetchall()
                        prip(dcar)

                        print("your sale for this month is", car[0][0])

                        while(1 >0):

                            bat = input("do yo want to surf more in this filter yes/no")

                            if(bat =="yes" or bat=="no"):
                                break

                            else:
                                continue

                        if(bat =="yes"):
                            continue

                        else:
                            break

                elif(sale =="2"):

                    car = 0

                    while(cat !="no"):

                        saleyear = input("sale of which year(enter year no.)")
                        sly = "saleyear"+"-"+"%"
                        print("empty")
                        c.execute("select count(*) from registry where D_O_R like %s;", (sly,))

                        car = c.fetchall()
                        c.execute("select * from registry group by name having D_O_R like '%s-%';", (saleyear,))
                        dcar = c.fetchall()
                        prip(dcar)
                        for alldata in dcar:
                            print(alldata)
                        if(car[0][0] ==0):
                            print("no sale in this year")

                        print("your sale for this year", car[0][0])

                        while(go >0):

                            cat = input("do yo want to surf more yes/no")

                            if(cat =="yes" or cat=="no"):
                                break

                            else:
                                continue

                        if(cat =="yes"):
                            continue

                        else:
                            break

                elif(sale =="3"):

                    car = 0

                    chop = 1

                    while(rat !="no"):

                        saleyear = input("year ")

                        salemonth = input("month")
                        slym = saleyear+"-"+salemonth+"-"+"%"

                        c.execute("select count(*) from registry where D_O_R like %s';", (slym,))

                        car = c.fetchall()
                        c.execute("select * from registry group by name having D_O_R like %s;", (slym,))
                        dcar = c.fetchall()
                        prip(dcar)
                        for alldata in dcar:
                            print(alldata)
                        if(car[0][0] ==0):
                            print("no sale in this year")

                        print("your sale for this year", car[0][0])

                        if(car ==0):

                            print("sale for this month and year doesn't exist")

                        print("sale for this month and year is", car)

                        while(chop >0):

                            rat = input("do yo want to surf more under this filter yes/no")

                            if(rat =="yes" or rat=="no"):
                                break

                            else:
                                continue
                        if(rat =="yes"):
                            continue

                        else:
                            break

                elif(sale =="back"):

                    break

                elif(sale =="again"):
                    continue

                else:
            
                    continue
            except Exception as hoooo:
                    print("UNEXPECTED ERROR:",hoooo)
            


    elif(x=='6'):
        ok='y'
        linecr("=", 2, 2, int(x))    
        while(ok!='n'):
            try:
                print("SORT BY: \n\n● 1 NAME \n\n● 2 STATE \n\n● 3 DATE \n\n● 4 SERIAL NUMBER \n\n● 5 SLOT \n"+("-"*96),"\n\n●[ENTER 'BACK' TO EXIT TO MAIN MENU]\n●[ADD 'D' TO THE END OF THE OPTION FOR DESCENDING SORT]","\n\n"+("-"*96))
                sork=input("CHOOSE :")
                spac2()
                sork=sork.lower()
                if(sork =="back"):
                    spac2()
                    endin()
                    break
                  
                
                elif len(sork)<3 and sork in huff or (sork[0] in huff and sork[1]=='d'):
                                              monoga(sork)
                
                else:
                    print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!!!!!!")
                    spac2()
                    linecr("-")
                    continue
                    
                while(True):

                            ok = input("DO YOU WISH TO CONTINUE??(y/n/yes/no) :")
                            ok=ok.lower()
                            spac2()
                            
                            if(ok =="y" or ok=="yes"):
                                linecr("-")    
                                break

                            elif(ok=='n' or ok=='no'):
                                        ok='n'
                                        endin()    
                                        break
                            else:
                                print("CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!!!!!!")
                                spac2()
                                
                                

            except Exception as kaka:
                print("ERROR:",kaka)
                time.sleep(0.48)
                spac2()
                linecr("-")
                continue
    
    elif(x =="7"):
        
        linecr("-", 2, 2, int(x))
        
        
        linecr("=", 2, 2, int(
            x), "FOR HELP CONTACT US ON \n\n●EMAIL: namekharuko@gmail.com \n\n●CUSTOMER CARE: 110-83-72-369")
        time.sleep(0.67)
        linecr("-")
        
    elif x=='BYE':
        endin(1)
        break
    else:
        
        linecr("-",2,2,9,"PLEASE CHOOSE FROM THE OPTIONS ONLY!!!!!!!!!!!!!!!")
        linecr("-")
        continue


print("BYE!!HAVE A NICE DAY :]")



#__________________________________________________________________________________________________________________________________

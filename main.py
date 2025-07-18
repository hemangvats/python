#Debangshu Roy and Hemang Vats 
#Velocity bus booking (Front end [GUI]). Refer to X link 
#for discord interface and commands. 
#The Database is centralised and the whole app is based oon the idea 
#of being decentralised and transparent

#importing required modules
import os
import csv
from tkinter import *
from tkinter import messagebox

#MainBookingPageData

def MainBookingPage():
    root= Tk()
    root.title('VBB Booking')
    root.geometry("800x500")

    F = open("userdata.csv", "r")
    read = list(csv.reader(F))

    F1 = open("locationdata.csv", "r")
    rdr = list(csv.reader(F1))

    F2 = open("Bustypedata.csv", "r")
    ddr = list(csv.reader(F2))

    for i in read:
        if w == i[3]:
            welcome_label = Label(root, text=f"Welcome {i[0]} {i[1]}", font=("Helvetica", 30, "bold", "italic"), fg="#ffc800", bg="#000000")
            welcome_label.pack(pady=15)
            
            #varaibles
            x = 0
            z = 0
            id = i[3]
        
            for i in rdr:
                loc_label = Label(root, text=f"Location - {i[0]} : Price {i[1]} Choice Number: {x}")
                loc_label.pack()
                x += 1

            locbookinglabel = Label(root, text="Enter any one choice number: ")
            locbookinglabel.pack()
            bookingchoice = Entry(root)
            bookingchoice.pack(pady=10)
            
            for y in ddr:
                bt_label = Label(root, text=f"Bus Type = {y[0]} : Price  = {y[1]} : Choice Number: {z} ")
                bt_label.pack()
                z += 1

            btannounce = Label(root, text="Enter any one choice number")
            btannounce.pack()
            bt_entry = Entry(root)
            bt_entry.pack(pady=10)

            travelnum = Label(root, text="Number of people travelling (In Numbericals)" )
            travelnum.pack()
            travelnumEntry = Entry(root)
            travelnumEntry.pack(pady=10)

            def BillWindow():
                bw = Tk()
                bw.title('Billing Window')
                bw.geometry("800x500")

                #backend calculation
                awc = bookingchoice.get()
                _cAWC = int(awc)
                rdrcwc = (rdr[_cAWC])
                rrdrcwc = rdrcwc[0]
                bwc = bt_entry.get()
                _bWC = int(bwc)
                ddrbwc = (ddr[_bWC])
                dddrbwc = ddrbwc[0]
                cwc = travelnumEntry.get()
                _cCWC = int(cwc)
                tolSum = ((int(rdrcwc[1]))+(int(ddrbwc[1])))*(_cCWC)
                strtolSum = str(tolSum)

                #backend of adding list to booking records
                oP = open("bookingrecords.csv", 'a', newline='')
                wrt = csv.writer(oP)
                bookingList = [id, rrdrcwc, dddrbwc, cwc, strtolSum]
                wrt.writerow(bookingList)

                #displaying final choices. 
                ChoiceLabel1 = Label(bw, text="Your choice is as follows: \n")
                ChoiceLabel1.pack()
                bwLocationLabel = Label(bw, text=f"Location: {rdrcwc[0]}")
                bwLocationLabel.pack()
                bwBt = Label(bw, text=f"Bus Choice:  {ddrbwc[0]}")
                bwBt.pack()
                no_ofPeople_travelling = Label(bw, text=f"Number of people travelling {_cCWC}")
                no_ofPeople_travelling.pack()
                bwPriceLabel = Label(bw, text=f"Total Price: {tolSum}")
                bwPriceLabel.pack()
            
            def records():
                j = open("bookingrecords.csv", 'r')
                jej = csv.reader(j)
                rt = Tk()
                rt.title('Previous Records')
                for i in jej: 
                    if w == i[0]:
        
                        record_frame = Frame(rt, highlightbackground="#FFF9A6")
                        record_frame.pack(padx = 20, pady= 20)

                        idlabel = Label(record_frame, text=f"Username : {i[0]}")
                        idlabel.pack(pady=5) 

                        reclocation = Label(record_frame, text=f"Destination : {i[1]}")
                        reclocation.pack(pady=5)

                        recbuschoice = Label(record_frame, text=f"Bus Type: {i[2]}")
                        recbuschoice.pack(pady=5)

                        recTotalpass = Label(record_frame, text=f"Passengers Travelled : {i[3]}")
                        recTotalpass.pack(pady=5)

                        recTotalmoni = Label(record_frame, text=f"Total Fare : {i[4]}")
                        recTotalmoni.pack(pady=5)

            confirmButton = Button(root, text="Confirm and Proceed", command=BillWindow)
            confirmButton.pack()

            previousBookings = Button(root, text="Previous Bookings", command=records)
            previousBookings.pack()

def adminSelectionPage():
    add = Tk()
    add.title('Admin Selection Page')
    add.geometry("800x500")

    def additionSelection():
        addition = Tk()
        addition.title('Choose To Add')
        #location
        def addLocationScreen():
            loc = Tk()
            loc.title('Add Location')
            loc.geometry("800x500")

            addLocationLabel = Label(loc, text="Add Any Location")
            addLocationLabel.grid(row=0, column=0)
            addLocationEntry = Entry(loc)
            addLocationEntry.grid(row=0, column=1)

            addpriceLabel = Label(loc, text="Add a price. ")
            addpriceLabel.grid(row=1, column=0)
            addpriceEntry = Entry(loc)
            addpriceEntry.grid(row=1, column=1)    

            def finalAddconfirmation():
                F = open("locationdata.csv", "a", newline='')
                write = csv.writer(F)
                L = [addLocationEntry.get(), addpriceEntry.get()]
                write.writerow(L)
                F.close()

            finalAddButton = Button(loc, text="Add", command=finalAddconfirmation)
            finalAddButton.grid(row=2, column=1)
             
        #location button 
        locationButton = Button(addition, text="Add Location", command=addLocationScreen)
        locationButton.grid(row=0, column=0)

        #bustype
        def addBustypeScreen():
            bus = Tk()
            bus.title('Admin Selection Page')
            bus.geometry("800x500")

            addBustypeLabel = Label(bus, text="Add Any Bus type")
            addBustypeLabel.grid(row=0, column=0)
            addBustypeEntry = Entry(bus)
            addBustypeEntry.grid(row=0, column=1)

            addpriceLabel = Label(bus, text="Add a price")
            addpriceLabel.grid(row=1, column=0)
            addpriceEntry = Entry(bus)
            addpriceEntry.grid(row=1, column=1)    

            def finaladdition():
                F = open("Bustypedata.csv", "a", newline='')
                write = csv.writer(F)
                L = [addBustypeEntry.get(), addpriceEntry.get()]
                write.writerow(L)
                F.close()
                
            finalAddButton = Button(bus, text="Add", command=finaladdition)
            finalAddButton.grid(row=2, column=1)

        #bustype button 
        bustypeButton = Button(addition, text="Add Bus Type", command=addBustypeScreen)
        bustypeButton.grid(row=1, column=0)

    def modification():
        #location edit
        def modifyLocation():
            modloc = Tk()
            modloc.title('Modify Location')

            G = open("locationdata.csv", "r")
            read = csv.reader(G)

            for z in read:
                locationLabel = Label(modloc, text=f"Location {z[0]} Price {z[1]}")
                locationLabel.pack()
            
            modLocationLabel = Label(modloc, text="Which one do you wish to edit.")
            modLocationLabel.pack()
            modLocation = Entry(modloc)
            modLocation.pack()
            G.close()
            
            def finalLocationEdit():
                newLoc = Tk()
                newLoc.title('Edit Location')
                F = open("locationdata.csv", 'r+')
                F1 = open("temp.csv", "w", newline='')
                re = csv.reader(F)
                wr = csv.writer(F1)

                for x in re:
                    if x[0] == modLocation.get():
                        newLocationLabel = Label(newLoc, text="Enter new Location")
                        newLocationLabel.grid(row=0, column=0)
                        newLocationEntry = Entry(newLoc)
                        newLocationEntry.grid(row=0, column=1)
                        newLocationPrice = Label(newLoc, text="Enter new price ")
                        newLocationPrice.grid(row=1, column=0)
                        newLocationpriceEntry = Entry(newLoc)
                        newLocationpriceEntry.grid(row=1, column=1)

                        def locationBackendFinal():
                            x[0] = newLocationEntry.get()
                            x[1] = newLocationpriceEntry.get()
                            wr.writerow(x)
                            messagebox.showinfo("Edited", "The modification is successful")
                            modloc.destroy()
                            newLoc.destroy()
                            mod.destroy()
                            F.close()
                            F1.close()
                            os.remove("locationdata.csv")
                            os.rename("temp.csv", "locationdata.csv")        

                        finalMod = Button(newLoc, text="Confirm Edit", command=locationBackendFinal)
                        finalMod.grid(row=2, column=1)

                    else:
                        wr.writerow(x)
                        continue           
                        
            modlocButton = Button(modloc, text="Edit", command=finalLocationEdit)
            modlocButton.pack()
        def modifyBus():
            modbt = Tk()
            modbt.title('Modify Location')

            G = open("locationdata.csv", "r")
            read = csv.reader(G)

            for z in read:
                locationLabel = Label(modbt, text=f"Location {z[0]} Price {z[1]}")
                locationLabel.pack()
            
            modbtLabel = Label(modbt, text="Which one do you wish to edit.")
            modbtLabel.pack()
            modbt = Entry(modbt)
            modbt.pack()
            G.close()
            def finalbusEdit():
                newBus = Tk()
                newBus.title('Edit Bus Type')
                H = open("Bustypedata.csv", 'r+')
                H1 = open("temp.csv", "w", newline='')
                re = csv.reader(H)
                wr = csv.writer(H1)

                for op in re:
                    if op[0] == modbt.get():
                        newBusationLabel = Label(newBus, text="Enter new Bus Type")
                        newBusationLabel.grid(row=0, column=0)
                        newBusationEntry = Entry(newBus)
                        newBusationEntry.grid(row=0, column=1)
                        newBusationPrice = Label(newBus, text="Enter new price ")
                        newBusationPrice.grid(row=1, column=0)
                        newBusationpriceEntry = Entry(newBus)
                        newBusationpriceEntry.grid(row=1, column=1)

                        def busBackendFinal():
                            op[0] = newBusationEntry.get()
                            op[1] = newBusationpriceEntry.get()
                            wr.writerow(op)
                            messagebox.showinfo("Edited", "The modification is successful")
                            modbt.destroy()
                            newBus.destroy()
                            H.close()
                            H1.close()
                            os.remove("Bustypedata.csv")
                            os.rename("temp.csv", "Bustypedata.csv")        
                        finalMod = Button(newBus, text="Confirm Edit", command=busBackendFinal)
                        finalMod.grid(row=2, column=1)

                    else:
                        wr.writerow(op)
                        continue           
                        
            modbusButton = Button(modbt, text="Edit", command=finalbusEdit)
            modbusButton.pack()

        mod = Tk()
        mod.title('Choose Modication')

        modButton1 = Button(mod, text="Modify Location and Price", command=modifyLocation)
        modButton1.grid(row=0, column=0)
        modButton2 = Button(mod, text="Modify Bustype", command=modifyBus)
        modButton2.grid(row=0, column=1)
    

    def deletion():
        #location deletion
        def locationdeletion():
            delloc=Tk()
            delloc.title('Delete Location')
            G = open("locationdata.csv", "r")
            read = csv.reader(G)

            for z in read:
                locationLabel = Label(delloc, text=f"Location {z[0]} Price {z[1]}")
                locationLabel.pack()
            delLocationLabel = Label(delloc, text="Which one do you wish to delete.")
            delLocationLabel.pack()
            delLocation = Entry(delloc)
            delLocation.pack()
            G.close()
            def finalLocationdelete():
                newLoc = Tk()
                newLoc.title('Delete Location')
                F = open("locationdata.csv", 'r+')
                F1 = open("temp.csv", "w", newline='')
                re = csv.reader(F)
                wr = csv.writer(F1)

                for x in re:
                    if x[0] == delLocation.get():
                        def locationBackendFinal():
                            messagebox.showinfo("Deleted", "The deletion is successful")
                            delloc.destroy()
                            newLoc.destroy()
                            dell.destroy()
                            F.close()
                            F1.close()
                            os.remove("locationdata.csv")
                            os.rename("temp.csv", "locationdata.csv")
                        finalDel = Button(newLoc, text="Confirm Delete", command=locationBackendFinal)
                        finalDel.grid(row=2, column=1)
                        continue
                    else:
                        wr.writerow(x)
            dellocButton = Button(delloc, text="Delete", command=finalLocationdelete)
            dellocButton.pack()

        # delete bus type
        def busdeletion():
            delbus=Tk()
            delbus.title('Delete Bus Type')
            G = open("Bustypedata.csv", "r")
            read = csv.reader(G)

            for z in read:
                busLabel = Label(delbus, text=f"Bustype {z[0]} Price {z[1]}")
                busLabel.pack()

            delBusLabel = Label(delbus, text="Which one do you wish to delete.")
            delBusLabel.pack()
            delBus = Entry(delbus)
            delBus.pack()
            G.close()
            
            def finalLocationdelete():
                newLoc = Tk()
                newLoc.title('Delete Location')
                F = open("Bustypedata.csv", 'r+')
                F1 = open("temp.csv", "w", newline='')
                re = csv.reader(F)
                wr = csv.writer(F1)

                for x in re:
                    if x[0] == delBus.get():
                        def BusTypeBackendFinal():
                            messagebox.showinfo("Deleted", "The deletion is successful")
                            delbus.destroy()
                            newLoc.destroy()
                            dell.destroy()
                            F.close()
                            F1.close()
                            os.remove("Bustypedata.csv")
                            os.rename("temp.csv", "Bustypedata.csv")
                        finalDel = Button(newLoc, text="Confirm Delete", command=BusTypeBackendFinal)
                        finalDel.grid(row=2, column=1)
                        continue
                    else:
                        wr.writerow(x)
            dellocButton = Button(delbus, text="Delete", command=finalLocationdelete)
            dellocButton.pack()
        dell = Tk()
        dell.title('Choose Deletion')

        delButton1 = Button(dell, text="Delete Location and Price", command=locationdeletion)
        delButton1.grid(row=0, column=0)
        delButton2 = Button(dell, text="Delete Bustype", command=busdeletion)
        delButton2.grid(row=0, column=1)

                
    additionButton = Button(add, text="Add",width=20, bg="#000000", fg="#ff0000", command=additionSelection)
    additionButton.grid(row=0, column=0)
    modificationButton = Button(add, text="Modify", width=20, bg="#000000", fg="#ff0000", command=modification)
    modificationButton.grid(row=0, column=1)
    deletionButton = Button(add, text="Delete", width=20, bg="#000000", fg="#ff0000",command=deletion)
    deletionButton.grid(row=0, column=2)

def AdminPanelLogin():
    root = Tk()
    root.title('Admin Login')
    root.geometry("800x500")

    admin_password = Label(root, text="Enter your Password")
    admin_password.grid(row=1,column=0)
    admin_password_entry = Entry(root)
    admin_password_entry.grid(row=1, column=1)
    
    def adminPassword():
        password = "Hem@ng&cyph3r"
        if admin_password_entry.get() == password:
            adminSelectionPage()
        
    conf_button = Button(root, text="Login as Admin", command=adminPassword)
    conf_button.grid(row=2, column=1)   

#csv userdata = [Firstname, Second Name, Email, Username, User password]



def SignInScreen():
    root = Tk()
    root.title('VBB Sign_In')
    root.geometry("800x500")
    
    name_label = Label(root, text="Enter your First name: ")
    name_label.grid(row=0, column=0)
    name_label_entry = Entry(root)
    name_label_entry.grid(row=0, column=1)

    secondname = Label(root, text="Enter your Second name: ")
    secondname.grid(row=1,column=0)
    secondname_entry = Entry(root)
    secondname_entry.grid(row=1, column=1)
    
    email = Label(root, text="Enter your Email: ")
    email.grid(row=2,column=0)
    email_entry = Entry(root)
    email_entry.grid(row=2, column=1)

    username = Label(root, text="Enter your username: ")
    username.grid(row=3, column=0)
    username_entry = Entry(root)
    username_entry.grid(row=3, column=1)

    userpassword = Label(root, text="Enter your password: ")
    userpassword.grid(row=4, column=0)
    userpassword_entry = Entry(root)
    userpassword_entry.grid(row=4, column=1)

    passwordconf = Label(root, text="Confirm your password: ")
    passwordconf.grid(row=5, column=0)
    passwordconf_entry = Entry(root)
    passwordconf_entry.grid(row=5, column=1)

    def passwordchecker():
            a = userpassword_entry.get()
            b = passwordconf_entry.get()
            
            if a == b:
                F = open("userdata.csv", "a", newline='')
                write = csv.writer(F)
                L = [name_label_entry.get(), secondname_entry.get(), email_entry.get(), username_entry.get(), userpassword_entry.get()]
                write.writerow(L)
                MainBookingPage()
                Tk.destroy()
            else:
                print("nhk")
                return

    sign_buttom = Button(root, text="Sign up", command=passwordchecker)
    sign_buttom.grid(row=6, column=1)

#command=addtodata(user_name, user_password_entry)

def AboutusScreen():
    abs = Tk()
    abs.title('About VBB')
    abs.geometry("800x500")

    aboutustext = Label(abs, text="About Us", font=("Helvetica", 30, "italic"), fg="#ffc800", bg="#000000")
    aboutustext.pack()

    defineabout = Label(abs, text="Stuck where to contact for a bus?\n Can't go to holidays with family because of logistics issues?\n We are your solution. \n Providing quality buses at affordable prices \n Plan your perfect holiday trip with us.\n Travel hassle free with Velocity \nContact us at bizwithcyph3r@gmail.com", font=("Helvetica", 20, "italic"), fg="#ffc800")
    defineabout.pack()

def FirstScreen():
    main = Tk()
    main.title('VBB Home')
    main.geometry("800x500")

    def LoginScreen():
        Tk.destroy(main)
        root = Tk()
        root.title('VBB User Login')
        root.geometry("800x500")
    
        user_name_label = Label(root, text="Enter your username: ")
        user_name_label.grid(row=0, column=0)
        user_name = Entry(root)
        user_name.grid(row=0, column=1)

        user_password = Label(root, text="Enter your Password")
        user_password.grid(row=1,column=0)
        user_password_entry = Entry(root)
        user_password_entry.grid(row=1, column=1)

        def LoginTrial():
            F = open("userdata.csv", "r")
            read = csv.reader(F)
            global w
            w = user_name.get()
            global t
            t = user_password_entry.get()
            for x in read:
                if x[3] == w and x[4] == t:
                    MainBookingPage()
                    Tk.destroy()
                    break
                else:
                    continue       

        login_button = Button(root, text="Login", command=LoginTrial)
        login_button.grid(row=2, column=1)

    #defining image
    bg = PhotoImage(file="trial.png")
    my_label = Label(main, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    #labels 
    FirstLabel = Label(main, text="Welcome to Velocity Bus Booking", font=("Helvetica", 30, "italic"), fg="#ffc800", bg="#000000")
    FirstLabel.pack()

    Secondlabel = Label(main, text="Please select", font=("Helvetica", 20, "italic"), fg="#ffc800", bg="#000000")
    Secondlabel.pack()

    #defnining buttons frame 
    buttons_frame = Frame(main, bg="#000000")
    buttons_frame.pack(pady=10)

    #buttons
    AdminButton = Button(buttons_frame, text="Admin Panel", command=AdminPanelLogin)
    AdminButton.grid(row=0, column=0, padx=20)

    CustomerLoginButton = Button(buttons_frame, text="Customer Login", command=LoginScreen)
    CustomerLoginButton.grid(row=0, column=1, padx=20)

    CustomerSignInButton = Button(buttons_frame, text="Customer Sign-Up", command=SignInScreen)
    CustomerSignInButton.grid(row=0, column=2, padx=20)

    AboutusButton = Button(buttons_frame, text="About Us", command=AboutusScreen)
    AboutusButton.grid(row=0, column=3, padx=20)

    #running 
    main.mainloop()

FirstScreen()

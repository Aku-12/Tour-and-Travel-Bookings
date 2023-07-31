from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("1500x1500")
root.state("zoomed")

root.title("Home Page")

def create_level(frame,text,x,y):
    label=Label(frame,text=text,font=("Arial",16,"bold"),bd=0,bg="#FFFACD")
    label.place(x=x,y=y)

def create_button(frame, text, x, y,ca): # creating the sub button function using parameter
    button = Button(frame, text=text, font=("Tahoma", 14, "bold"), border=0,fg="#8B7355" ,cursor="hand2", bg = "#FFFACD",command=ca)
    button.place(x=x, y=y)
    return button

def payment():
   root_book.destroy()
   a=Toplevel(root)
   a.pack() 
   

def booking():
   
     global root_book
     global frame_book
     root_book=Toplevel(root)
     root_book.geometry("1200x500")
     root_book.resizable(0,0)
     frame_book=Frame(root_book,width=700,height=320)
     frame_book.place(x=300,y=100)
    
     but_Next=Button(frame_book,text="Next",font=18,width=20)
     create_button(frame_book,"Next",300,290,payment)
     label_book1=Label(frame_book,text=" Tour Booking form",font=("Arial",24,"bold"))
     label_book1.place(x=100,y=0)

     months=StringVar()

     combobox1 =ttk.Combobox(frame_book,textvariable=months,values=("jan","feb","march","april","may","june","july","august","september","october","november","december"),width=5,state="readonly")
     combobox1.place(x=500,y=250)
     day=StringVar()
     num=[]
     for i in range(1,33):
            num.append(i)

     combobox1 =ttk.Combobox(frame_book,textvariable=day,values=num,width=2,state="readonly")
     combobox1.place(x=570,y=250)
     year= StringVar()
     spinbox = Spinbox(frame_book,textvariable=year,from_=2023,to_=2100,state="readonly",width=4)
     spinbox.place(x=625,y=250)

     months=StringVar()

     combobox1 =ttk.Combobox(frame_book,textvariable=months,values=("jan","feb","march","april","may","june","july","august","september","october","november","december"),width=5,state="readonly")
     combobox1.place(x=150,y=250)
     day=StringVar()
     num=[]
     for i in range(1,33):
            num.append(i)

     combobox1 =ttk.Combobox(frame_book,textvariable=day,values=num,width=2,state="readonly")
     combobox1.place(x=220,y=250)
     year= StringVar()
     spinbox = Spinbox(frame_book,textvariable=year,from_=2023,to_=2100,state="readonly",width=4)
     spinbox.place(x=275,y=250)

     label_name=Label(frame_book,text="Name")
     label_name.place(x=0,y=50)
     label_contact=Label(frame_book,text="Contact No")
     label_contact.place(x=350,y=50)
     label_email=Label(frame_book,text="Email")
     label_email.place(x=350,y=100)
     label_address=Label(frame_book,text="Address")
     label_address.place(x=350,y=150)
     label_surname=Label(frame_book,text="Surame")
     label_surname.place(x=0,y=100)
     label_visitors=Label(frame_book,text="Number of Visitors")
     label_visitors.place(x=0,y=150)
     label_guides=Label(frame_book,text="Number of Tour Guides")
     label_guides.place(x=0,y=200)
     label_startdate=Label(frame_book,text="Start Date")
     label_startdate.place(x=0,y=250)
     label_enddate=Label(frame_book,text="End Date")
     label_enddate.place(x=370,y=250)
     label_destination=Label(frame_book,text="Destination")
     label_destination.place(x=350,y=200)
     name_entry=Entry(frame_book,text="")
     name_entry.place(x=100,y=50)
     surname_entry=Entry(frame_book,text="")
     surname_entry.place(x=100,y=100)
     contact_entry=Entry(frame_book,text="")
     contact_entry.place(x=450,y=50)
     email_entry=Entry(frame_book,text="")
     email_entry.place(x=450,y=100)
     address_entry=Entry(frame_book,text="")
     address_entry.place(x=450,y=150)
     destination_entry=Entry(frame_book,text="",show="*")
     destination_entry.place(x=450,y=200)
    
   
     no_of_visitors=StringVar()
     num=[]
     for i in range(1,31):
          num.append(i)
     combobox1=ttk.Combobox(frame_book,textvariable=no_of_visitors,values=num,state="readonly",width=10)
     combobox1.place(x=150,y=150)
    

     no_of_visitors=StringVar()
     num=[]
     for i in range(1,6):
          num.append(i)
     combobox1=ttk.Combobox(frame_book,textvariable=no_of_visitors,values=num,state="readonly",width=10)
     combobox1.place(x=150,y=200)
# frame1=Frame()


def everest1():
    frame_a.config(width=1920,height=1080)
    frame_a.place(x=0,y=60)
    frame_a
    clear_frame()
    

    image=Image.open("MountEverest.webp")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest.jpg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=960,y=0)

    
    label=Label(frame_a,text="Everest Base Camp Trek",font=("Arial",18,"bold"),fg="blue",bg="#FFFACD")
    label.place(x=30,y=580)
    create_level(frame_a,"From Kathmandu to Solukhumbu",540,580)
    create_level(frame_a,"Tour Language\nEnglish, Nepali",420,635)
    create_level(frame_a,"Age Group \n12-75",640,635)
    create_level(frame_a,"Price\nRs12000",795,635)
    create_level(frame_a,"Services and Facilities        \nIncluded:Food, Acommodation,Travel expense\nNot included Personal expense medical expense",1240,635)
    create_level(frame_a,"Group size\n1-30",30,635)
    create_level(frame_a,"District\nSolukhumbu",1020,635)
    create_level(frame_a,"Duration \n7days",220,635)
    laabel7=Label(frame_a,text="   Tour Overview",font=("calibri",24,"bold"),bg="#FFFACD")
    laabel7.place(x=30,y=690)
    labeel8=Label(frame_a,text="It is more than a trekking as one can see a beautiful scenery of highest mountain in the world.The  everest base- \ncamp's peak elevation is 5364 meters (17598 feet) So people suffering from acrophobia should not try this cause,\n they may suffer from altitude sickness. The one who is a regular traveller or who can think they can should try this.\n Trekking to Everest Base Camp takes you to the closest possible place of the world’s highest point. Mt. Everest\n Base Camp (5,364 m) gives you the lifelong memory of the Great Himalayas looming on a row.             ",font=("Avenir",17),bg="#FFFACD")
    labeel8.place(x=30,y=740)
    labeel9=Label(frame_a,text="Day1: Kathmandu Airport-Lukla airport- trek to phakding \nDay2: phakding to namche bazaar                             \nDay3: Namche bazaar to tangboche                      \n Day:4 Trek to Dingbouche and trek to Louche\nDay5: Trek to Everest base camp                \n\t  Day6:Trek to kalapathar and back Namchebazaar      \n         Day7: Back to Lukla and back to Kathmandu",font=("Avenir",17),bg="#FFFACD")
    labeel9.place(x=1190,y=740)
    button_book=Button(frame_a,text="Book Your Tour",font=("Arial",19,"bold"),bg="yellow",command=booking)
    button_book.place(x=400,y=890)



def janakpur():
    frame_a.config(width=1920,height=1080)
    frame_a.place(x=0,y=60)
    frame_a
    clear_frame()
   

    image=Image.open("JanakiMandir.jpg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("JanakiMandir2.jpg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=960,y=0)

    # create_level(frame_a,"Everest Base Camp Trek",30,560)
    label=Label(frame_a,text="Janakpur Dham",font=("Arial",18,"bold"),fg="blue",bg="#FFFACD")
    label.place(x=30,y=580)
    create_level(frame_a,"From Kathmandu to Dhanusha",540,580)
    create_level(frame_a,"Tour Language\nEnglish, Nepali",420,635)
    create_level(frame_a,"Age Group \n12-75",640,635)
    create_level(frame_a,"Price\nRs12000",795,635)
    create_level(frame_a,"Services and Facilities        \nIncluded:Food, Acommodation,Travel expense\nNot included Personal expense medical expense",1240,635)
    create_level(frame_a,"Group size\n1-30",30,635)
    create_level(frame_a,"District\nDhanusha",1020,635)
    create_level(frame_a,"Duration \n7days",220,635)
    laabel7=Label(frame_a,text="   Tour Overview",font=("calibri",24,"bold"),bg="#FFFACD")
    laabel7.place(x=30,y=690)
    labeel8=Label(frame_a,text= "Janakpur Dham is a tour of historical sites at Janakpur(Dhanusha),birthplace of Sita. All the hindu people\n worship this place as a great ceremony in Chhath . Janakpur is a popular with different historical and \nreligious events. It is one of the most holy places of Hindus.You can get chance to explore Maithili culture\n and traditions by visiting there. ",font=("Avenir",17),bg="#FFFACD")
    labeel8.place(x=30,y=740)
    labeel9=Label(frame_a,text="Day1:Kathmandu to Ram Janaki Mandir(225km)(7-8 hrs)     \nDay2:Puja and full day sightseeing(Overnight Stay)           \nDay3:Ride back to Kathmandu by vehicles(7-8hrs)        ",font=("Avenir",17),bg="#FFFACD")
    labeel9.place(x=1190,y=740)
    button_book=Button(frame_a,text="Book Your Tour",font=("Arial",19,"bold"),bg="yellow",command=booking)
    button_book.place(x=400,y=890)

def pashupatinath():
    frame_a.config(width=1920,height=1080)
    frame_a.place(x=0,y=60)
    frame_a
    clear_frame()
   

    image=Image.open("pashupati.jpg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("Pashupati2.jpeg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=960,y=0)

    # create_level(frame_a,"Everest Base Camp Trek",30,560)
    label=Label(frame_a,text="Tour to Pashupatinath",font=("Arial",18,"bold"),fg="blue",bg="#FFFACD")
    label.place(x=30,y=580)
    create_level(frame_a,"From Kathmandu to Kathmandu",540,580)
    create_level(frame_a,"Tour Language\nEnglish, Nepali",420,635)
    create_level(frame_a,"Age Group \n12-75",640,635)
    create_level(frame_a,"Price\nRs5000",795,635)
    create_level(frame_a,"Services and Facilities        \nIncluded:Food, Acommodation,Travel expense\nNot included Personal expense medical expense",1240,635)
    create_level(frame_a,"Group size\n1-30",30,635)
    create_level(frame_a,"District\nKathmandu",1020,635)
    create_level(frame_a,"Duration \n7days",220,635)
    laabel7=Label(frame_a,text="   Tour Overview",font=("calibri",24,"bold"),bg="#FFFACD")
    laabel7.place(x=30,y=690)
    labeel8=Label(frame_a,text="Pashupatinath Temple is the most popular hindu temple overall Nepal. We can see carved wooden crafts\n,cubic sculptures, with two level roofs covered with copper and gold sheets.Four main doors  to the\n pagoda are covered with silver sheets, while the pinnacle is gold. The temple has two  interior rooms\n where the pashupatinath lord(aka shiva) idol is placed.   ",font=("Avenir",17),bg="#FFFACD")
    labeel8.place(x=30,y=740)
    labeel9=Label(frame_a,text="Day1:Visit the places near pashupatinath \n\tDay2:Puja and full day sight seeing (overnight stay)   \n\tDay3: Guheswari temple sightseeing and back to home   ",font=("Avenir",17),bg="#FFFACD")
    labeel9.place(x=1190,y=740)
    button_book=Button(frame_a,text="Book Your Tour",font=("Arial",19,"bold"),bg="yellow",command=booking)
    button_book.place(x=400,y=890)

def muktinath():
    frame_a.config(width=1920,height=1080)
    frame_a.place(x=0,y=60)
    frame_a
    clear_frame()
   

    image=Image.open("Muktinath.jpg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("Muktinath2.jpg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=960,y=0)

   
    label=Label(frame_a,text="Tour to Muktinath Temple",font=("Arial",18,"bold"),fg="blue",bg="#FFFACD")
    label.place(x=30,y=580)
    create_level(frame_a,"From Kathmandu  to Mustang",540,580)
    create_level(frame_a,"Tour Language\nEnglish, Nepali",420,635)
    create_level(frame_a,"Age Group \n12-75",640,635)
    create_level(frame_a,"Price\nRs12000",795,635)
    create_level(frame_a,"Services and Facilities        \nIncluded:Food, Acommodation,Travel expense\nNot included Personal expense medical expense",1240,635)
    create_level(frame_a,"Group size\n1-30",30,635)
    create_level(frame_a,"District\nMustang",1020,635)
    create_level(frame_a,"Duration \n5days",220,635)
    laabel7=Label(frame_a,text="   Tour Overview",font=("calibri",24,"bold"),bg="#FFFACD")
    laabel7.place(x=30,y=690)
    labeel8=Label(frame_a,text="  Muktinath is a Vishnu temple, sacred to both Hindus and Buddhists. It is located in Muktinath Valley at the foot \nof the Thorong La mountain pass in Mustang, Nepal. It is one of the world’s highest temples. The site is close to the\n village of Ranipauwa, which is sometimes mistakenly called Muktinath.Situated at an altitude of 3,710 meters \n(12,172 feet) at the base of the Thorong La mountain pass in the Mustang district, Muktinath is a highly\n venerated sacred place for both Hindus and Buddhists.       ",font=("Avenir",17),bg="#FFFACD")
    labeel8.place(x=30,y=740)
    labeel9=Label(frame_a,text="Day1: From Kathmandu to pokhara\n Day2: From pokhara to Mustang\n\t Day3:  Enjoy the beautiful scenery there\n\t        Day 4:Temple darshan and take a holy bath\n     Day5: Visit Jwala Mai temple",font=("Avenir",17),bg="#FFFACD")
    labeel9.place(x=1190,y=740)
    button_book=Button(frame_a,text="Book Your Tour",font=("Arial",19,"bold"),bg="yellow",command=booking)
    button_book.place(x=400,y=890)


def lumbini():
    frame_a.config(width=1920,height=1080)
    frame_a.place(x=0,y=60)
    frame_a
    clear_frame()
   

    image=Image.open("Lumbini.jpg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("Lumbini1.jpg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=960,y=0)

    # create_level(frame_a,"Everest Base Camp Trek",30,560)
    label=Label(frame_a,text="Everest Base Camp Trek",font=("Arial",18,"bold"),fg="blue",bg="#FFFACD")
    label.place(x=30,y=580)
    create_level(frame_a,"From Kathmandu to Kapilvastu",540,580)
    create_level(frame_a,"Tour Language\nEnglish, Nepali",420,635)
    create_level(frame_a,"Age Group \n12-75",640,635)
    create_level(frame_a,"Price\nRs12000",795,635)
    create_level(frame_a,"Services and Facilities        \nIncluded:Food, Acommodation,Travel expense\nNot included Personal expense medical expense",1240,635)
    create_level(frame_a,"Group size\n1-30",30,635)
    create_level(frame_a,"District\nKapilvastu",1020,635)
    create_level(frame_a,"Duration \n7days",220,635)
    laabel7=Label(frame_a,text="   Tour Overview",font=("calibri",24,"bold"),bg="#FFFACD")
    laabel7.place(x=30,y=690)
    labeel8=Label(frame_a,text="Lumbini is 4.8 km (3 mi) in length and 1.6 km (1.0 mi) in width. The holy site of Lumbini is bordered by a \nlarge monastic zone in which only monasteries can be built, no shops, hotels or restaurants. It is separated\n into an eastern and western monastic zone, the eastern having the Theravadin monasteries, the western having \nMahayana and Vajrayana monasteries. There is a long water filled canal separating the western \nand eastern zones, with a series of brick arch bridges joining the two sides along the length.   ",font=("Avenir",17),bg="#FFFACD")
    labeel8.place(x=30,y=740)
    labeel9=Label(frame_a,text="Day1: Kathmandu Airport to Bhairawa Airport\t  \n Day2: Bhairawa to Lumbini(kapilvastu)\t\t \n Day3: Visit Mayadevi temple and Ashoka pillar\n\tDay4: Visit Monasteries,Puskarini pond and museum\n Day5: Back to Home\t\t",font=("Avenir",17),bg="#FFFACD")
    labeel9.place(x=1190,y=740)
    button_book=Button(frame_a,text="Book Your Tour",font=("Arial",19,"bold"),bg="yellow",command=booking)
    button_book.place(x=400,y=890)

def rara():
    frame_a.config(width=1920,height=1080)
    frame_a.place(x=0,y=60)
    frame_a
    clear_frame()
   

    image=Image.open("Rara.jpg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("Rara1.jpg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=960,y=0)

    
    label=Label(frame_a,text="Trek to Rara Lake",font=("Arial",18,"bold"),fg="blue",bg="#FFFACD")
    label.place(x=30,y=580)
    create_level(frame_a,"From Kathmandu to Mugu",540,580)
    create_level(frame_a,"Tour Language\nEnglish, Nepali",420,635)
    create_level(frame_a,"Age Group \n12-75",640,635)
    create_level(frame_a,"Price\nRs12000",795,635)
    create_level(frame_a,"Services and Facilities        \nIncluded:Food, Acommodation,Travel expense\nNot included Personal expense medical expense",1240,635)
    create_level(frame_a,"Group size\n1-30",30,635)
    create_level(frame_a,"District\nMugu",1020,635)
    create_level(frame_a,"Duration \n6days",220,635)
    laabel7=Label(frame_a,text="   Tour Overview",font=("calibri",24,"bold"),bg="#FFFACD")
    laabel7.place(x=30,y=690)
    labeel8=Label(frame_a,text="Rara Lake lies at an elevation of 2,990 m (9,810 ft), has a water surface of 10.8 km2 (4.2 sq mi), a maximum depth \nof 167 m (548 ft), is 5.1 km (3.2 mi) long and 2.7 km (1.7 mi) wide. It drains into the Mugu Karnali River via the Nijar\n River.[7] Its water quality is characterized by high pH, conductivity and total hardness. It has been classified as\n oligotrophic as it is slightly polluted.[8] The lake changes its colour up to 5 times a day depending on the climate. Rara\n Lake is surrounded by thickly forested hills named Chuchemara Danda at 4,087 meters and Murma at 3630m.              ",font=("Avenir",17),bg="#FFFACD")
    labeel8.place(x=30,y=740)
    labeel9=Label(frame_a,text="  Day1:Flight from Kathmandu to Nepalgunj\n Day2: Travel from Neplagunj to Rara\n Day3: Rara lake sightseeing tour\n\t Day4: Horse riding,cycling,Village Tour     \n Day5: Drive back Rara to kalikot\n Day6: Drive kalikot to surkhet\t\n     Day7: Drive Surkhet to Kathmandu",font=("Avenir",17),bg="#FFFACD")
    labeel9.place(x=1240,y=740)
    button_book=Button(frame_a,text="Book Your Tour",font=("Arial",19,"bold"),bg="yellow",command=booking)
    button_book.place(x=400,y=890)

def khaptad():
    frame_a.config(width=1920,height=1080)
    frame_a.place(x=0,y=60)
    frame_a
    clear_frame()
   

    image=Image.open("Khaptad1.jpg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("Khaptad2.jpg")
    resized_image=image.resize((960,550))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=960,y=0)

    
    label=Label(frame_a,text="Tour to Khaptad(Doti)",font=("Arial",18,"bold"),fg="blue",bg="#FFFACD")
    label.place(x=30,y=580)
    create_level(frame_a,"From Kathmandu to Doti",540,580)
    create_level(frame_a,"Tour Language\nEnglish, Nepali",420,635)
    create_level(frame_a,"Age Group \n12-75",640,635)
    create_level(frame_a,"Price\nRs12000",795,635)
    create_level(frame_a,"Services and Facilities        \nIncluded:Food, Acommodation,Travel expense\nNot included Personal expense medical expense",1240,635)
    create_level(frame_a,"Group size\n1-30",30,635)
    create_level(frame_a,"District\nDoti",1020,635)
    create_level(frame_a,"Duration \n5days",220,635)
    laabel7=Label(frame_a,text="   Tour Overview",font=("calibri",24,"bold"),bg="#FFFACD")
    laabel7.place(x=30,y=690)
    labeel8=Label(frame_a,text="Khaptad National Park is located in the Far-western region of Nepal. The park was gazetted \nin 1984 covering an area of 225 sq. km. The area of buffer zone is 216 sq.km. The park\n is the only mid-mountain national park in western Nepal, representing a unique and important\n ecosystem. The late Khaptad Swami moved to the area in 1940's to meditate and worship.\n He spent about 50 years as a hermit and became a renowned spiritual saint.  ",font=("Avenir",17),bg="#FFFACD")
    labeel8.place(x=30,y=740)
    labeel9=Label(frame_a,text="Day1:From Kathmandu Airport to Nepalgunj Airport\n Day2:   From Nepalgunj to Doti(Khaptad area)\nDay3:Hike to khaptad dada\t\t\n Day5: Explore khaptad National park\t\n Day5: Visit Khaptad Baba Ashram\n Day6: Get back to home\t  ",font=("Avenir",17),bg="#FFFACD")
    labeel9.place(x=1190,y=740)
    button_book=Button(frame_a,text="Book Your Tour",font=("Arial",19,"bold"),bg="yellow",command=booking)
    button_book.place(x=400,y=890)


def pokhara():
     frame_a.config(width=1920,height=1080)
     frame_a.place(x=0,y=60)
     clear_frame()
    
     image=Image.open("pkr.jpg")
     resized_image=image.resize((1200,600))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=0,y=0)
    
     image=Image.open("Sarangkot.jpg")
     resized_image=image.resize((600,340))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=0,y=600)
     image=Image.open("Sarangkot1.jpg")
     resized_image=image.resize((600,340))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=600,y=600)
    
     label_pokhara_overview=Label(frame_a,text="Overview",font=("arial",26,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1480,y=10)
     label_pokhara_overview=Label(frame_a,text="Paragliding in pokhara has become one of the most         \npopular adventerous places in Nepal.You can join         \nparaglidingin Pokhara any time and month of the           \n year as long as it’s not raining and the thermals are active.\n It is operated throughout the year. The busy season is in \nSeptember/October/November/December and February\nMarch/April/May.\t\t",font=("calibri",21,"bold"),bg="#FFFACD")
     label_pokhara_overview.place(x=1240,y=55)
     label_pokhara_overview=Label(frame_a,text="Price\nRs 13000 per individual ",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1380,y=330)
    
     label_pokhara_overview=Label(frame_a,text="\tOpen hours    \n 6:00 AM to 6:00 PM",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1360,y=410)
     label_pokhara_overview=Label(frame_a,text="\tDuration \t\t \n 20 to 30 minutes",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1380,y=480)
     label_pokhara_overview=Label(frame_a,text="The above price includes:\n\t\tparagliding Flight\n\t\tPhotos and videos\n\t\tGovernmentTaxes\n\t\t Insurance package\n\t\t Pickup transport    ",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1220,y=570)
     book_button=Button(frame_a,text="Reserve Your Ticket",font=("Arial",19,"bold"),bg="#FFFACD",command=booking)
     book_button.place(x=1450,y=790)
     create_level(frame_a,"Click above buttons to reserve your seat ",1350,850)
     label_pokhara_overview=Label(frame_a,text="'Live a life by experiencing an adventerous sports'",font=("calibri",22,"bold"),bg="#FFFACD")
     label_pokhara_overview.place(x=1230,y=900)



def nagarkot():
     frame_a.config(width=1920,height=1080)
     frame_a.place(x=0,y=60)
     clear_frame()
   
     image=Image.open("nagarkot1.jpg")
     resized_image=image.resize((1200,600))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=0,y=0)
    
     image=Image.open("nagarkot.jpg")
     resized_image=image.resize((600,340))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=0,y=600)
     image=Image.open("nagarkot2.jpg")
     resized_image=image.resize((600,340))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=600,y=600)
    
     label_pokhara_overview=Label(frame_a,text="Overview",font=("arial",26,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1480,y=10)
     label_pokhara_overview=Label(frame_a,text="Nagarkot Dhulikhel Trek is one of the most popular\n trekking outside Kathmandu. Nagarkot is located just \n35km far from Kathmandu. We recommend you to\n take Nagarkot and Dhulikhel Trek if you are looking for\n short treks in Nepal. The nearest hill station from\n Kathmandu- Nagarkot view tower offers spectacular\n views of Central Himalaya including Langtang Mountain,\n Gaurishankar Mountain,Ganesh Mountain and Manaslu.",font=("calibri",21,"bold"),bg="#FFFACD")
     label_pokhara_overview.place(x=1220,y=55)
     label_pokhara_overview=Label(frame_a,text="Price\nRs 6000 per individual ",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1380,y=330)
    
     label_pokhara_overview=Label(frame_a,text="\tOpen hours    \n 6:00 AM to 6:00 PM",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1360,y=410)
     label_pokhara_overview=Label(frame_a,text="\tDuration \t\t \n 6-8 hrs minutes",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1380,y=480)
     label_pokhara_overview=Label(frame_a,text="The above price includes:\n\t\tBreakfast,Meal\n\t\tPhotos and videos\n\t\tGovernmentTaxes\n\t\t Insurance package\n\t\t Pickup transport    ",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1220,y=570)
     book_button=Button(frame_a,text="Reserve Your Ticket",font=("Arial",19,"bold"),bg="#FFFACD",command=booking)
     book_button.place(x=1450,y=790)
     create_level(frame_a,"Click above buttons to reserve your seat ",1350,850)
     label_pokhara_overview=Label(frame_a,text="'Live a life by experiencing an adventerous sports'",font=("calibri",22,"bold"),bg="#FFFACD")
     label_pokhara_overview.place(x=1230,y=900)



def koshi():
     frame_a.config(width=1920,height=1080)
     frame_a.place(x=0,y=60)
     clear_frame()
    
     image=Image.open("Koshi_rafting.jpg")
     resized_image=image.resize((1200,600))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=0,y=0)
    
     image=Image.open("Koshi_rafting1.jpg")
     resized_image=image.resize((600,340))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=0,y=600)
     image=Image.open("Koshi_rafting3.jpg")
     resized_image=image.resize((600,340))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=600,y=600)
    
     label_pokhara_overview=Label(frame_a,text="Overview",font=("arial",26,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1480,y=10)
     label_pokhara_overview=Label(frame_a,text="Bhote Koshi river rafting provide the closet Grade \nIV to V whitewater rafting experience on an extremely\n powerful rapid and whirlpool. Bhote Koshi river originates\n from the Tibetan plateau, which can easily access \nbecause it is not so away from Kathmandu. Bhote Koshi \nrafting is one of the best whitewater river rafting in \nthe world with full of excitement and fun.",font=("calibri",21,"bold"),bg="#FFFACD")
     label_pokhara_overview.place(x=1230,y=55)
     label_pokhara_overview=Label(frame_a,text="Price\nRs 13000 per individual ",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1380,y=330)
    
     label_pokhara_overview=Label(frame_a,text="\tOpen hours    \n 6:00 AM to 6:00 PM",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1360,y=410)
     label_pokhara_overview=Label(frame_a,text="\tDuration \t\t \n 20 to 30 minutes",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1380,y=480)
     label_pokhara_overview=Label(frame_a,text="The above price includes:\n\t\tLife Jacket to overcome risk\n\t\tPhotos and videos\n\t\tGovernmentTaxes\n\t\t Insurance package\n\t\t Pickup transport    ",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1220,y=570)
     book_button=Button(frame_a,text="Reserve Your Ticket",font=("Arial",19,"bold"),bg="#FFFACD",command=booking)
     book_button.place(x=1450,y=790)
     create_level(frame_a,"Click above buttons to reserve your seat ",1350,850)
     label_pokhara_overview=Label(frame_a,text="'Live a life by experiencing an adventerous sports'",font=("calibri",22,"bold"),bg="#FFFACD")
     label_pokhara_overview.place(x=1230,y=900)



def bhotekoshi():
     frame_a.config(width=1920,height=1080)
     frame_a.place(x=0,y=60)
     clear_frame()
    #  frame_a=Frame(root,width=1000,height=1200)
    #  frame_pokhara1.place(x=0,y=35)
     image=Image.open("Bhotekoshi2.jpg")
     resized_image=image.resize((1200,600))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=0,y=0)
    
     image=Image.open("Bhotekoshi.jpg")
     resized_image=image.resize((600,340))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=0,y=600)
     image=Image.open("Bhotekoshi1.jpg")
     resized_image=image.resize((600,340))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=600,y=600)
    
     label_pokhara_overview=Label(frame_a,text="Overview",font=("arial",26,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1480,y=10)
     label_pokhara_overview=Label(frame_a,text="Bungee jumping activity found its first ever spot at the\n Bhote Koshi gorge in Nepal. And now it is one of \nthe most famous spots for bungee jumping in the\n whole world. The gorge is located near Nepal-Tibet \nborder and has a height of 160 meters. What makes\n it special is the fact that is the highest bungee jumping\n in Nepal as well as the world. Flowing below the jump \nis the Bhote Koshi river which will give you the extra fun.",font=("calibri",21,"bold"),bg="#FFFACD")
     label_pokhara_overview.place(x=1240,y=55)
     label_pokhara_overview=Label(frame_a,text="Price\nRs 13000 per individual ",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1380,y=343)
    
     label_pokhara_overview=Label(frame_a,text="\tOpen hours    \n 6:00 AM to 6:00 PM",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1360,y=410)
     label_pokhara_overview=Label(frame_a,text="\tDuration \t\t \n 20 to 30 minutes",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1380,y=480)
     label_pokhara_overview=Label(frame_a,text="The above price includes:\n\t\tBunjee Ticket\n\t\tPhotos and videos\n\t\tGovernmentTaxes\n\t\t\tPickup transport\t\t    ",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1220,y=570)
     book_button=Button(frame_a,text="Reserve Your Ticket",font=("Arial",19,"bold"),bg="#FFFACD",command=booking)
     book_button.place(x=1450,y=790)
     create_level(frame_a,"Click above buttons to reserve your seat ",1350,850)
     label_pokhara_overview=Label(frame_a,text="'Live a life by experiencing an adventerous sports'",font=("calibri",22,"bold"),bg="#FFFACD")
     label_pokhara_overview.place(x=1230,y=900)



def mounteverest():
     frame_a.config(width=1920,height=1080)
     frame_a.place(x=0,y=60)
     clear_frame()
   
     image=Image.open("Everest1.png")
     resized_image=image.resize((1200,600))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=0,y=0)
    
     image=Image.open("MountEverest1.webp")
     resized_image=image.resize((600,340))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=0,y=600)
     image=Image.open("MountEverest2.jpg")
     resized_image=image.resize((600,340))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_a,image=converted)
     label.image=converted
     label.place(x=600,y=600)
    
     label_pokhara_overview=Label(frame_a,text="Overview",font=("arial",26,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1480,y=10)
     label_pokhara_overview=Label(frame_a,text="The Everest region in Nepal is more than just climbing \nand trekking, it is a life-changing experience and some\n see it as a journey close to achieving Nirvana,Located\n in the northeastern province of Nepal, this region is \nin a world of its own with vast glaciers, icefalls, the \nhighest mountains, deep valleys, precarious settlem-\nents, and hardy people challenging the harshest conditions \nthrown at them by nature in the thin air of high altitude.\t ",font=("calibri",21,"bold"),bg="#FFFACD")
     label_pokhara_overview.place(x=1210,y=55)
     label_pokhara_overview=Label(frame_a,text="Price\nRs 4000000 per individual ",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1380,y=330)
    
     label_pokhara_overview=Label(frame_a,text="\tOpen hours    \n 6:00 AM to 6:00 PM",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1360,y=410)
     label_pokhara_overview=Label(frame_a,text="\tDuration \t\t \n 20 to 30 minutes",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1380,y=480)
     label_pokhara_overview=Label(frame_a,text="The above price includes:\n\t\tCamping tent with amenities\n\t\tPhotos and videos\t\t\n\t\tGovernment Authority          \n\t\t Insurance package               ",font=("arial",21,"bold"),fg="grey",bg="#FFFACD")
     label_pokhara_overview.place(x=1230,y=570)
     book_button=Button(frame_a,text="Reserve Your Ticket",font=("Arial",19,"bold"),bg="#FFFACD",command=booking)
     book_button.place(x=1450,y=790)
     create_level(frame_a,"Click above buttons to reserve your seat ",1350,850)
     label_pokhara_overview=Label(frame_a,text="'Live a life by experiencing an adventerous sports'",font=("calibri",22,"bold"),bg="#FFFACD")
     label_pokhara_overview.place(x=1230,y=900)


topFrame = Frame(root, width = 1920, height = 680, bg = "#FFFACD")
topFrame.place(x = 0, y = 0)

bottomFrame = Frame(root, width = 1920, height = 500, bg = "#FFFACD")
bottomFrame.place(x = 0, y = 600)

backgroundImage = Image.open("mainbg.jpg")
resizeBackground = backgroundImage.resize((1920, 1160))
imageBackground = ImageTk.PhotoImage(resizeBackground)

logoImage = Image.open("flight.png")
resizeLogo = logoImage.resize((40, 40))
imageLogo = ImageTk.PhotoImage(resizeLogo)

bhaktapurImage = Image.open("bkt.jpg")
resizeBhaktapur = bhaktapurImage.resize((350, 200))
imageBhaktapur = ImageTk.PhotoImage(resizeBhaktapur)

patanImage = Image.open("patan.jpg")
resizePatan = patanImage.resize((350, 200))
imagePatan = ImageTk.PhotoImage(resizePatan)

pashupatiImage = Image.open("pashupati.jpg")
resizePashupati = pashupatiImage.resize((350, 200))
imagePashupati = ImageTk.PhotoImage(resizePashupati)

pokharaImage = Image.open("pkr.jpg")
resizePokhara = pokharaImage.resize((350, 200))
imagePokhara = ImageTk.PhotoImage(resizePokhara) 

backgroundLabel = Label(topFrame, image = imageBackground, border = 0, bg = "#FFFACD")
backgroundLabel.place(x = 0, y = 0)
bottomFrame_label=Label(bottomFrame,text="Top Destinations",font=("Helvetica Nue",30,"bold"),bg="#FFFACD")
bottomFrame_label.place(x=790,y=12)

frame1 = Frame(bottomFrame, width = 350, height = 350, bg = "#e4e4e4", border = 0)
frame1.place(x = 100, y = 70)

bhaktapurLabel = Label(frame1, image = imageBhaktapur, border = 0, bg = "#e4e4e4")
bhaktapurLabel.place(x = 0, y = 0)

bhaktapurLabel = Label(frame1,text="Bhaktapur Durbar Square\nPrice=Rs5000/person",font=25, border = 0, bg = "#e4e4e4")
bhaktapurLabel.place(x=57,y=220)

bhaktapurbutton=Button(frame1,text="Book Tour",font=30,bg="#EEEEE0",command=booking)
bhaktapurbutton.place(x=110,y=280)

frame2 = Frame(bottomFrame, width = 350, height = 350, bg = "#e4e4e4", border = 0)
frame2.place(x = 560, y = 70)

patanLabel = Label(frame2, image = imagePatan, border = 0, bg = "#e4e4e4")
patanLabel.place(x = 0, y = 0)

patanLabel= Label(frame2,text="Patan Durbar Square\nPrice=Rs5000/person",font=25, border = 0, bg = "#e4e4e4")
patanLabel.place(x=57,y=220)

patanbutton=Button(frame2,text="Book Tour",font=30,bg="#EEEEE0",command=booking)
patanbutton.place(x=110,y=280)

frame3 = Frame(bottomFrame, width = 350, height = 350, bg = "#e4e4e4", border = 0)
frame3.place(x = 1020, y = 70)

pashupatiLabel = Label(frame3, image = imagePashupati, border = 0, bg = "#e4e4e4")
pashupatiLabel.place(x = 0, y = 0)

pashupatiLabel = Label(frame3,text="Pashupatinath Temple\nPrice=Rs5000/person",font=25, border = 0, bg = "#e4e4e4")
pashupatiLabel.place(x=57,y=220)

pashupatibutton=Button(frame3,text="Book Tour",font=30,bg="#EEEEE0",command=booking)
pashupatibutton.place(x=110,y=280)

frame4 = Frame(bottomFrame, width = 350, height = 350, bg = "#e4e4e4", border = 0)
frame4.place(x = 1480, y = 70)

pokharaLabel = Label(frame4, image = imagePokhara, border = 0, bg = "#e4e4e4")
pokharaLabel.place(x = 0, y = 0)

pokharaLabel = Label(frame4,text="Pokhara\nPrice=Rs5000/person",font=25, border = 0, bg = "#e4e4e4")
pokharaLabel.place(x=57,y=220)

pokharabutton=Button(frame4,text="Book Tour",font=30,bg="#EEEEE0",command=booking)
pokharabutton.place(x=110,y=280)

buttonFrame = Frame(root, width = 1920, height = 68, border = 0, bg = "#FFFACD")
buttonFrame.place(x = 0, y = 0)

headingTitle = Label(buttonFrame, image = imageLogo, compound = LEFT, text = "  Tours & Travels Booking", bg = "#FFFACD", font = ("Helvetica Neue", 22, "bold"))
headingTitle.place(x = 34, y = 10)

frame_a=Frame(root,width=600,height=200,bg="#FFFACD")

def hello():
    clear_frame() 
    frame_a.config(width=1200)
    frame_a.config(height=1200)
    frame_a.place(x=20,y=40)
     
    button_booking=Button(frame_a,text="Book Your tour ",font=40,fg="green")
    button_booking.configure(width=10,height=2)

    button_booking.place(x=320,y=760)
    image=Image.open("mainbg.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("mainbg.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_a,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_a,text="Tour to muktinath(Temple of janak)",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_a,text="From kathmandu to Dhanusha",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=470,y=510)
    
    labeel1=Label(frame_a,text="Duration\n3 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_a,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_a,text="Age Group \nAll age group",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_a,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t Medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_a,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_a,text="District\nSolukhumbu",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_a,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_a,text=" muktinath dham is a tour of historical sites at muktinath ,birthplace of sita. All the hindu people\n worshipped this place as a great ceremony in chhath. Jankpur is popular with different historical and \nrelifious events. It is one of the most holy places of hindus.  You can get a chance to explore\n maithili culture and traditions by visiting there.",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_a,text="Day1: Kathmandu to Shree Ram a Mandir (225 km) 7/8 hours. Overnight Stay. \nDay2:     Puja and full day sightseeing. Overnight Stay                      \nDay3: Drive back to Kathmandu by vehicles-7/8 hours.     ",font=("Avenir",17))
    labeel9.place(x=850,y=660)

        
def hi():
    clear_frame() 
    frame_a.config(width=800)
    frame_a.config(height=200)
    frame_a.place(x=600,y=250)

def log_in():
    root.destroy()
    import signup 

def signup():
    root.destroy()
    import signup


def on_enter_home():
    root.destroy()
    import Tour

def on_enter_destination(e):
    frame_a.config(width=1600,height=150)
    frame_a.place(x=300,y=70)
    clear_frame() # clearing the frame before placing the buttons hello and hi...

    create_level(frame_a, "Koshi Province",10,10)
    create_level(frame_a, "Madhesh Province",215,10) 
    create_level(frame_a, "Bagmati Province",465,10)
    create_level(frame_a, "Gandaki Province",685,10)
    create_level(frame_a, "Lumbini Province",895,10)
    create_level(frame_a, "Karnali Province",1100,10)
    create_level(frame_a, "Sudurpashchim Province",1320,10)
    
    create_button(frame_a, "Everest Base Camp", 10, 80,everest1) # passing the arguments to the parameter...
    create_button(frame_a, "Janakpur", 230, 80 ,janakpur)
    create_button(frame_a, "Pashupatinath", 470,80,pashupatinath)
    create_button(frame_a, "Muktinath Temple", 690, 80 ,muktinath)
    create_button(frame_a, "Lumbini", 890, 80 ,lumbini)
    create_button(frame_a, "Rara Lake", 1090, 80 ,rara)
    create_button(frame_a, "Khaptad",1320 , 80 ,khaptad)




def on_enter_adventure(e):
    frame_a.config(width=1200)
    frame_a.config(height=150)
    frame_a.place(x=300,y=70)
    clear_frame() # clearing the frame before placing the buttons hello and hi...
    create_level(frame_a, "Paragliding",10,10)
    create_level(frame_a, "Trekking",260,10)
    create_level(frame_a, "Rafting",510,10)
    create_level(frame_a,  "Bungee Jumping",730,10)
    create_level(frame_a, "Mountaineering",1010,10)
    
    create_button(frame_a, "Pokhara Sarangkot", 5, 60,pokhara) # passing the arguments to the parameter... 
    create_button(frame_a, "Nagarkot", 260, 60 ,nagarkot)
    create_button(frame_a, "Koshi Rafting", 505, 60 ,koshi)
    create_button(frame_a, "BhoteKoshi", 730, 60 ,bhotekoshi)
    create_button(frame_a, "Mount Everest", 1010, 60 ,mounteverest)


def on_enter_help(e):
    frame_a.config(width=1150,height=350)
    frame_a.place(x=700,y=70)
    clear_frame()
    create_level(frame_a,"Problems",215,20)
    create_level(frame_a,"Feedback",800,20)
    create_level(frame_a,"Username",10,262)

    # clearing the frame before placing the buttons hello and hi...
    problems_text=Text(frame_a,height=9,width=60,font=("Helvetica",12,"bold"))
    problems_text.place(x=20,y=60)
    feedback_text=Text(frame_a,height=9,width=60,font=("Helvetica",12,"bold"))
    feedback_text.place(x=590,y=60)
    username_entry=Entry(frame_a,width=63)
    username_entry.place(x=120,y=260,height=35)
    submit_button=Button(frame_a,text="Submit",font=("Arial",16,"bold"),width=15,bg="#FFFACD")
    submit_button.place(x=600,y=260)
    
    
  
def on_enter_contact(e):
    frame_a.config(width=700,height=500)
    frame_a.place(x=1200,y=70)
    clear_frame() # clearing the frame before placing the buttons hello and hi...

    create_button(frame_a, "I am krishna", 50, 50,hello) # passing the arguments to the parameter...

    create_button(frame_a, "Fine", 150, 50,hello) 
    
#Create frame when hovered over account frame
def on_enter_account(e):
    frame_a.config(width=220,height=120)
    frame_a.place(x=1700,y=70)
    clear_frame() # clearing the frame before placing the buttons hello and hi...
    create_button(frame_a, "Login",50, 20, log_in ) # passing the arguments to the parameter...
    create_button(frame_a, "Sign Up",50, 50, signup) 


def create_main_button(buttonFrame, text, x , y, cmd):
    
    button = Button(buttonFrame, text=text, font = ("Tahoma", 14, "bold"), border = 0, bg = "#FFFACD", cursor = "hand2", command = cmd)
    
    button.bind("<Enter>", cmd)
    # button.bind("<Leave>", on_frame_leave)
    button.place(x=x, y=y)
    
        
    return button

def clear_frame(): # Line 12 and 22 are the functionality provided by this function...
    for widget in frame_a.winfo_children(): # fetches the information/name of buttons created in the frames...
        widget.destroy() # triggering the deletion of buttons that are already in there...
buttons = []

home_button =Button(buttonFrame,text="Home",bg="#FFFACD", font = ("Tahoma", 14, "bold"),bd=0,command = on_enter_home)
home_button.place(x=592,y=16)
buttons.append(create_main_button(buttonFrame, "Destination", 762, 16, on_enter_destination))
buttons.append(create_main_button(buttonFrame, "Adventure Type", 988, 16,on_enter_adventure))
buttons.append(create_main_button(buttonFrame, "Help and Feedback", 1268, 16,on_enter_help))
buttons.append(create_main_button(buttonFrame, "Contacts", 1574, 16,on_enter_contact))
buttons.append(create_main_button(buttonFrame, "Account", 1784, 16,on_enter_account))

root.mainloop()
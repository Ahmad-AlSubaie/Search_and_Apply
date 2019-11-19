import tkinter as tk #tkinter is our gui lib.
import webbrowser #webbrowser allows us to open user's default web browser. good for clicking on links.
import jsonlines
import io
import genCoverLetter as gcl

from Search_and_Apply.Search_and_Apply.spiders.IndeedSpider import searchFor
from Search_and_Apply.Search_and_Apply.IndeedExpressApply import ExpressApply



if __name__ == '__main__':#not sure what this does. might delete later.
    root = tk.Tk()#initialization of root.
    #what follows are some global variables.
    keywords = []
    links = ["link1","link2","link3","link4","link5"]
    name = "empty"
    email = "empty"
    position = "A fine position"
    company = "A fine company"
    phone = "777"

    def BuildMenu(): #buildmenu is called each time the main window is changed. just builds the menu.
        mb = tk.Menubutton(root,text="Menu")
        mb.grid(row=0,column=0)
        mb.menu =  tk.Menu (mb, tearoff = 0)
        mb["menu"] =  mb.menu
        mb.menu.add_command(label="Keywords",command=Keywords)
        mb.menu.add_command(label="Resume",command=Resume)
        mb.menu.add_command(label="Cover Letter",command=CoverLetter)
        mb.menu.add_command(label="Profile",command=Profile)
        mb.menu.add_command(label="Job Listings",command=Listings)
        mb.menu.add_command(label="Additional Information",command=AdditionalInfo)
        mb.menu.add_command(label="Quit",command=Quit)

    def Keywords(): #keywords page.
        for widget in root.winfo_children(): #eliminates all widgets. clears the window.
            widget.destroy()
        BuildMenu()
        tk.Message(root,text="Keywords",width=3000).grid(row=1,column=1) #message.
        tk.Label(root,text="Search Keywords").grid(row=2,column=1) #label
        key_ent = tk.Entry(root) #text entry
        key_ent.grid(row=2,column=2)
        tk.Button(root,text="Search",command=lambda:search(key_ent.get())).grid(row=2,column=3) #search button

    def search(new_keywords): #run one search per keyword. needs work. shouldn't take long.
        global keywords #imports global keywords list
        keywords = new_keywords #saves input from text entry field
        searchFor([keywords])
        print("searching... %s" % keywords)
        display_links()


    def clettergen():
        global position
        global company
        global name
        global email
        to_csv()
        gcl.write_cover_letter()

    def apply(L): #given name and email and a list of relevant links, call applyTo. needs some work. shouldn't take long.
        global name
        global email
        global links
        global applyBot

        applyBot.applyTo(L)

    def open_link(event): #simply opens the links.
        webbrowser.open_new_tab(event)

    def Resume(): #resume page. needs some work. shouldn't take long.
        for widget in root.winfo_children(): #eliminates all widgets. clears the window.
            widget.destroy()
        BuildMenu()
        tk.Message(root,text="Resume",width=3000).grid(row=1,column=1)

    def CoverLetter(): #coverletter page. needs some work. shouldn't take long.
        for widget in root.winfo_children(): #eliminates all widgets. clears the window.
            widget.destroy()
        BuildMenu()
        tk.Message(root,text="Cover Letter",width=3000).grid(row=1,column=1)

        tk.Label(root,text="Name").grid(row=3,column=1)
        name_ent = tk.Entry(root)
        name_ent.grid(row=3,column=2)
        tk.Button(root,text="Save Name",command=lambda: save_name(name_ent.get())).grid(row=3,column=3)

        tk.Label(root,text="Email").grid(row=4,column=1)
        email_ent = tk.Entry(root)
        email_ent.grid(row=4,column=2)
        tk.Button(root,text="Save Email",command=lambda: save_email(email_ent.get())).grid(row=4,column=3)

        tk.Label(root,text="Position").grid(row=5,column=1)
        position_ent = tk.Entry(root)
        position_ent.grid(row=5,column=2)
        tk.Button(root,text="Save Position",command=lambda: save_position(position_ent.get())).grid(row=5,column=3)

        tk.Label(root,text="Company").grid(row=6,column=1)
        company_ent= tk.Entry(root)
        company_ent.grid(row=6,column=2)
        tk.Button(root,text="Save Company",command=lambda: save_company(company_ent.get())).grid(row=6,column=3)

        tk.Label(root,text="Phone").grid(row=7,column=1)
        phone_ent= tk.Entry(root)
        phone_ent.grid(row=7,column=2)
        tk.Button(root,text="Phone",command=lambda: save_phone(phone_ent.get())).grid(row=7,column=3)

        tk.Button(root,text="Generate Cover Letter",command=clettergen).grid(row=9,column=2)
        #takes keywords, generates pdf.

    def save_phone(new_phone):
        global phone
        phone = new_phone
        print("Saving phone as %s" % phone)

    def to_csv():
        #to comma-separated string
        step1 = [position+","+company+","+name+","+email]
        step2 = ",".join(step1)
        s=io.StringIO(step2)
        with open('info.csv','w') as f:
            for line in s:
                f.write(line)

    def Profile(): #profile page. essentially finished.
        for widget in root.winfo_children():
            widget.destroy()
        BuildMenu()
        tk.Message(root,text="Profile",width=3000).grid(row=1,column=1)
        tk.Label(root,text="Name").grid(row=2,column=1)
        name_ent = tk.Entry(root)
        name_ent.grid(row=2,column=2)
        tk.Button(root,text="Save Name",command=lambda: save_name(name_ent.get())).grid(row=2,column=3)

        tk.Label(root,text="Email").grid(row=3,column=1)
        email_ent = tk.Entry(root)
        email_ent.grid(row=3,column=2)
        tk.Button(root,text="Save Email",command=lambda: save_email(email_ent.get())).grid(row=3,column=3)

        global applyBot
        applyBot = ExpressApply(name_ent, email_ent)

        #we could add things here. profile1, profile2, etc. would take some time.

    def save_name(new_name): #simply saves name from text field to global var.
        global name
        name = new_name
        print("Saving name as %s" % name)

    def save_email(new_email): #simply saves email from text field to global var.
        global email
        email = new_email
        print("Saving email as %s" % email)

    def Listings(): #listings page. functional.
        for widget in root.winfo_children():
            widget.destroy()
        BuildMenu()
        tk.Message(root,text="Job Listings",width=3000).grid(row=1,column=1)
        display_links()

    def display_links(): #fun function. turns global links list into hyperlinks in the window.


        with jsonlines.open("URLs_from_IndeedSpider.json", mode ='r') as reader:
            distros_dict = reader.iter(type = dict)

            global links
            i=0
            hyperlinks=[]
            for link in distros_dict:
                hyperlinks.append(tk.Label(root,text=link['Title'],fg="blue",cursor="hand2"))
                hyperlinks[i].grid(row=i+10,column=1)
                hyperlinks[i].bind("<Button-1>", lambda e: open_link(link['Link'])) #button-1 means left-click.
                tk.Button(root,text="Apply",command=apply).grid(row=i+10,column=2)
                i+=1

    def AdditionalInfo(): #additional info page.
        for widget in root.winfo_children():
            widget.destroy()
        BuildMenu()
        tk.Message(root,text="Additional Information",width=3000).grid(row=1,column=1)
        #not sure what goes here, if we're doing this, etc.

    def Quit(): #simply quits.
        root.destroy()
        exit()

    BuildMenu()
    root.geometry("640x480")
    tk.Message(root,text="welcome to Search and Apply.",width=3000).grid(row=1,column=1)
    root.mainloop() #starts the engine.

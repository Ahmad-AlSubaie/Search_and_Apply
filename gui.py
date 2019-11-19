import tkinter as tk #tkinter is our gui lib.
import webbrowser #webbrowser allows us to open user's default web browser. good for clicking on links.

from Search_and_Apply.Search_and_Apply.spiders.IndeedSpider import searchFor
from Search_and_Apply.Search_and_Apply.IndeedExpressApply import ExpressApply



if __name__ == '__main__':#not sure what this does. might delete later.
    root = tk.Tk()#initialization of root.
    #what follows are some global variables.
    keywords = []
    links = ["link1","link2","link3","link4","link5"]
    name = "empty"
    email = "empty"

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
        tk.Button(root,text="Search",command=lambda:searchFor([key_ent.get()])).grid(row=2,column=3) #search button

    def search(new_keywords): #run one search per keyword. needs work. shouldn't take long.
        global keywords #imports global keywords list
        keywords = new_keywords #saves input from text entry field
        print("searching... %s" % keywords)
        display_links()

    def apply(): #given name and email and a list of relevant links, call applyTo. needs some work. shouldn't take long.
        global name
        global email
        global links
        print("Applying...")

    def open_link(event): #simply opens the links.
        webbrowser.open_new_tab(event.widget.cget("text"))

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
        tk.Label(root,text="Search Keywords").grid(row=2,column=1) #some labels, entries, and buttons.
        key_ent = tk.Entry(root)
        key_ent.grid(row=2,column=2)
        tk.Button(root,text="Search",command=lambda:search(key_ent.get())).grid(row=2,column=3)

        tk.Label(root,text="Name").grid(row=3,column=1)
        name_ent = tk.Entry(root)
        name_ent.grid(row=3,column=2)
        tk.Button(root,text="Save Name",command=lambda: save_name(name_ent.get())).grid(row=3,column=3)

        tk.Label(root,text="Email").grid(row=4,column=1)
        email_ent = tk.Entry(root)
        email_ent.grid(row=4,column=2)
        tk.Button(root,text="Save Email",command=lambda: save_email(email_ent.get())).grid(row=4,column=3)

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
        global links
        i=0
        hyperlinks=[]
        for link in links:
            hyperlinks.append(tk.Label(root,text=link,fg="blue",cursor="hand2"))
            hyperlinks[i].grid(row=i+10,column=1)
            hyperlinks[i].bind("<Button-1>",open_link) #button-1 means left-click.
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

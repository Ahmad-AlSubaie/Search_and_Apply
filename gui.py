import tkinter as tk
import webbrowser

if __name__ == '__main__':
    root = tk.Tk()
    keywords = []
    links = ["link1","link2","link3","link4","link5"]
    name = "empty"
    email = "empty"
    
    def BuildMenu():
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
        
    def Keywords():
        for widget in root.winfo_children():
            widget.destroy()
        BuildMenu()
        tk.Message(root,text="Keywords",width=3000).grid(row=1,column=1)
        tk.Label(root,text="Search Keywords").grid(row=2,column=1)
        key_ent = tk.Entry(root)
        key_ent.grid(row=2,column=2)
        tk.Button(root,text="Search",command=lambda:search(key_ent.get())).grid(row=2,column=3)
        
    def search(new_keywords):
        global keywords
        keywords = new_keywords
        #run one search per keyword
        print("searching... %s" % keywords)
        display_links()
        
    def apply():
        #given name and email and a list of relevant links, call applyTo
        print("Applying...")
        
    def open_link(event):
        webbrowser.open_new_tab(event.widget.cget("text"))

    def Resume():
        for widget in root.winfo_children():
            widget.destroy()
        BuildMenu()
        tk.Message(root,text="Resume",width=3000).grid(row=1,column=1)
        #input resume?
        
    def CoverLetter():
        for widget in root.winfo_children():
            widget.destroy()
        BuildMenu()
        tk.Message(root,text="Cover Letter",width=3000).grid(row=1,column=1)
        tk.Label(root,text="Search Keywords").grid(row=2,column=1)
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
        #give keywords to cover letter function
        
    def Profile():
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
        
    def save_name(new_name):
        global name
        name = new_name
        print("Saving name as %s" % name)
        
    def save_email(new_email):
        global email
        email = new_email
        print("Saving email as %s" % email)
        
    def Listings():
        for widget in root.winfo_children():
            widget.destroy()
        BuildMenu()
        tk.Message(root,text="Job Listings",width=3000).grid(row=1,column=1)
        display_links()

    def display_links():
        global links
        i=0
        hyperlinks=[]
        for link in links:
            hyperlinks.append(tk.Label(root,text=link,fg="blue",cursor="hand2"))
            hyperlinks[i].grid(row=i+10,column=1)
            hyperlinks[i].bind("<Button-1>",open_link)
            i+=1
    
    def AdditionalInfo():
        for widget in root.winfo_children():
            widget.destroy()
        BuildMenu()
        tk.Message(root,text="Additional Information",width=3000).grid(row=1,column=1)
        #not sure what goes here, if we're doing this, etc.
        
    def Quit():
        root.destroy()
        exit()
    
    BuildMenu()
    root.geometry("640x480")
    tk.Message(root,text="welcome to Search and Apply.",width=3000).grid(row=1,column=1)
    root.mainloop()

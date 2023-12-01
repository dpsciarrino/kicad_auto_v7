from tkinter import *
from constants import TODAY_DATE, CONFIG_FILE

def config():
    entries = []

    root = Tk()
    root.title("KiCAD Startup Configuration")
    frame = Frame(root)

    ctx = [
        {
            "text": "Project Name: ",
            "rowcol": (0,0),
            "element": "Label"
        },
        {
            "text": "Sheet 1 Title: ",
            "rowcol": (1,0),
            "element": "Label"
        },
        {
            "text": "Sheet 1 Subtitle: ",
            "rowcol": (2,0),
            "element": "Label"
        },
        {
            "text": "Revision: ",
            "rowcol": (3,0),
            "element": "Label"
        },
        {
            "text": "Author: ",
            "rowcol": (4,0),
            "element": "Label"
        },
        {
            "text": "Project Name",
            "rowcol": (0,1),
            "element": "Entry"
        },
        {
            "text": "Title",
            "rowcol": (1,1),
            "element": "Entry"
        },
        {
            "text": "Subtitle",
            "rowcol": (2,1),
            "element": "Entry"
        },
        {
            "text": "Revision",
            "rowcol": (3,1),
            "element": "Entry"
        },
        {
            "text": "Author",
            "rowcol": (4,1),
            "element": "Entry"
        }
    ]

    def add_elements(parent_frame: Frame):
        for i in range(0, len(ctx)):
            config = ctx[i]
            element_type = config['element']
            
            if element_type == 'Label':
                label_text = config['text']
                label_row = config['rowcol'][0]
                label_col = config['rowcol'][1]

                Label(parent_frame, text=label_text, anchor=E, width=15).grid(row=int(label_row), column=int(label_col))
            
            elif element_type == 'Entry':
                entry_row = config['rowcol'][0]
                entry_col = config['rowcol'][1]

                e = Entry(parent_frame, width=50, bg='white', fg='black', borderwidth='2px')
                entries.append(e)

                e.grid(row=entry_row, column=entry_col)
    
    add_elements(frame)

    def enter():
        project_id = entries[0].get()
        title = entries[1].get()
        subtitle1 = entries[2].get()
        revision = entries[3].get()
        author = entries[4].get()

        # No empty fields allowed
        if project_id == "" or title == "" or subtitle1 == "" or revision == "" or author == "":
            print("Please fill in all fields.")
            return -1

        try:
            # writing to configuration file (config.txt)
            with open(CONFIG_FILE, 'w') as cfg:
                cfg.write(f"PROJECT_NAME='{project_id}'\n")
                cfg.write(f"TITLE='{title}'\n")
                cfg.write(f"REV='{revision}'\n")
                cfg.write(f"AUTHOR='{author}'\n")
                cfg.write(f"COMMENT1='{title}'\n")
                cfg.write(f"COMMENT2='{subtitle1}'\n")
                cfg.write(f"COMMENT3=''\n")
                cfg.write(f"COMMENT4=''\n")
                cfg.write(f"DATE='{TODAY_DATE}'")

                cfg.close()
            
            # Close the configuration popup
            root.destroy()

        except Exception as e:
            print(e.args)

    Button(frame, text="Enter", padx=25, pady=10, command=enter).grid(row=len(entries), column=0, columnspan=2)
    Button(frame, text="Cancel", padx=25, pady=10, command=exit).grid(row=len(entries)+1, column=0, columnspan=2)

    frame.pack(padx=25, pady=25)

    root.mainloop()
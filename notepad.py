#NOTEPAD
import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
#from tkinter import tkFileDialog
import os

main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("Notepad")

main_menu=tk.Menu()
new_icon = tk.PhotoImage(file ="My icons/new.png")
open_icon = tk.PhotoImage(file ="My icons/open.png")
save_icon = tk.PhotoImage(file ="My icons/save.png")
saveas_icon = tk.PhotoImage(file ="My icons/saveas.png")
exit_icon = tk.PhotoImage(file ="My icons/exit.png")

#file menu
file=tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File",menu=file)

text_url=" "
def new_file(event=None):
    global text_url
    text_url=" "
    text_editor.delete(1.0, tk.END)

file.add_command(label="New", compound=tk.LEFT,accelerator="ctrl+N", image=new_icon, command=new_file)

def open_file(event=None):
    global text_url
    text_url=filedialog.askopenfilename(initialdir=os.getcwd(), title="select file", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
    try:
        with open(text_url, "r") as for_read:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(text_url))

file.add_command(label="Open", compound=tk.LEFT,accelerator="ctrl+O", image=open_icon, command=open_file)


'''def save_file(event=None):
    global text_url
    try:
        if text_url:
            content=str(text_editor.get(1.0, tk.END))
            with open(text_url,"w",encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            content2= text_editor.get(1.0, tk.END)
            text_url = filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
            text_url.write(content2)
            text_url.close()
    except:
        #print("not working")
        return

file.add_command(label="Save", compound=tk.LEFT,accelerator="ctrl+S", image=save_icon, command=save_file)
'''
def save_file(event=None):
    global text_url
    try:
        content=text_editor.get(1.0, tk.END)
        text_url=filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
        text_url.write(content)
        text_url.close()
    except:
        #print("not working")
        return


file.add_command(label="Save", compound=tk.LEFT, accelerator="ctrl+S" ,image=saveas_icon, command=save_file)

def exit_fun(event=None):
    global text_change, text_url
    try:
        if text_change:
            mbox=messagebox.askyesnocancel("Warning","Do you want to save this file")
            if mbox is True:
                if text_url:
                    content=text_editor.get(1.0, tk.END)
                    with open(text_url, "w", encoding="utf-8") as for_read:
                        for_read.write(content)
                        main_application.destroy()
                else:
                    content2=text_editor.get(1.0, tk.END)
                    text_url=filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
                    text_url.write(content2)
                    text_url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
        
file.add_command(label="Exit", compound=tk.LEFT, image=exit_icon, command=exit_fun)
#main_application.config(menu=main_menu)

#edit menu
edit=tk.Menu(main_menu, tearoff=False)
cut_icon=tk.PhotoImage(file="My icons/cut.png")
copy_icon=tk.PhotoImage(file="My icons/copy.png")
paste_icon=tk.PhotoImage(file="My icons/clipboard.png")
find_icon=tk.PhotoImage(file="My icons/search.png")
clearall_icon=tk.PhotoImage(file="My icons/trash.png")

#find func
def find_func(event=None):
    def find():
        word=find_input.get()
        text_editor.tag_remove("match", "1.0", tk.END)
        matches=0
        if word:
            start_pos="1.0"
            while True:
                start_pos=text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos= f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config("match", foreground="red", background="yellow")

    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0, tk.END)
        new_content=content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)


    find_popup=tk.Toplevel()
    find_popup.geometry("450x200")
    find_popup.title("Find Word")
    find_popup.resizable(0,0)
    #frame for find
    find_frame=ttk.LabelFrame(find_popup, text="find and replace")
    find_frame.pack(pady=20)

    #label
    text_find=ttk.Label(find_frame, text="Find")
    text_replace=ttk.Label(find_frame, text="Replace")

    #Entry box
    find_input=ttk.Entry(find_frame, width=30)
    replace_input=ttk.Entry(find_frame, width=30)

    #buttons
    find_button=ttk.Button(find_frame, text="Find", command=find)
    replace_button=ttk.Button(find_frame, text="Replace", command=replace)

    #text level grid
    text_find.grid(row=0, column=0, padx=4, pady=4)
    text_replace.grid(row=1, column=0, padx=4, pady=4)

    #entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    #button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)




main_menu.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Cut", compound=tk.LEFT,accelerator="ctrl+X", image=cut_icon, command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label="Copy", compound=tk.LEFT,accelerator="ctrl+C", image=copy_icon, command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", compound=tk.LEFT,accelerator="ctrl+V", image=paste_icon, command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label="Find", compound=tk.LEFT,accelerator="ctrl+F", image=find_icon, command=find_func)
edit.add_command(label="Clear all", compound=tk.LEFT, image=clearall_icon, command=lambda: text_editor.delete(1.0, tk.END))


#status bar and tool bar 
show_status_bar=tk.BooleanVar()
show_status_bar.set(True)
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar_label.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bars.pack_forget()
        tool_bar_label.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bars.pack(side=tk.BOTTOM)
        show_toolbar=True

def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar=False
    else:
        status_bars.pack(side=tk.BOTTOM)
        show_status_bar=True


#view menu
view= tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="View", menu=view)
view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=0, variable = show_status_bar,compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label="Status Bar", onvalue=True, offvalue=0, variable= show_toolbar, compound=tk.LEFT, command=hide_statusbar)

'''#color menu
color_theme=tk.Menu(main_menu, tearoff=False)
theme_choose = tk.StringVar()
main_menu.add_cascade(label="Color Theme", menu=color_theme)
light_icon=tk.PhotoImage(file="My icons/sunlight.png")
dark_icon=tk.PhotoImage(file="My icons/dark.png")
color_icons=(light_icon, dark_icon)


#color theme set
color_dict={
    'Light':("#000000","#ffffff"),
    'Dark':("#c4c4c4","#2d2d2d")
    }

#color theme function
def change_theme():
    try:
        get_theme= theme_choose.get()
        colour_tuple=color_dict.get(get_theme)
        print(colour_tuple)
        fg_color, bg_color = str(colour_tuple[0]), str(colour_tuple[1])
        text_editor.config(background=bg_color, fg=fg_color)
    except:
        print(theme_choose)
        return        

count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], compound=tk.LEFT, command=change_theme)
    count+=1'''



#tool bar labels
tool_bar_label=ttk.Label(main_application)
tool_bar_label.pack(side=tk.TOP, fill=tk.X)

font_tuples=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar_label, width=15, textvariable=font_family, state="readonly")
font_box["values"]=font_tuples
font_box.current(font_tuples.index("Arial"))
font_box.grid(row=0,column=0, padx=5, pady=3)

#sizebox
size_variable=tk.IntVar()
font_size=ttk.Combobox(tool_bar_label, width=4, textvariable=size_variable, state="readonly")
font_size["values"]=tuple(range(8,82,2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=1, pady=2)

#bold button
bold_icon=tk.PhotoImage(file="My icons/bold-button.png")
bold_btn=ttk.Button(tool_bar_label, image=bold_icon)
bold_btn.grid(row=0, column=2)

#italic button
italic_icon=tk.PhotoImage(file="My icons/italic.png")
italic_btn=ttk.Button(tool_bar_label, image=italic_icon)
italic_btn.grid(row=0, column=3)

#underline button
underline_icon=tk.PhotoImage(file="My icons/underline.png")
underline_btn=ttk.Button(tool_bar_label, image=underline_icon)
underline_btn.grid(row=0, column=4)

#fontcolor button
fontcolor_icon=tk.PhotoImage(file="My icons/font.png")
fontcolor_btn=ttk.Button(tool_bar_label, image=fontcolor_icon)
fontcolor_btn.grid(row=0, column=5)

#align left button
alignleft_icon=tk.PhotoImage(file="My icons/text-alignment.png")
alignleft_btn=ttk.Button(tool_bar_label, image=alignleft_icon)
alignleft_btn.grid(row=0, column=6)

#align centre button
aligncentre_icon=tk.PhotoImage(file="My icons/align.png")
aligncentre_btn=ttk.Button(tool_bar_label, image=aligncentre_icon)
aligncentre_btn.grid(row=0, column=7)

#align right button
alignright_icon=tk.PhotoImage(file="My icons/align-right.png")
alignright_btn=ttk.Button(tool_bar_label, image=alignright_icon)
alignright_btn.grid(row=0, column=8)

#text Editor

text_editor=tk.Text(main_application)
text_editor.config(wrap="word", relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#status bar word and character count

status_bars=ttk.Label(main_application, text="Status Bar")
status_bars.pack(side=tk.BOTTOM)

#function character count
text_change=False
def change_word(event=None):
    global text_change
    if text_editor.edit_modified():
        text_change=True
        word=len(text_editor.get(1.0, "end-1c").split())
        character=len(text_editor.get(1.0, "end-1c").replace(" ",""))
        status_bars.config(text= f"character: {character} word: {word} ")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", change_word)
#function character count ends

#font family funtionality
font_now="Arial"
font_size_now=16

def change_font(main_applicatoin):
    global font_now
    font_now=font_family.get()
    text_editor.configure(font=(font_now, font_size_now))

def change_size(main_application):
    global font_size_now
    font_size_now=size_variable.get()
    text_editor.configure(font=(font_now, font_size_now))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_size)

#bold function
#print(tk.font.Font(font=text_editor["font"]).actual())
def bold_fun():
    text_get=tk.font.Font(font=text_editor["font"])
    if text_get.actual()["weight"]=="normal":
        text_editor.configure(font=(font_now, font_size_now, "bold"))
    if text_get.actual()["weight"]=="bold":
        text_editor.configure(font=(font_now, font_size_now, "normal"))

bold_btn.configure(command=bold_fun)

def iatlic_fun():
    text_get=tk.font.Font(font=text_editor["font"])
    if text_get.actual()["slant"]=="roman":
        text_editor.configure(font=(font_now, font_size_now, "italic"))
    if text_get.actual()["weight"]=="italic":
        text_editor.configure(font=(font_now, font_size_now, "slant"))

italic_btn.configure(command=iatlic_fun)


def underline_fun():
    text_get=tk.font.Font(font=text_editor["font"])
    if text_get.actual()["underline"]==0:
        text_editor.configure(font=(font_now, font_size_now, "underline"))
    if text_get.actual()["weight"]=="underline":
        text_editor.configure(font=(font_now, font_size_now, "normal"))

underline_btn.configure(command=underline_fun)

def color_choose():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

fontcolor_btn.configure(command=color_choose)

def align_left():
    text_get_all=text_editor.get(1.0, "end")
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "left")

alignleft_btn.configure(command=align_left)

def align_center():
    text_get_all=text_editor.get(1.0, "end")
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "center")

aligncentre_btn.configure(command=align_center)

def align_right():
    text_get_all=text_editor.get(1.0, "end")
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "right")

alignright_btn.configure(command=align_right)


main_application.config(menu=main_menu)
main_application.mainloop()

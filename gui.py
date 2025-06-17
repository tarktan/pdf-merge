import tkinter
from tkinter import ttk

class WidgetClass:
    def __init__(self, widget, parent, **kwargs):
        self.parent = parent
        self.widget = widget
        match widget:
            case 'Frame':
                self.widget = ttk.Label(self.parent, **kwargs)
            case 'Label':
                self.widget = ttk.Label(self.parent, **kwargs)
            case 'Button':
                self.widget = tkinter.Button(self.parent, **kwargs)
        self.widget.image = kwargs.get('image', None)

    def create(self, r, c, x=0, y=0, cs=1, rs=1):
        self.widget.grid(row=r, column=c, padx=x, pady=y, columnspan=cs, rowspan=rs)
        return self.widget

    def change(widget, update, state='normal', sbStart=0, sbEnd=0, w=10, **kwargs):
        print(widget.widgetName)
        match widget.widgetName:
            case 'ttk::frame':
                widget.configure(text=update, borderwidth=0, **kwargs)
            case 'ttk::label':
                widget.configure(text=update, justify='center', **kwargs)
            case 'button':
                widget.configure(text=update, state=state, bd=0, **kwargs)
                print(ttk.Style().configure("TButton"))
                print(ttk.Style().configure("Button"))
        
        return widget

class Window:
    def __init__(self, title):
        self.title  = title
        #self.icon   = icon

    def create_window(self):

        main = tkinter.Tk()
        main.title(self.title)
        #tk.iconbitmap(self.icon)
        #tk.attributes('-topmost', 'true')
        #ttk.Style().theme_use('alt')
        #ttk.Style().configure("TButton", relief="flat", highlightthickness=0, bd=0)
        main.geometry("")
        return main

    # Creates frame and binds to parent argument
    # load into gui
    def create_frame(self, parent):
        fr = tkinter.Frame(parent)
        fr.pack()
        return fr
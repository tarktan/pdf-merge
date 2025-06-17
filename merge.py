import os
from pypdf import PdfWriter
from tkinter import PhotoImage
from tkinter import filedialog
from gui import Window, WidgetClass



class Merge:
    def __init__(self):
        currentDir           = os.getcwd()
        self.assetsDir       = currentDir+'\\assets\\'
        icon                 = self.assetsDir+'myicon.ico'
        print(self.assetsDir)
        title = 'PDF Merge'
        self.winSize = ''
        self.win = Window(title)
        self.window = self.win.create_window()
        self.frame  = self.win.create_frame(self.window)
        self.window.geometry(self.winSize)
        self.window.iconbitmap(icon)
        self.files = ''
        self.gui()
        self.window.mainloop()

    def gui(self):
        mergeImg           = PhotoImage(file = f'{self.assetsDir}select.png')
        #mergeImg           = mergeImg.subsample(2)
        submitImg          = PhotoImage(file = f'{self.assetsDir}submit.png')
        #submitImg          = submitImg.subsample(2)
        #submitImg = None

        mergeFrame      = WidgetClass('Frame', self.frame).create(0, 0, x=20, y=10)
        self.mergeFrame = mergeFrame

        progLabel       = WidgetClass('Label', mergeFrame).create(0, 0, x=5, y=10, cs=3)
        mergeBtn        = WidgetClass('Button', mergeFrame, image=mergeImg).create(1, 0, x=5, y=10, cs=2)
        subButton       = WidgetClass('Button', mergeFrame, image=submitImg).create(1, 2, x=5, y=10, cs=2)
        pdfFrame        = WidgetClass('Frame', self.frame).create(1, 0, x=0, y=0, cs=3)
        self.pdfFrame   = pdfFrame
            
        self.txtInfoLabel    = WidgetClass('Label', mergeFrame).create(2, 0, cs=3)
        WidgetClass.change(progLabel, 'Files are Merged in\nAlphabetical Order.', borderwidth=0, font=('Verdana', 25))
        WidgetClass.change(mergeBtn, 'Merge PDFs', command=lambda:(Merge.file_select(self)))
        WidgetClass.change(subButton, 'Submit', command=lambda:(Merge.submit(self)), state='disabled')

        self.subButton = subButton

    def file_select(self):
        self.txt = []
        pdfPng = self.assetsDir+'pdf.png'
        png = PhotoImage(file=pdfPng)
        for lab in self.pdfFrame.winfo_children():
            lab.grid_remove()
        self.window.geometry(self.winSize)
        files = list(filedialog.askopenfilenames(title="Select file(s)"))
        # check if any files were selected, give error if not
        fileNum = len(files)
        if fileNum >= 1:
            files.sort()
            v=0
            h=0
            for file in files:
                h+=1
                if h == 4: h=0; v+=1
                pdfImage = WidgetClass('Label', self.pdfFrame, image=png, font=('Verdana', 10)).create(v, h, x=10, y=10)
                WidgetClass.change(pdfImage, (file.split('/'))[-1], compound='top')
            self.files = files
            self.subButton.configure(state='normal')
        else:
            self.txt.append('No File Selected')
            self.subButton.configure(state='disabled')
        Merge.update_txt_info(self.txtInfoLabel, '\n'.join(self.txt))

    def submit(self):
        merger = PdfWriter()            
        file = self.files[0]
        fname = (file.split('/'))[-1]
        path = file.split(fname)[0]
        for file in self.files:
            merger.append(file)
        merger.write(f'{path}merged.pdf')
        merger.close()
        Merge.update_txt_info(self.txtInfoLabel, 'Files Merged Successfully')
        self.subButton.configure(state='disabled')



    def update_txt_info(label, text):
    
        WidgetClass.change(label, text, font=('Verdana', 14))
        print(text)

main = Merge()
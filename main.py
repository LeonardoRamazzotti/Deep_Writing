# Deep Writing , a based Python Software for deep focus in writing without distraction

from tkinter import *
from configparser import ConfigParser
from tkinter import PhotoImage

# COLOR PALETTE =============================================================================================================================

Dark_grey = '#1E1E1E'
White_sheet = '#FFFFFB'
Blu_navy = '#304D63'
grey = '#424242'


#END  COLOR PALETTE =============================================================================================================================

# SETTINGS ======================================================================================================================================
parser = ConfigParser()
parser.read('config.txt')
saved_sheet_color = parser.get('color','main_color')
saved_bg_color = parser.get('color', 'background')
saved_font_color =parser.get('color','font_color' )
saved_font_size = parser.get('font', 'font_size')
saved_font_type = parser.get('font','font_type')
#END SETTINGS ======================================================================================================================================

def fullscreen():
    
    root.attributes('-fullscreen',True) 


def resize():

    root.attributes('-fullscreen',False)     



screen_check = False

root = Tk()
root.title('Deep Writing')

#IMAGE SECTION =====================================================================================================================================

quit_bt = PhotoImage(file='quit.png')

#END IMAGE SECTION =================================================================================================================================

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
win_size = str(screen_width)+'x'+str(screen_height-70)
root.geometry(win_size)

root.config(bg=saved_bg_color)
root.attributes('-fullscreen',True) 

frame_page = Frame(root,bg = saved_sheet_color,width=800,height=1040, borderwidth=0,highlightthickness=0)
frame_page.place(x=560,y=20)

text_area = Text(frame_page,bg = saved_bg_color,fg=saved_font_color,width=60,height=60,  borderwidth=0,highlightthickness=0, font = (saved_font_type,saved_font_size))
text_area.place(x=70,y=60)
quit_button = Button(root,image=quit_bt, borderwidth=0,highlightthickness=0,bg=saved_bg_color,activebackground=saved_bg_color,command = lambda: root.destroy())
quit_button.place(x=10,y=10)


root.mainloop()
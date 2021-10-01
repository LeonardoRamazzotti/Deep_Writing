# Deep Writing , a based Python Software for deep focus in writing without distraction

from tkinter import *
# COLOR PALETTE =============================================================================================================================

Dark_grey = '#1E1E1E'
White_sheet = '#FFFFFB'
Blu_navy = '#304D63'


#END  COLOR PALETTE =============================================================================================================================

root = Tk()
root.title('Deep Writing')
root.attributes('-fullscreen',False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
win_size = str(screen_width)+'x'+str(screen_height-70)
root.geometry(win_size)

root.mainloop()
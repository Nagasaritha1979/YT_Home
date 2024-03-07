
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


win=Tk()
win.geometry('400x600')
win.title('YOUTUBE')
win.resizable(False,False)

python_pic_label=None
python_pic_label1=None
python_pic_btn=None

analytics_label=None
analytics_label1=None
analytics_label2=None
analytics_label3=None
view_label=None
view_label1=None
sep1=None
like_label=None
like_label1=None
sep2=None
comment_label=None
comment_label1=None
sep3=None
share_label=None
share_label1=None

def hide_widgets():
    
    if python_pic_label is not None:
        python_pic_label.place_forget()
        
    if python_pic_label1 is not None:
        python_pic_label1.place_forget()
        
    if python_pic_btn is not None:
        python_pic_btn.place_forget()
        
    if analytics_label is not None:
        
        analytics_label.place_forget()
        
    if analytics_label1 is not None:
        
        analytics_label1.place_forget()
    
    if analytics_label2 is not None:
        analytics_label2.place_forget()
        
    if analytics_label3 is not None:
        analytics_label3.place_forget()
    
    if view_label is not None:
        view_label.place_forget()
    
    if view_label1 is not None:

        view_label1.place_forget()
    if sep1 is not None:

    
        sep1.place_forget()
    
    if like_label is not None:
        like_label.place_forget()
    if like_label1 is not None:
        like_label1.place_forget()
    if sep2 is not None:
        sep2.place_forget()
    if comment_label is not None:
        comment_label.place_forget()
    if comment_label1 is not None:
        comment_label1.place_forget()
    if sep3 is not None:
        sep3.place_forget()
    if share_label is not None:
        share_label.place_forget()
    if share_label1 is not None:
        share_label1.place_forget()



def home():
    hide_widgets()
    home=Image.open('D:\\Python_Programs\\home.png')
    home_final=ImageTk.PhotoImage(home)
    
    home1_btn.config(image=home_final)
    home1_btn.image=home_final
    
    shorts1_btn.config(image=shorts1_final)
    shorts1_btn.image=shorts1_final


    library1_btn.config(image=library1_final)
    library1_btn.image=library1_final
        
    
    display_label.config(text='You are in the Home page')
    
    
def shorts():
    hide_widgets()
    shorts=Image.open('D:\\Python_Programs\\shorts.png')
    shorts_final=ImageTk.PhotoImage(shorts)
    
    shorts1_btn.config(image=shorts_final)
    shorts1_btn.image=shorts_final
    
    home1_btn.config(image=home1_final)
    home1_btn.image=home1_final


    library1_btn.config(image=library1_final)
    library1_btn.image=library1_final
        
    
    display_label.config(text='You are in the Shorts page')
    



def library():
    hide_widgets()
    library=Image.open('D:\\Python_Programs\\library.png')
    library_final=ImageTk.PhotoImage(library)
    
    
    library1_btn.config(image=library_final)
    library1_btn.image=library_final
    
    
    
    home1_btn.config(image=home1_final)
    home1_btn.image=home1_final

    
    shorts1_btn.config(image=shorts1_final)
    shorts1_btn.image=shorts1_final


    display_label.config(text='You are in the Library page')

def create():
    hide_widgets()
    tp=Toplevel(win)
    tp.geometry('400x300')
    tp.overrideredirect(1) # to remove the Toplevel window titlebar
    x = win.winfo_x()
    y = win.winfo_y()
    tp.geometry("+%d+%d" %(x+5,y+328))
    tp.config(bg='gray55')
    
    create_label=Label(tp,text='Create',font=("Arial",18,'bold'),bg='gray55',fg='white')
    create_label.place(x=10,y=5)
    
    exit_button=Button(tp,cursor='hand2',text='X',font=("Arial",18,'bold'),fg='white',bg='gray55',activebackground='gray55',command=tp.destroy,bd=0)
    exit_button.place(x=350,y=5)
    
    create_short=Image.open('create_shorts.png')
    create_short_resize=create_short.resize((50,50))
    create_short_final=ImageTk.PhotoImage(create_short_resize)
    
    create_short_btn=Button(tp,image=create_short_final,font=("Arial",15,'bold'),activeforeground='white',text='   Create a Short',compound='left',bd=0,fg='white',bg='gray55',activebackground='gray55',cursor='hand2')
    create_short_btn.image=create_short_final
    create_short_btn.place(x=10,y=40)
    
    upload=Image.open('upload.png')
    upload_resize=upload.resize((50,50))
    upload_final=ImageTk.PhotoImage(upload_resize)

    upload_btn=Button(tp,image=upload_final,font=("Arial",15,'bold'),activeforeground='white',text='   Upload a Video',compound='left',bd=0,fg='white',bg='gray55',activebackground='gray55',cursor='hand2')
    upload_btn.image=upload_final
    upload_btn.place(x=10,y=100)
    
    go_live=Image.open('go_live.png')
    go_live_resize=go_live.resize((50,50))
    go_live_final=ImageTk.PhotoImage(go_live_resize)

    go_live_btn=Button(tp,image=go_live_final,font=("Arial",15,'bold'),activeforeground='white',text='   Go live',compound='left',bd=0,fg='white',bg='gray55',activebackground='gray55',cursor='hand2')
    go_live_btn.image=go_live_final
    go_live_btn.place(x=10,y=160)

    post=Image.open('post.png')
    post_resize=post.resize((50,50))
    post_final=ImageTk.PhotoImage(post_resize)

    post_btn=Button(tp,image=post_final,font=("Arial",15,'bold'),activeforeground='white',text='   Create a post',compound='left',bd=0,fg='white',bg='gray55',activebackground='gray55',cursor='hand2')
    post_btn.image=post_final
    post_btn.place(x=10,y=230)
    
    display_label.config(text='')

def python_func():
    global python_pic_btn,python_pic_label,python_pic_label1    
    def execute():
        global analytics_label,analytics_label1,analytics_label2,analytics_label3,view_label,view_label1,sep1,like_label,like_label1,sep2,comment_label,comment_label1,sep3,share_label,share_label1
        analytics_label=Label(frame,text='Analytics',font=("Arial",18,'bold'),fg='white',bg='black')
        analytics_label.place(x=120,y=150)
        
        analytics_label1=Label(frame,text='All time',font=("Arial",8),fg='white',bg='black')
        analytics_label1.place(x=120,y=180)
    
        analytics_label2=Label(frame,text='150' , font=("Arial",18,'bold'),fg='white',bg='black')
        analytics_label2.place(x=130,y=220)
        
        analytics_label3=Label(frame,text='Subscibers' , font=("Arial",12),fg='white',bg='black')
        analytics_label3.place(x=185,y=226)
        
        view_pic=Image.open('views.png')
        view_pic_resize=view_pic.resize((50,50))
        view_pic_final=ImageTk.PhotoImage(view_pic_resize)
    
              
        like_pic=Image.open('like.jpg')
        like_pic_resize=like_pic.resize((50,50))
        like_pic_final=ImageTk.PhotoImage(like_pic_resize)
            
        comments_pic=Image.open('comment.png')
        comments_pic_resize=comments_pic.resize((50,50))
        comments_pic_final=ImageTk.PhotoImage(comments_pic_resize)
    
    
        share_pic=Image.open('shares.png')
        share_pic_resize=share_pic.resize((50,50))
        share_pic_final=ImageTk.PhotoImage(share_pic_resize)
        
        view_label=Label(frame,text='10K',font=("Arial",10),image=view_pic_final,compound='top',bg='black',fg='white')
        view_label.image=view_pic_final
        view_label.place(x=5,y=270)
        
        view_label1=Label(frame,text='Views',font=("Arial",8),bg='black',fg='white')
        view_label1.place(x=10,y=340)
    
        styl = ttk.Style()
        styl.configure('yellow.TSeparator', background='yellow')
        sep1=ttk.Separator(frame,orient='vertical',style='yellow.TSeparator')
        sep1.place(x=70,y=270,relwidth=0, relheight=0.1)

        like_label=Label(frame,text='500',font=("Arial",10),image=like_pic_final,compound='top',bg='black',fg='white')
        like_label.image=like_pic_final
        like_label.place(x=90,y=270)

        like_label1=Label(frame,text='Likes',font=("Arial",8),bg='black',fg='white')
        like_label1.place(x=100,y=340)

        styl = ttk.Style()
        styl.configure('yellow.TSeparator', background='yellow')
        sep2=ttk.Separator(frame,orient='vertical',style='yellow.TSeparator')
        sep2.place(x=170,y=270,relwidth=0, relheight=0.1)

        comment_label=Label(frame,text='80',font=("Arial",10),image=comments_pic_final,compound='top',bg='black',fg='white')
        comment_label.image=comments_pic_final
        comment_label.place(x=200,y=270)

        comment_label1=Label(frame,text='Comments',font=("Arial",8),bg='black',fg='white')
        comment_label1.place(x=200,y=340)

        styl = ttk.Style()
        styl.configure('yellow.TSeparator', background='yellow')
        sep3=ttk.Separator(frame,orient='vertical',style='yellow.TSeparator')
        sep3.place(x=270,y=270,relwidth=0, relheight=0.1)
        
        share_label=Label(frame,text='130',font=("Arial",10),image=share_pic_final,compound='top',bg='black',fg='white')
        share_label.image=share_pic_final
        share_label.place(x=290,y=270)

        share_label1=Label(frame,text='Shares',font=("Arial",8),bg='black',fg='white')
        share_label1.place(x=290,y=340)
        
                   
    python_pic=Image.open('python_pic.png')
    python_pic_resize=python_pic.resize((100,100))
    python_pic_final=ImageTk.PhotoImage(python_pic_resize)
    
    
    python_pic_label=Label(frame,fg='white',image=python_pic_final,text='Nagasaritha KP',font=("Arial",15,'bold'),bg='black',compound='left')
    python_pic_label.image=python_pic_final
    python_pic_label.place(x=10,y=15)

    python_pic_label1=Label(frame,fg='white',text='@nagasarithakp',font=("Arial",8),bg='black')
    python_pic_label1.place(x=110,y=80)
    
    python_pic_btn=Button(frame,cursor='hand2',bd=0,command=execute,text= '. View channel analytics >',font=("Arial",8),fg='white',bg='black',activeforeground='white',activebackground='black')
    python_pic_btn.place(x=210,y=80)
    
    display_label.config(text='')

frame=Frame(win,width=400,height=540,bg='black')
frame.place(x=0,y=0)

frame1=Frame(win,width=400,height=60,bg='black',bd=5,highlightcolor='white')
frame1.place(x=0,y=540)



home1=Image.open('D:\\Python_Programs\\home1.png')
home1_final=ImageTk.PhotoImage(home1)

home1_btn=Button(frame1,bd=0,bg='black',activebackground='black',image=home1_final,cursor='hand2',command=home)
home1_btn.image=home1_final
home1_btn.place(x=10,y=2)

home1_label=Label(frame1,bg='black',fg='white',text='Home',font=("Arial",8))
home1_label.place(x=9,y=38)

shorts1=Image.open('D:\\Python_Programs\\shorts1.png')
shorts1_final=ImageTk.PhotoImage(shorts1)

shorts1_btn=Button(frame1,bd=0,bg='black',activebackground='black',image=shorts1_final,cursor='hand2',command=shorts)
shorts1_btn.image=shorts1_final
shorts1_btn.place(x=100,y=2)

shorts1_label=Label(frame1,bg='black',fg='white',text='Shorts',font=("Arial",8))
shorts1_label.place(x=99,y=38)

create1=Image.open('create.png')
create_resize=create1.resize((50,50))
create1_final=ImageTk.PhotoImage(create_resize)

create1_btn=Button(frame1,bd=0,bg='black',activebackground='black',image=create1_final,cursor='hand2',command=create)
create1_btn.image=create1_final
create1_btn.place(x=170,y=2)

library1=Image.open('D:\\Python_Programs\\library1.png')
library1_final=ImageTk.PhotoImage(library1)

library1_btn=Button(frame1,bd=0,bg='black',activebackground='black',image=library1_final,cursor='hand2',command=library)
library1_btn.image=library1_final
library1_btn.place(x=250,y=1)

library1_label=Label(frame1,bg='black',fg='white',text='Library',font=("Arial",8))
library1_label.place(x=249,y=38)

python1=Image.open('D:\\Python_Programs\\python1.png')
python1_resize=python1.resize((40,40))
python1_final=ImageTk.PhotoImage(python1_resize)

python1_btn=Button(frame1,bd=0,bg='black',activebackground='black',image=python1_final,cursor='hand2',command=python_func)
python1_btn.image=python1_final
python1_btn.place(x=320,y=1)

python1_label=Label(frame1,bg='black',fg='white',text='You',font=("Arial",8))
python1_label.place(x=328,y=40)


styl = ttk.Style()
styl.configure('yellow.TSeparator', background='yellow')
sep=ttk.Separator(frame,orient='horizontal',style='yellow.TSeparator')
sep.place(x=0,y=535,relwidth=1, relheight=0)

display_label=Label(frame,text='',font=("Arial",18),bg='black',fg='yellow')
display_label.place(x=70,y=250)


win.mainloop()

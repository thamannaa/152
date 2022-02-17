from tkinter import *
root=Tk()
root.title("multi dimensional arrays")
root.geometry("400x400")

label=Label(root)

array_1d=["lilly","billy","kelly"]
print(array_1d[1])

array_2d=[["lilly","A"],["billy","B"],["kelly","C"]]
print(array_2d[0][1])

array_3d=[[["lilly","A","excellent"],["billy","B","very good"],["kelly","C","good"]]]
print(array_3d[0][1][2])

def combine():
    label["text"]=array_3d[0][1][0]+" got grade "+array_3d[0][1][1]+" he is doing "+array_3d[0][1][2]

btn=Button(root,text="combine",command=combine)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
label.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()

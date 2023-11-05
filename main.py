import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk,ImageDraw
import numpy as np
import PIL

##2 main windows: Image window (Image_win)


class Image_win:

      def __init__(self,root,path):
          self.root = root
          #Opening the image 
          self.img = Image.open(path)
          
          #Setting up canvas and numpy array
          self.width,self.height=self.img.size
          self.original = (self.width,self.height)
          self.canvas = tk.Canvas(self.root,width=self.width,height=self.height,bg='white')
          
          #self.canvas = tk.Canvas(self.root)
          self.array = np.zeros((self.height,self.width))
          self.array = Image.fromarray(self.array).convert(mode="L")
          
          self.canvas.pack(expand=True,fill="both",anchor="center",side="top")
          
          self.buttonframe = Frame(self.root)
          self.buttonframe.pack(side = BOTTOM)
          self.zoomframe = Frame(self.root)
          self.zoomframe.pack(side=BOTTOM)
          ##Setting the buttons
          
          self.select_button = tk.Button(self.buttonframe,text="Select Coordinates",command=self.coordinate_select)
          self.end_button = tk.Button(self.buttonframe,text="End Coordinates",command=self.end_selection)
          self.confirm_button = tk.Button(self.buttonframe,text="Confirm Selection",command=self.confirm_selection)
          self.redo_button = tk.Button(self.buttonframe,text="Redo Selection",command=self.redo_selection)
          self.save_button = tk.Button(self.buttonframe,text="Save Mask",command=self.save)
          self.zoom_in_button = tk.Button(self.zoomframe,text="Zoom in",command=self.zoom_in)
          self.zoom_out_button = tk.Button(self.zoomframe,text="Zoom out",command=self.zoom_out)
          
          
          
          self.select_button.pack(anchor = CENTER)
          self.end_button.pack(side = RIGHT)
          self.confirm_button.pack(side = RIGHT)
          self.redo_button.pack(side= RIGHT)
          self.save_button.pack(side= RIGHT)
          self.zoom_in_button.pack(anchor = CENTER)
          self.zoom_out_button.pack(side = RIGHT)
          
          
          ##Image + Canvas
          photo = ImageTk.PhotoImage(master=self.root,image=self.img)
          self.image_window = self.canvas.create_image(0,0,anchor=tk.NW,image=photo)
          
          ##Other things
          self.coordinate_list = []
          self.temp_lines = []
          self.label = None
          self.root.mainloop()
          
          #Functions for each button
          
      #Function for Select Button
      def coordinate_select(self):
          #Binding the coordinate selection to left mouse click
          self.canvas.bind("<Button-1>",self.coordinates)
          
          #Deactivating the select button while selecting
          self.select_button.config(state=tk.DISABLED)
      
      def coordinates(self,event):
          
          #Track each mouse click and store the x and y coordinates in the list
          self.flag = True
          x,y = event.x,event.y
          
          
             
          self.coordinate_list.append(x)
          self.coordinate_list.append(y)
            
          
          
          if len(self.coordinate_list) > 2:
          
             self.line = self.canvas.create_line(self.x_last,self.y_last,x,y,fill="red",width=5)
             self.temp_lines.append(self.line)
          self.x_last = x
          self.y_last = y
             
                          

      #Function for End Button

      def end_selection(self):
          
          #To account for less than 3 coordinates
          if len(self.coordinate_list) <= 2:
             print("Invalid Coordinates")
             self.coordinate_list = []
             for i in self.temp_lines:
                 self.canvas.delete(i)
             #Reactivating selection button
             self.select_button.config(state=tk.ACTIVE)           
          else:
             
             print("Coordinates are: ",self.coordinate_list)
             
             for i in self.temp_lines:
                 self.canvas.delete(i)
             self.temp_lines = []
             self.polygon = self.canvas.create_polygon(self.coordinate_list,outline='red',width=2)
                    
             
             
             
      #Function for Confirm Button
      def confirm_selection(self):
          
          
          
          
          #######RUN MY NUMPY FUNCTION HERE########
          #######Will also open Label_win##########
          self.obtain_label()
          
          #self.masking()
          if self.label != None:
             print("Label is: ",self.label)
             self.masking()
          
          
          #########################################'
          #Setting Co-ordinates back to an empty list
             self.coordinate_list = []
          #Sets the polygon back
             self.polygon = 0
         
             #Reactivating selection button
             self.select_button.config(state=tk.ACTIVE)
             print("Confirmed Selection")
          
      #Function for Redo button
      def redo_selection(self):
          
          if self.polygon != 0:
             self.canvas.delete(self.polygon)
          else:
             for i in self.temp_lines:
                 self.canvas.delete(i)
          self.coordinate_list = []
          #Reactivating Selection button
          self.select_button.config(state=tk.ACTIVE)
          
      #Function for Save button
      
      def save(self):
      
          self.array = self.array.resize(self.original,resample = PIL.Image.NEAREST)
          self.array.save("mask.png")
          ##Close my window?###
          self.root.destroy()
                   
      #Function for running the masking             
      def masking(self):
          #print(self.coordinate_list," - ",self.label)
          draw = ImageDraw.Draw(self.array)
          draw.polygon(self.coordinate_list,fill = self.label)
      
      def obtain_label(self):
          
          def select():
              label = entry.get()
              try:
                 label = int(label)
                 self.label = label
              except:
                  print("Enter valid integer value")
                  entry.delete(0,tk.END)
              lab_win.destroy()
      
          
          lab_win = Toplevel(self.root)
          lab_win.title("Label Assigning")
          text = tk.Label(lab_win,text="Enter the class label to assign to pixel: ")
          entry = tk.Entry(lab_win)
          lab_button = tk.Button(lab_win,text="Select",command=select)
          text.pack()
          entry.pack()
          lab_button.pack()
          self.root.wait_window(lab_win)
          
      def zoom_in(self):
          
          self.width = round(self.width*1.2)
          self.height = round(self.height*1.2)
          new_image = self.img.resize((self.width,self.height))
          self.array = self.array.resize((self.width,self.height),resample=PIL.Image.NEAREST)
          new_photo = ImageTk.PhotoImage(new_image)
          self.canvas.itemconfig(self.image_window,image=new_photo)
          self.canvas.image = new_photo
          
          
      def zoom_out(self):
          self.width = round(self.width*0.8)
          self.height = round(self.height*0.8)
          new_image = self.img.resize((self.width,self.height))
          self.array = self.array.resize((self.width,self.height),resample=PIL.Image.NEAREST)
          new_photo = ImageTk.PhotoImage(new_image)
          self.canvas.itemconfig(self.image_window,image=new_photo)
          self.canvas.image = new_photo
      
                    
      
def open_image():
    
    file_path = filedialog.askopenfilename()
    print("File path: ",file_path)
    
    Image_win(root=window,path=file_path)
    


if __name__ == "__main__":

   
   global window
   window = tk.Tk()
   
   window.title("Image Viewer")
   
   open_button = tk.Button(window,text="Open Image",command=open_image)
   open_button.pack()
   
   
   window.mainloop()

   
                
import tkinter
import tkinter.messagebox

from matplotlib.pyplot import text

class pizza_calc:
    def __init__(self):
        
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')

        self.prompt1_label = tkinter.Label(self.top_frame, text = "Enter your Name: ")
        self.name_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt1_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.prompt1_label.pack(side='top')
        self.name_entry.pack(side='top')

        self.prompt2_label = tkinter.Label(self.top_frame,text='Select your toppings: ')
        self.topping1 = tkinter.Checkbutton(self.top_frame,text= 'Pepperoni')
        self.top2 = tkinter.Checkbutton(self.top_frame, text='Sausage')
        self.top2 = tkinter.Checkbutton(self.top_frame, text='Sausage')
        self.top3 = tkinter.Checkbutton(self.top_frame,text='mushrooms')
        self.top4 = tkinter.Checkbutton(self.top_frame,text = 'olives')
        self.top5 = tkinter.Checkbutton(self.top_frame,text = 'peppers')

        self.prompt2_label.pack(side='top')
        self.topping1.pack(side='top')
        self.top2.pack(side='top')
        self.top3.pack(side='top')
        self.top4.pack(side='top')
        self.top5.pack(side='top')

        self.prompt3_label = tkinter.Label(self.top_frame, text='Select your Crust: ')

        self.prompt3_label.pack(side='top')

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)

        self.rb1 = tkinter.Radiobutton(self.top_frame, 
                                        text = 'Hand-Tossed', 
                                        variable=self.radio_var, 
                                        value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, 
                                        text = 'Thin Crust', 
                                        variable=self.radio_var, 
                                        value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, 
                                        text = 'Deep Dish', 
                                        variable=self.radio_var, 
                                        value=3)
        self.rb2.select()
        
        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        self.rb3.pack(side='left')

        self.calc_button = tkinter.Button(self.main_window, text = 'Calculate Total', command=self.calc_total)
        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='bottom')
        self.quit_button.pack(side='bottom')

        tkinter.mainloop()
    
    def calc_total(self):
        tkinter.messagebox.showinfo("Receipt", 'Name: ' + 'Total:')
pizza_pizza = pizza_calc()


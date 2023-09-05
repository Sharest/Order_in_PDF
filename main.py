import fitz
import tkinter


class Window:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('600x300')
        self.root.title("Order in PDF")

        self.order = tkinter.Entry(self.root, width=80)
        self.adress = tkinter.Entry(self.root, width=80)

        self.order.insert(0, "Order number")
        self.adress.insert(0, "Order adress")

        self.doc = fitz.open()

    def get_information(self):
        order = str(self.order.get())
        adress = str(self.adress.get())

        self.order.delete(0, tkinter.END)
        self.adress.delete(0, tkinter.END)

        return order, adress

    def write_in_pdf(self):

        order, adress = self.get_information()
        page = self.doc.new_page()

        nl = '\n'
        text = f'{nl*5}{order}{nl*5}{adress}'
        page.add_freetext_annot(
            page.rect+20,
            text,
            fontsize=20,
            fontname='helv',
            rotate=270
        )
        return self.doc

    def save_doc(self):

        self.write_in_pdf()

        self.doc.save('orders.pdf')
        self.doc.close()
        self.root.destroy()

    def entry_clear(self, event):
        self.order.delete(0, tkinter.END)
        self.adress.delete(0, tkinter.END)

    def create_interface(self):

        self.order.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.adress.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        self.order.bind('<1>', self.entry_clear)
        self.adress.bind('<1>', self.entry_clear)

        next_order_btn = tkinter.Button(
            self.root, text='next order', height=2, width=10, command=self.write_in_pdf)
        next_order_btn.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)

        save_btn = tkinter.Button(
            self.root, text='save', height=2, width=10, command=self.save_doc)
        save_btn.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)

    def run(self):
        self.create_interface()
        self.root.mainloop()


if __name__ == '__main__':
    order = Window()
    order.run()

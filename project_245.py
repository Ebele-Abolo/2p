import Web3 library
from tkinter import *
root = Tk()

root.title("My Ethereum App")
root.geometry("500x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum Block", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
block_entry = Entry(root, text="This is Entry Widget", bd=2)

block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
gasused_info_label = Label(root, bg="white", font=("bold", 10))
gasused_info_label.place(relx=0.5, rely=0.38, anchor=CENTER)
gaslimit_info_label = Label(root, bg="white", font=("bold", 10))
gaslimit_info_label.place(relx=0.5, rely=0.5, anchor=CENTER)


url = "cfff1092c3ed447298e75c3d2222cc74"
web3 = Web3.HTTPProvider(url)

# Write Code for Task 01 below.
def ethereuam_block():
	number =int(block_entry.get())
	block_data = web3.eth.getBlock(number)
	transaction = web3.eth.get_transaction(block_data['transactions'][-1].hex())
	Value = transaction['value']
	value_in_ether = Value/ 10**18
	value_in_dollars = Value*1902.95

	gas = transaction['gas']
	gasused_info_label[" Value: $" + str(value_in_dollar)]
	gaslimit_info_label["gas: " + str(gas)]
	block_name_label["Value: " + str(block_entry)]
# Write Code for Task 02 below.





    block_entry.destroy()
    search_btn.destroy()


search_btn = Button(root, text="Search Ethereum transaction fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()


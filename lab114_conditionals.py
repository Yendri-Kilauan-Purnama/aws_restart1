# Lab Nomor 7, Working with Conditionals
# Dari Coach Reza
userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply == "yes":
    print("We can help you ship that package!")
elif userReply == "no":
    print("Please come back when you need to ship a package. Thank you.")
else:
    print("Silahkan input yang benar")

# Working with Conditionals
userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.") 


print("Would you like to buy stamps, buy an envelope, or make a copy?")
userReply = input("(Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")

# Python 3.8, belum ada match, yang ada baru 3.10, dijalankan akan error    
# di AWS ini Pyhton-nya masih versi 3.8, maka jalankan di Colab, baru bisa.
    
# print("Would you like to buy stamps, buy an envelope, or make a copy?")
# userReply = input("(Enter stamps, envelope, or copy) ")

# match userReply:
#     case "stamps":
#         print("We have many stamp designs to choose from.")
#     case "envelope":
#         print("We have many envelope sizes to choose from.")
#     case "copy":
#         copies = input("How many copies would you like? (Enter a number) ")
#         print("Here are {} copies.".format(copies))
#     case _:
#         print("Thank you, please come again")

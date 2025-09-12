my_data = open("data.txt", "x")
my_data.close()

my_data = open("data.txt", "w")   
my_data.write("Hello there, i am nick and i like coding!\n")
my_data.write("Today we are gonna code a game called...\n")
my_data.write("Omori.\n")
my_data.close()




# 1) შექმენით data.txt ფაილი პითონით, ამისთვის გამოიყენეთ ფაილზე "x"-ის უფლებით გახსნა (open ფუნქციას)
# ფაილის შექმნის შემდეგ გასხსენით ფაილი სტანდარუტი გზით, ჩაწერეთ ინფორმაცია და დახურეთ. შემდეგ ფაილი გახსენით with open as სინტქასით და readlines() მეთოდის დახამრებთ ცალცალკე ხაზებზე გამოიტანეთ ფაილში ჩაწერილი ინფორმაცია
a = 999999
b = 5.555555555555
c = 'x'
d = "Kokkola"
e = 2.33
f = 10
g = 300
h = "9 billions"
i = "3 billions"


print("Give speed of the car and the distance ")
speed = float(input("Speed:"))
distance = float(input("Distance:"))
a_time = speed/distance
hours = int(speed//distance)
minutes = int((a_time % 1) * 60);
print(a_time);
print(hours , " hours", minutes," minutes");


body_mass  = float(input("Body mass in kilograms:"))
heigth = float(input("heigth in meters:"))
bmi = body_mass / (heigth * heigth)
print(bmi)

dollars = int(input("Dollars:"))
euros = dollars * 0.92
print(euros)

seconds = int(input("Seconds"));
minutes = float(seconds)/60;
seconds =int((minutes % 1)*60)
minutes = minutes // 1
hours = minutes / 60
minutes = int((hours % 1) * 60)
hours = int(hours // 1)
print(hours, "hours " , minutes , "minutes " , seconds, "seconds")

euros = int(input("Give euros:"))
bills500 = euros // 500
euros_used = bills500 * 500;
bills200 = (euros - euros_used) // 200
euros_used += bills200 * 200;
bills100 = (euros -euros_used) // 100
euros_used += bills100 * 100;
bills50 = (euros - euros_used) // 50
euros_used += bills50 * 50;
bills20 = (euros -euros_used) // 20
euros_used += bills20 * 20;
bills10 = (euros - euros_used) // 10
euros_used += bills10 * 10;
bills5 = (euros - euros_used) // 5
if(euros % 5 != 0): bills5 += 1
print("500€ bills:", bills500,"200€ bills:",  bills200,"100€ bills:",  bills100,"50€ bills:",  bills50,"20€ bills:",  bills20,"10€ bills:",  bills10,"5€ bills:",  bills5)

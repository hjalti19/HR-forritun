#búum til input sem endurtekur sig (notandi getur sett inn gildi afur og aftur)
#Látum forritið stöðvast þegar sett er inn neikvæð tala
#Fáum forritið til að halda utan um stærsta jákvæða gildið og prenta það út þegar forritið stöðvast
Max_int = 0
while True:
    num_int = int(input("Input number: "))
    if num_int > Max_int:
        Max_int = num_int
    if num_int < 0:
        break
print(Max_int)

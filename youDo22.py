phrase1 = input("Enter two-word phrase 1: ")
phrase2 = input("Enter two-word phrase 2: ")
phrase3 = input("Enter two-word phrase 3: ")
phrase4 = input("Enter two-word phrase 4: ")
phrase5 = input("Enter two-word phrase 5: ")

ph1Len = len(phrase1)
ph2Len = len(phrase2)
ph3Len = len(phrase3)
ph4Len = len(phrase4)
ph5Len = len(phrase5)

ie1 = (phrase1[0] + phrase1[-1]).lower()
ie2 = (phrase2[0] + phrase2[-1]).lower()
ie3 = (phrase3[0] + phrase3[-1]).lower()
ie4 = (phrase4[0] + phrase4[-1]).lower()
ie5 = (phrase5[0] + phrase5[-1]).lower()

m1 = phrase1[len(phrase1) // 2]
m2 = phrase2[len(phrase2) // 2]
m3 = phrase3[len(phrase3) // 2]
m4 = phrase4[len(phrase4) // 2]
m5 = phrase5[len(phrase5) // 2]

first1 = phrase1[:phrase1.find(" ")]
first2 = phrase2[:phrase2.find(" ")]
first3 = phrase1[:phrase3.find(" ")]
first4 = phrase1[:phrase4.find(" ")]
first5 = phrase1[:phrase5.find(" ")]

second1 = phrase1[phrase1.find(" ") + 1 : ]
second2 = phrase2[phrase2.find(" ") + 1 : ]
second3 = phrase3[phrase3.find(" ") + 1 : ]
second4 = phrase4[phrase4.find(" ") + 1 : ]
second5 = phrase5[phrase5.find(" ") + 1 : ]

print("Phrases \t\t L \t\t IE \t\t M \t\t 1stW \t\t 2ndW")
print(phrase1 + " \t\t" + str(ph1Len) + " \t\t" + ie1 + " \t\t" + m1 + " \t\t" + first1 + " \t\t"  + second1)
print(phrase2 + " \t\t" + str(ph2Len) + " \t\t" + ie2 + " \t\t" + m2 + " \t\t" + first2 + " \t\t"  + second2)
print(phrase3 + " \t\t" + str(ph3Len) + " \t\t" + ie3 + " \t\t" + m3 + " \t\t" + first3 + " \t\t"  + second3)
print(phrase4 + " \t\t" + str(ph4Len) + " \t\t" + ie4 + " \t\t" + m4 + " \t\t" + first4 + " \t\t"  + second4)
print(phrase5 + " \t\t" + str(ph5Len) + " \t\t" + ie5 + " \t\t" + m5 + " \t\t" + first5 + " \t\t"  + second5)

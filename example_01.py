import re
pattern = "абв"
fin = open("c:/Users/Mike84/Desktop/Proba/HW_005/ex_in.txt", "r", encoding="utf-8")
fout = open("c:/Users/Mike84/Desktop/Proba/HW_005/ex_out.txt", "w", encoding="utf-8")
buf = fin.readlines()
for item in buf:
    var1 = re.split(" ", item)
    for i in var1:
        if pattern in i:
            var1.remove(i)
    fout.writelines(" ".join(var1))

fin.close()
fout.close()


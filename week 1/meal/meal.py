def convert(a, b):
    hasAmPm = False
    #check for a.m. or p.m.
    if "m" in b:
        c,d = b.split()
        hasAmPm = True
    else:
        c = ""
        d = ""
        hasAmPm = False



    if hasAmPm:
        print(f"a: {a}, c{c}, d{d}")
    else:
       # 24hr
       y = a + b

       if y.startswith("7") or y.startswith("800"):
           print("breakfast time")
       elif y.startswith("12") or y.startswith("1300"):
            print("lunch time")
       elif y.startswith("18") or y.startswith("1900"):
           print("dinner time")


#input
a, b = input("What time is it: ").split(":")
convert(a,b)
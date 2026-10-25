#Addition Table
print("          Addition Table")
print("        1  2  3  4  5  6  7  8  9")
print("    -----------------------------")
i=1
while i<=9:
    j=1
    row_str=str(i)+"   | "
    while j<=9:
        val=i+j
        if val<10:
            row_str+="  "+str(val)
        else:
            row_str+=" "+str(val)
        j+=1
    print(row_str)
    i+=1

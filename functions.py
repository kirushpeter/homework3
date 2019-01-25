#homework 3 by peter kirumba 

def compare(val1, val2, val3):
    if type(val1) == str:
        val1 = int(val1)
    if type(val2) == str:
        val2 = int(val2)
    if type(val3) == str:
        val3 = int(val3)

    if val1 == val2:
        print("val1:",val1,"equal to","val2:",val2)
        return True
    elif val1 == val3:
        print("val1:",val1,"equal to","val3:",val3)
        return True
    elif val2 == val3:
        print("val2:",val2,"equal to","val3:",val3)
        return True
    else:
        print("All paramaters are not equal to each other")
        print("val1:",val1,"val2:",val2,"val3:",val3)
        return False

print(compare(1,3,1))
print(compare(1,1,0))
print(compare(1,3,3))
print(compare(1,"1",0))
print(compare("5",5,3))
print(compare(5,2,"2"))
print(compare(1,3,3))
print(compare("1",2,3))
print(compare("8","1","3"))
print(compare("5",0,"7"))
print(compare("6","2","3"))

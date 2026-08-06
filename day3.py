# list data
# names = ['Nischay','kcnkjdq']
# countries = ["japan","usa","nepal"]
# print(countries[-1])
# append inside the list
# countries.append("India")
# print(countries[-1])
# removing the last element
# countries.pop()
# print(countries)

# adding in any position
# countries.insert(0,"india")
# print(countries)
# countries[1] = "china"
# print(countries)
# print(len(countries))


# tuple
# countries_tuple = ("Nepal","Japan","USA","Nepal")
# countries[2] = "India"
# print(countries)

# index
# print(countries_tuple.index("Nepal"))


# sets

# countries_sets = {"Nepal","Japan","USA","Nepal"}
# print(countries_sets)


# dictionary
# person_information = {
#     "full_name":"Nischay Shrestha",
#     "address" : "Dharan",
#     "company" : "Digital Pathshala"
# }


# print(person_information["full_name"])

# person_information["color"] = "blue"
# print(person_information)

# person_information.pop("company")
# print(person_information)

# person_information.insert("")

# tup = tuple("string")
# print(type(tup))

# nested_tuple = (4,5,6),(7,8)
# print(nested_tuple)

# unpacking the tuple
# tup = (4,5,6)
# a,b,c = tup 
# print(b)

# tup = 4,5,(6,7)
# a,b,(c,d) = tup 
# print(d)


# number swap
# a,b = 1,2
# print(a)
# print(b)
# a,b = b,a
# print(a)
# print(b)

# seq = [(1,2,3),(4,5,6),(7,8,9)]
# for a,b,c,d in seq:
#     print(f"a={a} b={b} c={c} d={d}")

# a = [1,2,2,2,2,3,4,5]
# print(a.count(2))



# list 
a_list = [2,3,7,None]
# print(a_list)

tup = ("foo","bax","baz")
b_list = list(tup)
# print(b_list)
b_list[1] = "Nischay"
# print(b_list)

b_list.append("drawf")
print(b_list)

b_list.insert(1,"red")
print(b_list)

print(b_list.pop(2))
print(b_list)

# print(b_list.pop("foo"))
# print(b_list)

b_list.append("foo")
print(b_list)

b_list.remove("foo")
print(b_list)

print("drawf" in b_list)

x = [4,None,"foo"]
x.extend([7,8,(2,3)])
print(x)


b = ["saw","small","He","foxes","six"]
b.sort(key=len)
print(b)

seq = [7,2,3,7,5,6,0,1]
print(seq[1:5])
#store marks of stud for three diffnt subs

subs={}
x=int(input("Enter the marks:"))
y=int(input("Enter the marks:"))
z=int(input("Enter the marks:"))

subs.update({"mech":x})
subs.update({"eng":y})
subs.update({"maths":z})

print(subs)
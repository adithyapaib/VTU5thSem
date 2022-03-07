import re
print("Successfull" if re.compile(r"^(a)\w{3}(z)$",re.VERBOSE).search(input("Enter the string: ")) else "Unsucesfull")

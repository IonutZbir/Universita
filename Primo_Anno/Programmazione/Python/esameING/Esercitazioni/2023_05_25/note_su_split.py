print("a,b,c".split(","))
print(",a,b,,c,".split(","))
print("a,b,c".split(",", maxsplit=1))
print("a,b,c".rsplit(","))
print("a,b,c".rsplit(",", maxsplit=1))
print("   a    b    c".split())
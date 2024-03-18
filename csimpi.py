class redPanda:pass

myList = [redPanda(), "not a redPanda", redPanda(), "also not a redPanda", redPanda()]

redPanda_instances = [obj for obj in myList if isinstance(obj, redPanda)]

for red_panda_instance in redPanda_instances:
    print(red_panda_instance)

print(len(redPanda_instances))
print(redPanda_instances[1])
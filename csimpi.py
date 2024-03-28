class redPanda:pass

rp_bestPanda = redPanda()
rp_secondBestPanda =redPanda()

myList = [rp_bestPanda, rp_secondBestPanda, rp_secondBestPanda, rp_bestPanda]

redPanda_instances = [obj for obj in myList if isinstance(obj, redPanda)]

for red_panda_instance in redPanda_instances:
    print(red_panda_instance)

print(len(redPanda_instances))
print(redPanda_instances[1])
print()
print(myList)
print(len(myList))
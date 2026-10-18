# break - used to STOP & COME OUT of loop / iteration
# continue - used to SKIP specific iteration & CONTINUE with rest of loop / iteration

print("--------- Iterate in range 10, STOP when get number 6 -----------------")

for i in range(1,10):
    print(i,end=" ")
    if i == 6:
        break
print("\n")

print("--------- Iterate in range 10, SKIP numbers 4, 8 -----------------")

for i in range(1,10):
    if i == 4 or i == 8:
        continue
    print(i,end=" ")

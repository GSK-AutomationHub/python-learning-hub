import copy


def equality_copy_deepcopy_check(collect,Operation,is_nested):
    if Operation.__eq__('Equality'):
        equal_collect = collect
        print("--------- Collections before Modification --------- ")
        print(f"Original_Collection = {collect} \nEqual_Collection = {equal_collect}")
        equal_collect[0] = 'equality_check'
        if id(collect) == id(equal_collect) and equal_collect[0] == collect[0]:
            print("--------- Collections after Modification --------- ")
            print(f"Original_Collection = {collect} \nEqual_Collection = {equal_collect}")
            print("equality check is successful")
        else:
            print("equality check is not successful")
    elif Operation.__eq__('Shallow Copy'):
        copy_collect = collect.copy()
        print("--------- Collections before Modification --------- ")
        print(f"Original_Collection = {collect} \nCopy_Collection = {copy_collect}")
        if is_nested.__eq__(True):
            copy_collect[3][0] = 'shallow_copy_check'
            if id(collect) != id(copy_collect) and copy_collect[3][0] == collect[3][0]:
                print("--------- Collections after Modification --------- ")
                print(f"Original_Collection = {collect} \nCopy_Collection = {copy_collect}")
                print("shallow copy check is successful")
            else:
                print("shallow copy check is not successful")
        else:
            copy_collect[0] = 'shallow_copy_check'
            if id(collect) != id(copy_collect) and copy_collect[0] != collect[0]:
                print("--------- Collections after Modification --------- ")
                print(f"Original_Collection = {collect} \nCopy_Collection = {copy_collect}")
                print("shallow copy check is successful")
            else:
                print("shallow copy check is not successful")
    elif Operation.__eq__('Deep Copy'):
        deep_copy_collect = copy.deepcopy(collect)
        print("--------- Collections before Modification --------- ")
        print(f"Original_Collection = {collect} \nDeep_Copy_Collection = {deep_copy_collect}")
        if is_nested.__eq__(True):
            deep_copy_collect[3][0] = 'deep_copy_check'
            if id(collect) != id(deep_copy_collect) and deep_copy_collect[3][0] != collect[3][0]:
                print("--------- Collections after Modification --------- ")
                print(f"Original_Collection = {collect} \nDeep_Copy_Collection = {deep_copy_collect}")
                print("deep copy check is successful")
            else:
                print("deep copy check is not successful")
        else:
            deep_copy_collect[0] = 'deep_copy_check'
            if id(collect) != id(deep_copy_collect) and deep_copy_collect[0] != collect[0]:
                print("--------- Collections after Modification --------- ")
                print(f"Original_Collection = {collect} \nDeep_Copy_Collection = {deep_copy_collect}")
                print("deep copy check is successful")
            else:
                print("deep copy check is not successful")

    else:
        print("Invalid Operation Submitted")






# list1 = [1,2,3,4,5,6]
# list2 = [1,2,3,['mango','grapes','berry'],5,6]
# equality_copy_deepcopy_check(list1, 'Shallow Copy',False)
# equality_copy_deepcopy_check(list2, 'Shallow Copy',True)

abc = ["value", "at", "index", "2" ]
abc_str = ",".join(abc)
print(abc_str)
abc_str = abc_str.replace("," , " ")
print(abc_str)

back_to_abc = abc_str.split()
print(back_to_abc)
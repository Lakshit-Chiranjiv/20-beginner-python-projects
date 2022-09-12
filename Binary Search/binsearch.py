from turtle import st


def bin_search(list,target):
    start = 0
    end = len(list)-1
    step = 1
    found = 0

    while(start <= end):
        print(f"Step {step} : List = {list[start:end+1]}")
        step += 1
        
        mid = (start+end)//2
        if list[mid] == target:
            print(f"\nElement found at index {mid}")
            found = 1
            break
        elif list[mid] > target:
            end = mid-1
        else:
            start = mid + 1
    if found == 0:
        print("\nElement not found in list")

list = [2,5,6,14,22,47,55,69,71,80]
target = 55

bin_search(list,target)
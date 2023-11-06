def func(nums,target):
    start,end = 0, len(nums)-1
    while start<=end:
        mid = (start+end)//2
        if nums[mid] == target:
            return f'Found at position {mid}'
        if nums[start] < nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid+1
            else:
                end = mid-1
    return f'{target} NOT Found'

def main():
    nums = [4,5,6,7,0,1,2]
    #target = 3
    #print(func(nums, target))
    i=0
    while i == 0:
        print('____________________')
        ask = int(input('Search(0) or quit(1): '))
        if ask == 0:
            target=int(input('SEARCH: '))
            print(func(nums,target))
        else:
            i = ask
            print('QUITED')


main()
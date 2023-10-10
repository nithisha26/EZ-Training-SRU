#ceil value
def searchInsert(nums,target):
    def binary(si,ei):
        if si<=ei:
            mid=(si+ei)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                return binary(si,mid-1)
            return binary(mid+1,ei)
        if si>len(nums)-1:
            return 0
        return nums[si]
    return binary(0,len(nums)-1)
nums=list(map(int,input().split()))
target=int(input())
print(searchInsert(nums,target))

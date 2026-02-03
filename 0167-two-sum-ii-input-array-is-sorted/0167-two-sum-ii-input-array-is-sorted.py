


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        mylist=[]
        while(l<=r):
            sum=numbers[l]+numbers[r]
            if(sum==target):
                mylist.append(l+1)
                mylist.append(r+1)
                return mylist
            elif(sum<target):
                l+=1
            else:
                r-=1
        return mylist
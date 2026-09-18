class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #use prefix/suffix
        # index = 2    [1,2,3,4]   --> prefix = [1,2]  suffix = [4]
        

         
        prefix = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            #1 * 1, 1 * 2, 2 * 3, 6 * 
            prefix[i] = product
        

        postfix = [1] * len(nums)
        prod = 1
        for i in range(len(nums)-1, -1,-1):
            prod *= nums[i]
            postfix[i] = prod

        output = [] 
        for i in range(len(nums)):
            #if i is 0, then just take postfix
            #if i == len(nums) -1, the just take prefix
            if i == 0:
                output.append(postfix[i + 1])
            elif i == len(nums) -1:
                output.append(prefix[i - 1])
            else:
                out = prefix[i-1] * postfix[i+1]

                output.append(out)
        return output
            
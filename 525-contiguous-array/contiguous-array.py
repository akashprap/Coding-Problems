class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zerocnt = 0
        onecnt = 0
        maxi = 0
        count_dict = {0: -1}  # Initialize dictionary with count 0 at index -1

        for j in range(len(nums)):
            if nums[j] == 0:
                zerocnt += 1
            else:
                onecnt += 1

            diff = onecnt - zerocnt  # Calculate the difference between ones and zeros

            if diff in count_dict:  # If the difference is already in the dictionary
                maxi = max(maxi, j - count_dict[diff])  # Update the maximum length
            else:
                count_dict[diff] = j  # If the difference is not in the dictionary, add it

        return maxi

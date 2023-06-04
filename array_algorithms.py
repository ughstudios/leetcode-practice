
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
        i = 0
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
            i += 1
        return False


assert containsNearbyDuplicate([1,2,3,1], 3) == True
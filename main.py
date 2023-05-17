print("Test Examples")

# Problem 1st solution
def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that
    they add up to target.
    """
    # Create an empty dictionary to store the indices of numbers as we iterate over the array
    num_indices_dict = {}

    # Iterate over the array
    for i, num in enumerate(nums):
        # Calculate the complement of the current number with respect to the target
        comp = target - num
        
        # If the complement is already in the dictionary, return its index along with the current index
        if comp in num_indices_dict:
            return [num_indices_dict[comp], i]
        
        # Otherwise, add the current number and its index to the dictionary
        num_indices_dict[num] = i
    
    # If we reach this point, it means there is no pair of numbers that add up to the target
    return None

print('Problem Example 1st--')
nums = [7, 70, 11, 15]
target = 77
print(two_sum(nums, target)) 

nums = [3, 3]
target = 6
print(two_sum(nums, target))  


#Problem 2nd Solution
def is_valid(s):
    """
    Given a string s containing characters '(', ')', '{', '}', '[' and ']',
    determine if the string is valid.
    """
    # Create a stack to keep track of opening brackets
    stack_list = []
    
    # Define a dictionary to store the matching opening bracket for each closing bracket
    bracket_map_dict = {')': '(', '}': '{', ']': '['}
    
    # Iterate over each character in the string
    for char in s:
        # If the current character is an opening bracket, push it onto the stack
        if char in bracket_map_dict.values():
            stack_list.append(char)
        # If the current character is a closing bracket
        elif char in bracket_map_dict.keys():
            # If the stack is empty or the top element of the stack does not match the current closing bracket, return False
            if not stack_list or stack_list.pop() != bracket_map_dict[char]:
                return False
    
    # If the stack is not empty, return False
    if stack_list:
        return False
    
    # If we reach this point, the string contains a valid sequence of brackets
    return True

print('Problem Example 2nd--')
# Example usage
s1 = "()"
print(is_valid(s1))  # Output: True

s2 = "(]"
print(is_valid(s2))  # Output: False


#Problem 3rd solution
def top_k_frequent(nums, k):
    """
    Given an integer array nums and an integer k, return the k most frequent elements.
    """
    # Create a dictionary to store the frequency of each element
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # Sort the dictionary by descending frequency and return the first k elements
    return [x[0] for x in sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:k]]

print('Problem Example 3rd--')
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(top_k_frequent(nums1, k1)) 

nums2 = [1]
k2 = 1
print(top_k_frequent(nums2, k2))

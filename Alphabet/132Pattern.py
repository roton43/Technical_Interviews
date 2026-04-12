import json

def solve(nums):
    stack = []
    second = float('-inf')
    
    for num in reversed(nums):
        if num < second:
            return "True"
        while stack and num > stack[-1]:
            second = stack.pop()
        stack.append(num)
    
    return "False"
    

if __name__ == "__main__":
    print("Enter the array (e.g., [1, 2, 3, 4]):")
    nums = json.loads(input())
    result = solve(nums)
    result = result.lower()
    print(result)
    
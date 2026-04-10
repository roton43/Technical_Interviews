def solution(num):
    if num == 0:
        return True
    return num % 10 != 0

if __name__ == "__main__":
    try:
        raw_input = input("Enter a number to check (e.g., 123): ") 
        num = int(raw_input)
        result = solution(num)
        print(str(result).lower())
    except Exception as e:
        print(f"Error: Make sure you enter a valid input.")
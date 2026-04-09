import json

def solution(bits):
    i = 0
    n = len(bits)
    while i < n - 1:
        if bits[i] == 1:
            i += 2  
        else:
            i += 1  
    return i == n - 1

if __name__ == "__main__":
    try:
        raw_input = input("Paste your bits array here (e.g., [1, 0, 0]): ") 
        bits = json.loads(raw_input)
        result = solution(bits)
        print(str(result).lower())
    except Exception as e:
        print(f"Error: Make sure you paste a valid list like [1, 0, 0].")
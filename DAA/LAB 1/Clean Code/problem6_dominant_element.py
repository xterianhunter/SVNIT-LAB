def find_dominant_brute_force(arr):
    n = len(arr)
    threshold = n // 2

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == arr[i]:
                count += 1
        if count > threshold:
            return arr[i], count

    return None


def find_dominant_boyer_moore(arr):
    n = len(arr)
    if n == 0:
        return None

    threshold = n // 2
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    if candidate is None:
        return None

    actual_count = 0
    for num in arr:
        if num == candidate:
            actual_count += 1

    if actual_count > threshold:
        return candidate, actual_count

    return None


def parse_input(raw_input):
    if not raw_input:
        return []
    return [int(x) for x in raw_input.replace(",", " ").split()]


def main():
    raw_input = input("Enter integers: ")
    arr = parse_input(raw_input)

    if not arr:
        print("No valid integers entered.")
        return

    result = find_dominant_boyer_moore(arr)
    if result:
        elem, count = result
        print(f"Dominant Element: {elem} (Count: {count}, Threshold: > {len(arr) // 2})")
    else:
        print("No dominant element exists.")


if __name__ == "__main__":
    main()

def compare_strings(s1, s2):
    len1, len2 = len(s1), len(s2)
    min_len = min(len1, len2)

    for i in range(min_len):
        c1, c2 = ord(s1[i].lower()), ord(s2[i].lower())
        if c1 < c2:
            return -1
        elif c1 > c2:
            return 1

    if len1 < len2:
        return -1
    elif len1 > len2:
        return 1

    for i in range(min_len):
        if s1[i] != s2[i]:
            if s1[i].islower() and s2[i].isupper():
                return -1
            elif s1[i].isupper() and s2[i].islower():
                return 1
            elif ord(s1[i]) < ord(s2[i]):
                return -1
            else:
                return 1

    return 0


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if compare_strings(left[i], right[j]) <= 0:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def find_duplicates(sorted_arr):
    duplicates = []
    n = len(sorted_arr)
    i = 0

    while i < n:
        count = 1
        while i + 1 < n and compare_strings(sorted_arr[i], sorted_arr[i + 1]) == 0:
            count += 1
            i += 1
        if count > 1:
            duplicates.append((sorted_arr[i], count))
        i += 1

    return duplicates


def main():
    raw_input = input("Enter employee names: ")
    names = [name.strip() for name in raw_input.split(",") if name.strip()]

    if not names:
        print("No valid employee names entered.")
        return

    sorted_names = merge_sort(names)
    duplicates = find_duplicates(sorted_names)

    print(f"Sorted Names: {', '.join(sorted_names)}")
    if duplicates:
        print("Duplicate Names:")
        for name, count in duplicates:
            print(f"'{name}' appears {count} times")
    else:
        print("No duplicate names exist.")


if __name__ == "__main__":
    main()

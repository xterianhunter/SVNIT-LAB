def find_first_unique_brute_force(names):
    n = len(names)
    for i in range(n):
        is_unique = True
        for j in range(n):
            if i != j and names[i] == names[j]:
                is_unique = False
                break
        if is_unique:
            return names[i]
    return None


def find_first_unique_hash_map(names):
    freq = {}
    for name in names:
        freq[name] = freq.get(name, 0) + 1

    for name in names:
        if freq[name] == 1:
            return name

    return None


def parse_input(raw_input):
    if not raw_input:
        return []
    return [name.strip() for name in raw_input.split(",") if name.strip()]


def main():
    raw_input = input("Enter employee access sequence: ")
    names = parse_input(raw_input)

    if not names:
        print("No valid names entered.")
        return

    unique_emp = find_first_unique_hash_map(names)
    if unique_emp is not None:
        print(f"First Unique Employee: {unique_emp}")
    else:
        print("No unique employee found.")


if __name__ == "__main__":
    main()

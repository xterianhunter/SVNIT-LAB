def compare_strings(s1, s2):
    min_len = min(len(s1), len(s2))
    for i in range(min_len):
        c1_low, c2_low = s1[i].lower(), s2[i].lower()
        if c1_low != c2_low:
            return -1 if c1_low < c2_low else 1

    if len(s1) != len(s2):
        return -1 if len(s1) < len(s2) else 1

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s1[i].islower() and s2[i].isupper():
                return -1
            if s1[i].isupper() and s2[i].islower():
                return 1
            return -1 if s1[i] < s2[i] else 1

    return 0


def analyze_directory_ordering(names):
    n = len(names)
    if n <= 1:
        return "ALREADY_SORTED", [], None, names.copy()

    violations = []
    for i in range(n - 1):
        if compare_strings(names[i], names[i + 1]) > 0:
            violations.append(i)

    if not violations:
        return "ALREADY_SORTED", [], None, names.copy()

    if len(violations) == 1:
        x, y = violations[0], violations[0] + 1
    elif len(violations) == 2:
        x, y = violations[0], violations[1] + 1
    else:
        return "UNFIXABLE_BY_ONE_SWAP", violations, None, None

    names_copy = names.copy()
    names_copy[x], names_copy[y] = names_copy[y], names_copy[x]

    for k in range(n - 1):
        if compare_strings(names_copy[k], names_copy[k + 1]) > 0:
            return "UNFIXABLE_BY_ONE_SWAP", violations, None, None

    return "FIXABLE_BY_SWAP", violations, (x, y), names_copy


def parse_input(raw_input):
    if not raw_input:
        return []
    return [name.strip() for name in raw_input.split(",") if name.strip()]


def main():
    raw_input = input("Enter employee names: ")
    names = parse_input(raw_input)

    if not names:
        print("No valid names entered.")
        return

    status, violations, swap_pos, fixed_list = analyze_directory_ordering(names)

    if status == "ALREADY_SORTED":
        print("Directory is already sorted.")
    elif status == "FIXABLE_BY_SWAP":
        x, y = swap_pos
        print(f"Directory is NOT sorted. Violations at indices: {violations}")
        print(f"Can be sorted by swapping position {x + 1} ('{names[x]}') and position {y + 1} ('{names[y]}').")
        print(f"Sorted directory: {', '.join(fixed_list)}")
    else:
        print(f"Directory is NOT sorted. Violations at indices: {violations}")
        print("Cannot be sorted by exchanging only two names.")


if __name__ == "__main__":
    main()

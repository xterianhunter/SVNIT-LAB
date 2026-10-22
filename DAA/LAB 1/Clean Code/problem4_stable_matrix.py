def check_matrix_stability(matrix):
    n = len(matrix)
    if n < 3:
        return True, 0, [], None

    violating_positions = []
    max_diff = -1
    max_diff_info = None

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            neighbour_sum = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1]
            diff = abs(matrix[i][j] - neighbour_sum)

            if diff > 0:
                violating_positions.append((i, j))
                if diff > max_diff:
                    max_diff = diff
                    max_diff_info = ((i, j), matrix[i][j], neighbour_sum, diff)

    if not violating_positions:
        return True, 0, [], None

    return False, len(violating_positions), violating_positions, max_diff_info


def main():
    try:
        n = int(input("Enter matrix size n: ").strip())
        print(f"Enter {n} rows:")
        matrix = []
        for _ in range(n):
            matrix.append([int(x) for x in input().replace(",", " ").split()])

        is_stable, count, positions, max_info = check_matrix_stability(matrix)
        if is_stable:
            print("Matrix is stable.")
        else:
            print("Matrix is NOT stable.")
            print(f"Total violating elements: {count}")
            print(f"Violating positions: {positions}")
            if max_info:
                (r, c), val, n_sum, diff = max_info
                print(f"Maximum difference at row {r + 1}, column {c + 1}: Element = {val}, Neighbour Sum = {n_sum}, Max |Diff| = {diff}")
    except (ValueError, IndexError) as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()

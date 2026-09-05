def is_locally_balanced(matrix):
    n = len(matrix)
    if n < 3:
        return True, None, None, None

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            neighbour_sum = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1]
            if matrix[i][j] != neighbour_sum:
                return False, (i, j), matrix[i][j], neighbour_sum

    return True, None, None, None


def main():
    try:
        n = int(input("Enter matrix size n: ").strip())
        print(f"Enter {n} rows:")
        matrix = []
        for _ in range(n):
            matrix.append([int(x) for x in input().replace(",", " ").split()])

        balanced, pos, val, n_sum = is_locally_balanced(matrix)
        if balanced:
            print("Matrix is locally balanced.")
        else:
            r, c = pos
            print("Matrix is NOT locally balanced.")
            print(f"First violation at row {r + 1}, column {c + 1}: Element = {val}, Neighbour Sum = {n_sum}")
    except (ValueError, IndexError) as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()

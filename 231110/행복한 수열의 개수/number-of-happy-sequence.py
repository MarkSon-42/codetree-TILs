def count_happy_sequences(n, m, grid):
    def count_consecutive(sequence):
        count = 1
        max_count = 1
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i - 1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        return max_count

    happy_sequences = 0

    # Check rows
    for row in grid:
        if count_consecutive(row) >= m:
            happy_sequences += 1

    # Check columns
    for j in range(n):
        column = [grid[i][j] for i in range(n)]
        if count_consecutive(column) >= m:
            happy_sequences += 1

    print(happy_sequences)

# Read input
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Count and print happy sequences
count_happy_sequences(n, m, grid)
"""Math & Geometry — Reusable Templates"""
from typing import List


def rotate_image(matrix: List[List[int]]) -> None:
    """LC #48 — Rotate 90° clockwise: transpose then reverse rows."""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """LC #54."""
    result = []
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    while top <= bottom and left <= right:
        for c in range(left, right+1): result.append(matrix[top][c])
        top += 1
        for r in range(top, bottom+1): result.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left-1, -1): result.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top-1, -1): result.append(matrix[r][left])
            left += 1
    return result


def my_pow(x: float, n: int) -> float:
    """LC #50 — Fast exponentiation O(log n)."""
    if n < 0: x, n = 1/x, -n
    result = 1
    while n:
        if n & 1: result *= x
        x *= x
        n >>= 1
    return result


def set_zeroes(matrix: List[List[int]]) -> None:
    """LC #73 — Use first row/col as markers. O(1) extra space."""
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if first_row_zero:
        for j in range(n): matrix[0][j] = 0
    if first_col_zero:
        for i in range(m): matrix[i][0] = 0


if __name__ == "__main__":
    m = [[1,2,3],[4,5,6],[7,8,9]]
    rotate_image(m)
    assert m == [[7,4,1],[8,5,2],[9,6,3]]
    assert spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert my_pow(2.0, 10) == 1024.0
    print("✅ All math & geometry templates passed!")

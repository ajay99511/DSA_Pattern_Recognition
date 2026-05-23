"""
## Problem: Valid Sudoku (LC #36)
- **Pattern**: Arrays & Hashing - Multi-Dimensional Set Tracking
- **Difficulty**: Medium
- **Key Insight**: Track seen digits in three separate sets — one per row, one per column, one per 3×3 box — using (row, digit), (col, digit), and (box_id, digit) as keys; a single pass over all 81 cells is sufficient.
- **Recognition Signal**: "validate sudoku" / "check rows, columns, and boxes for duplicates" → multi-dimensional set tracking
- **Complexity**: Time O(81) = O(1), Space O(81) = O(1) — fixed 9×9 board
- **My Confidence**: 🟡
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH:
# 1. Create three sets: rows_seen, cols_seen, boxes_seen.
# 2. Iterate over every cell (r, c) in the 9×9 board.
# 3. Skip cells containing '.'.
# 4. For each digit d:
#    a. Compute box_id = (r // 3, c // 3) — identifies which 3×3 box.
#    b. Check if (r, d) in rows_seen → duplicate in row → return False.
#    c. Check if (c, d) in cols_seen → duplicate in column → return False.
#    d. Check if (box_id, d) in boxes_seen → duplicate in box → return False.
#    e. Add (r, d), (c, d), (box_id, d) to their respective sets.
# 5. If no duplicates found → return True.

# SOLUTION:
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows_seen  = set()              # Tracks (row_index, digit) pairs
        cols_seen  = set()              # Tracks (col_index, digit) pairs
        boxes_seen = set()              # Tracks (box_id, digit) pairs

        for r in range(9):
            for c in range(9):
                d = board[r][c]
                if d == '.':            # Empty cell — skip
                    continue

                box_id = (r // 3, c // 3)  # 3×3 box identifier: (0-2, 0-2)

                # Check for duplicates in row, column, and box
                if (r, d) in rows_seen:
                    return False
                if (c, d) in cols_seen:
                    return False
                if (box_id, d) in boxes_seen:
                    return False

                # Record this digit's presence
                rows_seen.add((r, d))
                cols_seen.add((c, d))
                boxes_seen.add((box_id, d))

        return True                     # No violations found


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    # Valid board (from LeetCode example)
    valid_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    assert s.isValidSudoku(valid_board) == True, "valid board"

    # Invalid board — duplicate '8' in top-left box
    invalid_board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],  # '8' appears twice in box (0,0)
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    assert s.isValidSudoku(invalid_board) == False, "invalid: duplicate in box"

    # Invalid board — duplicate in row
    row_dup_board = [
        ["5","3",".",".","7",".",".",".","5"],  # '5' appears twice in row 0
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    assert s.isValidSudoku(row_dup_board) == False, "invalid: duplicate in row"

    # All empty board — valid
    empty_board = [["." for _ in range(9)] for _ in range(9)]
    assert s.isValidSudoku(empty_board) == True, "all empty board"

    print("✅ All tests passed!")

"""Backtracking — Reusable Templates"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """LC #78."""
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    """LC #90 — Skip duplicates."""
    nums.sort()
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]: continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """LC #39 — Unlimited reuse."""
    result = []
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining: break
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  # i, not i+1
            path.pop()
    candidates.sort()
    backtrack(0, [], target)
    return result


def permutations(nums: List[int]) -> List[List[int]]:
    """LC #46."""
    result = []
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    backtrack([], [False] * len(nums))
    return result


def solve_n_queens(n: int) -> List[List[str]]:
    """LC #51."""
    result = []
    cols = set()
    pos_diag = set()  # row + col
    neg_diag = set()  # row - col
    board = [['.' ] * n for _ in range(n)]
    
    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row+col) in pos_diag or (row-col) in neg_diag:
                continue
            cols.add(col); pos_diag.add(row+col); neg_diag.add(row-col)
            board[row][col] = 'Q'
            backtrack(row + 1)
            board[row][col] = '.'
            cols.remove(col); pos_diag.remove(row+col); neg_diag.remove(row-col)
    
    backtrack(0)
    return result


def word_search(board: List[List[str]], word: str) -> bool:
    """LC #79 — Grid backtracking."""
    rows, cols = len(board), len(board[0])
    def dfs(r, c, i):
        if i == len(word): return True
        if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[i]: return False
        tmp, board[r][c] = board[r][c], '#'
        found = any(dfs(r+dr,c+dc,i+1) for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)])
        board[r][c] = tmp
        return found
    return any(dfs(r,c,0) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    assert len(subsets([1,2,3])) == 8
    assert len(permutations([1,2,3])) == 6
    assert combination_sum([2,3,6,7], 7) == [[2,2,3],[7]]
    assert len(solve_n_queens(4)) == 2
    assert word_search([["A","B"],["C","D"]], "ABDC") == True
    print("✅ All backtracking templates passed!")

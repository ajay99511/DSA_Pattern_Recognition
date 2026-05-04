"""Greedy — Reusable Templates"""
from typing import List


def max_subarray(nums: List[int]) -> int:
    """LC #53 — Kadane's Algorithm."""
    max_sum = cur_sum = nums[0]
    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)
    return max_sum


def can_jump(nums: List[int]) -> bool:
    """LC #55 — Track farthest reachable."""
    farthest = 0
    for i in range(len(nums)):
        if i > farthest: return False
        farthest = max(farthest, i + nums[i])
    return True


def jump_game_ii(nums: List[int]) -> int:
    """LC #45 — BFS-like: count levels."""
    jumps = cur_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps


def gas_station(gas: List[int], cost: List[int]) -> int:
    """LC #134."""
    if sum(gas) < sum(cost): return -1
    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start


def partition_labels(s: str) -> List[int]:
    """LC #763 — Extend partition to cover last occurrence."""
    last = {c: i for i, c in enumerate(s)}
    start = end = 0
    result = []
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            result.append(end - start + 1)
            start = end + 1
    return result


if __name__ == "__main__":
    assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert can_jump([2,3,1,1,4]) == True
    assert can_jump([3,2,1,0,4]) == False
    assert jump_game_ii([2,3,1,1,4]) == 2
    assert gas_station([1,2,3,4,5], [3,4,5,1,2]) == 3
    assert partition_labels("ababcbacadefegdehijhklij") == [9,7,8]
    print("✅ All greedy templates passed!")

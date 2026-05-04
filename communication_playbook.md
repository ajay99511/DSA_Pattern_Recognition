# 🗣️ Communication Playbook

> **Reality**: FAANG interviews are ~50% coding, ~50% communication. A perfect silent solution scores lower than a good narrated one. This playbook makes your thinking visible.

---

## The 5-Step Talk-Through Protocol

Use this for EVERY problem — practice and real interviews.

### Step 1: RESTATE (30 seconds)
> "So the problem is asking me to [restate in your own words]."
> "The input is [describe], and I need to return [describe]."
> "Just to clarify — [ask about any ambiguity]."

**Why**: Confirms understanding. Catches misinterpretations early.

### Step 2: EXAMPLES (1 minute)
> "Let me trace through this example to make sure I understand..."
> "For input [X], the output should be [Y] because [reason]."
> "Let me also think about edge cases: empty input, single element, all same values..."

**Why**: Shows thoroughness. Interviewers love candidates who think about edges first.

### Step 3: APPROACH (2 minutes)
> "I'm thinking [pattern name] because I notice [signal in the problem]."
> "My plan is: first [step 1], then [step 2], then [step 3]."
> "The brute force would be O(n²), but using [technique], I can get O(n log n)."

**Why**: This is the MONEY step. State your approach BEFORE coding.

### Step 4: TRADEOFFS (30 seconds)
> "This gives me O(n) time and O(n) space."
> "An alternative would be [X] which trades [time for space / space for time]."
> "I'll go with [chosen approach] because [reason]."

**Why**: Shows you understand the design space, not just one solution.

### Step 5: EDGE CASES (30 seconds)
> "Before I code, let me note the edge cases I need to handle:"
> "Empty input, single element, all negatives, overflow..."

**Why**: Prevents bugs and shows defensive programming.

---

## During Coding: Narration Patterns

### While Writing Code, Say:
- "I'll start by initializing my [data structure]..."
- "Now I'm iterating through the array, and for each element I'm..."
- "This condition handles the case where..."
- "I'm using [structure] here because I need O(1) [lookup/insertion]..."

### When You Hit a Tricky Part:
- "Let me think about this transition carefully..."
- "The key insight here is that [explain the non-obvious part]..."
- "I need to be careful about the boundary — let me trace through..."

### When Debugging:
- "Let me trace through my code with the example..."
- "Ah, I see the issue — on line [X], I should [fix]..."
- "Let me verify this handles the edge case of [X]..."

---

## Phrases That Signal Senior-Level Thinking

### Pattern Recognition
- "This reminds me of the [pattern name] pattern because [signal]..."
- "I recognize this as a variation of [classic problem] with the twist of [difference]..."

### Complexity Awareness
- "The brute force would be O(n²), but I can do better..."
- "Given the constraint of N ≤ 10^5, I need an O(n log n) or O(n) solution..."
- "I'm trading O(n) extra space for O(n) time improvement, which is worth it because..."

### Design Decision Communication
- "I'm choosing a hash map over sorting because we don't need ordered output..."
- "I'll use a min-heap here because I need efficient access to the smallest element..."
- "For the DP state, dp[i] represents [precise definition]..."

### Self-Correction (L5+ signal)
- "Actually, let me reconsider — this approach won't handle [edge case]..."
- "I realize my initial thought has a flaw: [explain]. Let me pivot to [new approach]..."
- "Wait — I think there's a simpler way to do this..."

### Verification
- "Let me verify my solution handles all the cases we discussed..."
- "The time complexity is O(n) because [reasoning], space is O(n) because [reasoning]..."
- "One potential improvement would be [optimization], but it's not needed for these constraints..."

---

## What NOT to Do

| ❌ Don't | ✅ Instead |
|----------|-----------|
| Code silently for 10+ minutes | Narrate every major decision |
| Say "I've seen this before, the answer is..." | Explain your reasoning from first principles |
| Jump to coding immediately | Spend 3-5 minutes on approach first |
| Say "I don't know" and give up | Use the Failure Recovery Protocol — think out loud |
| Over-explain trivial code | Focus narration on the non-obvious parts |
| Ask "is this right?" after every line | Ask "does this approach make sense?" after explaining it |

---

## Practice Drill: The 2-Minute Explain

Every day, pick ONE solved problem. Set a 2-minute timer.

**Explain to an imaginary interviewer:**
1. What the problem asks (10 sec)
2. Why you chose this pattern (20 sec)
3. Your approach in 3 steps (40 sec)
4. Time/space complexity with reasoning (20 sec)
5. One edge case and how you handle it (20 sec)

If you can't do this fluently in 2 minutes, you haven't internalized the problem.

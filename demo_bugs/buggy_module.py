1. Fix description: Add a guard to prevent division when the denominator is zero and return a safe fallback or explicit error instead.

2. Code snippet showing before/after:
```python
# Before
ratio = total / count
```

```python
# After
if count == 0:
    ratio = 0  # or raise ValueError("count must not be zero")
else:
    ratio = total / count
```

3. Brief explanation: The crash happens because `count` can be `0`; checking it before division avoids `ZeroDivisionError` and makes the behavior explicit.
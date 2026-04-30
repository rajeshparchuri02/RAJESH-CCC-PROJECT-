# Smart Study Planner using Greedy + Dynamic Programming

class Subject:
    def __init__(self, name, time_required, marks):
        self.name = name
        self.time = time_required
        self.marks = marks

# -----------------------------
# GREEDY APPROACH
# -----------------------------
def greedy_selection(subjects, total_time):
    # Sort by marks per unit time (descending)
    subjects.sort(key=lambda x: x.marks / x.time, reverse=True)

    selected = []
    current_time = 0

    for sub in subjects:
        if current_time + sub.time <= total_time:
            selected.append(sub)
            current_time += sub.time

    return selected

# -----------------------------
# DYNAMIC PROGRAMMING (KNAPSACK)
# -----------------------------
def dp_selection(subjects, total_time):
    n = len(subjects)

    # DP table
    dp = [[0 for _ in range(total_time + 1)] for _ in range(n + 1)]

    # Build table
    for i in range(1, n + 1):
        for t in range(total_time + 1):
            if subjects[i-1].time <= t:
                dp[i][t] = max(
                    subjects[i-1].marks + dp[i-1][t - subjects[i-1].time],
                    dp[i-1][t]
                )
            else:
                dp[i][t] = dp[i-1][t]

    # Backtracking to find selected subjects
    selected = []
    t = total_time

    for i in range(n, 0, -1):
        if dp[i][t] != dp[i-1][t]:
            selected.append(subjects[i-1])
            t -= subjects[i-1].time

    return selected[::-1]

# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():
    subjects = [
        Subject("Maths", 3, 90),
        Subject("Physics", 2, 70),
        Subject("Chemistry", 4, 85),
        Subject("English", 1, 40),
        Subject("Programming", 2, 95)
    ]

    total_time = 6

    print("\n--- GREEDY APPROACH ---")
    greedy_result = greedy_selection(subjects.copy(), total_time)
    for sub in greedy_result:
        print(sub.name, "Time:", sub.time, "Marks:", sub.marks)

    print("\n--- DYNAMIC PROGRAMMING APPROACH ---")
    dp_result = dp_selection(subjects, total_time)
    for sub in dp_result:
        print(sub.name, "Time:", sub.time, "Marks:", sub.marks)

if __name__ == "__main__":
    main()

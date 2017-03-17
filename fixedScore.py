"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def Score_return():
    score = float(input("Enter score: "))
    if score < 0:
        return_value = "Invalid Score"
    elif score > 100:
        return_value = "Invalid Score"
    elif score >= 90:
        return_value = "Excellent"
    elif score >= 50:
        return_value = "Passable"
    else:
        return_value = "Bad"
    return(return_value)

print(Score_return())

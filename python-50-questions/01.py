# ✅ Ryerson letter grade

# def ryerson_letter_grade(pct):

# Given the percentage grade for the course, calculate and return the letter grade that would appear in the Ryerson grades transcript, as defined on the page Ryerson Grade Scales. The letter grade should be returned as a string that consists of the uppercase letter followed by the possible modifier "+" or "-". The function should work correctly for all values of pct from 0 to 150.

# (Same as all 49 programming problems that follow this problem, this can be solved in various different ways.)

# pct   Expected result
# 45    "F"
# 62    "C-"
# 89    "A"
# 107   "A+"


def ryerson_letter_grade(pct):
    if (pct < 0):
        return "Error, invalid entry. Must be between 0 and 150."
    elif (pct < 50):
        return "F"
    elif (pct < 53):
        return "D-"
    elif (pct < 57):
        return "D"
    elif (pct < 60):
        return "D+"
    elif (pct < 63):
        return "C-"
    elif (pct < 67):
        return "C"
    elif (pct < 70):
        return "C+"
    elif (pct < 73):
        return "B-"
    elif (pct < 77):
        return "B"
    elif (pct < 80):
        return "B+"
    elif (pct < 80):
        return "B+"
    elif (pct < 85):
        return "A-"
    elif (pct < 90):
        return "A"
    elif (pct < 150):
        return "A+"
    else:
        return "Error, invalid entry. Must be between 0 and 150."


def testRyersonLetterGrade():
    assert (ryerson_letter_grade(23) == "F")
    assert (ryerson_letter_grade(51) == "D-")
    assert (ryerson_letter_grade(123) == "A+")
    assert (ryerson_letter_grade(87) == "A")
    assert (ryerson_letter_grade(77) == "B+")


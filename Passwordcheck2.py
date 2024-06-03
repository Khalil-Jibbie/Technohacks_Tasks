import re

def assess_password_strength(password):
    
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])

    
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_criteria:
        feedback.append("Password should contain at least one special character.")
    
    
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback


password = input("Enter a password to assess: ")
strength, feedback = assess_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for message in feedback:
        print(f"- {message}")
import re

def assess_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !@#$%).")

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback


# --- Main Program ---
if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐")
    password = input("Enter your password: ")

    strength, suggestions = assess_password_strength(password)

    print(f"\nPassword Strength: {strength}")

    if suggestions:
        print("\nSuggestions to improve:")
        for tip in suggestions:
            print(f"- {tip}")

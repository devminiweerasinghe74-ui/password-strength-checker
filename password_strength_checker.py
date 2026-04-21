import string

def password_length_check(input_password):
    
    count_pass_length = len(input_password)

    has_upper = any(c.isupper() for c in input_password)
    has_digits = any(c.isdigit() for c in input_password)
    has_lower = any(c.islower() for c in input_password)
    has_symbols = any(c in string.punctuation for c in input_password)
    
    score = 0

    #Length scoring
    if count_pass_length>=10:
        score += 2
    elif count_pass_length>=6:
        score += 1
    
    #Character checking
    if has_upper:
        score += 1
    if has_digits:
        score += 1
    if has_lower:
        score += 1
    if has_symbols:
        score += 1
    
    #Strength decision
    if score<=2:
        strength = "Weak"
    elif score<=4:
        strength = "Medium"
    else:
        strength = "Strong"
    
    #Suggestions
    suggestions = []

    if count_pass_length < 6:
        suggestions.append("Increase password length")
    if not has_upper:
        suggestions.append("Add uppercase letters")
    if not has_digits:
        suggestions.append("Add digits")
    if not has_lower:
        suggestions.append("Add lowercase letters")
    if not has_symbols:
        suggestions.append("Add symbols")
        

    return strength,suggestions
    

def main():

    while True:
        password = input("\nEnter the password or enter q to exit: ")

        if password == 'q':
            break

        strength,suggestions = password_length_check(password)

        print(f"Password Strength: {strength}")

        if suggestions and strength != "Strong":
            print("Suggestions:")
            for s in suggestions:
                print("-",s)


if __name__ == "__main__":
    main()

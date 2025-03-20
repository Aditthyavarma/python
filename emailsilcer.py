def email_slicer(email):
    try:
        username, domain = email.split('@')
        return f"Username: {username}\nDomain: {domain}"
    except ValueError:
        return "Invalid email format!"

email = input("Enter your email: ")
print(email_slicer(email))


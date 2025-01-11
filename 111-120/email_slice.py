# 8. Email Slicer - Splits email into username and domain
def slice_email(email):
    try:
        # Split email at @ symbol
        username, domain = email.split('@')
        return {
            "username": username,
            "domain": domain
        }
    except:
        return "Invalid email format"
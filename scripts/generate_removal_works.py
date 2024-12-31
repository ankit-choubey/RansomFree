def generate_removal_instructions(email, platforms):
    instructions = {}
    for platform in platforms:
        if platform == "Google":
            instructions[platform] = "Visit https://myaccount.google.com/privacy-checkup to manage your Google data."
        elif platform == "Facebook":
            instructions[platform] = "Go to https://www.facebook.com/help/delete_account to delete your Facebook account."
        else:
            instructions[platform] = f"No manual instructions available for {platform}."
    return instructions
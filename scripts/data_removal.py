import requests

def send_removal_request(email, platform):
    """Send a data removal request to a specific platform."""
    removal_endpoints = {
        "Google": "https://myaccount.google.com/privacy-checkup",
        "Facebook": "https://www.facebook.com/help/delete_account",
        "Twitter": "https://help.twitter.com/forms/privacy",
    }

    if platform not in removal_endpoints:
        return f"Platform {platform} is not supported for automated removal."

    try:
        # Simulate sending a request (replace with real API calls if available)
        response = requests.post(removal_endpoints[platform], data={"email": email})
        if response.status_code == 200:
            return f"Removal request sent to {platform} successfully."
        else:
            return f"Failed to send removal request to {platform}. Status code: {response.status_code}."
    except Exception as e:
        return f"Error sending removal request to {platform}: {str(e)}"

def generate_removal_instructions(email, platforms):
    """Generate manual removal instructions for unsupported platforms."""
    instructions = {}
    for platform in platforms:
        if platform == "LinkedIn":
            instructions[platform] = (
                "Visit https://www.linkedin.com/help/linkedin/ask/TS-RSF to request data removal."
            )
        else:
            instructions[platform] = f"No instructions available for {platform}."
    return instructions

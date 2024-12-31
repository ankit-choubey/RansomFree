import os
import concurrent.futures

def run_theharvester(email):
    """Run theHarvester tool with the domain extracted from the email."""
    domain = email.split("@")[-1]
    command = f"python3 ~/Desktop/Ransomfree/tools/theHarvester/theHarvester.py"
    try:
        result = os.popen(command).read()
        return f"Your IPs & SubDomains Results:\n{result}"
    except Exception as e:
        return f"Error running Your IPs & SubDomains: {str(e)}"

def run_spiderfoot(email):
    """Run SpiderFoot tool optimized for email."""
    command = f"python3 ~/Desktop/Ransomfree/tools/spiderfoot/sf.py"
    try:
        result = os.popen(command).read()
        return f"Analyzes Your FootPrint Results:\n{result}"
    except Exception as e:
        return f"Error running Analyzes Your FootPrint: {str(e)}"

def run_holehe(email):
    """Run Holehe tool with the provided email."""
    command = f"holehe {email}"
    try:
        result = os.popen(command).read()
        return f"Website Presence Results:\n{result}"
    except Exception as e:
        return f"Error running Website Presence: {str(e)}"

def run_sherlock(email):
    """Run Sherlock tool with the username extracted from the email."""
    username = email.split("@")[0]
    command = f"sherlock {username} --timeout 10"
    try:
        result = os.popen(command).read()
        return f"Checking UserName :\n{result}"
    except Exception as e:
        return f"Error running UserName: {str(e)}"

def main():
    """Main function to run all tools simultaneously."""
    print("Welcome to the OSINT Automation Tool")
    email = input("Enter the email ID to investigate: ")

    if "@" not in email:
        print("Invalid email format. Please provide a valid email ID.")
        return

    # Run all tools concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_harvester = executor.submit(run_theharvester, email)
        future_spiderfoot = executor.submit(run_spiderfoot, email)
        future_holehe = executor.submit(run_holehe, email)
        future_sherlock = executor.submit(run_sherlock, email)

        results = [
            future_harvester.result(),
            future_spiderfoot.result(),
            future_holehe.result(),
            future_sherlock.result()
        ]

    # Display results in a user-friendly format
    print("\n" + "="*50)
    print(f"Results for {email}:\n")
    for result in results:
        print(result)
        print("\n" + "="*50)

if __name__ == "__main__":
    main()

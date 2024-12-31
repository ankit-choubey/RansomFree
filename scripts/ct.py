import os
import concurrent.futures

def run_theharvester(email):
    domain = email.split("@")[-1]
    command = f"python3 ~/Desktop/Ransomfree/tools/theHarvester/theHarvester.py -d {domain} -b all"
    try:
        result = os.popen(command).read()
        return {"tool": "Your IPs & SubDomains", "data": result}
    except Exception as e:
        return {"tool": "Your IPs & SubDomains", "data": f"Error: {str(e)}"}

def run_spiderfoot(email):
    command = f"python3 ~/Desktop/Ransomfree/tools/spiderfoot/sf.py -s email -t {email}"
    try:
        result = os.popen(command).read()
        return {"tool": "Analyzes Your FootPrint", "data": result}
    except Exception as e:
        return {"tool": "Analyzes Your FootPrint", "data": f"Error: {str(e)}"}

def run_holehe(email):
    command = f"holehe {email}"
    try:
        result = os.popen(command).read()
        return {"tool": "Website Presence", "data": result}
    except Exception as e:
        return {"tool": "Website Presence", "data": f"Error: {str(e)}"}

def run_sherlock(email):
    username = email.split("@")[0]
    command = f"sherlock {username} --timeout 10"
    try:
        result = os.popen(command).read()
        return {"tool": "Checking UserName", "data": result}
    except Exception as e:
        return {"tool": "Checking UserName", "data": f"Error: {str(e)}"}

def run_osint_tools(email):
    """Run all OSINT tools and return their results."""
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(run_theharvester, email),
            executor.submit(run_spiderfoot, email),
            executor.submit(run_holehe, email),
            executor.submit(run_sherlock, email)
        ]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return results
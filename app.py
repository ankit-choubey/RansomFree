from flask import Flask, render_template, request, send_file
from scripts.ct import run_osint_tools  # type: ignore
from scripts.data_removal import send_removal_request, generate_removal_instructions

app = Flask(__name__)

@app.route("/")
def index():
    """Render the homepage with the input form."""
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    """Run OSINT tools and display results."""
    email = request.form.get("email")
    if not email or "@" not in email:
        return render_template("index.html", error="Please enter a valid email address.")

    # Run OSINT tools
    results = run_osint_tools(email)
    return render_template("results.html", email=email, results=results)

@app.route("/remove_data", methods=["POST"])
def remove_data():
    """Render the data removal options page."""
    email = request.form.get("email")
    platforms = request.form.getlist("platforms")

    # Generate manual removal instructions
    instructions = generate_removal_instructions(email, platforms)

    # Save manual instructions to a text file
    with open("manual_removal.txt", "w") as file:
        file.write(f"Manual Data Removal Instructions for {email}\n")
        file.write("=" * 50 + "\n")
        for platform, instruction in instructions.items():
            file.write(f"{platform}: {instruction}\n")

    return render_template("remove_data.html", email=email, platforms=platforms, instructions=instructions)

@app.route("/removal_status", methods=["POST"])
def removal_status():
    """Handle automated data removal requests."""
    email = request.form.get("email")
    platforms = request.form.getlist("platforms")
    results = []

    with open("automated_removal.txt", "w") as file:
        file.write(f"Automated Data Removal Status for {email}\n")
        file.write("=" * 50 + "\n")

        for platform in platforms:
            result = send_removal_request(email, platform)
            results.append({"platform": platform, "status": result})
            file.write(f"{platform}: {result}\n")

    return render_template("removal_status.html", email=email, results=results)

@app.route("/download/<filename>")
def download_file(filename):
    """Serve the text files for download."""
    try:
        return send_file(filename, as_attachment=True)
    except FileNotFoundError:
        return f"File {filename} not found.", 404

if __name__ == "__main__":
    app.run(debug=True)


A minimal, dependency-free Python project featuring a command-line interface that reads from and writes to a local `data.json` database.

## Project Structure
- `app.py`: The main interactive command-line application.
- `data.json`: Local JSON file acting as a flat-file database.
- `README.md`: Documentation for the project.
- `.gitignore`: Standard Git configuration file to exclude cache and IDE folders.

## Features
- **Zero Dependencies**: Uses only standard Python library packages (`json`, `os`, `sys`, `datetime`, `ctypes`).
- **Data Persistence**: Automatically reads from and writes back updates to the local `data.json`.
- **Colorful Terminal UI**: Includes cross-platform ANSI colors (configured to support Windows Command Prompt and PowerShell as well).

## Getting Started

### Prerequisites
- Python 3.6 or higher.

### Running the Application
Run the script using python:
```bash
python app.py
```
=======
# astro-pawn-agent
A lightweight, multi-agent AI system built for Astro Pawn to automate FFL compliance, optimize inventory cross-selling, and handle customer reviews with zero token cost. Created for the Kaggle "Agents for Business" Capstone track.

Astro Pawn AI: Enterprise Agent System 🎸🛠️


Hey everyone. This is my submission for the Kaggle Capstone "Agents for Business" track.

Instead of building an abstract tech demo, I wanted to solve actual operational bottlenecks for a real brick-and-mortar business: Astro Pawn in Pearland, TX. Based on real storefront inventory and actual Google Reviews, I built a lightweight, multi-agent routing system designed to drive sales, enforce business rules, and save staff time—all while keeping compute costs at absolute zero.

💡 The Business Problem
Pawn shops deal with massive context switching. In a single hour, an employee might have to:

De-escalate a frustrated customer at the counter.

Check the back room for a specific model of bass guitar.

Explain complex, highly-regulated FFL (Federal Firearms License) transfer fees over the phone.

The Solution: A specialized, multi-agent AI system that acts as a digital general manager, automatically triaging these inquiries before they eat up staff time.

🏗️ Architecture & "Token-Diet" Design
This project was built using the Antigravity ADK. Because LLM API costs can spiral quickly for small businesses, I designed this with a strict zero-cost local routing architecture.

Instead of making an expensive LLM call just to figure out what a user wants, the main_router_agent uses local keyword mapping to instantly route queries to one of three specialized sub-agents.

Customer Success Agent: Reads sentiment. If a review mentions "bad vibes," it drafts an apology and logs an internal training alert. If it praises "Stephanie," it logs employee kudos.

Sales & Inventory Concierge: Queries the local data.json database. If a customer asks for a standard bass and we only have a 5-string, the agent automatically pivots to cross-sell a Fender Rumble 15 Amp.

FFL Compliance Expert: Automates regulatory FAQs. It accurately quotes the standard $40 FFL transfer fee, but knows to apply the $30 discount if the user is a Texas LTC holder.

🚀 How to Run Locally
Because of the lightweight routing design, you don't need any complex environment variables or heavy API keys to test the core logic.

1. Clone the repository

Bash
git clone https://github.com/yourusername/astro-pawn-agent.git
cd astro-pawn-agent
2. Verify the dataset
Ensure the data.json file is in your root directory. This acts as our localized business context (mock POS system and store rules).

3. Run the interactive terminal

Bash
python app.py
🧪 Try These Test Scenarios!
Once the terminal is running, try dropping these real-world scenarios into the prompt to see how the Router delegates the work:

Test the Compliance Rules: Type How much for a gun transfer?

Test the Sales Pipeline: Type Do you guys have any bass guitars right now?

Test the Brand Protection: Type The staff ignored me and gave me bad vibes.

Built for the Kaggle AI Agents Capstone Track: Agents for Business
>>>>>>> 8687fc4cd4dace150b08179a45de35e47a88a492

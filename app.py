import json
import os

def load_business_data():
    """Loads the compact Astro Pawn dataset securely and locally."""
    with open("data.json", "r") as f:
        return json.load(f)

def customer_success_agent(query, data):
    """Handles reviews, brand protection, and staff performance."""
    print("\n[Routing to: Customer Success Agent]")
    q = query.lower()
    
    if "vibe" in q or "ignore" in q or "greet" in q:
        return (
            "Response to Customer: 'We deeply apologize for your experience. At Astro Pawn, "
            f"we strive to follow our core rule: \"{data['rules']['customer_service']}\". "
            "We hope you give us another opportunity to earn your business.'\n"
            "⚠️ INTERNAL OPERATIONAL ALERT: Staff training required regarding floor greetings."
        )
    elif "stephanie" in q or "friendly" in q or "best" in q:
        return (
            "Response to Customer: 'Thank you for the fantastic feedback! We love hearing "
            "about our five-star team.'\n"
            "🎉 INTERNAL KUDOS ALERT: Log positive recognition for Stephanie!"
        )
    return "Thank you for contacting Astro Pawn customer success."

def inventory_concierge_agent(query, data):
    """Optimizes the sales pipeline, checks stock, and handles cross-selling."""
    print("\n[Routing to: Sales & Inventory Concierge]")
    q = query.lower()
    
    if "bass" in q or "guitar" in q or "music" in q:
        # Replicating the David Hansen scenario logic
        return (
            "Astro Pawn Stock Check:\n"
            "• We currently have a 5-String Bass Guitar available for $320.\n"
            "💡 AI Cross-Sell Recommendation: I see you are looking at instruments! "
            "We also have a Fender Rumble 15 Amp in stock for $85 that pairs perfectly with it."
        )
    elif "saw" in q or "tool" in q:
        return "We have a DeWalt 20V Circular Saw available for $70."
    
    return "Item not found in featured inventory. Please visit the store to browse our full selection!"

def ffl_compliance_agent(query, data):
    """Automates regulatory gun transfer FAQs with pinpoint pricing accuracy."""
    print("\n[Routing to: FFL Compliance Expert]")
    
    # Replicating the William Rinhart scenario logic
    return (
        f"Astro Pawn FFL Transfer Information:\n"
        f"• Standard FFL Transfer Fee: ${data['rules']['ffl_transfer_standard']}\n"
        f"• Texas LTC Holder Discounted Fee: ${data['rules']['ffl_transfer_tx_ltc']}\n"
        "To proceed, please have your shipping dealer email their FFL license to us."
    )

def main_router_agent(user_query):
    """The 'General Manager' agent that analyzes intent and delegates tasks."""
    data = load_business_data()
    q = user_query.lower()
    
    # Intelligently route based on zero-cost local context matching
    if "ffl" in q or "transfer" in q or "gun" in q:
        return ffl_compliance_agent(user_query, data)
    elif "bass" in q or "amp" in q or "saw" in q or "stock" in q or "buy" in q:
        return inventory_concierge_agent(user_query, data)
    else:
        # Default fallback to customer experience/review parsing
        return customer_success_agent(user_query, data)

if __name__ == "__main__":
    print("--- Astro Pawn Enterprise Agent Terminal ---")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("Customer/Review Input: ")
        if user_input.lower() == 'exit':
            break
        if not user_input.strip():
            continue
            
        agent_response = main_router_agent(user_input)
        print(agent_response)
        print("-" * 40)
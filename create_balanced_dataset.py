import pandas as pd
import json

# Define expanded email-response pairs
email_data = [
    # Original scenarios from before...
    # Meeting scheduling
    {"email": "Can we schedule a meeting for next week?", 
     "response": "I'd be happy to meet next week. Could you please suggest a few time slots that work best for you?"},
    {"email": "I need to reschedule our 2pm call today.", 
     "response": "No problem at all. Would tomorrow at the same time work for you? If not, please suggest an alternative time."},
    
    # New scenarios below:
    # Sales and Client Relations
    {"email": "I'm interested in your enterprise solution. Can we discuss pricing?",
     "response": "Thank you for your interest in our enterprise solution. I'd be delighted to discuss pricing and how we can meet your specific needs. Would you be available for a brief call this week?"},
    {"email": "We've been experiencing issues with the latest delivery.",
     "response": "I apologize for any inconvenience with the recent delivery. Could you please provide specific details about the issues you're experiencing? This will help us address them promptly."},
    
    # HR and Internal Communications
    {"email": "When can I expect my annual performance review?",
     "response": "Your annual performance review is scheduled for next month. I'll send you the exact date and time by the end of this week, along with any preparation materials you might need."},
    {"email": "I'd like to request time off for next month.",
     "response": "Thank you for your time-off request. Please submit it through our HR portal, and I'll review it right away. Generally, we try to process these requests within 48 hours."},
    
    # IT Support
    {"email": "My account is locked after multiple login attempts.",
     "response": "I'll help you regain access to your account. For security purposes, please verify your employee ID, and I'll guide you through our account recovery process."},
    {"email": "When will the system maintenance be completed?",
     "response": "The system maintenance is scheduled to complete by 6 PM EST today. I'll send out a notification once all systems are back online and fully operational."},
    
    # Project Management
    {"email": "We're falling behind on the milestone deadlines.",
     "response": "I understand your concern about the project timeline. Let's schedule a brief team meeting tomorrow to review our priorities and adjust the schedule. I'll prepare a revised timeline for discussion."},
    {"email": "Can you share the latest project metrics?",
     "response": "I'll prepare a comprehensive report of our current project metrics. You'll receive it within the next hour, including progress updates, resource allocation, and any potential bottlenecks we're addressing."},
    
    # Finance and Budget
    {"email": "The invoice for Project X hasn't been processed yet.",
     "response": "I'll look into the status of the Project X invoice right away. Could you please share the invoice number? I'll ensure it gets processed through our system and update you on the payment timeline."},
    {"email": "We need to discuss the Q3 budget allocation.",
     "response": "I agree we should review the Q3 budget allocation. I've prepared a preliminary analysis of our spending patterns and future needs. Would you like to schedule a detailed discussion this week?"},
    
    # Legal and Compliance
    {"email": "Please review the attached contract draft.",
     "response": "I'll review the contract draft and provide my feedback by end of day tomorrow. In the meantime, please let me know if there are any specific clauses you'd like me to focus on."},
    {"email": "When is the deadline for the compliance training?",
     "response": "The compliance training deadline is set for the end of this month. You can access the training modules through our learning portal. I'll send you the direct link and your login credentials."},
    
    # Marketing and Communications
    {"email": "Need approval for the social media campaign.",
     "response": "I'll review the social media campaign materials today. Please ensure you've included the campaign objectives, target metrics, and budget allocation in your proposal for a faster approval process."},
    {"email": "When will the new product brochures be ready?",
     "response": "The new product brochures are currently in final design review. We expect to have them ready for distribution by next Wednesday. I'll share the digital proof with you tomorrow for a final check."},
    
    # Customer Support
    {"email": "Customer reporting issues with latest software update.",
     "response": "I'll investigate the reported issues with our technical team immediately. Could you provide the specific error messages or behaviors the customer is experiencing? This will help us diagnose and resolve the problem faster."},
    {"email": "Need urgent response for VIP client inquiry.",
     "response": "I'm prioritizing this VIP client inquiry right now. I'll personally handle their request and ensure they receive a response within the next hour. Please share any specific requirements or preferences we should consider."},
    
    # Remote Work and Collaboration
    {"email": "Having trouble accessing the shared drive.",
     "response": "Let me help you with the shared drive access. First, please try clearing your cache and restarting your VPN connection. If that doesn't work, I'll coordinate with IT support to resolve this immediately."},
    {"email": "Team members in different time zones missing meetings.",
     "response": "I understand the challenges with global team coordination. I'll create a shared calendar with all time zones clearly marked and propose alternate meeting times that work better for everyone."}
]

# Convert to training format
def create_training_data(email_pairs, output_path="training_data.jsonl"):
    with open(output_path, "w", encoding="utf-8") as f:
        for pair in email_pairs:
            formatted_pair = {
                "prompt": f"### EMAIL:\n{pair['email']}\n\n### RESPONSE:\n",
                "completion": pair["response"]
            }
            f.write(json.dumps(formatted_pair) + "\n")
    
    print(f"Created training dataset with {len(email_pairs)} pairs")

# Create the dataset
create_training_data(email_data)
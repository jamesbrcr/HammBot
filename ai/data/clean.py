# Cleaning message data
import pandas as pd
import re

# Load the CSV file
input_file = 'ai/data/jarebear_messages.csv'  
output_file = 'ai/data/jmessages_clean.csv'  

# Read the CSV into a DataFrame
df = pd.read_csv(input_file)

print(df.columns)

# Define a function to clean the messages
def clean_message(message):
    if pd.isna(message):
        return ""
    # Convert to string
    message = str(message)
    # Remove patterns like <@.....>
    message = re.sub(r'<@\d+>', '', message)
    # Strip any leading/trailing whitespace
    return message.strip()

# Apply the cleaning function to each message
df['Message'] = df['Message'].apply(clean_message)

# Remove rows where the message length is less than 3 characters
df = df[df['Message'].str.len() >= 3]

# Save the cleaned data to a new CSV file
df.to_csv(output_file, index=False)

print(f"Cleaned data saved to {output_file}")
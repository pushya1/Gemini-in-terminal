import google.generativeai as genai
from colorama import Fore, Back, Style, init

# Initialize the colorama module
init()

# Function to print colored text
def print_colored(text, color, font=Style.BRIGHT):
    print(color +font +text + Style.RESET_ALL)

# Main function
def main():
    print_colored("Hello, USER!", Style.BRIGHT)

    # Configure the GenerativeAI API
    genai.configure(api_key="PAST_YOUR_KEY_HERE")

    # Create a GenerativeModel instance
    model = genai.GenerativeModel('gemini-pro')

    # Loop for continuous interaction
    while True:
        query = input(Fore.YELLOW+Style.NORMAL + "How can I help you today? (Type 'bye' to exit)\n"+Fore.RED+Style.BRIGHT)

        # Check for exit condition
        if query.lower() == 'bye' or 'exit':
            print_colored("Goodbye!", Fore.WHITE)
            break

        # Generate response
        response = model.generate_content(query)
        print_colored(response.text, Fore.CYAN)
        print_colored("_______________________________________", Fore.YELLOW)

if __name__ == "__main__":
    main()

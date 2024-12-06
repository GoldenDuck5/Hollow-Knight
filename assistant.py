import os
import pyttsx3
import webbrowser
import platform
import openai
import re
from sympy import symbols, solve, simplify, plot
import matplotlib.pyplot as plt
import numpy as np

# Initialize OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Text-to-Speech
text_to_speech_engine = pyttsx3.init()
text_to_speech_engine.setProperty('rate', 150)
text_to_speech_engine.setProperty('volume', 1.0)

def speak(text):
    """Speak the given text."""
    print(f"Assistant: {text}")
    text_to_speech_engine.say(text)
    text_to_speech_engine.runAndWait()

# --- File Management Functions ---
def search_file(file_name, directory):
    """Search for a file in a directory."""
    try:
        for root, dirs, files in os.walk(directory):
            if file_name in files:
                return os.path.join(root, file_name)
        return "File not found."
    except Exception as e:
        return f"Error searching for the file: {e}"

def delete_file(file_path):
    """Delete a file."""
    try:
        os.remove(file_path)
        return "File deleted successfully."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"Error deleting file: {e}"

def list_files(directory):
    """List all files in a directory."""
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        return "Directory not found."
    except Exception as e:
        return f"Error listing files: {e}"

# --- SymPy and Matplotlib Integration ---
def solve_equation(equation_str):
    """Solve a mathematical equation."""
    try:
        x = symbols('x')
        equation = eval(equation_str)
        solutions = solve(equation, x)
        return solutions
    except Exception as e:
        return f"Error solving equation: {e}"

def simplify_expression(expression_str):
    """Simplify a mathematical expression."""
    try:
        x = symbols('x')
        expression = eval(expression_str)
        simplified = simplify(expression)
        return simplified
    except Exception as e:
        return f"Error simplifying expression: {e}"

def plot_function(expression_str):
    """Plot a mathematical function."""
    try:
        x = np.linspace(-10, 10, 400)
        y = eval(expression_str)
        plt.plot(x, y)
        plt.title(f"Plot of {expression_str}")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.grid()
        plt.show()
    except Exception as e:
        return f"Error plotting function: {e}"

# --- OpenAI Integration --- 
def get_openai_response(prompt):
    """Get a response from OpenAI API."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can also use "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return "I'm having trouble connecting to OpenAI right now. Please try again later."

# --- Natural Language Matching ---
def interpret_command(user_input):
    """Interpret user input using patterns and keywords."""
    user_input = user_input.lower()

    # Regular Expressions for Matching Commands
    if re.search(r"(solve|find).*equation", user_input):
        return "solve_equation"
    elif re.search(r"(simplify|reduce).*expression", user_input):
        return "simplify_expression"
    elif re.search(r"(plot|graph|visualize).*function", user_input):
        return "plot_function"
    elif re.search(r"(find|search).*file", user_input):
        return "find_file"
    elif re.search(r"(delete|remove).*file", user_input):
        return "delete_file"
    elif re.search(r"(list|show).*files", user_input):
        return "list_files"
    elif re.search(r"(search|open).*browser", user_input):
        return "web_search"
    elif re.search(r"(exit|bye|quit)", user_input):
        return "exit"
    else:
        return "openai_fallback"

# --- Main Assistant Functionality ---
def assistant_functionality():
    """Main function to run the assistant."""
    speak("Hello! I am your assistant. How can I help you today?")
    
    while True:
        user_input = input("You: ").strip()
        command = interpret_command(user_input)
        
        try:
            if command == "solve_equation":
                speak("Please provide the equation to solve. Use 'x' as the variable.")
                equation = input("Equation: ").strip()
                solutions = solve_equation(equation)
                speak(f"The solutions are: {solutions}")

            elif command == "simplify_expression":
                speak("Please provide the expression to simplify.")
                expression = input("Expression: ").strip()
                result = simplify_expression(expression)
                speak(f"The simplified expression is: {result}")

            elif command == "plot_function":
                speak("Please provide the mathematical function to plot. Use 'x' as the variable.")
                function = input("Function: ").strip()
                result = plot_function(function)
                if result:
                    speak(result)

            elif command == "find_file":
                speak("What is the name of the file?")
                file_name = input("File Name: ").strip()
                result = search_file(file_name, ".")  # Search in the current directory
                speak(result)

            elif command == "delete_file":
                speak("What is the file path?")
                file_path = input("File Path: ").strip()
                result = delete_file(file_path)
                speak(result)

            elif command == "list_files":
                speak("Which directory should I list?")
                directory = input("Directory: ").strip()
                result = list_files(directory)
                if isinstance(result, list):
                    speak(", ".join(result))
                else:
                    speak(result)

            elif command == "web_search":
                speak("What should I search for?")
                query = input("Search Query: ").strip()
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak(f"Here are the search results for {query}.")

            elif command == "exit":
                speak("Goodbye! Have a great day.")
                break

            elif command == "openai_fallback":
                response = get_openai_response(user_input)
                speak(response)
        except Exception as e:
            speak(f"An error occurred while processing your request: {e}")

# Start the assistant
if __name__ == "__main__":
    assistant_functionality()

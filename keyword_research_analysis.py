import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from colorama import Fore, Style
# Function for keyword input
def keyword_identification():
    """
    Prompt the user to input keywords.
    """
    keywords = input("Enter keywords separated by commas: ").split(',')
    keywords = [keyword.strip() for keyword in keywords]
    print(Fore.GREEN + "Keywords identified: " + ', '.join(keywords) + Style.RESET_ALL)
    return keywords


# Simulated logic to fetch related keywords (can be replaced with real logic if implemented later)
def fetch_related_keywords(keyword):
    """
    Simulate fetching related keywords for the entered keyword.
    """
    related_keywords = [f"{keyword} trends", f"{keyword} analysis", f"{keyword} insights", f"{keyword} tips"]
    print(f"Related keywords for '{keyword}': {related_keywords}")
    return related_keywords


# Analyze each keyword to simulate metrics
def analyze_keyword_metrics(keywords):
    """
    Analyze each keyword and simulate some metrics calculation.
    """
    keyword_metrics = {}
    for keyword in keywords:
        print(f"Analyzing metrics for keyword: {keyword}")
        search_volume = len(keyword) * 1000
        total_reaches = len(keyword) * 2000
        difficulty = len(keyword) * 10

        # Simulate fetching related keywords
        related_keywords = fetch_related_keywords(keyword)

        keyword_metrics[keyword] = {
            "Search Volume": search_volume,
            "Total Reaches": total_reaches,
            "Difficulty": difficulty,
            "Related Keywords": ', '.join(related_keywords)
        }
    print("Metrics analysis complete.")
    return keyword_metrics


# Function to display results in a tabular format
def display_results(data):
    """
    Display results neatly using tabular formatting.
    """
    table_data = []
    for keyword, metrics in data.items():
        table_data.append([
            keyword,
            metrics["Search Volume"],
            metrics["Total Reaches"],
            metrics["Difficulty"],
            metrics["Related Keywords"]
        ])

    headers = ["Keyword", "Search Volume", "Total Reaches", "Difficulty", "Related Keywords"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


# Save metrics to a CSV without overwriting old data (append logic)
def save_results_to_csv(data, filename):
    """
    Append results to a CSV file rather than overwriting.
    """
    try:
        # If the file already exists, load its content
        try:
            existing_df = pd.read_csv(filename, index_col=0)
        except FileNotFoundError:
            # If no file exists, start with an empty DataFrame
            existing_df = pd.DataFrame()
        
        # Convert the current data to a DataFrame and append
        new_df = pd.DataFrame.from_dict(data, orient='index')
        combined_df = pd.concat([existing_df, new_df]).drop_duplicates()
        combined_df.to_csv(filename, index=True)
        print(Fore.BLUE + f"Results saved to {filename}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Failed to save results to CSV: {e}" + Style.RESET_ALL)


# Main menu logic
def main():
    filename = "keyword_metrics.csv"
    while True:
        # Main menu for interaction
        print("\nSelect an option:")
        print("1. Search for a new keyword")
        print("2. View previous search results")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Handle new keyword search
            keywords = keyword_identification()
            keyword_metrics = analyze_keyword_metrics(keywords)

            # Display the results
            print("\nKeyword Metrics:")
            display_results(keyword_metrics)

            # Save the new search results persistently
            save_results_to_csv(keyword_metrics, filename)

        elif choice == '2':
            # View previous search results if any exist
            try:
                previous_results = pd.read_csv(filename, index_col=0)
                print("\nPrevious Search Results:")
                print(tabulate(previous_results, headers='keys', tablefmt="grid"))
            except FileNotFoundError:
                print(Fore.RED + "No previous search results found. Please search for keywords first." + Style.RESET_ALL)

        elif choice == '3':
            # Exit menu loop
            print(Fore.CYAN + "Exiting the application. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
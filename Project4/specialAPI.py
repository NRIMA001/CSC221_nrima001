import requests
import matplotlib.pyplot as plt

"""To get a specific country's COVID'19 Data"""

def get_covid_stats(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)
    data = response.json()

    if 'message' in data:
        print(f"Error: {data['message']}")
        return

    country_name = data['country']
    total_cases = data['cases']
    total_deaths = data['deaths']
    total_recovered = data['recovered']

    # Plotting
    categories = ['Total Cases', 'Total Deaths', 'Total Recovered']
    values = [total_cases, total_deaths, total_recovered]

    plt.bar(categories, values, color=['blue', 'red', 'green'])
    plt.xlabel('Categories')
    plt.ylabel('Counts')
    plt.title(f'COVID-19 Statistics for {country_name}')
    plt.show()

if __name__ == "__main__":
    country = input("Enter the name of the country to get COVID-19 statistics: ")
    get_covid_stats(country)

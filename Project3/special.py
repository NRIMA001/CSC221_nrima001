import csv
import matplotlib.pyplot as plt
import numpy as np

# Read the mortality-fecundity data from the CSV file
def read_mortality_fecundity_data(file_path):
    with open("mortality-fecundity.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        mortality_rates = []
        fecundity_rates = []
        for row in reader:
            mortality_rates.append(float(row[0]))
            fecundity_rates.append(float(row[1]))
    return mortality_rates, fecundity_rates

# Fit a model to the mortality-fecundity data
def fit_model(mortality_rates, fecundity_rates):
  # We can use a variety of models to fit the data. Here, we use a polynomial model.
  model = np.polyfit(mortality_rates, fecundity_rates, 2)
  return model

# Generate predictions using the fitted model
def generate_predictions(mortality_rates, model):
  predictions = []
  for mortality_rate in mortality_rates:
    prediction = np.polyval(model, mortality_rate)
    predictions.append(prediction)
  return predictions

# Plot the mortality-fecundity data and the model fit
def plot_mortality_fecundity_data(mortality_rates, fecundity_rates, model):
  predictions = generate_predictions(mortality_rates, model)

  fig, ax = plt.subplots()
  ax.scatter(mortality_rates, fecundity_rates, label="Data")
  ax.plot(mortality_rates, predictions, label="Model fit")

  ax.set_xlabel("Mortality rate")
  ax.set_ylabel("Fecundity rate")
  ax.legend()

  plt.show()

if __name__ == "__main__":
  # Read the mortality-fecundity data from the CSV file
  mortality_rates, fecundity_rates = read_mortality_fecundity_data("mortality_fecundity_data.csv")

  # Fit a model to the mortality-fecundity data
  model = fit_model(mortality_rates, fecundity_rates)

  # Generate predictions using the fitted model
  predictions = generate_predictions(mortality_rates, model)

  # Plot the mortality-fecundity data and the model fit
  plot_mortality_fecundity_data(mortality_rates, fecundity_rates, model)

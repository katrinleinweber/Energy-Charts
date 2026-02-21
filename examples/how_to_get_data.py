# -*- coding: utf-8 -*-
"""
This script demonstrates how to fetch installed power data from the
Energy Charts API and transform it into a structured pandas DataFrame.
"""

from energy_charts.api import EnergyChartsAPI
from energy_charts.enums import Countries
from energy_charts.parser import make_dataframe

if __name__ == "__main__":
    # Create an instance of the API accessor
    api = EnergyChartsAPI()

    # Fetch data from the API
    response = api.get_public_power(
        Countries.GERMANY,
        start="2024-01-01T00:00+01:00",
        end="2024-01-02T00:00+01:00",
        subtype=None,
    )

    # Convert the API response to a DataFrame
    df = make_dataframe(response)

    # Display the first few rows of the DataFrame
    print(df.head())

    # Save the DataFrame to a CSV file
    # df.to_csv("installed_power.csv", index=False)

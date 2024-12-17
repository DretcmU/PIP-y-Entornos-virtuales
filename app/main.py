import charts
import pandas as pd

def run():
  # #Código equivalente usando PANDAS
  # df(dataframe) 
  df = pd.read_csv("data.csv")  # Nos ahorramos el método creado read_csv.py
  df = df[df['Continent'] == 'South America']  
  # Equivalente a -> data = list(filter(lambda item : item['Continent'] == 'South America',data))
  countries = df['Country'].values
  # Equivalente a -> countries = list(map(lambda x: x['Country'], data))
  percentages = df['World Population Percentage'].values
  # Equivalente a -> percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

if __name__ == '__main__':
    run()
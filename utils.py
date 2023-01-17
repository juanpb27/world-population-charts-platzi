import re

def get_population(country_dict):
  keys = ['col', 'bol']
  values = [300, 400]
  
  return keys, values


def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  
  return result

def get_population_csv(data, country):
  country_dict = list(filter(lambda item : item['Country/Territory'] == country, data))[0]

  exp = re.compile('^[0-9]')
  population = {keys[:4] : int(values) for (keys, values) in country_dict.items() if exp.match(keys)}

  keys = population.keys()
  values = population.values()
  
  return keys, values

def get_percentages(data):
  percentages = {item['Country/Territory'] : float(item['World Population Percentage']) for item in data if float(item['World Population Percentage']) > 0}
  
  keys = percentages.keys()
  values = percentages.values()
  
  return keys, values
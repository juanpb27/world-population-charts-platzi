import utils
import read_csv
import charts

def run_country():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    keys, values = utils.get_population_csv(data, country)
    charts.generate_bar_chart(keys, values)

def run_world():
  data = read_csv.read_csv('./app/data.csv')
  keys, values = utils.get_percentages(data)
  charts.generate_pie_chart(keys, values)
  

if __name__ == '__main__':
  response = int(input('1-Country, 2-World: '))
  if(response == 1):
    run_country()
  else:
    run_world()
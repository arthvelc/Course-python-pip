import utils
import read_csv
import charts
import pandas

def run():


  '''data = read_csv.read_csv('/home/artur/python/course_python_pip/app/data.csv')
  #data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))

  '''
  df =pandas.read_csv('data.csv')
#solo si quiero filtrar datos en pandas :D
  df=df[df['Continent']=='North America']

  #Vamos a obtener los paises y porcentajes
  countries= df['Country'].values
  percentages= df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data=read_csv.read_csv('data.csv')
  country = input('Selecciona Pais: ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], values)


if __name__ == '__main__':
  run()
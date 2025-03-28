class Country:
    def __init__(self, name, area, population):
        self.name = name
        self.area = float(area)
        self.population = int(population)
    def __repr__(self):
        return f"{self.name} - Площа: {self.area} км2, Населення: {self.population}"

class PopulationData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.countries = self.read_population_data()

    def read_population_data(self):
        data = []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                country, area, population = line.strip().split(', ')
                data.append(Country(country, area, population))
        return data

def main():
    file_path = 'countriesAndPopulation.txt'
    population_data = PopulationData(file_path)
    population_data.print_sorted_data()
if __name__ == "__main__":
    main()

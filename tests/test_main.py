import pytest
from main import PopulationData, Country

@pytest.fixture(scope="module")
def population_data():
    file_content = "Ukraine, 603500, 41800000\nUSA, 9833517, 331000000\nCanada, 9984670, 38008005\n"
    file_path = 'test_countries_and_population.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(file_content)
    
    return PopulationData(file_path)

@pytest.mark.usefixtures("population_data")
class TestPopulationData:


    @pytest.mark.parametrize(
        "expected_order", 
        [
            ["USA", "Ukraine", "Canada"],
        ]
    )
    def test_sort_countries_by_population(self, population_data, expected_order):
        sorted_countries = population_data.sort_countries_by_population()
        sorted_country_names = [country.name for country in sorted_countries]
        assert sorted_country_names == expected_order

    def test_display_sorted_countries(self, population_data, capsys):
        population_data.display_sorted_countries()
        captured = capsys.readouterr()
        assert "Сортування за площею" in captured.out
        assert "Сортування за населенням" in captured.out
        assert "USA - Площа: 9833517.0 км2, Населення: 331000000" in captured.out
        assert "Canada - Площа: 9984670.0 км2, Населення: 38008005" in captured.out

    # Тест на правильне зчитування даних з файлу
    def test_read_population_data(self, population_data):
        countries = population_data.countries
        assert len(countries) == 3
        assert countries[0].name == "Ukraine"
        assert countries[1].name == "USA"
        assert countries[2].name == "Canada"
        assert countries[0].population == 41800000
        assert countries[1].population == 331000000
        
    def test_empty_file(self):
        empty_file_path = 'empty_countries.txt'
        with open(empty_file_path, 'w', encoding='utf-8') as file:
            file.write('')
        
        population_data_empty = PopulationData(empty_file_path)
        assert len(population_data_empty.countries) == 0 

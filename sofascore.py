# Source: https://github.com/Urbistondo/sofa-score-scraper/blob/master/player_scraper.py

import csv
import os

from selenium.webdriver.common.by import By
from selenium import webdriver


def get_players_average_ratings(write_file=True, file_name="sofascore_players_ratings"):
    if os.path.isfile('./' + file_name + '.csv'):
        return read_dict_from_csv("sofascore_players_ratings")

    chromepath = "selenium/webdriver/chrome/chromedriver.exe"
    driver = webdriver.Chrome(chromepath)

    team_links = {
        '1': ['Netherlands', 'https://www.sofascore.com/team/football/netherlands/4705'],
        '2': ['Ecuador',  'https://www.sofascore.com/team/football/ecuador/4757'],
        '3': ['Senegal',  'https://www.sofascore.com/team/football/senegal/4739'],
        '4': ['Qatar', 'https://www.sofascore.com/team/football/qatar/4792'],
        '5': ['England', 'https://www.sofascore.com/team/football/england/4713'],
        '6': ['Wales', 'https://www.sofascore.com/team/football/wales/4702'],
        '7': ['USA', 'https://www.sofascore.com/team/football/usa/4724'],
        '8': ['Iran', 'https://www.sofascore.com/team/football/iran/4766'],
        '9': ['Saudi Arabia', 'https://www.sofascore.com/team/football/saudi-arabia/4834'],
        '10': ['Poland', 'https://www.sofascore.com/team/football/poland/4703'],
        '11': ['Mexico', 'https://www.sofascore.com/team/football/mexico/4781'],
        '12': ['Argentina', 'https://www.sofascore.com/team/football/argentina/4819'],
        '13': ['France', 'https://www.sofascore.com/team/football/france/4481'],
        '14': ['Tunisia', 'https://www.sofascore.com/team/football/tunisia/4729'],
        '15': ['Denmark', 'https://www.sofascore.com/team/football/denmark/4476'],
        '16': ['Australia', 'https://www.sofascore.com/team/football/australia/4741'],
        '17': ['Spain', 'https://www.sofascore.com/team/football/spain/4698'],
        '18': ['Japan', 'https://www.sofascore.com/team/football/japan/4770'],
        '19': ['Germany', 'https://www.sofascore.com/team/football/germany/4711'],
        '20': ['Costa Rica', 'https://www.sofascore.com/team/football/costa-rica/4756'],
        '21': ['Belgium', 'https://www.sofascore.com/team/football/belgium/4717'],
        '22': ['Croatia', 'https://www.sofascore.com/team/football/croatia/4715'],
        '23': ['Morocco', 'https://www.sofascore.com/team/football/morocco/4778'],
        '24': ['Canada', 'https://www.sofascore.com/team/football/canada/4752'],
        '25': ['Brazil', 'https://www.sofascore.com/team/football/brazil/4748'],
        '26': ['Switzerland', 'https://www.sofascore.com/team/football/switzerland/4699'],
        '27': ['Cameroon', 'https://www.sofascore.com/team/football/cameroon/4751'],
        '28': ['Serbia', 'https://www.sofascore.com/team/football/serbia/6355'],
        '29': ['Portugal', 'https://www.sofascore.com/team/football/portugal/4704'],
        '30': ['South Korea', 'https://www.sofascore.com/team/football/south-korea/4735'],
        '31': ['Uruguay', 'https://www.sofascore.com/team/football/uruguay/4725'],
        '32': ['Ghana', 'https://www.sofascore.com/team/football/ghana/4764'],
    }
    player_paths = []
    for key, value in team_links.items():
        print('Extracting %s player links...' % value[0])
        driver.get(value[1])
        players = driver.find_elements(By.XPATH, "//*[contains(@class, 'sc-hLBbgP kIfRA')]/a")
        for p in players:
            player_paths.append(p.get_attribute('href'))

    players_with_ratings = dict()
    for p in player_paths:
        driver.get(p)
        player_name = driver.find_element(By.XPATH, "//h2[@class='sc-eDWCr elTPvO']").text
        average_rating = float(driver.find_element(By.XPATH, "//span[@class='sc-eDWCr jDQYpw']").text)
        players_with_ratings[player_name] = average_rating

    driver.quit()

    if write_file:
        write_dict_to_csv(players_with_ratings, file_name)

    return players_with_ratings


def write_dict_to_csv(dict_data, file_name):
    with open(file_name + ".csv", 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dict_data.items():
            writer.writerow([key, value])


def read_dict_from_csv(file_name):
    with open(file_name + ".csv") as csv_file:
        reader = csv.reader(csv_file)
        mydict = dict(reader)
        return mydict


# get_players_average_ratings()

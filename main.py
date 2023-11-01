import pandas as pd
import os
import json
import ast 
import math
from tkinter import *
from PIL import Image, ImageTk

def run():
	pass

def update_databases():
	database_file = open('./records/current_database.json', 'r')
	current_database = ast.literal_eval(json.load(database_file))
	database_file.close()

	current_files = scan_for_files()

	files_not_in_system = []
	new_files = [file for file in current_files if file not in current_database]
	new_files_dataframes = {file: pd.read_excel(file) for file in new_files}
	new_entries = format_new_entries(new_files_dataframes)
	return new_entries
	"""
	current_log = pd.read_excel('./records/current_log.xlsx')
	updated_log = current_log + new_entries
	pd.to_excel('./records/current_log.xlsx')

	updated_database = open('./records/current_database.json', 'w')
	json.dump(current_files, updated_database)
	updated_database.close()

	Monthly Inventory
	Product Breakdowns
	Dried Flower equivilancy
	Trimmed equivilancy
	"""


def most_recent_uploads():
	"""
	Returns a list of files, descending from the most recent upload.
	"""
	database_file = open('./records/current_database.json', 'r')
	current_database = ast.literal_eval(json.load(database_file))
	database_file.close()
	return current_database[::-1]


def scan_for_files():
	"""
	Returns a list of all of the .XLSX files from the inventory records.
	"""
	filepaths = []
	for files in os.walk('./records'):
		for file in files[2]:
			if file.startswith('~') == False and file.endswith('.xlsx'):
				filepaths.append(files[0] + '/' + file)
	return filepaths


def format_new_entries(dataframe_dict: dict) -> pd.DataFrame:
	"""
	get input from user into same format as the log
	"""
	for file in dataframe_dict:
		df = dataframe_dict[file]
		df.dropna(axis=0, how='all', inplace=True)
		df.dropna(axis=1, how='all', inplace=True)
		if len(df.columns == 6) and df.iloc[0,0] == 'Cannabis Form':
			pass
		else:
			raise ValueError(file + ' was not formatted properly.')
	return dfs


def app():
	root = Tk()
	root.title("QAQCC LIMS SYSTEM")

	icon_load = Image.open('./static/mini_logo.png')
	render = ImageTk.PhotoImage(icon_load)
	root.iconbitmap(False, render)
	return root
"""
---------NOTES---------
if cannabis is being imported
	apply_new batch code (Sarah needs to make new batch numbers, otherwise we can't identify)





"""



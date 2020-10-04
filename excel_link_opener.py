# excel_link_opener.py - Opens all links in a particular column in a chosen
# excel document.

import openpyxl
import webbrowser
import time
import os

folder_name = "Output"
msg = "Please run mangadex_sifter.py first and then this script."

def link_opener(file_path, col=3):
	"""Opens all links in the given column in an
	excel document."""	
	wb = openpyxl.load_workbook(file_path)
	ws = wb.active
	links = []
	for i in range(2, ws.max_row + 1):
		links.append(ws.cell(row=i, column=col).value)
		
	# Opening about 20 tabs at the same time will cause mangadex to soft ban 
	# your ip. Hence time.sleep is used to keep a gap between tabs.
	for i, link in enumerate(links):
		if i % 15 == 0 and i != 0:
			time.sleep(10)
		print("Opening", link)
		webbrowser.open(link)

	print("Task Complete.")

if __name__ == "__main__":	
	if os.path.exists(folder_name):
		res = []
		for filename in os.listdir(folder_name):
			if filename.endswith(".xlsx"):
				res.append(filename)
		if not res:
			print(msg)
		else:
			print("These files are available: \n")
			for filename in res:
				print(filename)			
				
			name = input("\nWhich one should be opened? ")
			file_path = os.path.join(folder_name, name)
			link_opener(file_path)
	else:
		print(msg)



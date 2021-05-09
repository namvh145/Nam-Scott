import gspread

gc = gspread.oauth()

sh = gc.open("Technology")

print(sh.sheet1.get('A1'))
import openpyxl

wb = openpyxl.load_workbook("files/new_wb.xlsx")

# ws = wb.active

ws = wb["Sheet"]
ws.title = "Sheet3"

wb.save("files/new_wb.xlsx")
print(ws)

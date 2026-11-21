import openpyxl
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # playwrightFW1
CONFIG_PATH = os.path.join(BASE_DIR, "testData", "userinfo.xlsx")


class ExcelUtility:

    def getRowCount(self,filename, sheetName):
        wb = openpyxl.load_workbook(filename)
        sheet = wb[sheetName]
        return sheet.max_row

    def getColumnCount(self,filename, sheetName):
        wb = openpyxl.load_workbook(filename)
        sheet = wb[sheetName]
        return sheet.max_column

    def getCellData(self,filename, sheetName, rowNumber, columnNumber):
        wb = openpyxl.load_workbook(filename)
        sheet = wb[sheetName]
        return sheet.cell(row=rowNumber, column=columnNumber).value

    def setCellData(self,filename, sheetName, rowNumber, columnNumber, inputData):
        wb = openpyxl.load_workbook(filename)
        sheet = wb[sheetName]
        sheet.cell(row=rowNumber, column=columnNumber).value = inputData


# print(getRowCount(CONFIG_PATH,"Sheet1"))
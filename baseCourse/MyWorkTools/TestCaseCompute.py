import xlwt
import xlrd
import os

def readAllExcel(fileArray):
    for file in fileArray:
        # print(file)
        workbook = xlrd.open_workbook(file)
        print(workbook.sheet_names())
        sheet1 = workbook.sheet_by_index(0)
        cols = sheet1.ncols
        print(cols)

def getAllExcelFile():
    excelArray = []
    for files in os.walk('.'):
        for file in files[2]:      #2代表array里面第三个元素，第一个元素是.，第二个元素是[]，第三个元素才是file的array
            filePart = os.path.splitext(file)
            if (filePart[1] == '.xlsx' or filePart[1] == '.xls' ):
                if('~' not in filePart[0]):    #去掉临时文件
                    excelArray.append(file)

    return excelArray


readAllExcel(getAllExcelFile())

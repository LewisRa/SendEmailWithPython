#Python and Excel using win32com - Hello World

#pip install pipwin

#win32com.client.Dispatch('Excel.Application') vs  win32.gencache.EnsureDispatch('Excel.Application')???

from win32com import client
excel = client.Dispatch('Excel.Application')
wb = excel.Workbooks.Add()
ws= wb.Worksheets.Add()
ws.Name = "My Worksheet"
ws.Range("A1:A1").Value= "Hello World"
excel.DisplayAlerts = False #Before saving the file set DisplayAlerts to False to suppress the warning dialog
wb.SaveAs(r"C:\Users\rache\Documents\GitHub\SendEmailWithPython\helloWorld_win32Excel\helloWorld.xlsx")
#Don't use XlSaveConflictResolution because it "Specifies the way conflicts are to be resolved whenever a shared workbook is updated 
#xlLocalSessionChanges = The local user's changes are always accepted.
excel.DisplayAlerts = True #After the file is saved it is usually a good idea to set DisplayAlerts back to True
excel.Application.Quit()
from typing import List
import googleheets 
import manoa
import telega
import pcp 

pcp_google_table = googleheets.PCP_GoogleTable()
manoa_db = manoa.DB()
#def get_worksheet(wrksht_id)->googleheets.gspread.Worksheet:
def get_worksheet(wrksht_id):   
    return pcp_google_table.get_wrksht(wrksht_id)
def get_manoa_cursor(sql_request):
    return manoa_db.get(sql_request)

#def get_last_order_from_manoa()->manoa.pyodbc.Cursor:
def get_last_order_from_manoa():
    
    cursor = manoa_db.get_last_order()
    for row in cursor:
        return row

def fill_wrksht_new_order():
    wrksht = get_worksheet(googleheets.PCP_GoogleTable().wsht_neworder_id)
    manoa_last_order = get_last_order_from_manoa()

    pcp.fill_wrksht_new_order(wrksht,manoa_last_order)
   
    
#def get_worksheets_list()->List:
def get_worksheets_list():
    return pcp_google_table.get_worksheets_list()

def get_listmodels_from_wrksht():
    return pcp_google_table.get_listmodels_from_wrksht()

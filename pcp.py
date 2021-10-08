import googleheets 
import manoa



def fill_wrksht_new_order(wrksht , last_order):    
    #for i  in range(3,11):
    #    wrksht.update_cell(i, 3, manoa_new_order_row[i-3])

    models = googleheets.PCP_GoogleTable().models

    wrksht.update_cell(3, 3, last_order[0]) # потому что можно
    wrksht.update_cell(4, 3, last_order.customerName)
    wrksht.update_cell(5, 3, last_order.cellPhone)
    wrksht.update_cell(10, 3, last_order.tlunotLakoah)
    tlunotLakoah_str = str(last_order.tlunotLakoah)
    tlunotLakoah_list = tlunotLakoah_str.split()
    
    for item in tlunotLakoah_list:
        
        if str(item).upper() in models:
            print(item)
            wrksht.update_cell(7, 3, item.upper())

    if tlunotLakoah_str.find('יש אישור'):
        wrksht.update_cell(13, 3, 'יש אישור')

        

def fill_wrksht_customers():
    ggl_tables = googleheets.PCP_GoogleTable()
    wrksht = ggl_tables.get_wrksht(ggl_tables.wsht_customers_id)

    #manoa_db = manoa.DB()
    sql = str('''
    select id ,
    contactPerson,
    name ,
    cellPhone,
    fax,
    email,   
    notes,
    messages
    from DBO.customers c 
    ''')
    manoa_dt = manoa.DB().get_as_dt(sql)
    
    
    ggl_tables.update_wrksht_as_dt(wrksht , manoa_dt)

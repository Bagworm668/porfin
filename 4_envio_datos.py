import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

def enviar_a_google_sheets(datos):
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)

    client = gspread.authorize(credentials)
    spreadsheet = client.open('pagina')
    worksheet = spreadsheet.get_worksheet(0)
    last_row = len(worksheet.col_values(1)) + 1
    worksheet.update('A{}'.format(last_row), [datos]) 
    worksheet1 = spreadsheet.get_worksheet(0)
    data = worksheet.get_all_values()
    df = pd.DataFrame(data)
    st.dataframe(df)


#def envair_a_streamlit(data):
 #   scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
#    credentials = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
#    client = gspread.authorize(credentials)
#    SPREADSHEET_ID = '11f25kN6FrVXbKmffX8vk2Q0Sly1fUN_PetQDcRZ0OK8'
#    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
   
#    data = sheet.get_all_records()
   # global comentarios
 #     comentarios = [data]    
    
    
    
def main():
    st.title('Enviar datos a Google Sheets')

        # Obtener los datos ingresados por el usuario
    datos = st.text_input('Ingrese los datos')
    lista =[datos]
    
    # Botón para enviar los datos a Google Sheets
    if st.button('Enviar'):
        enviar_a_google_sheets(lista)
        st.success('Datos enviados correctamente')
        
        

if __name__ == '__main__':
    main()      

#sheet = client.create('pagina')
#sheet.share("juancamiloxone@gmail.com", perm_type='user', role='writer')


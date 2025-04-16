def load_data():
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    from transform import transformed_list
    import pandas as pd
    import json
    
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",  
        "https://www.googleapis.com/auth/drive.file"
    ]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name("/home/mudassir/airflow/dags/assignment-451322-17937ded2009.json",scope)
    client = gspread.authorize(creds)

    
    spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1pomrAKQcqLLrrMjmh-eXFxuDZVBb6vdpCxA1PTc_F6w/edit?gid=0#gid=0")
    worksheet = spreadsheet.sheet1  

    with open('/home/mudassir/airflow/dags/Transformed_data.json','r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    data_list = df.values.tolist()
    worksheet.append_rows(data_list)

    print("Data added successfully!")

import json 
import requests,json
transformed_list = []
def transform_data():
    with open('/home/mudassir/airflow/dags/data.json','r') as f:
        get_data = json.load(f)
    print(get_data)
    for state in get_data:
        transformed_dict = {}
        batch = state.get('hits',{}).get('hits',{})
        for record in batch:
            source = record.get('_source')
            product = source.get('product')
            sub_product = source.get('sub_product')
            issue = source.get('issue')
            complaint_id = source.get('complaint_id')
            company_response = source.get('company_response')
            submitted_via = source.get('submitted_via')
            company = source.get('company')
            state_name = source.get('state')
            sub_issue = source.get('sub_issue')
            date_received = source.get('date_received')
            transformed_dict['product'] = product
            transformed_dict['company'] = company 
            transformed_dict['sub_product'] = sub_product 
            transformed_dict['issue'] = issue
            transformed_dict['complaint_id'] = complaint_id
            transformed_dict['company_response'] = company_response
            transformed_dict['submitted_via'] = submitted_via
            transformed_dict['state_name'] = state_name
            transformed_dict['sub_issue'] = sub_issue 
            transformed_dict['date_received'] = date_received
            
            transformed_list.append(transformed_dict)
            print(transformed_list)
    with open('/home/mudassir/airflow/dags/Transformed_data.json','w') as f:
        json.dump(transformed_list,fp=f,ensure_ascii=False,indent=4)
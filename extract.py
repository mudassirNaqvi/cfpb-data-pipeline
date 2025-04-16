
def extract_data():
    from datetime import date, datetime, timedelta
    import requests,json
    
    list_state = []
    i = 0
    list_of_states=list(requests.get("https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_hash.json").json().keys())
    for name in list_of_states:
        i += 1
        size=10
        time_delta=365
        max_date = (date.today()).strftime("%Y-%m-%d")
        min_date = (date.today() - timedelta(days=time_delta)).strftime("%Y-%m-%d")
        state=name
        url_of_data ='https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?field=complaint_what_happened&size={}&date_received_max={}&date_received_min={}&state={}'


        results=requests.get(url_of_data.format(size,max_date, min_date, state)).json()
        list_state.append(results)

    with open('/home/mudassir/airflow/dags/data.json','w') as f:
        json.dump(list_state,fp=f,ensure_ascii=False,indent=4)
        
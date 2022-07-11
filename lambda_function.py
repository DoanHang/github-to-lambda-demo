import pandas as pd
def lambda_handler(event, context):
    d= {'name' :['Gigi Hadid', 'Alice'], 'age': [30, 20]}
    df= pd.DataFrame(data=d)
    print(df)
    print('Done- Hang xinh!!!')
    
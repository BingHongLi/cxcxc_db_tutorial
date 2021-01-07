import boto3

client = boto3.client('dynamodb')

# 取得資料
response = client.get_item(
    TableName="cxcxc-saa-demo",
    Key={
        'Name': {'S': 'Acme Band'},
        'Age': {'N': '30'}
    }
)

# 打印結果
print(response.get('Item'))
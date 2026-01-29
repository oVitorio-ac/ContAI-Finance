import json
import boto3
import pandas as pd
from io import StringIO

def lambda_handler(event, context):
    """
    Lambda function to process CSV files in S3
    """
    s3_client = boto3.client('s3')
    
    try:
        # Extract information from S3 event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        # Download CSV file from S3
        response = s3_client.get_object(Bucket=bucket, Key=key)
        csv_content = response['Body'].read().decode('utf-8')
        
        # Process CSV with pandas
        df = pd.read_csv(StringIO(csv_content))
        
        # Basic analysis
        analysis = {
            'filename': key,
            'rows': len(df),
            'columns': len(df.columns),
            'column_names': list(df.columns),
            'data_types': df.dtypes.to_dict(),
            'missing_values': df.isnull().sum().to_dict(),
            'numeric_summary': {}
        }
        
        # Statistics for numeric columns
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            analysis['numeric_summary'] = df[numeric_cols].describe().to_dict()
        
        # Save analysis back to S3
        analysis_key = key.replace('.csv', '_analysis.json')
        s3_client.put_object(
            Bucket=bucket,
            Key=analysis_key,
            Body=json.dumps(analysis, indent=2, default=str),
            ContentType='application/json'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'CSV processed successfully',
                'analysis_file': analysis_key,
                'summary': {
                    'rows': analysis['rows'],
                    'columns': analysis['columns']
                }
            })
        }
        
    except Exception as e:
        print(f"Error processing CSV: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
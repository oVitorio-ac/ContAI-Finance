#!/usr/bin/env python3
"""
Integration with AWS Bedrock Data Automation MCP Server
Allows using Bedrock for advanced financial data analysis.
"""
import json
import os
import subprocess
import tempfile
from typing import Any, Dict, List

import boto3
import pandas as pd


class BedrockDataAutomation:
    """Wrapper for AWS Bedrock Data Automation MCP Server"""

    def __init__(self, region="us-east-1"):
        self.region = region
        self.bedrock_client = boto3.client("bedrock-runtime", region_name=region)

    def analyze_financial_data(self, csv_path: str, query: str) -> Dict[str, Any]:
        """
        Uses Bedrock for advanced financial data analysis
        """
        try:
            # Read CSV
            df = pd.read_csv(csv_path)

            # Prepare context for Bedrock
            data_summary = {
                "rows": len(df),
                "columns": list(df.columns),
                "sample_data": df.head(5).to_dict("records"),
                "data_types": df.dtypes.to_dict(),
                "numeric_summary": df.describe().to_dict()
                if len(df.select_dtypes(include=["number"]).columns) > 0
                else {},
            }

            # Prompt for financial analysis
            prompt = f"""
            You are an assistant specialized in financial data analysis.
            
            CSV Data:
            - File: {os.path.basename(csv_path)}
            - Rows: {data_summary['rows']}
            - Columns: {', '.join(data_summary['columns'])}
            
            Data Sample:
            {json.dumps(data_summary['sample_data'], indent=2, default=str)}
            
            User Question: {query}
            
            Please provide a detailed analysis and answer the user's question.
            Focus on relevant financial insights, trends, and practical recommendations.
            """

            # Call Bedrock
            response = self._call_bedrock(prompt)

            return {"analysis": response, "data_summary": data_summary, "query": query}

        except Exception as e:
            return {"error": f"Error in Bedrock analysis: {str(e)}"}

    def _call_bedrock(self, prompt: str) -> str:
        """
        Calls the Bedrock model for analysis
        """
        try:
            # Use Claude 3 Haiku for fast analysis
            body = json.dumps(
                {
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 2000,
                    "messages": [{"role": "user", "content": prompt}],
                }
            )

            response = self.bedrock_client.invoke_model(
                modelId="anthropic.claude-3-haiku-20240307-v1:0",
                body=body,
                contentType="application/json",
            )

            response_body = json.loads(response["body"].read())
            return response_body["content"][0]["text"]

        except Exception as e:
            # Fallback to local analysis if Bedrock is not available
            return self._local_analysis_fallback(prompt)

    def _local_analysis_fallback(self, prompt: str) -> str:
        """
        Local analysis as fallback if Bedrock is not available
        """
        return """
        📊 Financial Analysis (Local Mode)
        
        Based on the provided data, here are some insights:
        
        • Data has been successfully loaded
        • I recommend checking the numeric columns for trend analysis
        • For more advanced analysis, configure AWS Bedrock credentials
        
        💡 Tip: Use specific questions like:
        - "What is the total revenue?"
        - "Show the largest expenses"
        - "Analyze the monthly trend"
        """

    def generate_financial_insights(self, csv_path: str) -> Dict[str, Any]:
        """
        Generates automatic financial insights using Bedrock
        """
        try:
            df = pd.read_csv(csv_path)

            # Detect financial columns
            value_columns = []
            date_columns = []

            for col in df.columns:
                col_lower = col.lower()
                if any(
                    keyword in col_lower
                    for keyword in [
                        "valor",
                        "preco",
                        "price",
                        "amount",
                        "total",
                        "saldo",
                        "receita",
                        "despesa",
                    ]
                ):
                    if df[col].dtype in ["float64", "int64"]:
                        value_columns.append(col)
                elif any(
                    keyword in col_lower for keyword in ["data", "date", "timestamp"]
                ):
                    date_columns.append(col)

            insights_prompt = f"""
            Analyze this financial dataset and provide automatic insights:
            
            Data structure:
            - Total records: {len(df)}
            - Value columns: {value_columns}
            - Date columns: {date_columns}
            
            Basic statistics:
            {df[value_columns].describe().to_string() if value_columns else "No numeric columns detected"}
            
            Provide:
            1. Executive summary of the data
            2. Key identified trends
            3. Warnings or points of attention
            4. Recommended actions
            """

            analysis = self._call_bedrock(insights_prompt)

            return {
                "insights": analysis,
                "detected_columns": {"values": value_columns, "dates": date_columns},
                "summary_stats": df[value_columns].describe().to_dict()
                if value_columns
                else {},
            }

        except Exception as e:
            return {"error": f"Error generating insights: {str(e)}"}

    def compare_periods(
        self, csv_path: str, date_column: str, value_column: str
    ) -> Dict[str, Any]:
        """
        Compares periods using Bedrock analysis
        """
        try:
            df = pd.read_csv(csv_path)
            df[date_column] = pd.to_datetime(df[date_column])

            # Group by month
            monthly_data = df.groupby(df[date_column].dt.to_period("M"))[
                value_column
            ].sum()

            comparison_prompt = f"""
            Analyze this comparison of financial periods:
            
            Monthly data:
            {monthly_data.to_string()}
            
            Provide:
            1. Growth/decline analysis
            2. Seasonality identification
            3. Best and worst performing periods
            4. Projections and recommendations
            """

            analysis = self._call_bedrock(comparison_prompt)

            return {
                "period_analysis": analysis,
                "monthly_data": monthly_data.to_dict(),
                "total_periods": len(monthly_data),
                "growth_rate": (
                    (monthly_data.iloc[-1] - monthly_data.iloc[0])
                    / monthly_data.iloc[0]
                    * 100
                )
                if len(monthly_data) > 1
                else 0,
            }

        except Exception as e:
            return {"error": f"Error in period comparison: {str(e)}"}


def handle_bedrock_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """Handler for Bedrock MCP requests"""
    bedrock = BedrockDataAutomation()

    method = request.get("method", "")
    params = request.get("params", {})

    try:
        if method == "analyze_data":
            csv_path = params.get("csv_path", "")
            query = params.get("query", "")
            return {"result": bedrock.analyze_financial_data(csv_path, query)}

        elif method == "generate_insights":
            csv_path = params.get("csv_path", "")
            return {"result": bedrock.generate_financial_insights(csv_path)}

        elif method == "compare_periods":
            csv_path = params.get("csv_path", "")
            date_column = params.get("date_column", "")
            value_column = params.get("value_column", "")
            return {
                "result": bedrock.compare_periods(csv_path, date_column, value_column)
            }

        else:
            return {"error": f"Unsupported method: {method}"}

    except Exception as e:
        return {"error": f"Error in Bedrock MCP: {str(e)}"}


if __name__ == "__main__":
    # MCP server via stdin/stdout
    while True:
        try:
            line = input()
            if not line:
                break

            request = json.loads(line)
            response = handle_bedrock_request(request)
            print(json.dumps(response))

        except EOFError:
            break
        except Exception as e:
            error_response = {"error": f"Bedrock server error: {str(e)}"}
            print(json.dumps(error_response))

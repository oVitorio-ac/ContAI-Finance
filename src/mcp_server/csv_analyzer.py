#!/usr/bin/env python3
#!/usr/bin/env python3
"""
MCP Server for financial CSV file analysis.
Allows Amazon Q Developer to analyze financial data from uploaded CSVs.
"""
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import pandas as pd

# Add the project directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class CSVAnalyzer:
    """Analyzer for financial CSV files"""

    def __init__(self, media_path: str = "media/uploads"):
        self.media_path = Path(media_path)

    def list_csv_files(self) -> List[Dict[str, Any]]:
        """Lists all available CSV files"""
        csv_files = []
        if self.media_path.exists():
            for file_path in self.media_path.glob("*.csv"):
                try:
                    df = pd.read_csv(file_path)
                    csv_files.append(
                        {
                            "filename": file_path.name,
                            "path": str(file_path),
                            "rows": len(df),
                            "columns": list(df.columns),
                            "size_kb": round(file_path.stat().st_size / 1024, 2),
                        }
                    )
                except Exception as e:
                    csv_files.append(
                        {
                            "filename": file_path.name,
                            "path": str(file_path),
                            "error": str(e),
                        }
                    )
        return csv_files

    def analyze_csv(self, filename: str) -> Dict[str, Any]:
        """Analyzes a specific CSV file"""
        file_path = self.media_path / filename

        if not file_path.exists():
            return {"error": f"File {filename} not found"}

        try:
            df = pd.read_csv(file_path)

            # Basic analysis
            analysis = {
                "filename": filename,
                "shape": {"rows": len(df), "columns": len(df.columns)},
                "columns": list(df.columns),
                "data_types": df.dtypes.to_dict(),
                "missing_values": df.isnull().sum().to_dict(),
                "summary_stats": {},
            }

            # Statistics for numeric columns
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                analysis["summary_stats"] = df[numeric_cols].describe().to_dict()

            # Specific financial analysis
            financial_analysis = self._analyze_financial_data(df)
            analysis.update(financial_analysis)

            return analysis

        except Exception as e:
            return {"error": f"Error analyzing {filename}: {str(e)}"}

    def _analyze_financial_data(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Specific analysis for financial data"""
        financial_info = {}

        # Detect value/money columns
        value_columns = []
        for col in df.columns:
            if any(
                keyword in col.lower()
                for keyword in ["valor", "preco", "price", "amount", "total", "saldo"]
            ):
                if df[col].dtype in ["float64", "int64"]:
                    value_columns.append(col)

        if value_columns:
            financial_info["value_columns"] = value_columns

            for col in value_columns:
                financial_info[f"{col}_analysis"] = {
                    "total": float(df[col].sum()),
                    "average": float(df[col].mean()),
                    "min": float(df[col].min()),
                    "max": float(df[col].max()),
                    "positive_count": int((df[col] > 0).sum()),
                    "negative_count": int((df[col] < 0).sum()),
                    "zero_count": int((df[col] == 0).sum()),
                }

        # Detect date columns
        date_columns = []
        for col in df.columns:
            if any(keyword in col.lower() for keyword in ["data", "date", "timestamp"]):
                date_columns.append(col)

        if date_columns:
            financial_info["date_columns"] = date_columns

        return financial_info

    def query_data(self, filename: str, query: str) -> Dict[str, Any]:
        """Executes specific queries on the data"""
        file_path = self.media_path / filename

        if not file_path.exists():
            return {"error": f"File {filename} not found"}

        try:
            df = pd.read_csv(file_path)

            # Pre-defined queries
            query_lower = query.lower()

            if "total" in query_lower or "soma" in query_lower:
                return self._calculate_totals(df)
            elif "média" in query_lower or "average" in query_lower:
                return self._calculate_averages(df)
            elif "maior" in query_lower or "max" in query_lower:
                return self._find_maximum_values(df)
            elif "menor" in query_lower or "min" in query_lower:
                return self._find_minimum_values(df)
            elif "positivo" in query_lower or "receita" in query_lower:
                return self._filter_positive_values(df)
            elif "negativo" in query_lower or "despesa" in query_lower:
                return self._filter_negative_values(df)
            else:
                return {
                    "message": "Query not recognized. Try: total, average, max, min, positive, negative"
                }

        except Exception as e:
            return {"error": f"Query error: {str(e)}"}

    def _calculate_totals(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Calculates totals for numeric columns"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        totals = {}
        for col in numeric_cols:
            totals[col] = float(df[col].sum())
        return {"totals": totals}

    def _calculate_averages(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Calculates averages for numeric columns"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        averages = {}
        for col in numeric_cols:
            averages[col] = float(df[col].mean())
        return {"averages": averages}

    def _find_maximum_values(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Finds maximum values"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        maximums = {}
        for col in numeric_cols:
            max_idx = df[col].idxmax()
            maximums[col] = {
                "value": float(df[col].max()),
                "row": int(max_idx),
                "row_data": df.iloc[max_idx].to_dict(),
            }
        return {"maximums": maximums}

    def _find_minimum_values(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Finds minimum values"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        minimums = {}
        for col in numeric_cols:
            min_idx = df[col].idxmin()
            minimums[col] = {
                "value": float(df[col].min()),
                "row": int(min_idx),
                "row_data": df.iloc[min_idx].to_dict(),
            }
        return {"minimums": minimums}

    def _filter_positive_values(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Filters positive values"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        positive_data = {}
        for col in numeric_cols:
            positive_df = df[df[col] > 0]
            positive_data[col] = {
                "count": len(positive_df),
                "total": float(positive_df[col].sum()),
                "average": float(positive_df[col].mean())
                if len(positive_df) > 0
                else 0,
            }
        return {"positive_values": positive_data}

    def _filter_negative_values(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Filters negative values"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        negative_data = {}
        for col in numeric_cols:
            negative_df = df[df[col] < 0]
            negative_data[col] = {
                "count": len(negative_df),
                "total": float(negative_df[col].sum()),
                "average": float(negative_df[col].mean())
                if len(negative_df) > 0
                else 0,
            }
        return {"negative_values": negative_data}


def handle_mcp_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """Main handler for MCP requests"""
    analyzer = CSVAnalyzer()

    method = request.get("method", "")
    params = request.get("params", {})

    try:
        if method == "list_files":
            return {"result": analyzer.list_csv_files()}

        elif method == "analyze_file":
            filename = params.get("filename", "")
            return {"result": analyzer.analyze_csv(filename)}

        elif method == "query_data":
            filename = params.get("filename", "")
            query = params.get("query", "")
            return {"result": analyzer.query_data(filename, query)}

        else:
            return {"error": f"Unsupported method: {method}"}

    except Exception as e:
        return {"error": f"MCP server error: {str(e)}"}


if __name__ == "__main__":
    # Simple MCP server via stdin/stdout
    while True:
        try:
            line = input()
            if not line:
                break

            request = json.loads(line)
            response = handle_mcp_request(request)
            print(json.dumps(response))

        except EOFError:
            break
        except Exception as e:
            error_response = {"error": f"Server error: {str(e)}"}
            print(json.dumps(error_response))

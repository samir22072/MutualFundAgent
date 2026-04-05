import json
from crewai.tools import tool
from data.data_access import search_mutual_funds_db

@tool("search_mutual_funds")
def search_mutual_funds(criteria_json_str: str) -> str:
    """
    Highly flexible tool to search, filter, and sort mutual funds.
    You must pass a valid JSON string map.
    Possible keys (all optional):
    - 'risk_profile': 'low', 'medium', or 'high'
    - 'min_cagr_1_year': float (e.g. 10.5)
    - 'min_cagr_3_year': float
    - 'min_cagr_5_year': float
    - 'sort_by': '1Y', '3Y', or '5Y' (default is '3Y')
    - 'limit': int (how many funds to return, default is 5)

    Example argument: '{"risk_profile": "high", "sort_by": "3Y", "limit": 3}'
    Returns a JSON string of the returned mutual funds.
    """
    try:
        criteria = json.loads(criteria_json_str)
        funds = search_mutual_funds_db(criteria)
        return json.dumps(funds)
    except Exception as e:
        return json.dumps({"error": f"Invalid JSON criteria or fetching error: {str(e)}"})

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'mutual_funds.db')

# Create a single global connection
global_conn = sqlite3.connect(DB_PATH, check_same_thread=False)
global_conn.row_factory = sqlite3.Row

def search_mutual_funds_db(criteria: dict) -> list[dict]:
    """
    Flexible search function replacing get_funds_by_risk_profile_db, get_top_funds_by_cagr_db, and filter_funds_db.
    criteria: map containing optional filters:
    - risk_profile: str (e.g., 'low')
    - min_cagr_1_year: float
    - min_cagr_3_year: float
    - min_cagr_5_year: float
    - sort_by: str ('1Y', '3Y', '5Y') - defaults to '3Y'
    - limit: int - defaults to 5
    """
    try:
        cursor = global_conn.cursor()
        
        query = "SELECT fund_name, fund_risk_profile, cagr_1_year, cagr_3_year, cagr_5_year FROM mutual_funds WHERE is_deleted = 0"
        params = []
        
        if "risk_profile" in criteria and criteria["risk_profile"] and criteria["risk_profile"].lower() != "unknown":
            query += " AND fund_risk_profile = ?"
            params.append(criteria["risk_profile"].lower())
            
        if "min_cagr_1_year" in criteria and criteria["min_cagr_1_year"] is not None:
            query += " AND cagr_1_year >= ?"
            params.append(criteria["min_cagr_1_year"])
            
        if "min_cagr_3_year" in criteria and criteria["min_cagr_3_year"] is not None:
            query += " AND cagr_3_year >= ?"
            params.append(criteria["min_cagr_3_year"])
            
        if "min_cagr_5_year" in criteria and criteria["min_cagr_5_year"] is not None:
            query += " AND cagr_5_year >= ?"
            params.append(criteria["min_cagr_5_year"])
            
        sort_by = criteria.get("sort_by", "3Y")
        if sort_by == "1Y":
            query += " ORDER BY cagr_1_year DESC"
        elif sort_by == "5Y":
            query += " ORDER BY cagr_5_year DESC"
        else:
            query += " ORDER BY cagr_3_year DESC"
            
        limit = criteria.get("limit", 5)
        query += " LIMIT ?"
        params.append(limit)
            
        cursor.execute(query, params)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except Exception as e:
        print(f"Error fetching search_mutual_funds_db: {e}")
        return []

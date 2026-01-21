"""
Abraham Accords Literacy Initiative - Interactive Dashboard
Author: Vanessa Ngeno
Project: Mapping Literacy for Humanity
Deploy to: Hugging Face Spaces
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Import pages module
from pages_content import render_page

# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(
    page_title="Abraham Accords Literacy Initiative",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS
# ============================================================================
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8fafc;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
    }
    .insight-box {
        background-color: #fef3c7;
        border-left: 4px solid #f59e0b;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fee2e2;
        border-left: 4px solid #ef4444;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d1fae5;
        border-left: 4px solid #10b981;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA PREPARATION
# ============================================================================

@st.cache_data
def load_data():
    """Load and prepare all datasets with updated calculations"""
    
    # AALNI Rankings Data (Updated)
    aalni_data = pd.DataFrame({
        'Country': ['Sudan', 'Morocco', 'Israel', 'UAE', 'Bahrain'],
        'AALNI_Score': [115.7, 24.5, 2.0, 1.8, 1.5],
        'Adult_Literacy_Rate': [57.0, 72.1, 97.8, 96.3, 97.5],
        'Gender_Parity_Index': [0.69, 0.81, 0.99, 0.99, 0.99],
        'Rural_Urban_Gap': [30.0, 25.8, 2.5, 3.0, 2.0],
        'Conflict_Status': ['Severe_Conflict', 'Stable', 'Stable', 'Stable', 'Stable'],
        'Phase_1_Allocation_M': [700.0, 135.3, 15.0, 12.0, 8.0],
        'Phase_2_Allocation_M': [266.6, 0.0, 0.0, 0.0, 0.0],
        'Total_Need_M': [966.6, 135.3, 15.0, 12.0, 8.0],
        'Phase_1_Percent': [72.4, 100.0, 100.0, 100.0, 100.0]
    })
    
    # Morocco Timeline Data (Updated with Phase 1 projection)
    morocco_timeline = pd.DataFrame({
        'Year': [2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2026, 2028, 2030],
        'Literacy_Rate': [39.6, 43.2, 45.9, 47.7, 57.7, 63.1, 67.8, 69.4, 72.1, 78.5, 85.0, 95.0],
        'Type': ['Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 
                'Actual', 'Actual', 'Projected', 'Projected', 'Projected'],
        'Phase': ['Pre-intervention', 'Pre-intervention', 'Pre-intervention', 'Intervention Start',
                 'Phase 1', 'Phase 1', 'Phase 1', 'Phase 1', 'Phase 1', 
                 'Phase 1', 'Phase 1 Complete', 'SDG Achieved']
    })
    
    # Cost-Effectiveness Data (Updated with $1.86 efficiency)
    cost_effectiveness = pd.DataFrame({
        'Program': ['UAE Compulsory\nEducation', 'Morocco National\nProgram', 
                   'Bahrain Workplace\nMandate', 'Israel Ulpan\nMethod', 
                   'UAE National\nStrategy'],
        'Country': ['UAE', 'Morocco', 'Bahrain', 'Israel', 'UAE'],
        'Cost_Per_Point': [0.53, 1.86, 3.37, 28.31, 150.0],
        'Literacy_Improvement': [42.0, 19.8, 12.5, 12.8, 0.5],
        'Duration_Years': [49, 10, 34, 75, 8],
        'Cost_Per_Person': [22.4, 36.74, 42.15, 362.33, 75.0],
        'Beneficiaries_M': [8.2, 8.46, 0.85, 0.12, 0.05]
    })
    
    # Feature Importance Data (88.9% Rule)
    feature_importance = pd.DataFrame({
        'Feature': ['Secondary\nEnrollment', 'Gender\nParity', 'Learning\nQuality', 
                   'Rural-Urban\nGap', 'Out-of-School\nChildren', 'Primary\nEnrollment',
                   'Year', 'Conflict\nSeverity', 'Investment\nAmount'],
        'Importance': [26.3, 18.5, 16.7, 14.7, 12.8, 2.6, 2.6, 2.2, 1.6],
        'Category': ['Systemic', 'Systemic', 'Systemic', 'Systemic', 'Systemic',
                    'Infrastructure', 'Temporal', 'Context', 'Financial']
    })
    
    # 2030 Projections Data (Updated with scenario-based outcomes)
    projections_2030 = pd.DataFrame({
        'Country': ['Sudan', 'Sudan', 'Morocco', 'Israel', 'UAE', 'Bahrain'],
        'Scenario': ['Phase 1 Only', 'Phase 1 + Phase 2', 'Phase 1', 'Baseline', 'Baseline', 'Baseline'],
        'Current_2024': [57.0, 57.0, 72.1, 97.8, 96.3, 97.5],
        'Projected_2030': [57.0, 87.5, 95.0, 98.0, 98.9, 97.4],
        'Gap_to_SDG': [38.0, 7.5, 0.0, 0.0, 0.0, 0.0],
        'Status': ['Stabilized', 'Substantial Progress', 'SDG Achieved', 'Maintained', 'Maintained', 'Maintained'],
        'Investment_M': [700.0, 966.6, 135.3, 15.0, 12.0, 8.0]
    })
    
    # Sudan Conflict Impact Data
    sudan_conflict = pd.DataFrame({
        'Year': [2014, 2016, 2018, 2019, 2020, 2022, 2024, 2026, 2028, 2030],
        'Literacy_Rate': [60.7, 60.5, 60.7, 60.0, 59.0, 59.0, 57.0, 57.0, 57.0, 57.0],
        'Conflict_Intensity': [0, 0, 1, 2, 3, 5, 8, 6, 4, 2],
        'Type': ['Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 
                'Actual', 'Phase 1 Proj.', 'Phase 1 Proj.', 'Phase 2 Proj.']
    })
    
    return aalni_data, morocco_timeline, cost_effectiveness, feature_importance, projections_2030, sudan_conflict

# Load data
aalni_data, morocco_timeline, cost_effectiveness, feature_importance, projections_2030, sudan_conflict = load_data()

# ============================================================================
# HEADER
# ============================================================================
st.markdown("""
<div class="main-header">
    <h1>Abraham Accords Literacy Initiative</h1>
    <h3>Evidence-Based Investment Strategy for 27.1 Million Lives</h3>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR
# ============================================================================
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select View:",
    ["Executive Summary", "AALNI Rankings", "Morocco Case Study", 
     "Sudan Conflict Analysis", "Cost-Effectiveness", "Feature Importance (88.9% Rule)", 
     "2030 Projections", "Policy Recommendations"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Key Metrics")
st.sidebar.metric("Phase 1 Investment", "$950M", "73% of need")
st.sidebar.metric("Total Evidence-Based Need", "$1.3B", "3-6 years")
st.sidebar.metric("Expected ROI", "$9.1-13.0B", "700-1000%")
st.sidebar.metric("Lives Impacted", "27.1M", "54% women/girls")
st.sidebar.metric("Phase 1 Beneficiaries", "8.7M", "73% of target")

st.sidebar.markdown("---")
st.sidebar.markdown("### Phased Strategy")
st.sidebar.info("""
**Phase 1 (Years 1-3): $950M**
- Morocco: SDG 4 by 2028
- Sudan: 5.1M in accessible areas
- High performers: Maintained

**Phase 2 (Years 4-6): $357.5M**
- Contingent on Sudan stability
- Systemic transformation
- Final 3.2M beneficiaries
""")

st.sidebar.markdown("---")
st.sidebar.markdown("""
### Partners
- Peblink
- World Literacy Foundation
- World Literacy Research Center
- Abraham Accords Educational Alliance
""")

# ============================================================================
# RENDER SELECTED PAGE
# ============================================================================
render_page(page, aalni_data, morocco_timeline, cost_effectiveness, 
           feature_importance, projections_2030, sudan_conflict)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6b7280; padding: 2rem;">
    <p><strong>Data Sources:</strong> UNESCO Institute for Statistics, World Bank EdStats, UNICEF</p>
    <p><strong>Analysis:</strong> Vanessa Ngeno | Master's in Data Analytics & Visualization | Yeshiva University</p>
    <p><strong>Partners:</strong> Peblink, World Literacy Foundation, World Literacy Research Center, Abraham Accords Educational Alliance</p>
    <p style="font-size: 0.85em; margin-top: 1rem;">
        <strong>Literacy Definition:</strong> UNESCO standard - ability to read and write a short, simple statement about everyday life (15+ years adult literacy)
    </p>
    <p style="font-size: 0.85em;">
        <strong>Morocco Efficiency:</strong> $1.86 per person per point (validated p<0.0001, R²=0.846) from $310.9M investment reaching 8.46M beneficiaries with 19.8-point improvement.
    </p>
    <p style="font-size: 0.85em;">
        <strong>Sudan Context:</strong> Literacy declined 3.7 percentage points during 2014-2024 conflict period. External reports (UNICEF, UNESCO, World Bank) validate dataset trends. 
        Phase 1 focuses on accessible populations; Phase 2 contingent on stability.
    </p>
    <p style="font-size: 0.85em; margin-top: 0.5rem;">
        For questions or detailed technical appendices, please contact the project team.
    </p>
</div>
""", unsafe_allow_html=True)

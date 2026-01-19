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
    page_icon="📚",
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
    """Load and prepare all datasets"""
    
    # AALNI Rankings Data
    aalni_data = pd.DataFrame({
        'Country': ['Sudan', 'Morocco', 'Israel', 'UAE', 'Bahrain'],
        'AALNI_Score': [115.7, 24.5, 2.0, 1.8, 1.5],
        'Adult_Literacy_Rate': [57.0, 72.1, 97.8, 96.3, 97.5],
        'Gender_Parity_Index': [0.69, 0.81, 0.99, 0.99, 0.99],
        'Rural_Urban_Gap': [30.0, 25.8, 2.5, 3.0, 2.0],
        'Conflict_Status': ['Severe_Conflict', 'Stable', 'Stable', 'Stable', 'Stable'],
        'Investment_Allocation_M': [755.4, 160.1, 13.0, 11.8, 9.7],
        'Allocation_Percent': [79.5, 16.8, 1.4, 1.2, 1.0]
    })
    
    # Morocco Timeline Data
    morocco_timeline = pd.DataFrame({
        'Year': [2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2026, 2028, 2030],
        'Literacy_Rate': [39.6, 43.2, 45.9, 47.7, 57.7, 63.1, 67.8, 69.4, 72.1, 76.7, 81.0, 85.4],
        'Type': ['Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Actual', 'Projected', 'Projected', 'Projected'],
        'Intervention': [False, False, False, True, False, False, False, False, False, False, False, False]
    })
    
    # Cost-Effectiveness Data
    cost_effectiveness = pd.DataFrame({
        'Program': ['UAE Compulsory\nEducation', 'Morocco National\nProgram', 
                   'Bahrain Workplace\nMandate', 'Israel Ulpan\nMethod', 
                   'UAE National\nStrategy'],
        'Country': ['UAE', 'Morocco', 'Bahrain', 'Israel', 'UAE'],
        'Cost_Per_Point': [0.53, 1.62, 3.37, 28.31, 150.0],
        'Literacy_Improvement': [42.0, 19.8, 12.5, 12.8, 0.5],
        'Duration_Years': [49, 10, 34, 75, 8],
        'Cost_Per_Person': [22.4, 32.09, 42.15, 362.33, 75.0]
    })
    
    # Feature Importance Data
    feature_importance = pd.DataFrame({
        'Feature': ['Secondary\nEnrollment', 'Gender\nParity', 'Learning\nQuality', 
                   'Rural-Urban\nGap', 'Out-of-School\nChildren', 'Primary\nEnrollment',
                   'Year', 'Investment'],
        'Importance': [26.3, 18.5, 16.7, 14.7, 12.8, 2.6, 2.6, 1.6]
    })
    
    # 2030 Projections Data
    projections_2030 = pd.DataFrame({
        'Country': ['Sudan', 'Morocco', 'Israel', 'UAE', 'Bahrain'],
        'Current_2024': [57.0, 72.1, 97.8, 96.3, 97.5],
        'Projected_2030': [54.1, 85.4, 98.0, 98.9, 97.4],
        'Gap_to_SDG': [40.9, 9.6, 0.0, 0.0, 0.0],
        'Status': ['Critical', 'Needs Support', 'On Track', 'On Track', 'On Track']
    })
    
    return aalni_data, morocco_timeline, cost_effectiveness, feature_importance, projections_2030

# Load data
aalni_data, morocco_timeline, cost_effectiveness, feature_importance, projections_2030 = load_data()

# ============================================================================
# HEADER
# ============================================================================
st.markdown("""
<div class="main-header">
    <h1>Abraham Accords Literacy Initiative</h1>
    <h3>Mapping Literacy Needs Across 27.1 Million Lives</h3>
    <p>Evidence-Based Investment Strategy | $950M Three-Year Plan</p>
    <p style="font-size: 0.9em; opacity: 0.9;">Vanessa Ngeno | Yeshiva University</p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR
# ============================================================================
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select View:",
    ["Executive Summary", "AALNI Rankings", "Morocco Case Study", 
     "Cost-Effectiveness", "Feature Importance", "2030 Projections", 
     "Policy Recommendations"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Key Metrics")
st.sidebar.metric("Total Investment", "$950M", "3-year plan")
st.sidebar.metric("Expected ROI", "$6.65-9.5B", "700-1000%")
st.sidebar.metric("Lives Impacted", "27.1M", "54% women/girls")
st.sidebar.metric("Countries Analyzed", "5", "Abraham Accords")

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
           feature_importance, projections_2030)

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
        <strong>Note:</strong> Morocco program baseline (52.3%) differs from national average (47.7%) due to participant selection. 
        Sudan data (2020-2022) partially interpolated due to conflict-related measurement gaps.
    </p>
    <p style="font-size: 0.85em; margin-top: 0.5rem;">
        For questions or detailed technical appendices, please contact the project team.
    </p>
</div>
""", unsafe_allow_html=True)

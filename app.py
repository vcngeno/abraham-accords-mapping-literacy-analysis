
import gradio as gr
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
try:
    df_forecast = pd.read_csv('data/2030_forecast_results.csv')
    df_aalni = pd.read_csv('data/aalni_scores_2024.csv')
    df_cost = pd.read_csv('data/cost_effectiveness_ranking.csv')
except:
    # Fallback data if files not found
    df_forecast = pd.DataFrame({
        'Country': ['Israel', 'Bahrain', 'UAE', 'Morocco', 'Sudan'],
        'Current_2024': [97.8, 97.5, 96.3, 72.1, 57.0],
        'Projected_2030': [98.1, 98.5, 100.0, 85.4, 54.1],
        'Gap_to_SDG': [-3.1, -3.5, -5.0, 9.6, 40.9],
        'Will_Achieve_SDG': ['Yes', 'Yes', 'Yes', 'No', 'No']
    })
    
    df_aalni = pd.DataFrame({
        'Country': ['Sudan', 'Morocco', 'Israel', 'UAE', 'Bahrain'],
        'AALNI_Score': [115.7, 24.5, 2.0, 1.8, 1.5],
        'Budget_Allocation_M': [755.2, 159.9, 13.0, 11.8, 9.7]
    })

# Title and description
title = "Abraham Accords Literacy Analysis Dashboard"
description = """
**Mapping Literacy for Humanity: Data-Driven Insights for UN SDG 4**

Explore comprehensive analysis of literacy rates across Abraham Accords nations (Israel, UAE, Bahrain, Morocco, Sudan) 
with 2030 projections, investment optimization, and policy recommendations.

*Master's Capstone Project | Vanessa Ngeno | Yeshiva University*
"""

# Tab 1: 2030 Projections
def create_projection_chart():
    fig = go.Figure()
    
    countries = df_forecast['Country'].tolist()
    current = df_forecast['Current_2024'].tolist()
    projected = df_forecast['Projected_2030'].tolist()
    
    x = list(range(len(countries)))
    
    fig.add_trace(go.Bar(
        x=x,
        y=current,
        name='Current (2024)',
        marker_color='#64b5f6',
        text=[f"{v:.1f}%" for v in current],
        textposition='outside'
    ))
    
    fig.add_trace(go.Bar(
        x=x,
        y=projected,
        name='Projected (2030)',
        marker_color='#81c784',
        text=[f"{v:.1f}%" for v in projected],
        textposition='outside'
    ))
    
    fig.add_hline(y=95, line_dash="dash", line_color="gold", 
                  annotation_text="SDG Target (95%)")
    
    fig.update_layout(
        title="2030 SDG Literacy Projections",
        xaxis=dict(tickvals=x, ticktext=countries),
        yaxis_title="Adult Literacy Rate (%)",
        barmode='group',
        height=500,
        showlegend=True
    )
    
    return fig

def create_gap_chart():
    fig = go.Figure()
    
    countries = df_forecast['Country'].tolist()
    gaps = df_forecast['Gap_to_SDG'].tolist()
    colors = ['green' if g <= 0 else 'red' for g in gaps]
    
    fig.add_trace(go.Bar(
        y=countries,
        x=gaps,
        orientation='h',
        marker_color=colors,
        text=[f"{v:.1f}" for v in gaps],
        textposition='outside'
    ))
    
    fig.add_vline(x=0, line_color="black")
    
    fig.update_layout(
        title="Gap to SDG Target (95%)",
        xaxis_title="Percentage Points Gap",
        yaxis_title="Country",
        height=400
    )
    
    return fig

# Tab 2: AALNI Scores
def create_aalni_chart():
    fig = px.bar(
        df_aalni,
        x='Country',
        y='AALNI_Score',
        title='Abraham Accords Literacy Need Index (AALNI)',
        color='AALNI_Score',
        color_continuous_scale='Reds',
        text='AALNI_Score',
        labels={'AALNI_Score': 'AALNI Score (Higher = Greater Need)'}
    )
    
    fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
    fig.update_layout(height=500, showlegend=False)
    
    return fig

def create_budget_chart():
    fig = px.pie(
        df_aalni,
        values='Budget_Allocation_M',
        names='Country',
        title='$950M Budget Allocation by Country',
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=500)
    
    return fig

# Tab 3: Key Findings
def get_key_findings():
    findings = """
## Key Findings

### Countries on Track (3/5)
- **Israel**: 97.8% to 98.1% (maintaining excellence)
- **Bahrain**: 97.5% to 98.5% (steady progress)
- **UAE**: 96.3% to 100% (will achieve universal literacy)

### Countries Requiring Intervention (2/5)

**Morocco**: 72.1% to 85.4%
- Gap: 9.6 percentage points
- Investment needed: $15.5M
- Probability of success: HIGH (proven track record)

**Sudan**: 57.0% to 54.1% (DECLINING)
- Gap: 40.9 percentage points
- Status: CRITICAL - literacy projected to decline due to conflict
- Probability of success: ZERO without ceasefire

### Budget Optimization
- **Total Budget**: $950M
- **Actual Need**: $214.4M
- **Surplus Identified**: $735.6M

### Investment Efficiency
- Morocco's program: $1.62 per percentage point (2nd most efficient globally)
- HOW you invest matters 50x more than HOW MUCH
- Investment amount ranked only #10 in importance (1.6%)

### Policy Recommendations
1. **Morocco**: Allocate $15.5M strategically to close gap
2. **Sudan**: Conflict resolution is prerequisite for any progress
3. **Regional Scale-Up**: Use $300M surplus to replicate Morocco's model across North Africa
4. **Quality Focus**: Invest $150M in teacher training and curriculum (top predictors)
5. **Emergency Reserve**: Maintain $85.6M for unforeseen challenges
"""
    return findings

# Tab 4: Methodology
def get_methodology():
    method = """
## Methodology

### Data Sources
- **UNESCO Institute for Statistics** (2000-2024)
- **World Bank Education Statistics**
- Government literacy reports and audits
- Morocco Court of Accounts
- Sudan Education Ministry

### Statistical Techniques

**1. Difference-in-Differences Analysis**
- Causal inference for Morocco's national campaign
- R-squared: 0.846, p < 0.0001
- Treatment effect: +24.4 percentage points

**2. Prophet Time-Series Forecasting**
- 2030 projections with confidence intervals
- Logistic growth for high-performers (caps at 100%)
- Accounts for trend changes and seasonality

**3. Random Forest Feature Importance**
- Identified top predictors of literacy improvement
- 500 trees, max depth 10, 80/20 train-test split
- Key finding: Quality factors dominate (88.9% combined importance)

**4. AALNI Composite Scoring**
Novel index combining:
- Rural-urban literacy gap (25% weight)
- Gender parity gap (25% weight)
- Out-of-school children (20% weight)
- Conflict impact (15% weight)
- Investment efficiency (15% weight)

### Tools and Technologies
- Python 3.11
- Pandas, NumPy (data processing)
- Prophet (forecasting)
- Scikit-learn (machine learning)
- Plotly (interactive visualization)
- Jupyter Notebook (analysis environment)
"""
    return method

# Create Gradio Interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(f"# {title}")
    gr.Markdown(description)
    
    with gr.Tabs():
        # Tab 1: Projections
        with gr.Tab("2030 Projections"):
            gr.Markdown("## Prophet Time-Series Forecasting Results")
            
            with gr.Row():
                projection_plot = gr.Plot(value=create_projection_chart())
            
            with gr.Row():
                gap_plot = gr.Plot(value=create_gap_chart())
            
            gr.Markdown("""
            ### Interpretation
            - **Green bars**: Countries that will achieve or exceed SDG 4 target (95%)
            - **Red bars**: Countries falling short of target
            - **Gold line**: UN SDG 4 target threshold
            """)
        
        # Tab 2: AALNI Analysis
        with gr.Tab("AALNI Scores"):
            gr.Markdown("## Abraham Accords Literacy Need Index")
            
            with gr.Row():
                aalni_plot = gr.Plot(value=create_aalni_chart())
            
            with gr.Row():
                budget_plot = gr.Plot(value=create_budget_chart())
            
            gr.Markdown("""
            ### About AALNI
            The Abraham Accords Literacy Need Index combines multiple vulnerability factors to prioritize resource allocation:
            - Higher scores indicate greater educational need
            - Sudan (115.7) has 47x higher need than Bahrain (1.5)
            - Budget allocation proportional to AALNI scores
            """)
        
        # Tab 3: Key Findings
        with gr.Tab("Key Findings"):
            findings_text = gr.Markdown(get_key_findings())
        
        # Tab 4: Methodology
        with gr.Tab("Methodology"):
            method_text = gr.Markdown(get_methodology())
        
        # Tab 5: About
        with gr.Tab("About"):
            gr.Markdown("""
            ## About This Project
            
            **Project Title**: Mapping Literacy for Humanity: Abraham Accords Data Initiative
            
            **Author**: Vanessa Ngeno  
            **Institution**: Peblink | Yeshiva University  
            **Program**: MS in Data Analytics and Visualization  
       
            
            ### Academic Context
            This capstone project demonstrates complete data science lifecycle:
            - Data collection and cleaning
            - Exploratory data analysis
            - Statistical modeling and machine learning
            - Causal inference
            - Time-series forecasting
            - Policy recommendations
            - Interactive visualization
            
            ### Repository
            Full analysis available on GitHub:  
            [github.com/vcngeno/abraham-accords-mapping-literacy-analysis](https://github.com/vcngeno/abraham-accords-mapping-literacy-analysis)
            
            ### Contact
            - Email: vanessangeno@gmail.com
            - LinkedIn: https://www.linkedin.com/in/vanessa-ngeno-048391180/
            - Portfolio: vcngeno.github.io

            
            ### Citation
            If you use this analysis, please cite:
```
            Ngeno, V. (2025). Mapping Literacy for Humanity: Abraham Accords Data Initiative.
            Peblink Internship Project
```
            
            ---
            
            *Using data analytics to map literacy needs and build educational bridges across the Abraham Accords nations.*
            """)

# Launch
if __name__ == "__main__":
    demo.launch()

"""
Pages Content Module
Contains all page rendering functions for the dashboard
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def render_page(page, aalni_data, morocco_timeline, cost_effectiveness, 
                feature_importance, projections_2030):
    """Main router function to render the selected page"""
    
    if page == "Executive Summary":
        render_executive_summary(aalni_data)
    elif page == "AALNI Rankings":
        render_aalni_rankings(aalni_data)
    elif page == "Morocco Case Study":
        render_morocco_case_study(morocco_timeline)
    elif page == "Cost-Effectiveness":
        render_cost_effectiveness(cost_effectiveness)
    elif page == "Feature Importance":
        render_feature_importance(feature_importance)
    elif page == "2030 Projections":
        render_2030_projections(projections_2030)
    elif page == "SDG 4 Alignment":
        render_sdg4_alignment(aalni_data)
    elif page == "Policy Recommendations":
        render_policy_recommendations()


def render_executive_summary(aalni_data):
    """Render the Executive Summary page"""
    st.header("Executive Summary")
    
    # Key Stats in 4 columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>Population Affected</h4>
            <h2>27.1M</h2>
            <p>14.7M women & girls</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>Total Investment</h4>
            <h2>$950M</h2>
            <p>3-year strategic plan</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h4>Expected ROI</h4>
            <h2>700-1000%</h2>
            <p>$6.65-9.5B return</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h4>Success Rate</h4>
            <h2>80%</h2>
            <p>4 of 5 achieve SDG 4</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # The Challenge
    st.subheader("The Challenge")
    st.markdown("""
    The Abraham Accords united nations through peace, but peace dividends require literacy. 
    Across five Abraham Accords nations, **27.1 million people** lack functional literacy, 
    with **14.7 million being women and girls**. Without intervention, only 3 of 5 countries 
    will achieve UN Sustainable Development Goal 4 (universal literacy) by 2030.
    """)
    
    # The Solution
    st.subheader("The Solution: AALNI Framework")
    st.markdown("""
    We created the **Abraham Accords Literacy Need Index (AALNI)** - the first standardized 
    regional literacy assessment tool. AALNI combines five weighted factors:
    
    - **Baseline Gap (30%)**: Distance from 95% SDG target
    - **Gender Disparity (25%)**: Gender Parity Index deviation
    - **Rural-Urban Divide (20%)**: Geographic literacy inequality
    - **Economic Constraint (15%)**: Poverty rate impact
    - **Quality Deficit (10%)**: Learning effectiveness
    - **Plus Conflict Multiplier**: Up to 3× for unstable regions
    """)
    
    # Key Findings
    st.subheader("Key Findings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h4>Morocco Proves the Model</h4>
            <p><strong>$311M investment (2014-2024):</strong></p>
            <ul>
                <li>Literacy: 41.8% → 72.1% (+19.1 points)</li>
                <li>Cost efficiency: $1.62 per person per point</li>
                <li>Reached 8.46 million beneficiaries</li>
                <li>Ranks #2 of 5 programs analyzed</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
            <h4>Sudan's Critical Challenge</h4>
            <p><strong>Despite 79.5% allocation ($755M):</strong></p>
            <ul>
                <li>Literacy declining: 57.0% → 54.1% by 2030</li>
                <li>38-point gap to SDG target</li>
                <li>Conflict is the constraint, not funding</li>
                <li>Phased, conditional approach required</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
        <h4>The 88.9% Rule: How You Spend Matters 50× More Than How Much</h4>
        <p>Our Random Forest analysis (R² = 0.972) reveals that <strong>investment ranks #10</strong> 
        in importance. The top 5 systemic factors explain <strong>88.9% of literacy outcomes</strong>:</p>
        <ol>
            <li>Secondary Enrollment (26.3%)</li>
            <li>Gender Parity (18.5%)</li>
            <li>Learning Quality (16.7%)</li>
            <li>Rural-Urban Gap (14.7%)</li>
            <li>Out-of-School Children (12.8%)</li>
        </ol>
        <p><strong>Policy Implication:</strong> We're not funding literacy programs—we're funding literacy systems.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Investment Allocation
    st.subheader("$950M Investment Allocation")
    
    fig = go.Figure(data=[go.Pie(
        labels=aalni_data['Country'],
        values=aalni_data['Investment_Allocation_M'],
        hole=0.4,
        marker=dict(colors=['#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#8b5cf6']),
        textinfo='label+percent',
        textposition='outside'
    )])
    
    fig.update_layout(
        title="Investment Distribution by Country",
        showlegend=True,
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Sudan", "$755.4M", "79.5%")
        st.caption("Conflict emergency + 38-point gap")
    
    with col2:
        st.metric("Morocco", "$160.1M", "16.8%")
        st.caption("Final SDG push + rural acceleration")
    
    with col3:
        st.metric("High Performers", "$34.5M", "3.6%")
        st.caption("Israel, UAE, Bahrain maintenance")
    
    # ROI Waterfall Chart
    st.markdown("---")
    st.subheader("Return on Investment Breakdown: $6.65-9.5B Economic Impact")
    
    st.markdown("""
    The $950M investment generates **$6.65-9.5 billion** in economic returns by 2030. 
    Here's where that value comes from:
    """)
    
    # ROI Waterfall data (conservative estimate)
    waterfall_data = {
        'Category': ['Investment', 'Direct Productivity\nGains', 'Health\nImprovements', 
                    'Reduced Conflict\nRisk', 'Spillover\nEffects', 'Total Return'],
        'Value': [-950, 4200, 1500, 950, 800, 0],  # Last value recalculated
        'Cumulative': [0, 0, 0, 0, 0, 6500]  # Will calculate
    }
    
    # Calculate cumulative
    cumulative = -950
    cumulative_values = [-950]
    for i in range(1, len(waterfall_data['Value'])-1):
        cumulative += waterfall_data['Value'][i]
        cumulative_values.append(cumulative)
    cumulative_values.append(6500)  # Final total
    
    waterfall_data['Cumulative'] = cumulative_values
    
    # Create waterfall chart
    fig_roi = go.Figure()
    
    # Investment (starting point - red)
    fig_roi.add_trace(go.Bar(
        x=[waterfall_data['Category'][0]],
        y=[abs(waterfall_data['Value'][0])],
        marker_color='#ef4444',
        name='Investment',
        text=[f'-${abs(waterfall_data["Value"][0])}M'],
        textposition='outside',
        showlegend=True
    ))
    
    # Positive contributions (green)
    for i in range(1, len(waterfall_data['Category'])-1):
        fig_roi.add_trace(go.Bar(
            x=[waterfall_data['Category'][i]],
            y=[waterfall_data['Value'][i]],
            marker_color='#10b981',
            name='Gains' if i == 1 else None,
            text=[f'+${waterfall_data["Value"][i]}M'],
            textposition='outside',
            showlegend=(i == 1)
        ))
    
    # Total return (blue)
    fig_roi.add_trace(go.Bar(
        x=[waterfall_data['Category'][-1]],
        y=[waterfall_data['Cumulative'][-1]],
        marker_color='#3b82f6',
        name='Total Return',
        text=[f'${waterfall_data["Cumulative"][-1]}M'],
        textposition='outside',
        showlegend=True
    ))
    
    fig_roi.update_layout(
        title="ROI Waterfall: From $950M Investment to $6.5B Return (Conservative)",
        yaxis_title="Value ($M)",
        height=450,
        showlegend=True,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_roi, use_container_width=True)
    
    # ROI Breakdown explanation
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Direct Productivity Gains: $4.2B**
        - 3.39M people achieve literacy
        - Avg. $6,000 lifetime productivity increase
        - 10-year present value (5% discount)
        - Based on World Bank earnings data
        """)
    
    with col2:
        st.markdown("""
        **Health Improvements: $1.5B**
        - Literate mothers → healthier children
        - Reduced infant mortality
        - Better healthcare utilization
        - Preventive health behaviors
        """)
    
    with col3:
        st.markdown("""
        **Reduced Conflict Risk: $950M**
        - Education reduces extremism
        - Economic opportunities decrease violence
        - Particularly relevant for Sudan
        - Based on conflict economics research
        """)
    
    st.markdown("""
    **Spillover Effects: $800M**
    - Inter-generational benefits (educated parents → educated children)
    - Community-level improvements
    - Innovation and entrepreneurship
    - Democratic participation
    
    **Total Conservative Return: $6.5B (ROI: 684%)**
    
    *Optimistic scenario ($9.5B) uses $10,000 productivity gain (OECD data) and 25% spillover multiplier*
    """)
    
    st.markdown("""
    <div class="insight-box">
        <h4>Key Insight: Every Dollar Returns $7-10</h4>
        <p>This is not charity—it's a <strong>high-return development investment</strong>. 
        For context, the average Fortune 500 company achieves 10-15% ROI. This initiative 
        achieves <strong>684-900% ROI</strong> over 10 years while improving 27.1 million lives.</p>
    </div>
    """, unsafe_allow_html=True)


def render_aalni_rankings(aalni_data):
    """Render the AALNI Rankings page"""
    st.header("AALNI Priority Rankings")
    
    st.markdown("""
    The **Abraham Accords Literacy Need Index (AALNI)** is a composite score that prioritizes 
    countries based on literacy gaps, gender disparities, geographic inequalities, economic 
    constraints, and learning quality—adjusted for conflict severity.
    
    **Higher score = Greater need for intervention**
    """)
    
    # Rankings Table
    st.subheader("Rankings Overview")
    
    display_df = aalni_data[['Country', 'AALNI_Score', 'Adult_Literacy_Rate', 
                             'Investment_Allocation_M', 'Allocation_Percent']].copy()
    display_df.columns = ['Country', 'AALNI Score', 'Current Literacy (%)', 
                         'Investment ($M)', 'Allocation (%)']
    display_df['Rank'] = range(1, len(display_df) + 1)
    display_df = display_df[['Rank', 'Country', 'AALNI Score', 'Current Literacy (%)', 
                             'Investment ($M)', 'Allocation (%)']]
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # Visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("AALNI Scores by Country")
        fig = go.Figure(data=[
            go.Bar(
                x=aalni_data['Country'],
                y=aalni_data['AALNI_Score'],
                marker=dict(
                    color=aalni_data['AALNI_Score'],
                    colorscale='Reds',
                    showscale=True,
                    colorbar=dict(title="Need Level")
                ),
                text=aalni_data['AALNI_Score'].round(1),
                textposition='outside'
            )
        ])
        
        fig.update_layout(
            xaxis_title="Country",
            yaxis_title="AALNI Score (Higher = Greater Need)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Current Literacy Rates")
        fig = go.Figure(data=[
            go.Bar(
                x=aalni_data['Country'],
                y=aalni_data['Adult_Literacy_Rate'],
                marker=dict(
                    color=aalni_data['Adult_Literacy_Rate'],
                    colorscale='Greens',
                    showscale=True,
                    colorbar=dict(title="Literacy %")
                ),
                text=aalni_data['Adult_Literacy_Rate'].round(1),
                textposition='outside'
            )
        ])
        
        fig.add_hline(y=95, line_dash="dash", line_color="gold", 
                     annotation_text="SDG Target (95%)")
        
        fig.update_layout(
            xaxis_title="Country",
            yaxis_title="Adult Literacy Rate (%)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Component Breakdown
    st.subheader("Sudan Component Breakdown (Rank #1)")
    
    st.markdown("""
    Sudan's AALNI score of **115.7** results from:
    - **Baseline Gap:** 38.0 points → 11.40 weighted points
    - **Gender Disparity:** 31.0% gap → 7.75 weighted points
    - **Rural-Urban Gap:** 30.0 points → 6.00 weighted points
    - **Economic Constraint:** 46.0% poverty → 6.90 weighted points
    - **Quality Deficit:** 65 points → 6.50 weighted points
    - **Base Score:** 38.55
    - **× Conflict Multiplier:** 3.0× (Severe Conflict)
    - **= Final AALNI:** 115.7
    """)
    
    # Gender Gap Heatmap
    st.markdown("---")
    st.subheader("Gender Disparity Analysis: 14.7M Women and Girls Affected")
    
    st.markdown("""
    Gender parity accounts for **25% of AALNI scores**. This visualization shows the 
    literacy gap between males and females across all five countries.
    """)
    
    # Create gender data
    gender_data = pd.DataFrame({
        'Country': ['Sudan', 'Morocco', 'Israel', 'UAE', 'Bahrain'],
        'Male_Literacy': [65.7, 79.6, 98.0, 96.5, 97.7],
        'Female_Literacy': [48.3, 64.6, 97.6, 96.1, 97.3],
        'Women_Affected_M': [6.8, 4.2, 0.2, 0.3, 0.1]
    })
    
    gender_data['Gender_Gap'] = gender_data['Male_Literacy'] - gender_data['Female_Literacy']
    gender_data['Gap_Percent'] = (gender_data['Gender_Gap'] / gender_data['Male_Literacy'] * 100).round(1)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Grouped bar chart
        fig_gender = go.Figure()
        
        fig_gender.add_trace(go.Bar(
            name='Male Literacy',
            x=gender_data['Country'],
            y=gender_data['Male_Literacy'],
            marker_color='#3b82f6',
            text=gender_data['Male_Literacy'].round(1),
            textposition='outside'
        ))
        
        fig_gender.add_trace(go.Bar(
            name='Female Literacy',
            x=gender_data['Country'],
            y=gender_data['Female_Literacy'],
            marker_color='#ec4899',
            text=gender_data['Female_Literacy'].round(1),
            textposition='outside'
        ))
        
        fig_gender.add_hline(y=95, line_dash="dash", line_color="gold",
                           annotation_text="SDG Target (95%)")
        
        fig_gender.update_layout(
            title="Male vs Female Literacy Rates by Country",
            yaxis_title="Literacy Rate (%)",
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig_gender, use_container_width=True)
    
    with col2:
        # Gender gap impact table
        st.markdown("**Gender Gap Impact:**")
        
        gap_display = gender_data[['Country', 'Gender_Gap', 'Women_Affected_M']].copy()
        gap_display.columns = ['Country', 'Gap (points)', 'Women Affected (M)']
        gap_display = gap_display.sort_values('Gap (points)', ascending=False)
        
        st.dataframe(gap_display.style.format({
            'Gap (points)': '{:.1f}',
            'Women Affected (M)': '{:.1f}M'
        }).background_gradient(subset=['Gap (points)'], cmap='Reds'),
        use_container_width=True, hide_index=True)
        
        st.markdown("""
        **Total: 14.7M women and girls** lack functional literacy across the region.
        
        **Critical finding:** Sudan's 17.4-point gender gap affects **6.8M women** - 
        nearly half of all affected women in the region.
        """)
    
    # Gender allocation breakdown
    st.markdown("**Investment Allocation for Gender Equity:**")
    
    gender_investment = pd.DataFrame({
        'Country': ['Sudan', 'Morocco', 'Israel', 'UAE', 'Bahrain'],
        'Gender_Allocation_M': [189, 40, 3, 3, 2],
        'Percent_of_Country_Budget': [25, 25, 23, 25, 21]
    })
    
    fig_gender_invest = go.Figure(data=[
        go.Bar(
            x=gender_investment['Country'],
            y=gender_investment['Gender_Allocation_M'],
            marker_color='#ec4899',
            text=gender_investment['Gender_Allocation_M'],
            texttemplate='$%{text}M',
            textposition='outside'
        )
    ])
    
    fig_gender_invest.update_layout(
        title="Gender-Specific Investment Allocation (25% of country budgets)",
        yaxis_title="Investment ($M)",
        height=350
    )
    
    st.plotly_chart(fig_gender_invest, use_container_width=True)
    
    st.markdown("""
    <div class="insight-box">
        <h4>Policy Implication: Gender Equity is Not Optional</h4>
        <p>With gender parity explaining <strong>18.5% of literacy outcomes</strong> (from our Random Forest model), 
        investing in women's education is not just morally right—it's statistically necessary for success.</p>
        <p><strong>Sudan's gender allocation ($189M)</strong> targets:</p>
        <ul>
            <li>Girls' education stipends and scholarships</li>
            <li>Safe transportation to schools</li>
            <li>Female teacher recruitment and training</li>
            <li>Community engagement with male family members</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


def render_morocco_case_study(morocco_timeline):
    """Render the Morocco Case Study page"""
    st.header("Morocco: $311M Investment Impact Analysis")
    
    st.markdown("""
    Morocco's National Literacy Program (2014-2024) provides empirical validation 
    of our investment strategy. This is **proof of concept** for the AALNI framework.
    """)
    
    # Key Results
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Literacy Improvement", "+19.1 pts", "41.8% → 72.1%")
    
    with col2:
        st.metric("Annual Growth Rate", "+2.12 pts/yr", "p < 0.0001")
    
    with col3:
        st.metric("Cost Efficiency", "$1.62", "per person per point")
    
    with col4:
        st.metric("Efficiency Rank", "#2 of 5", "Top-tier")
    
    # Timeline Visualization
    st.subheader("Morocco's Literacy Trajectory (2008-2030)")
    
    fig = go.Figure()
    
    # Actual data
    actual_data = morocco_timeline[morocco_timeline['Type'] == 'Actual']
    projected_data = morocco_timeline[morocco_timeline['Type'] == 'Projected']
    
    fig.add_trace(go.Scatter(
        x=actual_data['Year'],
        y=actual_data['Literacy_Rate'],
        mode='lines+markers',
        name='Actual Literacy Rate',
        line=dict(color='#3b82f6', width=3),
        marker=dict(size=8)
    ))
    
    # Projected data
    fig.add_trace(go.Scatter(
        x=projected_data['Year'],
        y=projected_data['Literacy_Rate'],
        mode='lines+markers',
        name='Projected',
        line=dict(color='#f59e0b', width=3, dash='dash'),
        marker=dict(size=8)
    ))
    
    # SDG Target line
    fig.add_hline(y=95, line_dash="dash", line_color="gold",
                 annotation_text="SDG Target (95%)",
                 annotation_position="right")
    
    # Intervention marker
    fig.add_vline(x=2014, line_dash="dash", line_color="green",
                 annotation_text="Intervention Start (2014)",
                 annotation_position="top")
    
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Adult Literacy Rate (%)",
        height=500,
        hovermode='x unified',
        yaxis=dict(range=[35, 100])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Before/After DiD Comparison
    st.subheader("Before vs After Intervention: Difference-in-Differences Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Calculate average growth rates
        before_data = actual_data[actual_data['Year'] < 2014]
        after_data = actual_data[actual_data['Year'] >= 2014]
        
        # Before period growth
        if len(before_data) > 1:
            before_years = before_data['Year'].max() - before_data['Year'].min()
            before_improvement = before_data['Literacy_Rate'].max() - before_data['Literacy_Rate'].min()
            before_annual_rate = before_improvement / before_years if before_years > 0 else 0
        else:
            before_annual_rate = 0
        
        # After period growth
        if len(after_data) > 1:
            after_years = after_data['Year'].max() - after_data['Year'].min()
            after_improvement = after_data['Literacy_Rate'].max() - after_data['Literacy_Rate'].min()
            after_annual_rate = after_improvement / after_years if after_years > 0 else 0
        else:
            after_annual_rate = 2.12  # From the analysis
        
        # DiD Effect
        did_effect = after_annual_rate - before_annual_rate
        
        # Create comparison bar chart
        fig_did = go.Figure(data=[
            go.Bar(
                x=['Before Intervention\n(2008-2013)', 'After Intervention\n(2014-2024)', 'DiD Effect'],
                y=[before_annual_rate, after_annual_rate, did_effect],
                marker=dict(
                    color=['#94a3b8', '#10b981', '#3b82f6'],
                ),
                text=[f'+{before_annual_rate:.2f}%/yr', 
                      f'+{after_annual_rate:.2f}%/yr',
                      f'+{did_effect:.2f}%/yr'],
                textposition='outside'
            )
        ])
        
        fig_did.update_layout(
            title="Annual Literacy Growth Rate Comparison",
            yaxis_title="Percentage Points per Year",
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig_did, use_container_width=True)
        
        st.markdown(f"""
        **Interpretation:**
        - **Before (2008-2013):** +{before_annual_rate:.2f} points/year (natural trend)
        - **After (2014-2024):** +{after_annual_rate:.2f} points/year (with intervention)
        - **DiD Effect:** +{did_effect:.2f} points/year (intervention impact)
        
        The intervention **increased** the annual literacy growth rate by **{did_effect:.2f} percentage points**.
        """)
    
    with col2:
        # Create counterfactual visualization
        fig_counterfactual = go.Figure()
        
        # Actual trajectory
        fig_counterfactual.add_trace(go.Scatter(
            x=actual_data['Year'],
            y=actual_data['Literacy_Rate'],
            mode='lines+markers',
            name='Actual (With Intervention)',
            line=dict(color='#10b981', width=3),
            marker=dict(size=8)
        ))
        
        # Counterfactual (what would have happened without intervention)
        counterfactual_years = list(range(2014, 2025))
        baseline_2014 = 47.7  # Literacy rate in 2014
        counterfactual_rates = [baseline_2014 + (year - 2014) * before_annual_rate 
                               for year in counterfactual_years]
        
        fig_counterfactual.add_trace(go.Scatter(
            x=counterfactual_years,
            y=counterfactual_rates,
            mode='lines',
            name='Counterfactual (Without Intervention)',
            line=dict(color='#ef4444', width=3, dash='dash'),
        ))
        
        # Intervention marker
        fig_counterfactual.add_vline(x=2014, line_dash="dash", line_color="gray",
                     annotation_text="Intervention",
                     annotation_position="top")
        
        # Shaded area showing the intervention effect
        fig_counterfactual.add_trace(go.Scatter(
            x=counterfactual_years + counterfactual_years[::-1],
            y=counterfactual_rates + [actual_data[actual_data['Year'] == year]['Literacy_Rate'].values[0] 
                                      if year in actual_data['Year'].values else counterfactual_rates[i]
                                      for i, year in enumerate(counterfactual_years)][::-1],
            fill='toself',
            fillcolor='rgba(59, 130, 246, 0.2)',
            line=dict(color='rgba(255,255,255,0)'),
            name='Intervention Gain',
            showlegend=True
        ))
        
        fig_counterfactual.update_layout(
            title="Actual vs Counterfactual Trajectory",
            xaxis_title="Year",
            yaxis_title="Literacy Rate (%)",
            height=400,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_counterfactual, use_container_width=True)
        
        # Calculate total gain from intervention
        actual_2024 = 72.1
        counterfactual_2024 = baseline_2014 + (2024 - 2014) * before_annual_rate
        total_gain = actual_2024 - counterfactual_2024
        
        st.markdown(f"""
        **Counterfactual Analysis:**
        - **Without intervention:** Would be at {counterfactual_2024:.1f}% in 2024
        - **With intervention:** Actually at {actual_2024:.1f}% in 2024
        - **Total gain from intervention:** +{total_gain:.1f} percentage points
        
        The blue shaded area represents the **additional literacy gains** directly attributable to the $311M investment.
        """)
    
    st.markdown("---")
    
    # Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h4>What Worked</h4>
            <ul>
                <li><strong>Comprehensive approach:</strong> Addressed all 5 critical factors</li>
                <li><strong>Long-term commitment:</strong> 10 years of consistent investment</li>
                <li><strong>Scale:</strong> 8.46M beneficiaries created efficiency</li>
                <li><strong>Targeted programs:</strong> Tayssir CCT, rural schools, teacher training</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
            <h4>2030 Gap Analysis</h4>
            <ul>
                <li><strong>Projected 2030:</strong> 85.4%</li>
                <li><strong>SDG Target:</strong> 95.0%</li>
                <li><strong>Gap:</strong> 9.6 percentage points</li>
                <li><strong>Additional needed:</strong> $15.6M</li>
                <li><strong>Focus:</strong> Rural areas (25.8-point urban-rural gap)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
        <h4>Policy Implication</h4>
        <p>Morocco validates the AALNI framework. Systematic, sustained investment produces 
        measurable results. The model is ready to scale—with adjustments for local context 
        (conflict in Sudan, acceleration timeline for Morocco's final push).</p>
    </div>
    """, unsafe_allow_html=True)


def render_cost_effectiveness(cost_effectiveness):
    """Render the Cost-Effectiveness page"""
    st.header("Cost-Effectiveness Analysis")
    
    st.markdown("""
    Comparing intervention efficiency across the Abraham Accords region to identify 
    best practices and inform investment allocation.
    """)
    
    # Rankings Table
    st.subheader("Program Efficiency Rankings")
    
    display_df = cost_effectiveness.copy()
    display_df['Rank'] = range(1, len(display_df) + 1)
    display_df = display_df[['Rank', 'Country', 'Program', 'Cost_Per_Point', 
                             'Literacy_Improvement', 'Duration_Years']]
    display_df.columns = ['Rank', 'Country', 'Program', 'Cost per Point ($)', 
                         'Impact (pts)', 'Duration (yrs)']
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # Visualization
    st.subheader("Cost per Percentage Point Improvement")
    
    fig = go.Figure(data=[
        go.Bar(
            y=cost_effectiveness['Program'],
            x=cost_effectiveness['Cost_Per_Point'],
            orientation='h',
            marker=dict(
                color=cost_effectiveness['Cost_Per_Point'],
                colorscale='RdYlGn_r',
                showscale=True,
                colorbar=dict(title="Cost ($)")
            ),
            text=cost_effectiveness['Cost_Per_Point'].round(2),
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        xaxis_title="Cost per Percentage Point ($)",
        yaxis_title="Program",
        height=400,
        xaxis_type="log"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Key Insights
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h4>Most Efficient: UAE Compulsory Education</h4>
            <ul>
                <li><strong>Cost:</strong> $0.53 per point</li>
                <li><strong>Impact:</strong> +42.0 percentage points</li>
                <li><strong>Duration:</strong> 49 years</li>
                <li><strong>Key Factor:</strong> Long-term systemic approach</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
            <h4>Morocco's Position: #2 of 5</h4>
            <ul>
                <li><strong>Cost:</strong> $1.62 per point</li>
                <li><strong>Efficiency:</strong> 3× less efficient than #1</li>
                <li><strong>Impact:</strong> +19.8 points in 10 years</li>
                <li><strong>Status:</strong> Top-tier cost-effectiveness</li>
            </ul>
            <p><strong>Accelerated Timeline:</strong> Morocco achieved comparable 
            impact in 1/5th the time (10 vs 49 years)</p>
        </div>
        """, unsafe_allow_html=True)


def render_feature_importance(feature_importance):
    """Render the Feature Importance page"""
    st.header("The 88.9% Rule: What Actually Drives Literacy?")
    
    st.markdown("""
    We used Random Forest machine learning (R² = 0.972, explaining 97.2% of variance) 
    to identify what truly matters for literacy improvement. The results are counterintuitive.
    """)
    
    # Feature Importance Chart
    st.subheader("Factor Importance in Literacy Outcomes")
    
    # Reverse the order so Secondary Enrollment is at top
    feature_importance_reversed = feature_importance.iloc[::-1].reset_index(drop=True)
    
    fig = go.Figure(data=[
        go.Bar(
            x=feature_importance_reversed['Importance'],
            y=feature_importance_reversed['Feature'],
            orientation='h',
            marker=dict(
                color=['#6b7280']*3 + ['#10b981']*5,  # Gray for bottom 3, green for top 5
            ),
            text=feature_importance_reversed['Importance'].round(1),
            texttemplate='%{text}%',
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        xaxis_title="Importance (%)",
        yaxis_title="Factor",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Key Findings
    st.markdown("""
    <div class="warning-box">
        <h4>Counterintuitive Finding: Money Isn't Everything</h4>
        <p><strong>Investment ranked #10</strong> out of 14 factors, explaining only <strong>1.6%</strong> 
        of literacy outcomes.</p>
        <p>This means: <strong>Simply increasing funding doesn't guarantee improvement.</strong> 
        Systemic factors (education quality, equity, access) matter <strong>50× more</strong>.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Sudan's $755M Allocation Strategy")
    
    sudan_allocation = pd.DataFrame({
        'Priority': ['Secondary Education', 'Gender Equity', 'Learning Quality', 
                    'Rural Access', 'Basic Literacy'],
        'Percentage': [30, 25, 20, 15, 10],
        'Amount_M': [227, 189, 151, 113, 76]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = go.Figure(data=[go.Pie(
            labels=sudan_allocation['Priority'],
            values=sudan_allocation['Amount_M'],
            hole=0.3
        )])
        
        fig.update_layout(title="Sudan's Strategic Allocation", height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.dataframe(sudan_allocation.style.format({
            'Percentage': '{}%',
            'Amount_M': '${:.0f}M'
        }), use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="insight-box">
        <h4>This Is NOT a Traditional Literacy Program</h4>
        <p>Sudan's $755M isn't for basic reading classes. It's a comprehensive education 
        system rebuild focused on the factors that actually drive outcomes: secondary schools, 
        gender equity, teacher quality, rural access, and removing barriers to education.</p>
    </div>
    """, unsafe_allow_html=True)


def render_2030_projections(projections_2030):
    """Render the 2030 Projections page"""
    st.header("2030 SDG Achievement Forecast")
    
    st.markdown("""
    Using Prophet time-series forecasting, we project which countries will achieve 
    UN Sustainable Development Goal 4 (95% literacy) by 2030.
    """)
    
    # Summary Stats
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Countries on Track", "3 of 5", "Israel, UAE, Bahrain")
    
    with col2:
        st.metric("Countries Falling Short", "2 of 5", "Morocco, Sudan")
    
    with col3:
        st.metric("Success Rate", "80%", "4 of 5 will achieve")
    
    # Projections Chart
    st.subheader("Current vs. 2030 Projected Literacy Rates")
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Current (2024)',
        x=projections_2030['Country'],
        y=projections_2030['Current_2024'],
        marker_color='#3b82f6'
    ))
    
    fig.add_trace(go.Bar(
        name='Projected (2030)',
        x=projections_2030['Country'],
        y=projections_2030['Projected_2030'],
        marker_color='#10b981'
    ))
    
    fig.add_hline(y=95, line_dash="dash", line_color="gold",
                 annotation_text="SDG Target (95%)")
    
    fig.update_layout(
        barmode='group',
        xaxis_title="Country",
        yaxis_title="Literacy Rate (%)",
        height=450
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Status Details
    st.subheader("Detailed Status by Country")
    
    for _, row in projections_2030.iterrows():
        status_color = {
            'On Track': 'success-box',
            'Needs Support': 'insight-box',
            'Critical': 'warning-box'
        }[row['Status']]
        
        st.markdown(f"""
        <div class="{status_color}">
            <h4>{row['Country']}: {row['Status']}</h4>
            <ul>
                <li><strong>Current (2024):</strong> {row['Current_2024']}%</li>
                <li><strong>Projected (2030):</strong> {row['Projected_2030']}%</li>
                <li><strong>Gap to SDG:</strong> {row['Gap_to_SDG']:.1f} percentage points</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Additional Investment Needed
    st.subheader("Additional Investment Required")
    
    st.markdown("""
    To achieve UN SDG 4 by 2030, the following additional investments are needed:
    
    - **Morocco**: $15.6M (9.6 points × $1.62/point efficiency)
    - **Sudan**: $198.8M (40.9 points × $1.62/point × 3× conflict multiplier)
    - **Total Additional**: $214.4M
    
    This represents only **22.6%** of the $950M budget, confirming the AALNI allocation is well-calibrated.
    """)
    
    # Conflict Impact on Literacy - Sudan Focus
    st.markdown("---")
    st.subheader("Conflict Impact on Literacy: The Sudan Crisis")
    
    st.markdown("""
    **Why is Sudan's literacy declining while others improve?** This visualization shows the 
    devastating impact of conflict on educational outcomes.
    """)
    
    # Sudan historical data with conflict events
    sudan_timeline = pd.DataFrame({
        'Year': [2005, 2008, 2010, 2012, 2014, 2016, 2018, 2019, 2020, 2021, 2023, 2024],
        'Literacy_Rate': [61.0, 60.5, 60.0, 59.5, 59.0, 58.5, 58.0, 57.5, 57.5, 57.2, 57.1, 57.0],
        'Conflict_Intensity': [6, 5, 4, 5, 6, 7, 6, 8, 7, 9, 10, 10],  # Scale 0-10
        'Major_Event': ['Darfur Crisis', '', '', '', '', '', '', 'Political Unrest', 
                       'Transition', 'Military Coup', 'Civil War Begins', 'Escalation']
    })
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Dual-axis chart: Literacy vs Conflict
        fig_conflict = go.Figure()
        
        # Literacy rate (declining - blue line)
        fig_conflict.add_trace(go.Scatter(
            x=sudan_timeline['Year'],
            y=sudan_timeline['Literacy_Rate'],
            mode='lines+markers',
            name='Literacy Rate',
            yaxis='y1',
            line=dict(color='#3b82f6', width=3),
            marker=dict(size=10)
        ))
        
        # Conflict intensity (increasing - red bars)
        fig_conflict.add_trace(go.Bar(
            x=sudan_timeline['Year'],
            y=sudan_timeline['Conflict_Intensity'],
            name='Conflict Intensity',
            yaxis='y2',
            marker_color='#ef4444',
            opacity=0.6
        ))
        
        # Add annotations for major events
        for idx, row in sudan_timeline.iterrows():
            if row['Major_Event']:
                fig_conflict.add_annotation(
                    x=row['Year'],
                    y=row['Literacy_Rate'],
                    text=row['Major_Event'],
                    showarrow=True,
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=2,
                    arrowcolor='#ef4444',
                    ax=0,
                    ay=-40,
                    font=dict(size=9, color='#ef4444')
                )
        
        fig_conflict.update_layout(
            title="Sudan: Inverse Relationship Between Conflict and Literacy",
            xaxis_title="Year",
            yaxis=dict(
                title="Literacy Rate (%)",
                titlefont=dict(color='#3b82f6'),
                tickfont=dict(color='#3b82f6'),
                range=[55, 63]
            ),
            yaxis2=dict(
                title="Conflict Intensity (Scale 0-10)",
                titlefont=dict(color='#ef4444'),
                tickfont=dict(color='#ef4444'),
                overlaying='y',
                side='right',
                range=[0, 12]
            ),
            height=450,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_conflict, use_container_width=True)
    
    with col2:
        st.markdown("**Conflict Impact:**")
        
        conflict_stats = pd.DataFrame({
            'Metric': ['Schools Destroyed', 'Teachers Displaced', 'Children Out of School', 
                      'Literacy Decline'],
            'Value': ['2,400+', '15,000+', '3.5M', '-4.0 pts']
        })
        
        st.dataframe(conflict_stats, use_container_width=True, hide_index=True)
        
        st.markdown("""
        **Correlation Analysis:**
        - **R = -0.89** (strong negative correlation)
        - As conflict intensity increases, literacy declines
        - 2023-2024: Civil war → sharpest decline
        """)
    
    # The Brutal Reality
    st.markdown("""
    <div class="warning-box">
        <h4>The Brutal Reality: You Cannot Teach Literacy in a War Zone</h4>
        <p><strong>From 2005 to 2024:</strong></p>
        <ul>
            <li>Literacy declined from 61.0% → 57.0% (-4.0 points)</li>
            <li>Conflict intensity increased from 6/10 → 10/10</li>
            <li>2,400+ schools destroyed or damaged</li>
            <li>15,000+ teachers killed, displaced, or fled</li>
            <li>3.5 million children out of school</li>
        </ul>
        <p><strong>Without conflict resolution, Sudan's $755M allocation will not achieve its goals.</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Scenario comparison
    st.subheader("Sudan Scenarios: Conflict vs Peace")
    
    scenarios = pd.DataFrame({
        'Scenario': ['Current Trajectory\n(Conflict Continues)', 
                    'Humanitarian Phase\n(Partial Stability)',
                    'Full Peace\n(Conflict Resolved)'],
        '2030_Literacy': [54.1, 65.0, 78.0],
        'Investment_Effectiveness': [10, 40, 85],
        'Probability': [50, 35, 15]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_scenarios = go.Figure(data=[
            go.Bar(
                x=scenarios['Scenario'],
                y=scenarios['2030_Literacy'],
                marker_color=['#ef4444', '#f59e0b', '#10b981'],
                text=scenarios['2030_Literacy'],
                texttemplate='%{text}%',
                textposition='outside'
            )
        ])
        
        fig_scenarios.add_hline(y=95, line_dash="dash", line_color="gold",
                              annotation_text="SDG Target")
        
        fig_scenarios.update_layout(
            title="2030 Literacy Under Different Scenarios",
            yaxis_title="Projected Literacy Rate (%)",
            height=400
        )
        
        st.plotly_chart(fig_scenarios, use_container_width=True)
    
    with col2:
        fig_effectiveness = go.Figure(data=[
            go.Bar(
                x=scenarios['Scenario'],
                y=scenarios['Investment_Effectiveness'],
                marker_color=['#ef4444', '#f59e0b', '#10b981'],
                text=scenarios['Investment_Effectiveness'],
                texttemplate='%{text}%',
                textposition='outside'
            )
        ])
        
        fig_effectiveness.update_layout(
            title="Investment Effectiveness by Scenario",
            yaxis_title="% of Funds Reaching Target Beneficiaries",
            height=400
        )
        
        st.plotly_chart(fig_effectiveness, use_container_width=True)
    
    st.markdown("""
    <div class="insight-box">
        <h4>Policy Implication: Parallel Track Approach</h4>
        <p>Sudan's $755M allocation is <strong>conflict-contingent and phased</strong>:</p>
        <ul>
            <li><strong>Phase 1 (Current):</strong> $200M for humanitarian education in camps and stable regions</li>
            <li><strong>Phase 2 (Partial stability):</strong> $227M for regional reconstruction</li>
            <li><strong>Phase 3 (Peace):</strong> $151M for full system rebuild</li>
            <li><strong>Reserve:</strong> $177M held until security improves</li>
        </ul>
        <p><strong>If conflict continues:</strong> Redirect unspent funds to Morocco's full SDG achievement 
        and Saudi Arabia/Qatar expansion. Sudan doesn't kill the program—it's a parallel track.</p>
    </div>
    """, unsafe_allow_html=True)


def render_sdg4_alignment(aalni_data):
    """Render the SDG 4 Alignment page"""
    st.header("UN SDG 4 Alignment: Quality Education for All")
    
    st.markdown("""
    Our Abraham Accords Literacy Initiative directly advances **UN Sustainable Development Goal 4: 
    Quality Education**, specifically **Target 4.6: Adult and Youth Literacy by 2030**.
    """)
    
    # SDG 4 Overview
    st.subheader("SDG 4: Ensure Inclusive and Equitable Quality Education")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Official Target 4.6:**
        > "By 2030, ensure that all youth and a substantial proportion of adults, 
        > both men and women, achieve literacy and numeracy"
        
        **Benchmark:** 95% adult literacy rate globally
        
        **Our Target:** 4 of 5 Abraham Accords nations achieve 95% by 2030 (80% success rate)
        """)
    
    with col2:
        st.metric("Global Progress", "87%", "Current adult literacy")
        st.metric("Our Region Baseline", "76.1%", "2024")
        st.metric("Our 2030 Target", "82.4%", "+6.3 points")
    
    # Five Pillars Infographic
    st.markdown("---")
    st.subheader("The Five Pillars of SDG 4 and AALNI Alignment")
    
    # Create pillars data
    pillars_data = pd.DataFrame({
        'Pillar': ['EQUITY', 'QUALITY', 'INCLUSION', 'LIFELONG\nLEARNING', 'SUSTAINABILITY'],
        'SDG_Focus': [
            'Eliminate disparities',
            'Learning outcomes',
            'Reach marginalized',
            'Early childhood to adult',
            'Adequate financing'
        ],
        'AALNI_Component': [
            'Gender Parity (25%)\nRural-Urban Gap (20%)',
            'Learning Quality (10%)\nSecondary Enrollment',
            'Out-of-School Children\nConflict Adjustment',
            'Adult Focus\nSpillover Effects',
            '$950M Evidence-Based\n700-1000% ROI'
        ],
        'Score': [45, 36, 25, 15, 100]  # Visual representation
    })
    
    # Pillars visualization - horizontal bars showing alignment strength
    fig_pillars = go.Figure()
    
    colors = ['#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#8b5cf6']
    
    for i, row in pillars_data.iterrows():
        fig_pillars.add_trace(go.Bar(
            y=[row['Pillar']],
            x=[row['Score']],
            orientation='h',
            name=row['Pillar'],
            marker_color=colors[i],
            text=row['AALNI_Component'],
            textposition='inside',
            textfont=dict(size=10, color='white'),
            hovertemplate=f"<b>{row['Pillar']}</b><br>SDG Focus: {row['SDG_Focus']}<br>AALNI: {row['AALNI_Component']}<extra></extra>",
            showlegend=False
        ))
    
    fig_pillars.update_layout(
        title="Five Pillars: SDG 4 Framework ↔ AALNI Implementation",
        xaxis_title="Alignment Strength",
        height=400,
        xaxis=dict(showticklabels=False, showgrid=False),
        yaxis=dict(categoryorder='array', categoryarray=pillars_data['Pillar'].tolist()[::-1])
    )
    
    st.plotly_chart(fig_pillars, use_container_width=True)
    
    # Detailed Alignment Matrix
    st.markdown("---")
    st.subheader("SDG 4 Targets: Detailed Alignment Matrix")
    
    alignment_data = pd.DataFrame({
        'SDG Target': [
            '4.1: Primary & Secondary Education',
            '4.2: Early Childhood Development',
            '4.3: Technical & Vocational Education',
            '4.4: Skills for Employment',
            '4.5: Eliminate Disparities',
            '4.6: Adult & Youth Literacy',
            '4.7: Sustainable Development Education',
            '4.a: Safe Learning Environments',
            '4.b: Scholarships',
            '4.c: Qualified Teachers'
        ],
        'AALNI Alignment': [
            'Secondary Enrollment (26.3% importance)',
            'Spillover effects in ROI',
            'Learning Quality Index (10%)',
            'Productivity gains ($4.2B ROI)',
            'Gender Parity (25%) + Rural-Urban (20%)',
            'PRIMARY FOCUS - 95% by 2030',
            'Reduced conflict risk ($950M ROI)',
            'Sudan Phase 1 humanitarian education',
            'Sudan gender equity ($189M)',
            'Morocco teacher training success'
        ],
        'Strength': [90, 60, 70, 85, 95, 100, 75, 80, 85, 80]
    })
    
    # Color-coded table
    def color_strength(val):
        if val >= 90:
            return 'background-color: #d1fae5'  # Green
        elif val >= 75:
            return 'background-color: #bfdbfe'  # Blue
        elif val >= 60:
            return 'background-color: #fef3c7'  # Yellow
        else:
            return 'background-color: #fee2e2'  # Red
    
    styled_alignment = alignment_data.style.applymap(color_strength, subset=['Strength'])
    st.dataframe(styled_alignment, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Color Legend:** 
    🟢 Green (90-100%): Strong alignment | 🔵 Blue (75-89%): Good alignment | 
    🟡 Yellow (60-74%): Moderate alignment | 🔴 Red (<60%): Limited alignment
    """)
    
    # Regional Laboratory Concept
    st.markdown("---")
    st.subheader("Abraham Accords Nations: A Natural SDG 4 Laboratory")
    
    st.markdown("""
    The diversity of Abraham Accords nations creates a unique opportunity to test 
    and refine literacy interventions across different contexts.
    """)
    
    laboratory_data = pd.DataFrame({
        'Country': ['Israel', 'UAE', 'Bahrain', 'Morocco', 'Sudan'],
        'Literacy': [97.8, 96.3, 97.5, 72.1, 57.0],
        'SDG_Status': ['Achieved', 'Achieved', 'Achieved', 'On Track (2032)', 'Critical'],
        'Learning_Role': ['Mentor (Ulpan method)', 'Mentor (Compulsory education)', 
                         'Mentor (Workplace literacy)', 'Proof of Concept', 'Test Case (Conflict resilience)'],
        'Role_Type': ['Mentor', 'Mentor', 'Mentor', 'Learner', 'Emergency']
    })
    
    # Scatter plot showing diversity
    fig_lab = go.Figure()
    
    colors_map = {'Mentor': '#10b981', 'Learner': '#3b82f6', 'Emergency': '#ef4444'}
    
    for role in laboratory_data['Role_Type'].unique():
        subset = laboratory_data[laboratory_data['Role_Type'] == role]
        fig_lab.add_trace(go.Scatter(
            x=subset.index,
            y=subset['Literacy'],
            mode='markers+text',
            name=role,
            marker=dict(size=30, color=colors_map[role]),
            text=subset['Country'],
            textposition='top center',
            textfont=dict(size=12, color='black'),
            hovertemplate='<b>%{text}</b><br>Literacy: %{y:.1f}%<br>' + 
                         'Role: ' + subset['Learning_Role'].values[0] + '<extra></extra>'
        ))
    
    fig_lab.add_hline(y=95, line_dash="dash", line_color="gold",
                     annotation_text="SDG Target (95%)")
    
    fig_lab.update_layout(
        title="Regional Laboratory: Diversity Creates Learning",
        xaxis_title="",
        yaxis_title="Adult Literacy Rate (%)",
        height=400,
        xaxis=dict(showticklabels=False),
        yaxis=dict(range=[50, 105])
    )
    
    st.plotly_chart(fig_lab, use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h4>High Performers (3 countries)</h4>
            <p><strong>Role:</strong> Regional mentors</p>
            <p><strong>Contribution:</strong></p>
            <ul>
                <li>Share best practices</li>
                <li>Provide technical assistance</li>
                <li>Demonstrate what's possible</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
            <h4>Morocco</h4>
            <p><strong>Role:</strong> Proof of concept</p>
            <p><strong>Contribution:</strong></p>
            <ul>
                <li>Validates intervention model</li>
                <li>41.8% → 72.1% in 10 years</li>
                <li>$1.62/point efficiency benchmark</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="warning-box">
            <h4>Sudan</h4>
            <p><strong>Role:</strong> Conflict resilience test</p>
            <p><strong>Contribution:</strong></p>
            <ul>
                <li>Tests education in crisis</li>
                <li>Humanitarian learning models</li>
                <li>Phased, adaptive approach</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Unique Advantages
    st.markdown("---")
    st.subheader("Why This Initiative Advances SDG 4 Uniquely")
    
    advantages = pd.DataFrame({
        'Traditional SDG 4 Approach': [
            'Country-by-country programs',
            'Political negotiation for funding',
            'Ignores conflict impact',
            'Gender-blind allocation',
            'Focuses on enrollment numbers',
            'Limited cost-effectiveness tracking'
        ],
        'Abraham Accords AALNI Approach': [
            'Regional framework with comparability',
            'Evidence-based formula (AALNI)',
            'Conflict multiplier (3× for Sudan)',
            '25% allocated to gender equity',
            'Learning outcomes prioritized (26.3%)',
            'Ranked by cost per point ($0.53-$150)'
        ]
    })
    
    st.table(advantages)
    
    # Key Talking Points
    st.markdown("---")
    st.subheader("Key Talking Points for Stakeholders")
    
    st.markdown("""
    <div class="insight-box">
        <h4>30-Second Elevator Pitch</h4>
        <p>"Our Abraham Accords Literacy Initiative directly addresses UN Sustainable Development Goal 4, 
        Target 4.6: achieving 95% adult literacy by 2030. We've built the first regional assessment 
        framework that accounts for conflict, gender disparities, and rural-urban gaps—the exact equity 
        priorities outlined in the SDG framework."</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box">
        <h4>2-Minute Deep Dive</h4>
        <p><strong>SDG 4 rests on five pillars:</strong> equity, quality, inclusion, lifelong learning, 
        and sustainable financing.</p>
        
        <p><strong>Our AALNI framework operationalizes all five:</strong></p>
        <ul>
            <li><strong>Equity</strong> drives our gender parity index (25%) and rural-urban gap metrics (20%)</li>
            <li><strong>Quality</strong> is measured through learning outcomes—our Random Forest model identifies 
            secondary enrollment as the #1 predictor (26.3%) of literacy success</li>
            <li><strong>Inclusion</strong> is embedded in our focus on out-of-school children (12.8% importance) 
            and Sudan's refugee education</li>
            <li><strong>Lifelong learning</strong> appears in our multi-generational ROI calculations 
            ($800M spillover effects)</li>
            <li><strong>Sustainable financing</strong> is proven through Morocco's $1.62 cost-effectiveness 
            and our 700-1000% ROI</li>
        </ul>
        
        <p><strong>The Abraham Accords nations provide a unique laboratory:</strong> three high performers 
        serving as regional mentors, Morocco as proof-of-concept for accelerated progress, and Sudan as a 
        test of conflict-resilient education.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Connection to other SDGs
    st.markdown("---")
    st.subheader("Literacy as a Cross-Cutting SDG Enabler")
    
    st.markdown("""
    Achieving SDG 4 (literacy) directly accelerates progress on 6 other SDGs:
    """)
    
    crosscutting = pd.DataFrame({
        'SDG': ['SDG 1: No Poverty', 'SDG 3: Good Health', 'SDG 5: Gender Equality',
               'SDG 8: Economic Growth', 'SDG 10: Reduced Inequality', 'SDG 16: Peace & Justice'],
        'Impact': [
            'Literate people earn 15-25% more ($4.2B in our ROI)',
            'Literate mothers → 50% lower child mortality ($1.5B)',
            '14.7M women/girls empowered through literacy',
            'Productivity gains drive economic competitiveness',
            'Closes rural-urban gaps (20% of AALNI)',
            'Education reduces conflict risk ($950M ROI)'
        ],
        'AALNI_Connection': [
            'Direct productivity ROI',
            'Health improvement ROI',
            'Gender Parity Index (25%)',
            'Economic ROI justification',
            'Rural-Urban Gap (20%)',
            'Conflict multiplier & Sudan approach'
        ]
    })
    
    st.dataframe(crosscutting, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="insight-box">
        <h4>Bottom Line for Stakeholders</h4>
        <p>Investing in literacy isn't just about reading and writing—it's about unlocking human potential 
        across every dimension of sustainable development. Our $950M investment in SDG 4 generates returns 
        across SDGs 1, 3, 5, 8, 10, and 16. This is the highest-leverage development investment available.</p>
    </div>
    """, unsafe_allow_html=True)


def render_policy_recommendations():
    """Render the Policy Recommendations page"""
    st.header("Policy Recommendations")
    
    st.markdown("""
    Based on comprehensive analysis of literacy needs across five Abraham Accords nations, 
    we present evidence-based recommendations for international stakeholders, government 
    partners, and the academic community.
    """)
    
    # For International Stakeholders
    st.subheader("For International Stakeholders")
    
    st.markdown("""
    <div class="insight-box">
        <h4>1. Approve $950M AALNI-Based Allocation</h4>
        <ul>
            <li>Sudan: $755.4M (79.5%) - conflict-contingent, phased release</li>
            <li>Morocco: $160.1M + $15.6M boost (18.5%)</li>
            <li>High performers: $34.5M (3.6%) for maintenance</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
        <h4>2. Adopt the 88.9% Rule Framework</h4>
        <ul>
            <li>All investments must address top 5 systemic factors</li>
            <li>Reject proposals focused solely on basic literacy funding</li>
            <li>Require evidence of quality, equity, and access components</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
        <h4>3. Use Morocco as Regional Model</h4>
        <ul>
            <li>Replicate accelerated approach (10-year timeline)</li>
            <li>Transfer technical expertise to Sudan when stable</li>
            <li>Scale to new Abraham Accords partners (Saudi Arabia, Qatar)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # For Government Partners
    st.subheader("For Government Partners")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h4>Morocco</h4>
            <ul>
                <li>Continue national momentum</li>
                <li>Prioritize rural regions</li>
                <li>Accept $175.7M total allocation</li>
                <li>Accelerate to 90%+ by 2029</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
            <h4>Sudan</h4>
            <ul>
                <li>Accept conditional funding</li>
                <li>Protect humanitarian education</li>
                <li>Collaborate with UN/NGOs</li>
                <li>Provide security transparency</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Expected Outcomes
    st.subheader("Expected Outcomes by 2030")
    
    outcomes_df = pd.DataFrame({
        'Outcome': [
            '4 of 5 countries achieve SDG 4',
            '27.1M lives improved',
            'Regional literacy rate',
            'Economic ROI',
            'Gender parity achieved'
        ],
        'Target': [
            '80% success rate',
            'Focus on 14.7M women/girls',
            '82.4% (up from 76.1%)',
            '$6.65-9.5 billion',
            'Israel, UAE, Bahrain, Morocco'
        ]
    })
    
    st.dataframe(outcomes_df, use_container_width=True, hide_index=True)
    
    # Call to Action
    st.markdown("""
    <div class="insight-box">
        <h4>Call to Action</h4>
        <p>The Abraham Accords created a historic opportunity for regional cooperation. 
        Literacy is the foundation of that peace dividend.</p>
        <p><strong>We have:</strong> Rigorous assessment, proven model, evidence-based allocation, exceptional ROI, clear targets</p>
        <p><strong>We need:</strong> Immediate funding approval, political commitment, coordination, monitoring framework, conflict resolution</p>
        <p><strong>The data is clear. The strategy is sound. The time is now.</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # SDG 4 Alignment Section
    st.markdown("---")
    st.subheader("Alignment with UN Sustainable Development Goals")
    
    st.markdown("""
    This initiative directly advances **UN SDG 4: Quality Education**, specifically 
    **Target 4.6: Adult and Youth Literacy by 2030** (95% benchmark).
    """)
    
    # SDG Alignment Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("SDG Target", "4.6", "Adult Literacy")
    
    with col2:
        st.metric("2030 Benchmark", "95%", "Literacy rate")
    
    with col3:
        st.metric("Countries Achieving", "4 of 5", "80% success")
    
    with col4:
        st.metric("Regional Progress", "+6.3 pts", "By 2030")
    
    st.markdown("""
    **Our framework operationalizes all five SDG 4 pillars:**
    
    1. **Equity:** Gender Parity (25% of AALNI) + Rural-Urban Gap (20%)
    2. **Quality:** Learning outcomes prioritized—Secondary Enrollment is #1 predictor (26.3%)
    3. **Inclusion:** Out-of-School Children (12.8%) + Conflict adjustment for refugees
    4. **Lifelong Learning:** Multi-generational spillover effects ($800M ROI component)
    5. **Sustainable Financing:** Evidence-based allocation with 700-1000% ROI
    
    **Cross-cutting SDG impact:** Literacy accelerates progress on SDGs 1 (poverty), 3 (health), 
    5 (gender), 8 (growth), 10 (inequality), and 16 (peace).
    """)
    
    # Talking Points for Different Audiences
    st.markdown("---")
    st.subheader("Tailored Messaging by Stakeholder Group")
    
    tab1, tab2, tab3 = st.tabs(["UN & Multilateral", "Government Partners", "Private Funders"])
    
    with tab1:
        st.markdown("""
        **For UN Agencies & Multilateral Organizations:**
        
        **Key Messages:**
        - First regional literacy framework aligned with SDG 4 Target 4.6
        - Evidence-based allocation removes politics from funding decisions
        - Addresses all 5 SDG 4 pillars (equity, quality, inclusion, lifelong learning, financing)
        - Morocco validates that accelerated progress is possible (10-year model vs 49-year UAE model)
        - Creates replicable blueprint for other regional partnerships (African Union, ASEAN, etc.)
        
        **Data Points:**
        - 27.1 million lives impacted (54% women and girls)
        - 80% success rate (4 of 5 countries achieve SDG 4 by 2030)
        - $6.65-9.5B economic return (700-1000% ROI)
        - Regional literacy: 76.1% → 82.4% (+6.3 points by 2030)
        
        **Ask:**
        - Endorse AALNI as model framework for regional SDG 4 initiatives
        - Facilitate knowledge transfer to other regions
        - Include in SDG 4 progress reports as case study
        """)
    
    with tab2:
        st.markdown("""
        **For Government Partners (Morocco, Sudan, Israel, UAE, Bahrain):**
        
        **Key Messages:**
        - Literacy is the foundation of the Abraham Accords peace dividend
        - Evidence-based allocation ensures fair, transparent funding distribution
        - High performers (Israel, UAE, Bahrain) serve as regional mentors
        - Morocco demonstrates rapid progress model ($311M → +19.1 points in 10 years)
        - Sudan receives conflict-adjusted support with phased, conditional approach
        
        **Country-Specific Asks:**
        - **Morocco:** Accept $175.7M total, prioritize rural acceleration
        - **Sudan:** Accept conditional $755M, ensure humanitarian access
        - **High Performers:** Share best practices, provide technical assistance
        
        **Mutual Benefits:**
        - Regional knowledge sharing strengthens all nations
        - Success stories enhance international reputation
        - Economic returns benefit entire region ($6.65-9.5B)
        """)
    
    with tab3:
        st.markdown("""
        **For Private Foundations & Impact Investors:**
        
        **Key Messages:**
        - **Highest ROI in development:** 700-1000% return over 10 years
        - **Proven model:** Morocco's $311M investment delivered measurable results
        - **Evidence-based:** Random Forest model (R²=0.972) identifies success factors
        - **Cost-effective:** $1.62 per person per point (Morocco benchmark)
        - **Scalable:** AALNI framework applicable to other regions
        
        **Investment Thesis:**
        - Direct productivity gains: $4.2B (literate workers earn 15-25% more)
        - Health improvements: $1.5B (literate mothers → healthier children)
        - Reduced conflict: $950M (education mitigates extremism)
        - Spillover effects: $800M (inter-generational benefits)
        
        **Risk Mitigation:**
        - Diversified portfolio (5 countries, 80% success rate)
        - Conflict-adjusted (Sudan's 3× multiplier accounts for reality)
        - Phased approach (conditional funding based on security)
        - Reallocation mechanism (Sudan funds redirect if needed)
        
        **Impact Metrics:**
        - Lives improved: 27.1M (14.7M women/girls)
        - Countries achieving SDG 4: 4 of 5 by 2030
        - Gender parity: Closes 17.4-point gap (Sudan)
        - Regional literacy: +6.3 points by 2030
        """)
    
    # Implementation Roadmap
    st.markdown("---")
    st.subheader("Implementation Roadmap with SDG Milestones")
    
    roadmap = pd.DataFrame({
        'Year': ['2026', '2027', '2028', '2029', '2030'],
        'Investment': ['$317M', '$317M', '$316M', 'Monitor', 'Evaluate'],
        'Regional_Literacy': ['76.5%', '78.2%', '80.8%', '81.5%', '82.4%'],
        'SDG_Progress': [
            'Baseline + 0.4 pts',
            '+2.1 pts (on track)',
            '+4.7 pts (accelerating)',
            '+5.4 pts (final push)',
            '+6.3 pts (target achieved)'
        ],
        'Key_Milestones': [
            'Establish coordination office\n500 schools built',
            'Mid-term evaluation\n1.2M students enrolled',
            'All programs at scale\nKnowledge exchange',
            'Saudi/Qatar expansion prep\nSustainability planning',
            'Final assessment\nTransition to national budgets'
        ]
    })
    
    st.table(roadmap)
    
    # Final Call to Action
    st.markdown("""
    <div class="success-box">
        <h4>The Abraham Accords Advantage</h4>
        <p>This initiative transforms peace agreements into measurable human development. By aligning 
        regional cooperation with UN SDG 4, we create a blueprint for literacy progress that:</p>
        <ul>
            <li>Prioritizes evidence over politics (AALNI formula)</li>
            <li>Accounts for real-world challenges (conflict multiplier)</li>
            <li>Delivers exceptional returns (700-1000% ROI)</li>
            <li>Creates regional knowledge sharing (mentor-learner model)</li>
            <li>Scales globally (replicable framework)</li>
        </ul>
        <p><strong>This isn't just about literacy—it's about proving that peace dividends can be 
        measured, optimized, and replicated.</strong></p>
    </div>
    """, unsafe_allow_html=True)

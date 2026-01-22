"""
Page rendering functions for Abraham Accords Literacy Dashboard
Updated with conflict-realistic framework and revised calculations
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def render_page(page, aalni_data, morocco_timeline, cost_effectiveness, 
                feature_importance, projections_2030, sudan_conflict):
    """Route to appropriate page renderer"""
    
    if page == "Executive Summary":
        render_executive_summary(aalni_data, projections_2030)
    elif page == "AALNI Rankings":
        render_aalni_rankings(aalni_data)
    elif page == "Morocco Case Study":
        render_morocco_case_study(morocco_timeline, cost_effectiveness)
    elif page == "Sudan Conflict Analysis":
        render_sudan_analysis(sudan_conflict)
    elif page == "Cost-Effectiveness":
        render_cost_effectiveness(cost_effectiveness)
    elif page == "Feature Importance (88.9% Rule)":
        render_feature_importance(feature_importance)
    elif page == "2030 Projections":
        render_2030_projections(projections_2030)
    elif page == "Policy Recommendations":
        render_policy_recommendations(aalni_data, projections_2030)

# ============================================================================
# EXECUTIVE SUMMARY
# ============================================================================
def render_executive_summary(aalni_data, projections_2030):
    st.header("Executive Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Illiterate", "27.1M", "Across 5 nations")
    with col2:
        st.metric("Women & Girls", "14.7M", "54% of total")
    with col3:
        st.metric("Phase 1 Budget", "$950M", "73% funded")
    with col4:
        st.metric("Phase 2 Need", "$357.5M", "Contingent")
    
    st.markdown("---")
    
    # Key Findings
    st.subheader("Key Findings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
        <h4>Morocco's Proven Model</h4>
        <ul>
            <li><strong>$310.9M investment</strong> (2014-2024)</li>
            <li><strong>8.46M beneficiaries</strong> reached</li>
            <li><strong>19.8-point improvement</strong> achieved</li>
            <li><strong>$1.86 per person per point</strong> efficiency</li>
            <li><strong>43.8% penetration</strong> of illiterate population</li>
            <li><strong>Validated:</strong> p<0.0001, R²=0.846</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
        <h4>Sudan's Critical Challenge</h4>
        <ul>
            <li><strong>3.7-point decline</strong> during 2014-2024 conflict</li>
            <li><strong>54.1% projection</strong> by 2030 without intervention</li>
            <li><strong>16.23M illiterate adults</strong> (43% of population)</li>
            <li><strong>Phase 1:</strong> $700M for 5.1M in accessible areas</li>
            <li><strong>Phase 2:</strong> $267M systemic transformation (peace required)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # The 88.9% Rule
    st.subheader("The 88.9% Rule: What Really Drives Literacy")
    
    st.markdown("""
    <div class="insight-box">
    <p><strong>Breakthrough Finding:</strong> Random Forest analysis reveals <strong>how you spend matters 50× more than how much you spend</strong></p>
    <p>Top 5 systemic factors explain <strong>88.9%</strong> of literacy outcomes, while investment amount ranks #10 at only <strong>1.6%</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Success Scenarios
    st.subheader("2030 Success Scenarios")
    
    scenario_data = pd.DataFrame({
        'Scenario': ['Phase 1 Only\n(No Sudan Peace)', 'Phase 1 + Phase 2\n(Peace by 2027)', 'Best Case\n(Early Peace)'],
        'Countries_Achieving_SDG': [3, 4, 5],
        'Success_Rate': [60, 80, 100],
        'Sudan_Outcome': ['57-60%\n(Stabilized)', '85-90%\n(Transformed)', '90-95%\n(Near SDG)'],
        'Total_Investment': ['$950M', '$1,307.5M', '$1,307.5M+']
    })
    
    st.dataframe(scenario_data, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ROI Summary
    st.subheader("Return on Investment")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Conservative ROI", "$9.1B", "700% return")
    with col2:
        st.metric("Optimistic ROI", "$13.0B", "1000% return")
    with col3:
        st.metric("Payback Period", "3-4 years", "Rapid return")

# ============================================================================
# AALNI RANKINGS
# ============================================================================
def render_aalni_rankings(aalni_data):
    st.header("Abraham Accords Literacy Need Index (AALNI)")
    
    st.markdown("""
    The AALNI is the first standardized regional literacy assessment framework, combining:
    - **Baseline Gap** (30%): Distance from 95% SDG target
    - **Gender Disparity** (25%): Gender parity index gaps
    - **Rural-Urban Divide** (20%): Geographic inequality
    - **Economic Constraint** (15%): Poverty rates
    - **Quality Deficit** (10%): Learning quality gaps
    - **Conflict Multiplier**: 1.0× (stable) to 3.0× (severe conflict)
    """)
    
    # AALNI Scores Chart
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=aalni_data['Country'],
        y=aalni_data['AALNI_Score'],
        marker_color=['#ef4444', '#f59e0b', '#10b981', '#10b981', '#10b981'],
        text=aalni_data['AALNI_Score'].round(1),
        textposition='outside'
    ))
    
    fig.update_layout(
        title="AALNI Vulnerability Scores (Higher = Greater Need)",
        xaxis_title="Country",
        yaxis_title="AALNI Score",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Phase 1 Allocation
    st.subheader("Phase 1 Budget Allocation ($950M)")
    
    fig2 = go.Figure(data=[go.Pie(
        labels=aalni_data['Country'],
        values=aalni_data['Phase_1_Allocation_M'],
        hole=0.3,
        marker_colors=['#ef4444', '#f59e0b', '#3b82f6', '#3b82f6', '#3b82f6']
    )])
    
    fig2.update_layout(title="Phase 1 Allocation by Country", height=400)
    st.plotly_chart(fig2, use_container_width=True)
    
    # Detailed Table
    st.subheader("Detailed Allocation Breakdown")
    
    allocation_table = aalni_data[['Country', 'AALNI_Score', 'Phase_1_Allocation_M', 
                                   'Phase_2_Allocation_M', 'Total_Need_M', 'Phase_1_Percent']].copy()
    allocation_table.columns = ['Country', 'AALNI Score', 'Phase 1 ($M)', 
                                'Phase 2 ($M)', 'Total Need ($M)', 'Phase 1 Coverage (%)']
    
    st.dataframe(allocation_table, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="insight-box">
    <strong>Key Insight:</strong> Sudan receives 72.4% of Phase 1 funding ($700M of $967M total need) 
    due to extreme vulnerability (AALNI score 115.7) and 3× conflict multiplier. Phase 2 ($267M) 
    contingent on improved stability for systemic transformation.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# MOROCCO CASE STUDY
# ============================================================================
def render_morocco_case_study(morocco_timeline, cost_effectiveness):
    st.header("Morocco: Validated Success Model")
    
    st.markdown("""
    Morocco's National Literacy Program (2014-2024) provides the empirical foundation 
    for the Abraham Accords regional investment framework.
    """)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Investment", "$310.9M", "10 years")
    with col2:
        st.metric("Beneficiaries", "8.46M", "43.8% penetration")
    with col3:
        st.metric("Improvement", "+19.8 points", "52.3% → 72.1%")
    with col4:
        st.metric("Efficiency", "$1.86", "per person per point")
    
    # Timeline Chart
    st.subheader("Morocco Literacy Timeline (2008-2030)")
    
    fig = go.Figure()
    
    # Split into actual and projected
    actual = morocco_timeline[morocco_timeline['Type'] == 'Actual']
    projected = morocco_timeline[morocco_timeline['Type'] == 'Projected']
    
    fig.add_trace(go.Scatter(
        x=actual['Year'],
        y=actual['Literacy_Rate'],
        mode='lines+markers',
        name='Actual',
        line=dict(color='#3b82f6', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=projected['Year'],
        y=projected['Literacy_Rate'],
        mode='lines+markers',
        name='Projected (Phase 1)',
        line=dict(color='#10b981', width=3, dash='dash'),
        marker=dict(size=8)
    ))
    
    # Add SDG target line
    fig.add_hline(y=95, line_dash="dot", line_color="gold", 
                  annotation_text="SDG 4 Target (95%)")
    
    # Add intervention start marker
    fig.add_vline(x=2014, line_dash="dash", line_color="red",
                  annotation_text="Intervention Start")
    
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Adult Literacy Rate (%)",
        height=500,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="success-box">
    <h4>Statistical Validation</h4>
    <ul>
        <li><strong>Difference-in-Differences:</strong> p<0.0001 (highly significant)</li>
        <li><strong>R² = 0.846:</strong> 84.6% of variance explained</li>
        <li><strong>Annual improvement:</strong> +2.12 percentage points during intervention</li>
        <li><strong>Counterfactual:</strong> +1.35 points/year natural trend</li>
        <li><strong>Treatment effect:</strong> +0.77 additional points/year attributable to program</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Phase 1 Projection
    st.subheader("Morocco Phase 1 Outcome (2024-2028)")
    
    st.markdown("""
    **Investment:** $135.3M (100% of evidence-based need)
    
    **Target:** Achieve 95% SDG 4 by 2028 (2 years ahead of 2030 deadline)
    
    **Strategy:**
    - National program continuation: $90M
    - Rural expansion (address 25.8-point urban-rural gap): $30M
    - Gender equity programs (close remaining 19% GPI gap): $15M
    
    **Expected Outcome:** Morocco becomes regional proof-of-concept, demonstrating 
    that systematic, evidence-based investment achieves SDG 4 targets.
    """)

# ============================================================================
# SUDAN CONFLICT ANALYSIS
# ============================================================================
def render_sudan_analysis(sudan_conflict):
    st.header("Sudan: Conflict-Contingent Strategy")
    
    st.markdown("""
    <div class="warning-box">
    <h4>Critical Finding: Literacy Cannot Improve During Active Conflict</h4>
    <p><strong>Empirical evidence from dataset:</strong> Literacy declined 3.7 percentage points 
    during 2014-2024 conflict period (60.7% → 57.0%)</p>
    <p><strong>Forecast without intervention:</strong> Continued decline to 54.1% by 2030</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Conflict Impact Chart
    fig = go.Figure()
    
    # Literacy rate (left y-axis)
    fig.add_trace(go.Scatter(
        x=sudan_conflict['Year'],
        y=sudan_conflict['Literacy_Rate'],
        name='Literacy Rate',
        mode='lines+markers',
        line=dict(color='#3b82f6', width=3),
        yaxis='y'
    ))
    
    # Conflict intensity (right y-axis)
    fig.add_trace(go.Scatter(
        x=sudan_conflict['Year'],
        y=sudan_conflict['Conflict_Intensity'],
        name='Conflict Intensity',
        mode='lines+markers',
        line=dict(color='#ef4444', width=3),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title="Sudan: Literacy Decline Correlates with Conflict Escalation",
        xaxis_title="Year",
        yaxis=dict(
            title="Literacy Rate (%)",
            titlefont=dict(color='#3b82f6'),
            tickfont=dict(color='#3b82f6'),
            range=[50, 65]
        ),
        yaxis2=dict(
            title="Conflict Intensity (0-10 scale)",
            titlefont=dict(color='#ef4444'),
            tickfont=dict(color='#ef4444'),
            overlaying='y',
            side='right',
            range=[0, 10]
        ),
        height=500,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Two-Phase Strategy
    st.subheader("Sudan's Dual-Timeline Strategy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
        <h4>Phase 1 (Years 1-3): $700M</h4>
        <p><strong>Conflict-Resilient Foundation</strong></p>
        <ul>
            <li><strong>Target:</strong> 5.1M beneficiaries (72% of goal)</li>
            <li><strong>Focus:</strong> Accessible populations only
                <ul>
                    <li>IDP camps with UN/NGO access</li>
                    <li>Stable regions (Port Sudan, secure areas)</li>
                    <li>Cross-border refugee programs</li>
                </ul>
            </li>
            <li><strong>Expected Outcome:</strong> Stabilize at 57-60% (prevent decline to 54.1%)</li>
            <li><strong>Impact:</strong> 5-10 point gains in stable zones</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
        <h4>Phase 2 (Years 4-6): $267M</h4>
        <p><strong>Systemic Transformation (Contingent)</strong></p>
        <ul>
            <li><strong>Triggers:</strong>
                <ul>
                    <li>Conflict severity ≤ 2.0 (improved stability)</li>
                    <li>Phase 1 demonstrates 5-10 point gains</li>
                    <li>$357.5M donor commitments secured</li>
                </ul>
            </li>
            <li><strong>Investments:</strong>
                <ul>
                    <li>Secondary education infrastructure: $150M</li>
                    <li>Comprehensive gender programs: $67M</li>
                    <li>Rural infrastructure: $30M</li>
                    <li>Remaining 2.0M beneficiaries: $20M</li>
                </ul>
            </li>
            <li><strong>Expected Outcome:</strong> 85-90% literacy (substantial progress)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # External Context
    st.subheader("External Validation")
    
    st.markdown("""
    **Dataset observation** (primary evidence): 3.7-point decline during 2014-2024 conflict
    
    **External reports** (validation):
    - UNICEF (2023): 2,400+ schools destroyed or damaged in conflict zones
    - UNESCO (2024): Approximately 15,000 teachers displaced
    - World Bank (2023): 3.5M children out of school due to conflict
    
    **Precedent validation:**
    - Afghanistan (2002-2015): Emergency education during conflict → rapid transformation post-conflict
    - Rwanda (1994-2010): Humanitarian response → 98% enrollment within 10 years of peace
    - Colombia (2000-2016): Mobile schools during insurgency → full expansion after 2016 peace agreement
    """)

# ============================================================================
# COST-EFFECTIVENESS
# ============================================================================
def render_cost_effectiveness(cost_effectiveness):
    st.header("Cost-Effectiveness Analysis")
    
    st.markdown("""
    Comparative analysis of literacy interventions across the Abraham Accords region.
    Morocco's model ranks #2 globally for optimal speed-to-cost ratio.
    """)
    
    # Cost per point comparison
    fig = go.Figure(data=[go.Bar(
        x=cost_effectiveness['Program'],
        y=cost_effectiveness['Cost_Per_Point'],
        text=cost_effectiveness['Cost_Per_Point'].round(2),
        textposition='outside',
        marker_color=['#10b981', '#3b82f6', '#f59e0b', '#ef4444', '#991b1b']
    )])
    
    fig.update_layout(
        title="Cost Efficiency: $ Per Percentage Point Improvement",
        xaxis_title="Program",
        yaxis_title="Cost per Point ($)",
        yaxis_type="log",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Detailed comparison table
    st.subheader("Detailed Program Comparison")
    
    comparison_table = cost_effectiveness.copy()
    comparison_table = comparison_table.sort_values('Cost_Per_Point')
    comparison_table['Rank'] = range(1, len(comparison_table) + 1)
    
    comparison_table = comparison_table[['Rank', 'Program', 'Country', 'Cost_Per_Point', 
                                        'Literacy_Improvement', 'Duration_Years', 
                                        'Cost_Per_Person', 'Beneficiaries_M']]
    
    comparison_table.columns = ['Rank', 'Program', 'Country', '$/Point', 
                                'Improvement (pts)', 'Duration (yrs)', 
                                '$/Person', 'Beneficiaries (M)']
    
    st.dataframe(comparison_table, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>Why Morocco's Model is Optimal for Regional Scale-Up:</h4>
    <ul>
        <li><strong>UAE Compulsory Education</strong> ($0.53/point): Cheapest but 49 years duration - too slow for 2030 SDG deadline</li>
        <li><strong>Morocco National Program</strong> ($1.86/point): 3.5× more expensive than UAE BUT 4.9× faster (10 vs 49 years)</li>
        <li><strong>Speed-to-Cost Ratio:</strong> Morocco achieves urgent results at reasonable cost</li>
        <li><strong>Scale Proven:</strong> 8.46M beneficiaries demonstrates replicability</li>
        <li><strong>Statistical Validation:</strong> p<0.0001, R²=0.846 confirms reliability</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# FEATURE IMPORTANCE (88.9% RULE)
# ============================================================================
def render_feature_importance(feature_importance):
    st.header("The 88.9% Rule: What Really Drives Literacy")
    
    st.markdown("""
    <div class="success-box">
    <h3>Breakthrough Finding from Random Forest Analysis (R²=0.972)</h3>
    <p><strong>Top 5 systemic factors explain 88.9% of literacy outcomes.</strong></p>
    <p><strong>Investment amount ranks #9 at only 1.6%.</strong></p>
    <p><strong>Conclusion: HOW you spend matters 50× more than HOW MUCH you spend.</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature importance chart - reverse order so highest is at top
    feature_importance_sorted = feature_importance.iloc[::-1].copy()
    
    fig = go.Figure(data=[go.Bar(
        y=feature_importance_sorted['Feature'],
        x=feature_importance_sorted['Importance'],
        orientation='h',
        text=feature_importance_sorted['Importance'].round(1),
        textposition='outside',
        marker_color=['#10b981' if cat == 'Systemic' else '#3b82f6' if cat == 'Infrastructure' 
                     else '#f59e0b' if cat == 'Temporal' else '#64748b' if cat == 'Context'
                     else '#ef4444' for cat in feature_importance_sorted['Category']]
    )])
    
    fig.update_layout(
        title="Random Forest Feature Importance (%)",
        xaxis_title="Importance (%)",
        yaxis_title="Feature",
        height=500,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Top 5 Breakdown
    st.subheader("The Top 5: Combined 88.9% Explanatory Power")
    
    top_5 = feature_importance.head(5).copy()
    top_5['Investment_Priority'] = [
        'Build/rebuild secondary schools in conflict-affected areas',
        'Girls education programs; close 17.4-point gender gap in Sudan',
        'Teacher training; learning quality assessment systems',
        'Rural school construction; transportation infrastructure',
        'Enrollment drives; address barriers keeping children out of school'
    ]
    
    for idx, row in top_5.iterrows():
        st.markdown(f"""
        <div class="metric-card">
        <h4>#{idx+1}: {row['Feature'].replace(chr(10), ' ')} - {row['Importance']}%</h4>
        <p><strong>Investment Priority:</strong> {row['Investment_Priority']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Policy Implications
    st.subheader("Policy Implications")
    
    st.markdown("""
    **Traditional Approach (Wrong):**
    - "We need more money for literacy programs"
    - Focuses on budget size
    - Ignores systemic barriers
    
    **Evidence-Based Approach (Correct):**
    - "We need to address secondary enrollment, gender parity, learning quality, rural access, and out-of-school children"
    - Focuses on systemic factors that explain 88.9% of outcomes
    - Investment amount is implementation tool, not primary driver
    
    **This is why Sudan requires different strategies:**
    - **During conflict (Phase 1):** Cannot address systemic factors at scale → Focus on accessible populations
    - **Post-conflict (Phase 2):** Can implement systemic transformation → Secondary schools, gender programs, rural infrastructure
    """)

# ============================================================================
# 2030 PROJECTIONS
# ============================================================================
def render_2030_projections(projections_2030):
    st.header("2030 SDG 4 Projections: Scenario Analysis")
    
    st.markdown("""
    Prophet time-series forecasting with scenario-based outcomes for Sudan.
    """)
    
    # Create visualization showing all scenarios
    fig = go.Figure()
    
    # High performers (baseline scenario)
    high_performers = projections_2030[projections_2030['Scenario'] == 'Baseline']
    fig.add_trace(go.Bar(
        name='High Performers',
        x=high_performers['Country'],
        y=high_performers['Projected_2030'],
        marker_color='#10b981',
        text=high_performers['Projected_2030'].round(1),
        textposition='outside'
    ))
    
    # Morocco
    morocco = projections_2030[projections_2030['Country'] == 'Morocco']
    fig.add_trace(go.Bar(
        name='Morocco (Phase 1)',
        x=['Morocco'],
        y=morocco['Projected_2030'].values,
        marker_color='#3b82f6',
        text=morocco['Projected_2030'].round(1),
        textposition='outside'
    ))
    
    # Sudan scenarios
    sudan_phase1 = projections_2030[(projections_2030['Country'] == 'Sudan') & 
                                    (projections_2030['Scenario'] == 'Phase 1 Only')]
    sudan_phase2 = projections_2030[(projections_2030['Country'] == 'Sudan') & 
                                    (projections_2030['Scenario'] == 'Phase 1 + Phase 2')]
    
    fig.add_trace(go.Bar(
        name='Sudan Phase 1 Only',
        x=['Sudan (Phase 1)'],
        y=sudan_phase1['Projected_2030'].values,
        marker_color='#f59e0b',
        text=sudan_phase1['Projected_2030'].round(1),
        textposition='outside'
    ))
    
    fig.add_trace(go.Bar(
        name='Sudan Phase 1+2',
        x=['Sudan (Phase 2)'],
        y=sudan_phase2['Projected_2030'].values,
        marker_color='#10b981',
        text=sudan_phase2['Projected_2030'].round(1),
        textposition='outside'
    ))
    
    fig.add_hline(y=95, line_dash="dash", line_color="gold",
                  annotation_text="SDG 4 Target (95%)")
    
    fig.update_layout(
        title="2030 Literacy Projections by Scenario",
        yaxis_title="Projected Literacy Rate (%)",
        barmode='group',
        height=500,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Scenario details
    st.subheader("Detailed Scenario Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="warning-box">
        <h4>Base Case: Phase 1 Only</h4>
        <p><strong>Assumption:</strong> No Sudan peace</p>
        <p><strong>Investment:</strong> $950M</p>
        <p><strong>Outcomes:</strong></p>
        <ul>
            <li>Morocco: 95% (SDG achieved)</li>
            <li>High performers: 97-99% (maintained)</li>
            <li>Sudan: 57-60% (stabilized)</li>
        </ul>
        <p><strong>Success Rate: 3 of 5 (60%)</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
        <h4>Optimistic: Phase 1 + Phase 2</h4>
        <p><strong>Assumption:</strong> Sudan peace by 2027</p>
        <p><strong>Investment:</strong> $1,307.5M</p>
        <p><strong>Outcomes:</strong></p>
        <ul>
            <li>Morocco: 95% (SDG achieved)</li>
            <li>High performers: 97-99% (maintained)</li>
            <li>Sudan: 85-90% (substantial progress)</li>
        </ul>
        <p><strong>Success Rate: 4 of 5 (80%)</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="success-box">
        <h4>Best Case: Early Peace</h4>
        <p><strong>Assumption:</strong> Sudan peace by 2026</p>
        <p><strong>Investment:</strong> $1,307.5M+</p>
        <p><strong>Outcomes:</strong></p>
        <ul>
            <li>Morocco: 95% (SDG achieved)</li>
            <li>High performers: 97-99% (maintained)</li>
            <li>Sudan: 90-95% (near SDG by 2032)</li>
        </ul>
        <p><strong>Success Rate: 5 of 5 by 2032 (100%)</strong></p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# POLICY RECOMMENDATIONS
# ============================================================================
def render_policy_recommendations(aalni_data, projections_2030):
    st.header("Evidence-Based Policy Recommendations")
    
    st.markdown("""
    Strategic guidance for donors, governments, and development partners based on 
    comprehensive data analysis and validated interventions.
    """)
    
    # For Donors
    st.subheader("For International Donors")
    
    st.markdown("""
    <div class="success-box">
    <h4>Phase 1 Immediate Deployment ($950M)</h4>
    <ul>
        <li><strong>Morocco:</strong> $135.3M → SDG 4 achievement by 2028</li>
        <li><strong>High Performers:</strong> $35M → Excellence maintenance</li>
        <li><strong>Sudan:</strong> $700M → Conflict-resilient programs</li>
        <li><strong>M&E Infrastructure:</strong> $80M → Core monitoring</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>Phase 2 Conditional Funding ($357.5M)</h4>
    <ul>
        <li><strong>Trigger #1:</strong> Phase 1 demonstrates 5-10 point gains</li>
        <li><strong>Trigger #2:</strong> Sudan conflict severity ≤ 2.0</li>
        <li><strong>Trigger #3:</strong> M&E systems operational</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # For Governments
    st.subheader("For National Governments")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Morocco:**
        - Accept $135.3M allocation
        - Prioritize rural expansion
        - Close gender parity gap
        - Target: SDG 4 by 2028
        """)
    
    with col2:
        st.markdown("""
        **Sudan:**
        - Accept $700M Phase 1
        - Focus on accessible populations
        - Build Phase 2 readiness
        - Engage in ceasefire negotiations
        """)
    
    # For Development Community
    st.subheader("For Development Community")
    
    st.markdown("""
    **Adopt the AALNI Framework:**
    - First standardized regional literacy tool
    - Evidence-based, transparent, conflict-adjusted
    - Replicable across any multi-country initiative
    
    **Focus on the 88.9% Rule:**
    - Invest in systemic factors, not just budgets
    - Secondary enrollment, gender parity, learning quality, rural access
    
    **Learn from Precedents:**
    - Afghanistan, Rwanda, Colombia demonstrate phased approach works
    - Humanitarian response during conflict → Systemic transformation post-conflict
    """)
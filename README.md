# Abraham Accords Literacy Initiative

**Mapping Literacy for Humanity: Evidence-Based Investment Strategy**

[![Interactive Dashboard](https://img.shields.io/badge/Dashboard-Live-blue)](https://huggingface.co/spaces/YOUR_USERNAME/abraham-accords-dashboard)
[![View Analysis](https://img.shields.io/badge/Notebook-nbviewer-orange)](https://nbviewer.org/github/vcngeno/abraham-accords-mapping-literacy-analysis/blob/main/notebooks/Mapping_Literacy_for_the_Abraham_Accords_Nations.ipynb)

> **Note:** GitHub may timeout on large notebooks with embedded visualizations. Use nbviewer for best experience.


---

## Project Overview

Comprehensive data science analysis mapping literacy needs across 27.1 million people in five Abraham Accords nations (Morocco, Sudan, Israel, UAE, Bahrain). Develops evidence-based investment strategy for achieving UN Sustainable Development Goal 4 (95% literacy by 2030).

## Key Findings

### Morocco's Proven Model
- **$310.9M investment** (2014-2024) → **8.46M beneficiaries**
- **19.8-point improvement** (52.3% → 72.1%)
- **$1.86 per person per point** efficiency
- **Validated:** p<0.0001, R²=0.846

### Sudan's Critical Challenge
- **3.7-point decline** during 2014-2024 conflict period (60.7% → 57.0%)
- **Projected 54.1%** by 2030 without intervention
- **Two-phase strategy:** $700M conflict-resilient foundation + $267M systemic transformation (peace-contingent)

### The 88.9% Rule
**Breakthrough finding:** Top 5 systemic factors explain **88.9%** of literacy outcomes. Investment amount ranks #9 at only **1.6%**.

**HOW you spend matters 50× more than HOW MUCH you spend.**

### Investment Strategy

| Phase | Timeline | Budget | Coverage | Outcome |
|-------|----------|--------|----------|---------|
| **Phase 1** | Years 1-3 | $950M | 73% of need | 3 of 5 countries achieve SDG 4 |
| **Phase 2** | Years 4-6 | $357.5M | 27% of need | 4 of 5 countries achieve SDG 4 |
| **Total** | 3-6 years | **$1.3B** | 100% | 11.9M beneficiaries |

### Return on Investment
- **Conservative:** $9.1B (700% ROI)
- **Optimistic:** $13.0B (1000% ROI)
- **Payback period:** 3-4 years

---

## Repository Structure

```
abraham-accords-dashboard/
├── app.py                         # Streamlit dashboard main file
├── pages_content.py               # Dashboard page renderers
├── requirements.txt               # Python dependencies
├── data/                          # Raw and cleaned datasets
│   ├── abraham_accords_unified_dataset.csv
│   ├── aalni_scores_2024.csv
│   ├── cost_effectiveness_rankings.csv
│   └── ...
├── notebooks/                     # Jupyter analysis notebooks
├── visualizations/                # Charts and interactive maps
├── results/                       # Model outputs
└── docs/                          # Project documentation
```

---

## Deliverables

### 1. Abraham Accords Literacy Need Index (AALNI)
First standardized regional literacy framework combining:
- Baseline Gap (30%), Gender Disparity (25%), Rural-Urban Divide (20%)
- Economic Constraint (15%), Quality Deficit (10%)
- Conflict Multiplier (1.0× to 3.0×)

### 2. Interactive Dashboard
7-page Streamlit application featuring:
- Executive summary with scenario analysis
- AALNI vulnerability rankings
- Morocco validated success model
- Sudan conflict-contingent strategy
- Cost-effectiveness analysis
- Feature importance (88.9% Rule)
- 2030 SDG projections

### 3. Predictive Models

| Model | Purpose | Performance |
|-------|---------|-------------|
| **Difference-in-Differences** | Morocco impact validation | R²=0.846, p<0.0001 |
| **Random Forest** | Feature importance (88.9% Rule) | R²=0.972, MAE=2.22 pts |
| **Gamma GLM** | Cost prediction | Pseudo R²=0.832 |
| **Prophet** | 2030 forecasting | 95% confidence intervals |

### 4. Policy Recommendations
- **Donors:** Phase 1 immediate deployment + Phase 2 triggers
- **Governments:** Country-specific strategies (Morocco, Sudan)
- **Development community:** AALNI framework adoption

---

## Getting Started

### Prerequisites
```bash
Python 3.11+
Streamlit
Jupyter Notebook/Lab
```

### Installation

```bash
# Clone the repository
git clone https://github.com/vcngeno/abraham-accords-mapping-literacy-analysis.git
cd abraham-accords-mapping-literacy-analysis

# Install dependencies
pip install -r requirements.txt
```

### Run the Dashboard

```bash
streamlit run app.py
```

### Run the Analysis
```bash
jupyter lab
# Open notebooks/Mapping_Literacy_for_the_Abraham_Accords_Nations.ipynb
```

---

## Interactive Visualizations

View the live dashboard pages:
- **Executive Summary:** Key metrics and scenario analysis
- **AALNI Rankings:** Vulnerability scoring and budget allocation
- **Morocco Case Study:** Validated success model
- **Sudan Analysis:** Conflict impact and two-phase strategy
- **Cost-Effectiveness:** Comparative program analysis
- **88.9% Rule:** Feature importance breakdown
- **2030 Projections:** SDG 4 achievement scenarios

---

## Data Sources

- **UNESCO Institute for Statistics** - Adult literacy rates, gender parity
- **World Bank EdStats** - Education expenditure, enrollment
- **UNICEF** - Out-of-school children, conflict impact
- **National Statistics** - Country-specific program data
- **Morocco Court of Accounts** - Program evaluation reports

---

## Methodology Highlights

### Evidence-Based Investment Calculation

**Morocco's empirical model applied regionally:**

```
Target Beneficiaries = Illiterate Population × 43.8% penetration
Base Investment = Beneficiaries × 19.8 points × $1.86/point
Adjusted Investment = Base × Conflict Multiplier
Total Need = Sum(Country Investments) × 1.15 (infrastructure)
```

**Result:** $1,307.5M total evidence-based need

### The 88.9% Rule

**Top 5 systemic factors:**
1. Secondary Enrollment (26.3%)
2. Gender Parity (18.5%)
3. Learning Quality (16.7%)
4. Rural-Urban Gap (14.7%)
5. Out-of-School Children (12.8%)

**#9: Investment Amount (1.6%)**

---

## Key Results

### 2030 Projections by Scenario

| Scenario | Investment | Countries Achieving SDG | Sudan Outcome |
|----------|------------|------------------------|---------------|
| **Phase 1 Only** | $950M | 3 of 5 (60%) | 57-60% (stabilized) |
| **Phase 1 + Phase 2** | $1.3B | 4 of 5 (80%) | 85-90% (transformed) |
| **Best Case** | $1.3B+ | 5 of 5 (100%) | 90-95% (near SDG) |

---

## Contact

For questions about methodology, data, or collaboration opportunities, please open an issue or reach out directly.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Citation


```Ngeno, V. (2025). The Abraham Accords Nations Literacy Analysis: Mapping Literacy for Humanity
```

---

**Data-driven. Evidence-based. Achievable. The roadmap to regional literacy by 2030.**

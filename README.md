![Abraham Accords Literacy Analysis](docs/abraham_accords_banner.jpg)

# Abraham Accords Literacy Analysis
**Mapping Literacy for Humanity: Where Words Are Needed Most**

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Overview

Data science analysis identifying literacy gaps across Abraham Accords nations (Israel, UAE, Bahrain, Morocco, Sudan) in support of UN Sustainable Development Goal 4 (Quality Education).


## Key Findings

- **Morocco's $311M Investment:** Increased literacy from 47.7% to 72.1% (+24.4 points) with $1.62/point efficiency
- **Sudan Crisis:** Literacy projected to decline by 2.9 points due to conflict (AALNI score: 115.7)
- **Investment Impact:** Investment accounts for only 1.6% of literacy improvement; systemic factors (secondary education, gender equity, learning quality) drive 88.9% of results

## Deliverables

1. **Abraham Accords Literacy Need Index (AALNI)** - Composite vulnerability scoring
2. **Interactive Heat Maps** - 3 GIS visualizations (HTML)
3. **Predictive Models** - DiD Panel Regression, Gamma GLM, Random Forest, Prophet forecasting
4. **2030 SDG Projections** - Only 3/5 countries will achieve 95% literacy target
5. **Policy Brief** - $950M investment allocation with $735.6M optimization opportunity

## Repository Structure
```
abraham-accords-literacy-analysis/
├── data/                          # Raw and cleaned datasets (8 CSV files)
├── notebooks/                     # Jupyter notebook with complete analysis
├── visualizations/                # Charts and interactive maps (11 files)
├── results/                       # Model outputs and rankings
├── docs/                          # Project documentation
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Models & Methodology

| Model | Purpose | Performance |
|-------|---------|-------------|
| Difference-in-Differences | Morocco intervention impact | R² = 0.846, p < 0.0001 |
| Gamma GLM | Cost-effectiveness analysis | Pseudo R² = 0.832 |
| Random Forest | Feature importance | R² = 0.972, MAE = 2.22 points |
| Prophet | 2030 SDG forecasting | 95% confidence intervals |

## Getting Started

### Prerequisites
```bash
Python 3.13+
Jupyter Notebook/Lab
```

### Installation
```bash
# Clone the repository
git clone https://github.com/vcngeno/abraham-accords-literacy-analysis.git
cd abraham-accords-literacy-analysis

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter lab
```

### Run the Analysis
Open `notebooks/Mapping_Literacy_for_the_Abraham_Accords_Nations.ipynb` and run all cells.

## Interactive Visualizations

View the interactive heat maps:
- [Main Literacy Heat Map](visualizations/abraham_accords_literacy_heat_map.html)
- [Conflict Impact Map](visualizations/abraham_accords_conflict_impact_map.html)
- [Temporal Animation 2010-2024](visualizations/abraham_accords_temporal_heat_map.html)

## 📄 Data Sources

- UNESCO Institute for Statistics (UIS)
- World Bank Education Statistics
- Morocco Court of Accounts
- National Ministries of Education (5 countries)
- Academic literature (Oxford, WLF, The Conversation)

## Acknowledgments

This project was conducted as part of the Peblink Internship Project in partnership with:
- The Abraham Accords Educational Alliance
- World Literacy Foundation
- World Literacy Research Center

## Contact

**Vanessa Ngeno**  
Master of Science in Data Analytics & Visualization

## License

This project is licensed under the MIT License

## Citation

```
Ngeno, V. (2025). The Abraham Accords Nations Literacy Analysis: Mapping Literacy for Humanity
```

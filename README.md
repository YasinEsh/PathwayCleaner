# PathwayCleaner 🚀
PathwayCleaner is a Python-based tool designed to streamline and refine pathway enrichment analysis results. It identifies overlapping pathway terms based on shared genes, filters redundant entries, and visualizes the most statistically significant pathways for better interpretability

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)](CONTRIBUTING.md)

## Features
- Identifies overlapping pathway terms based on gene overlap (≥65% overlap).
- Retains the most statistically significant terms based on adjusted p-values.
- Generates a publication-ready visualization of the top 10 pathways.



## Example Output
Below is a comparison of pathway enrichment results before and after applying PathwayCleaner:

### Before Applying PathwayCleaner
Unreduced pathways visualization:<img width="548" alt="Unreduced" src="https://github.com/user-attachments/assets/9ed8a78e-ae89-4c8c-a04e-ccedfe33398e" />

### After Applying PathwayCleaner
Reduced pathways visualization:            <img width="404" alt="Reduced" src="https://github.com/user-attachments/assets/eab44d0a-b939-4dd1-8a7e-7094f1a0bdd7" />






## Requirements
- Python >= 3.*
- pandas
- matplotlib
- seaborn
Install the dependencies with:
```bash
pip install pandas matplotlib seaborn





# PathwayCleaner 🚀
PathwayCleaner is a Python-based tool designed to streamline and refine pathway enrichment analysis results. It identifies overlapping pathway terms based on shared genes, filters redundant entries, and visualizes the most statistically significant pathways for better interpretability.

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)](CONTRIBUTING.md)

## Features
- Identifies overlapping pathway terms based on gene overlap (≥65% overlap).
- Retains the most statistically significant terms based on adjusted p-values.
- Generates a publication-ready visualization of the top 10 pathways.

---

## Example Output
Below is a comparison of pathway enrichment results before and after applying PathwayCleaner:

### Before Applying PathwayCleaner

![Unreduced pathways visualization](path/to/image1.png)

<p align="center"><i>Unreduced pathways visualization</i></p>

---

### After Applying PathwayCleaner

![Reduced pathways visualization](path/to/image2.png)

<p align="center"><i>Reduced pathways visualization</i></p>

---

## Requirements
- Python >= 3.*
- pandas
- matplotlib
- seaborn

Install the dependencies with:
```bash
pip install pandas matplotlib seaborn

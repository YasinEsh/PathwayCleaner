<img width="548" alt="Unreduced" src="https://github.com/user-attachments/assets/520b6c8b-3e45-4db0-958a-7fbbd6223c54" /># PathwayCleaner 🚀
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
Unreduced pathways visualization:

![Unreduced Pathways](<img width="548" alt="Unreduced" src="https://github.com/user-attachments/assets/f0d4564d-de3e-400a-8e9d-05ad11b3d588" />
)

### After Applying PathwayCleaner
Reduced pathways visualization:

![Reduced Pathways](<img width="404" alt="Reduced" src="https://github.com/user-attachments/assets/87f889ee-d55d-486d-a199-922086158c47" />
)





## Requirements
- Python >= 3.*
- pandas
- matplotlib
- seaborn
Install the dependencies with:
```bash
pip install pandas matplotlib seaborn





import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Function to calculate overlap between two sets of genes
def calculate_overlap(genes1, genes2):
    set1, set2 = set(genes1.split(';')), set(genes2.split(';'))
    overlapping_genes = set1 & set2
    overlap_percentage = len(overlapping_genes) / min(len(set1), len(set2)) if min(len(set1), len(set2)) > 0 else 0
    return overlap_percentage >= 0.65, overlapping_genes, overlap_percentage

# Function to unify pathway terms based on gene overlap
def unify_terms(df):
    df_sorted = df.sort_values('Adjusted P-value').reset_index(drop=True)
    overlap_record = {}
    kept_terms = []

    for i, current_row in df_sorted.iterrows():
        should_keep = True
        to_remove = []

        for kept_index in list(kept_terms):
            kept_row = df_sorted.loc[kept_index]
            overlap, overlapping_genes, overlap_percentage = calculate_overlap(current_row['Genes'], kept_row['Genes'])
            comparison_key = f"{current_row['Term']} vs {kept_row['Term']}"
            overlap_record[comparison_key] = overlap_percentage * 100

            if overlap:
                if overlap_percentage == 1.0:
                    if current_row['Adjusted P-value'] < kept_row['Adjusted P-value']:
                        to_remove.append(kept_index)
                    else:
                        should_keep = False
                        break
                elif current_row['Adjusted P-value'] < kept_row['Adjusted P-value']:
                    to_remove.append(kept_index)
                else:
                    should_keep = False
                    break
        
        for idx in to_remove:
            kept_terms.remove(idx)
        
        if should_keep:
            kept_terms.append(i)

    final_df = df_sorted.loc[kept_terms].reset_index(drop=True)
    return final_df, overlap_record

# Main script for processing and visualization
if __name__ == "__main__":
    # Prompt user for file path
    file_path = input("Enter the full file path of the Reactome data file (e.g., 'Reactome_2022_table.txt'): ").strip()
    
    # Check if file exists
    if not os.path.isfile(file_path):
        print(f"Error: File not found at {file_path}. Please provide a valid file path.")
        exit(1)
    
    # Load the data
    try:
        data = pd.read_csv(file_path, delimiter='\t')
    except Exception as e:
        print(f"Error reading the file: {e}")
        exit(1)

    # Fill missing genes with empty strings
    data['Genes'] = data['Genes'].fillna('')

    # Extract the directory path
    directory_path = os.path.dirname(file_path)

    # Apply the unification process
    final_df, overlap_record = unify_terms(data)

    # Save the results
    final_df_path = os.path.join(directory_path, "Filtered_Reactome_2022_table.csv")
    overlap_record_path = os.path.join(directory_path, "Overlap_Record.txt")

    final_df.to_csv(final_df_path, index=False)

    with open(overlap_record_path, 'w') as file:
        for key, value in overlap_record.items():
            file.write(f"{key}: {value:.2f}%\n")

    print("Filtered dataframe saved to:", final_df_path)
    print("Overlap record saved to:", overlap_record_path)

    # Visualization
    # Load the filtered data
    filtered_data = final_df

    # OPTION 1: Static total protein count (e.g., Reactome database total)
    total_proteins_in_reactome = 137  # Replace this with the actual Reactome total if known

    # OPTION 2: Dynamic total protein count (based on the dataset being analyzed)
    total_proteins_in_analysis = filtered_data['Genes'].str.split(';').explode().nunique()

    # Choose the appropriate total (uncomment one)
    # total_proteins = total_proteins_in_reactome  # Static count
    total_proteins = total_proteins_in_analysis  # Dynamic count

    # Ensure the 'Genes' column is treated as strings and count the number of genes
    filtered_data['Gene_Count'] = filtered_data['Genes'].str.split(';').apply(len)

    # Calculate the percentage and add it as a new column
    filtered_data['percentage'] = (filtered_data['Gene_Count'] / total_proteins) * 100

    # Remove the suffix (R-HSA-######) from the 'Term' column
    filtered_data['Term'] = filtered_data['Term'].str.replace(r' R\.HSA\.\d+$', '', regex=True)

    # Sort the DataFrame by 'Adjusted P-value' in ascending order and select the top 10 terms
    top10_df = filtered_data.sort_values('Adjusted P-value').head(10)

    # Create the plot
    plt.figure(figsize=(6, 3))
    sns.barplot(
        data=top10_df,
        x='percentage',
        y='Term',
        hue='Adjusted P-value',
        palette=sns.color_palette(["#C9ADA7", "#4A4E69", "#22223B"]),
        dodge=False,
        alpha=0.8
    )

    # Customize the plot
    plt.xlabel("Percentage of Pathway Proteins in Dataset", fontsize=10)
    plt.ylabel("")
    plt.xlim(0, 30)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.legend(title="Adjusted P-value", fontsize=8, title_fontsize=9)
    plt.title("Top 10 Pathways by Adjusted P-value", fontsize=12)
    plt.grid(False)
    sns.despine()

    # Save the plot to a file
    plot_path = os.path.join(directory_path, "top10_pathways_plot.pdf")
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.show()

    print("Plot saved to:", plot_path)

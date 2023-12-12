# Load packages -----------------------------------------------------------

library(tidyverse)
library(corrplot)
library(caret)
library(igraph)
library(showtext)

# Load data ---------------------------------------------------------------
lucas <- read_csv("cleaned_2018_bk_fungi.csv")

# Select relevant columns for correlation analysis
chemical_vars <- c("P", "N", "K", "CaCO3", "pH_H2O", "pH_CaCl2", "OC")
physical_vars <- c("BD 0-10", "BD 10-20", "BD 0-20", "EC", "elevation")
biological_vars <- c("fungal_abundance", "fungal_OTU_counts")

# Combine all variables
all_vars <- c(chemical_vars, biological_vars, physical_vars)
lucas[all_vars] <- lapply(lucas[all_vars], function(x) as.numeric(as.character(x)))
lucas_complete <- na.omit(lucas[, all_vars])

# Calculate correlation matrix
correlation_matrix <- cor(lucas_complete[, all_vars])
print(correlation_matrix)

variable_order <- c("P", "N", "K", "CaCO3", "pH_H2O", "pH_CaCl2", "OC", "BD 0-10", "BD 10-20", "BD 0-20", "EC", "elevation", "fungal_abundance", "fungal_OTU_counts")

# Reorder the correlation matrix based on variable_order
ordered_matrix <- correlation_matrix[variable_order, variable_order]

label_colors <- c("#ff6633", "#ff6633", "#ff6633", "#ff6633", "#ff6633", "#ff6633", "#ff6633", "#4ddbff", "#4ddbff", "#4ddbff", "#4ddbff", "#4ddbff", "#39ac39", "#39ac39")

# Plot the reordered correlation matrix with values and colored labels
corrplot(
  ordered_matrix,
  method = "color",
  type = "upper",
  tl.col = label_colors,  # Specify colors for variable labels
  col = colorRampPalette(c("#639432", "#cccccc", "#8B572A"))(100),
  addCoef.col = "black",  # Color of the correlation values
  number.cex = 0.7  # Adjust the size of correlation values
  )

# Add custom legend
legend("topleft", legend = c("Chemical", "Physical", "Biological"),
       fill = c("#ff6633", "#4ddbff", "#39ac39"), title = "Variable Types")

# Create a scatter plot matrix
pairs(lucas_complete[, all_vars], main = "Scatter Plot Matrix")

variable_types <- rep(length(all_vars))


# Create a graph from the correlation matrix
correlation_graph <- graph.adjacency(correlation_matrix > 0.8, mode = "undirected", diag = FALSE)


plot(
  correlation_graph,
  layout = layout_with_fr(correlation_graph),
  vertex.label.cex = 0.8,
  main = "Network Plot of Highly Correlated Variables",
  vertex.color = "#cccccc",
  vertex.label.color = "black", 
  edge.width = E(correlation_graph)
)
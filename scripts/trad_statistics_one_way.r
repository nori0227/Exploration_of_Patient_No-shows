# Analysis for variance (1-way ANOVA) in R 

my_data <- read.csv('/cloud/project/output_noshow1_balanced_2022-11-16.csv')

#install packages
install.packages("dplyr")
library(dplyr)

if(!require(devtools)) install.packages("devtools")
devtools::install_github("kassambara/ggpubr")
library("ggpubr")

res.aov <- aov(patient_age ~ patient_gender, data = my_data)
summary(res.aov)
TukeyHSD(res.aov)

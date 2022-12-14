# Summary of 2_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: mse
- **max_depth**: 3
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True

## Optimized metric
rmse

## Training time

82.1 seconds

### Metric details:
| Metric   |         Score |
|:---------|--------------:|
| MAE      |   8.87349     |
| MSE      | 159.633       |
| RMSE     |  12.6346      |
| R2       |   0.597501    |
| MAPE     |   1.97625e+14 |



## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (patient_age_groupper <= 0.5) and (practice_id > 301251.5) and (id > 630153.0) then response: 37.76 | based on 43,883 samples

if (patient_age_groupper > 0.5) and (patient_age_groupper <= 1.5) and (patient_id > 99583.0) then response: 3.633 | based on 12,449 samples

if (patient_age_groupper > 0.5) and (patient_age_groupper > 1.5) and (id <= 623979.0) then response: 14.396 | based on 4,877 samples

if (patient_age_groupper > 0.5) and (patient_age_groupper <= 1.5) and (patient_id <= 99583.0) then response: 7.619 | based on 4,145 samples

if (patient_age_groupper <= 0.5) and (practice_id <= 301251.5) and (appointment_duration > 17.5) then response: 44.068 | based on 3,161 samples

if (patient_age_groupper <= 0.5) and (practice_id <= 301251.5) and (appointment_duration <= 17.5) then response: 56.702 | based on 3,045 samples

if (patient_age_groupper <= 0.5) and (practice_id > 301251.5) and (id <= 630153.0) then response: 19.955 | based on 1,889 samples

if (patient_age_groupper > 0.5) and (patient_age_groupper > 1.5) and (id > 623979.0) then response: 14.772 | based on 1,551 samples





## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold 1)
![SHAP Dependence from Fold 1](learner_fold_0_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions (Fold 1)
![SHAP worst decisions from fold 1](learner_fold_0_shap_worst_decisions.png)
### Top-10 Best decisions (Fold 1)
![SHAP best decisions from fold 1](learner_fold_0_shap_best_decisions.png)

[<< Go back](../README.md)

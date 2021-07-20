
# Employee Retention Model

• We know that larger companies contain more than thousand employees working for
them, so taking care of the needs and satisfaction of each employee is a challenging
task to do, it results in valuable and talented employees leave the company without
giving the proper reason.

• Employee churn is a major problem for many firms these days. Great talent is scarce,
hard to keep and in high demand.

• It uses the data of previous employees who have worked for the company and by
finding a pattern it predicts the retention in the form of yes or no.
## Dataset Discription

[Download Dataset](https://www.kaggle.com/gummulasrikanth/hr-employee-retention)

satisfaction_level: Level of satisfaction {0–1}.

❖ last_evaluationTime: Time since last performance evaluation (in years).

❖ number_project: Number of projects completed while at work.

❖ average_montly_hours: Average monthly hours at the workplace.

❖ time_spend_company: Number of years spent in the company.

❖ Work_accident: Whether the employee had a workplace accident.

❖ left: Whether the employee left the workplace or not {0, 1}.

❖ promotion_last_5years: Whether the employee was promoted in the last
five years.

❖ sales: Department the employee works for.

❖ salary: Relative level of salary {low, medium, high}
  
## Model Building & Evaluation

•I have used hyperparameter tuning and analyze the performance of the model by
applying different algorithms like Decision tree, Logistic regression and Random
forest.

• I have applied different parameters in this three model and we got 98 % accuracy
for Random Forest Classifier with parameters like n_estimators=28,
bootstrap=True, max_features='sqrt'

 • with used of Random Forest Classifier with above
 given fetures i am getting 99.15% accuracy.

## Screenshots

![App Screenshot](https://github.com/YashGoswami143/test/blob/main/ER1.PNG?raw=true)
![App Screenshot](https://github.com/YashGoswami143/test/blob/main/ER2.PNG?raw=true)
![App Screenshot](https://github.com/YashGoswami143/test/blob/main/ER3.PNG?raw=true)

  
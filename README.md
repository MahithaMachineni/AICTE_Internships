# AICTE_Internships
# **Model link** 
https://drive.google.com/file/d/1C8Z4luQ3dX4DLTDGaGrH5klNWs6VET1G/view?usp=drivesdk

---

# **Water Quality Prediction - RMS**

This project aims to predict multiple water quality parameters using machine learning techniques, specifically `MultiOutputRegressor` wrapped around a `RandomForestRegressor`. It was developed as part of a one-month **AICTE Virtual Internship sponsored by Shell in June 2025**.

---

## **Overview**

Access to clean water is a critical global concern. Accurate prediction of various water quality metrics can help in early detection of pollution and ensure timely intervention.

In this project, we:

- Collected and preprocessed real-world water quality datasets  
- Used supervised machine learning for multi-target regression  
- Built a pipeline using `MultiOutputRegressor` with `RandomForestRegressor`  
- Evaluated the model using appropriate regression metrics  

---

## **Technologies Used**

- **Python 3.12**
- **Pandas**, **NumPy** – Data handling  
- **Scikit-learn** – Machine learning model and evaluation  
- **Matplotlib**, **Seaborn** – Data visualization  
- **Jupyter Notebook** – Interactive experimentation  

---

## **Predicted Water Quality Parameters**

The model predicts multiple water quality parameters such as:

- **NH₄** (Ammonium)  
- **BOD₅ (BSK5)** – Biochemical Oxygen Demand  
- **Colloids**  
- **O₂** – Dissolved Oxygen  
- **NO₃** – Nitrate  
- **NO₂** – Nitrite  
- **SO₄** – Sulfate  
- **PO₄** – Phosphate  
- **CL** – Chloride  

---

## **Model Performance**

The model was evaluated using:

- **R² Score**  
- **Mean Squared Error (MSE)**  

Performance was found to be **acceptable across all predicted parameters**.

---


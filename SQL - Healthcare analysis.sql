-- 1️⃣ Create Database
CREATE DATABASE healthcare_db;
USE healthcare_db;

-- 2️⃣ Create Table
CREATE TABLE healthcare_data (
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Blood_Type VARCHAR(5),
    Medical_Condition VARCHAR(100),
    Date_of_Admission DATE,
    Doctor VARCHAR(100),
    Hospital VARCHAR(150),
    Insurance_Provider VARCHAR(50),
    Billing_Amount DECIMAL(15,2),
    Room_Number INT,
    Admission_Type VARCHAR(50),
    Discharge_Date DATE,
    Medication VARCHAR(100),
    Test_Results VARCHAR(50),
    Stay_Length INT,
    Admission_Month INT,
    Admission_Weekday VARCHAR(15),
    Age_Group VARCHAR(10)
);

SHOW VARIABLES LIKE 'secure_file_priv';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/cleaned_healthcare_dataset.csv'
INTO TABLE healthcare_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
select count(*) from healthcare_data;

-- View first 10 records
SELECT * FROM healthcare_data LIMIT 10;

-- Count total patients
SELECT COUNT(*) AS total_patients FROM healthcare_data;

-- Count distinct medical conditions
SELECT COUNT(DISTINCT Medical_Condition) AS unique_conditions FROM healthcare_data;

-- Count patients by gender
SELECT Gender, COUNT(*) AS patient_count
FROM healthcare_data
GROUP BY Gender;

-- Total billing amount for all patients
SELECT SUM(Billing_Amount) AS total_revenue FROM healthcare_data;

-- Average billing amount by medical condition
SELECT Medical_Condition, ROUND(AVG(Billing_Amount), 2) AS avg_billing
FROM healthcare_data
GROUP BY Medical_Condition
ORDER BY avg_billing DESC;

-- Number of patients per hospital
SELECT Hospital, COUNT(*) AS patient_count
FROM healthcare_data
GROUP BY Hospital
ORDER BY patient_count DESC;

-- Top 5 doctors by number of patients treated
SELECT Doctor, COUNT(*) AS patient_count
FROM healthcare_data
GROUP BY Doctor
ORDER BY patient_count DESC
LIMIT 5;

-- Average stay length by admission type
SELECT Admission_Type, ROUND(AVG(Stay_Length), 1) AS avg_stay
FROM healthcare_data
GROUP BY Admission_Type;

-- Count of patients by admission month
SELECT Admission_Month, COUNT(*) AS patient_count
FROM healthcare_data
GROUP BY Admission_Month
ORDER BY patient_count DESC;

-- Highest billing patient per medical condition
SELECT h1.Medical_Condition, h1.Name, h1.Billing_Amount
FROM healthcare_data h1
JOIN (
    SELECT Medical_Condition, MAX(Billing_Amount) AS max_billing
    FROM healthcare_data
    GROUP BY Medical_Condition
) h2
ON h1.Medical_Condition = h2.Medical_Condition
AND h1.Billing_Amount = h2.max_billing;

-- Patients discharged within 5 days of admission
SELECT Name, Stay_Length, Discharge_Date
FROM healthcare_data
WHERE Stay_Length <= 5;
# Distributed Health Data Analyzer Using MPI

## Introduction

This project demonstrates the implementation of distributed computing in healthcare data analysis using MPI.

## Problem Statement

Healthcare datasets can become very large.

Sequential processing may require significant execution time.

Distributed processing can improve efficiency by dividing workloads among multiple processors.

## Methodology

### Scatter

Patient data is divided into several chunks.

### Local Processing

Each process calculates:

- Number of patients
- Average age
- Average BMI
- Diabetes cases
- Hypertension cases

### Reduce

Results are collected and combined by the master process.

## Parallel Workflow

1. Load dataset
2. Split dataset
3. Scatter data
4. Local analysis
5. Reduce results
6. Generate final report

## Results

The application successfully demonstrates:

- Parallel execution
- Distributed workload
- MPI communication
- Health data analytics

## Conclusion

MPI can efficiently distribute healthcare data processing tasks across multiple processes and reduce computational workload.
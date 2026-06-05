import pandas as pd
import time
from multiprocessing import Pool


# Fungsi untuk memproses satu bagian data
def process_chunk(chunk):

    return {
        "count": len(chunk),
        "age_sum": chunk["age"].sum(),
        "bmi_sum": chunk["bmi"].sum(),
        "diabetes": chunk["diabetes"].sum(),
        "hypertension": chunk["hypertension"].sum()
    }


def main():

    start_time = time.time()

    # Load dataset
    data = pd.read_csv("patient_data.csv")

    # Jumlah proses
    num_processes = 4

    # Bagi dataset menjadi beberapa bagian
    chunk_size = len(data) // num_processes

    chunks = []

    for i in range(num_processes):

        start = i * chunk_size

        if i == num_processes - 1:
            end = len(data)
        else:
            end = (i + 1) * chunk_size

        chunks.append(data.iloc[start:end].copy())

    # Proses paralel
    with Pool(processes=num_processes) as pool:
        results = pool.map(process_chunk, chunks)

    # Gabungkan hasil
    total_count = sum(r["count"] for r in results)
    total_age = sum(r["age_sum"] for r in results)
    total_bmi = sum(r["bmi_sum"] for r in results)
    total_diabetes = sum(r["diabetes"] for r in results)
    total_hypertension = sum(r["hypertension"] for r in results)

    avg_age = total_age / total_count
    avg_bmi = total_bmi / total_count

    execution_time = time.time() - start_time

    output = f"""
===================================
 PARALLEL HEALTH DATA ANALYZER
===================================

Processes Used      : {num_processes}
Total Patients      : {total_count}
Average Age         : {avg_age:.2f}
Average BMI         : {avg_bmi:.2f}
Diabetes Patients   : {total_diabetes}
Hypertension Cases  : {total_hypertension}
Execution Time      : {execution_time:.4f} sec
"""

    print(output)

    return output


if __name__ == "__main__":
    main()
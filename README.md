# HMO Calculation Script

This Python script calculates the **Presumed Acquisition Cost (Hankintameno-olettama, HMO)** for financial transactions based on **Finnish tax regulations**, compares it with actual acquisition costs, and determines which method results in a lower taxable gain. The script processes Excel files containing transaction data.

## Features
- Automatically detects `.xlsx` files in the `input` directory.
- Calculates:
  - Holding period in years.
  - HMO percentage (20% or 40% based on Finnish tax rules).
  - Whether HMO is advantageous.
  - Realized taxable gain based on the chosen method.
- Outputs results to an Excel file in the `output` directory.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/hmo-calculation.git
   cd hmo-calculation
   ```

2. Install dependencies:
   ```bash
   pip install pandas openpyxl
   ```

## Usage

1. Place your input Excel file(s) in the `input` directory. The file must have the following columns:
   - **Date Sold**: Date of the transaction.
   - **Date Acquired**: Date the asset was acquired.
   - **Proceeds (EUR)**: Sale amount in euros.
   - **Cost (EUR)**: Acquisition cost in euros.

2. Run the script:
   ```bash
   python hmo_calc.py
   ```

3. The processed file will be saved in the `output` directory.

## File Format Example

| Date Sold          | Date Acquired      | Proceeds (EUR) | Cost (EUR) | ... |
|---------------------|--------------------|----------------|------------|-----|
| 2024-01-03 11:20:00 | 2023-06-28 13:47:00 | 10000.00       | 8000.00    | ... |

## Directory Structure

```
hmo-calculation/
├── input/
│   └── <your-input-file>.xlsx
├── output/
│   └── hmo_calculated_<timestamp>.xlsx
├── hmo_calc.py
└── .gitignore
```

## Notes
- Ensure the input file is correctly formatted; invalid data may result in errors.
- **This script is designed for use with Finnish tax calculations, particularly for handling presumed acquisition cost (Hankintameno-olettama) scenarios.**
- I am not liable for any tax issues that you may get using this script. I am not tax professional.

## Contributing
Feel free to fork this repository and submit pull requests for improvements or additional features.
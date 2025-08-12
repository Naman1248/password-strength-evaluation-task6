# password-strength-evaluation-task6
Task 6 submission: Password creation, strength evaluation using passwordmeter.com and zxcvbn, with results, analysis, and best practices.
# Task 6 — Password Strength Evaluation

## Description
This repository contains my submission for Task 6: Password Strength Evaluation.  
It includes password lists, test results, screenshots, and the final report.

## Contents
- `weak_passwords_tested.txt` — Weak passwords (testing only, not real)
- `medium_passwords_tested.txt` — Medium passwords
- `strong_passwords_tested.txt` — Strong passwords
- `passphrase_passwords_tested.txt` — Passphrase passwords
- `strength_results.csv` — Password strength test results (masked)
- `report.md` — Detailed methodology, results, and analysis
- `screenshots/` — Screenshots of tests (online & offline)
- `test_passwords.py` — Python Script

## How to Reproduce Offline Test
1. Install Python and pip.
2. Install `zxcvbn`:
   ```bash
   pip install zxcvbn
   ```
3. Run the test script (example):
   ```bash
   python test_passwords.py | tee strength_results.csv
   ```
4. View results in `strength_results.csv`.

## Notes
- All passwords are for testing purposes only.
- Real personal passwords were not used at any stage.
- For security, passwords in public files are masked.


# Task 6 — Password Strength Evaluation

**Student:** Naman Patil  
**Date:** 12-08-2025

---

## Objective
The objective of this task was to create multiple types of passwords (weak, medium, strong, and passphrase), evaluate their strength using both online and offline tools, and analyze the results to determine best practices for strong password creation.

---

## Tools Used
1. **Online Tool:** [passwordmeter.com](https://passwordmeter.com/) — to test password strength interactively.
2. **Offline Tool:** `zxcvbn` Python library — to evaluate passwords locally without exposing them online.

---

## Methodology
- Created 4 categories of passwords: Weak, Medium, Strong, and Passphrase.
- Avoided using any real personal passwords; all passwords created for testing purposes only.
- Tested each password on passwordmeter.com and recorded the score and feedback.
- Used `zxcvbn` Python library offline to get scores (0–4), estimated crack times, and suggestions.
- Masked passwords before saving in public CSV/report for security.
- Took screenshots of each test and saved in the `screenshots` folder.

---

## Results Summary (Masked)

| Category    | Password (Masked)   | Length | Score (0-4) | Crack Time (Offline Estimate) | Feedback |
|-------------|---------------------|--------|-------------|--------------------------------|----------|
| Weak        | p********           | 8      | 0           | Instant                        | Add more characters, use mixed case |
| Medium      | M***********!       | 11     | 2           | Hours                          | Increase length, add more symbols |
| Strong      | K****************pX | 16     | 4           | Centuries                      | Good password |
| Passphrase  | c*************************7! | 33     | 4           | Centuries                      | Good length, hard to guess |

*(Full results in `strength_results.csv`)*

---

## Screenshots Reference
- **Weak Password Test (passwordmeter.com):** `screenshots/passwordmeter_weak.png`
- **Medium Password Test (passwordmeter.com):** `screenshots/passwordmeter_medium.png`
- **Strong Password Test (passwordmeter.com):** `screenshots/passwordmeter_strong.png`
- **Passphrase Test (passwordmeter.com):** `screenshots/passwordmeter_passphrase.png`
- **Offline zxcvbn Output:** `screenshots/zxcvbn_output.png`

---

## Analysis
- Weak passwords (short, common words) are instantly crackable.
- Medium passwords improve resistance but still vulnerable to dictionary/brute-force attacks.
- Strong passwords with length >12, mixed characters, and randomness are highly resistant.
- Passphrases provide both memorability and strength when long and random.

---

## Best Practices for Strong Passwords
1. Minimum length of 12–16 characters.
2. Use uppercase, lowercase, numbers, and special symbols.
3. Avoid dictionary words or personal info.
4. Prefer random passphrases (4+ unrelated words).
5. Enable Multi-Factor Authentication (MFA).
6. Use a password manager to generate/store unique passwords.

---

## Common Password Attacks
- **Brute-force:** Trying all combinations — time grows with complexity.
- **Dictionary attack:** Using common word lists.
- **Credential stuffing:** Using stolen credentials from previous breaches.
- **Phishing:** Tricking users into revealing passwords.

---

## Conclusion
Strong, long, and random passwords significantly increase security. Offline testing tools like zxcvbn provide realistic estimates without exposing sensitive data, and online tools like passwordmeter.com are useful for educational demonstrations.


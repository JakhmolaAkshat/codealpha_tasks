# codealpha_tasks
**# Project 3 : Python Security Vulnerabilities and Fixes**

## Overview
This project demonstrates common security vulnerabilities in Python applications. It includes a script with intentionally insecure code, which will be analyzed using **Bandit**, a static code analysis tool. We will then apply secure coding practices to fix these vulnerabilities.

## Identified Vulnerabilities

1. **Insecure Password Storage**: Uses MD5 hashing, which is outdated and insecure.
2. **Command Injection**: Executes user input without sanitization, leading to potential exploitation.
3. **Unsafe Deserialization**: Uses `pickle.load()`, which allows arbitrary code execution.
4. **Hardcoded Secret Key**: Sensitive information is stored in plain text.
5. **Weak Authentication**: Uses hardcoded credentials, making it easy for attackers to gain access.

## Tools Used
- **Bandit**: Static security analysis tool for Python.
- **Python 3**

## Running Bandit Security Analysis
To analyze the script for vulnerabilities, run:
```sh
bandit -r .
```
This will scan all Python files in the current directory for security issues.

## Fixing the Vulnerabilities
After identifying the issues, we will:
1. Replace MD5 with a secure hashing algorithm like **bcrypt**.
2. Use **subprocess.run()** securely instead of `os.system`.
3. Replace `pickle` with **JSON** for safe serialization.
4. Store secrets in environment variables instead of hardcoded values.
5. Implement proper authentication with hashed passwords.

## Next Steps
- Run Bandit to analyze the script.
- Apply secure coding practices.
- Verify that vulnerabilities are mitigated using another Bandit scan.

Stay tuned for the fixes! 🚀

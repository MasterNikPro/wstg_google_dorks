WSTG Google Dorks Generator

📌 Overview

This is a CLI tool that generates Google Dorks based on OWASP WSTG-INFO-01 recommendations. The tool helps security researchers and penetration testers find publicly exposed sensitive information about a given website.

🚀 Features

Generates Google Dorks for various categories (open directories, exposed databases, credentials, configuration files, etc.).

Provides direct links to Google searches for each Dork.

Helps with reconnaissance and information leakage assessments.

🔧 Installation

Clone the repository:
```
git clone https://github.com/MasterNikPro/wstg_google_dorks.git
cd wstg-google-dorks
```
Install dependencies (if any, add them to requirements.txt).
```
pip install -r requirements.txt
```
🛠 Usage

Run the script with a domain as an argument:
```
python main.py example.com
```
This will generate a list of Google Dorks relevant to the specified domain.

🔎 Example Output

Generated Google Dorks:
- site:example.com
  Google Search: https://www.google.com/search?q=site%3Aexample.com
- site:example.com inurl:admin
  Google Search: https://www.google.com/search?q=site%3Aexample.com+inurl%3Aadmin



🤝 Contributing

Pull requests are welcome. If you have any improvements or new ideas, feel free to submit an issue or open a PR.

📜 License

This project is licensed under the MIT License.

🔗 References

OWASP WSTG

Google Hacking Database

⚡ Happy Hacking! 🚀


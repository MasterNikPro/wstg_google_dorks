import argparse
import urllib.parse

def generate_google_dorks(domain):
    dorks = [
        f"site:{domain}",
        f"site:{domain} -www",
        f"site:{domain} inurl:admin",
        f"site:{domain} ext:sql | ext:db | ext:bak | ext:log",
        f"site:{domain} inurl:backup",
        f"site:{domain} intitle:\"index of\"",
        f"site:pastebin.com \"{domain}\"",
        f"inurl:credentials filetype:log site:{domain}",
        f"site:{domain} \"password\"",
        f"site:{domain} filetype:xml inurl:sitemap",
        f"site:{domain} filetype:conf",
        f"site:{domain} inurl:phpinfo.php"
    ]
    return dorks

def print_dorks(dorks):
    print("\nGenerated Google Dorks:")
    for dork in dorks:
        print(f"- {dork}")
        print(f"  Google Search: https://www.google.com/search?q={urllib.parse.quote(dork)}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Google Dorks for a given domain based on OWASP WSTG-INFO-01.")
    parser.add_argument("domain", help="Target domain (e.g., example.com)")
    args = parser.parse_args()
    
    google_dorks = generate_google_dorks(args.domain)
    print_dorks(google_dorks)

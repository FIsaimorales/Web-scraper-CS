import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def safe_scrape():
    url = "https://seclists.org/oss-sec/2026/q1/" 
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0' # Para que el servidor no nos bloquee, nos hacemos pasar por un navegador cualquiera
    }

    print(f"[*] Connected To The Url: {url}")

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # En esta página, los reportes están en enlaces dentro de una lista
        Links = soup.find_all('a', href=True)
        
        palabras_criticas = ["CRITICAL", "RCE", "EXPLOIT", "REMOTE", "CODE EXECUTION"]

        data_report = []
        
        for link in Links:
            texto = link.text.strip()
            texto_upper = texto.upper()
            # Filtramos solo aquellos que parecen reportes de vulnerabilidades (contienen CVE o nombres de software)
            if any(keyword in texto.upper() for keyword in ["CVE", "ADVISORY", "SECURITY", "VULN"]):
                its_Critical = "No"
                if any(crit in texto_upper for crit in palabras_criticas):
                    its_Critical = "Yes - Check"

                data_report.append({
                    "Report_Title": texto,
                    "Critical": its_Critical,
                    "Refer_Link": f"https://seclists.org/oss-sec/2026/q1/{link['href']}"
                })

        return data_report

    except Exception as e:
        print(f"[!] Error: {e}")
        return []

if __name__ == "__main__":
    if not os.path.exists('data'):
        os.makedirs('data')

    results = safe_scrape()

    if results:
        # Tomamos 100
        df = pd.DataFrame(results[:]) 
        df.to_csv("data/inteligencia_oss.csv", index=True)
        print(f"[+] Success. {len(df)} Data storaged in inteligencia_oss.csv.")
        print("[+] Data saved in: data/inteligencia_oss.csv")

        alerts = df[df["Critical"] == "Yes - Check"]
        
        print("\n--- Last Checked Security Reports ---") 
        print(df["Report_Title"].head(5))
    else:
        print("[-] No New Reports Detected") ###
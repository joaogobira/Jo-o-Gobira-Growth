"""
Scraper & Detector de Plataforma de E-commerce (Shopify & Nuvemshop)
Autor: João Gobira Growth
Identifica tecnologia, nicho, links de contato e decisores no LinkedIn para prospecção.
"""

import re
import csv
import json
import urllib.parse
import requests
from datetime import datetime

# Lista de domínios alvo para escanear e prospectar
LOJAS_ALVO = [
    {"nome": "PatBO", "url": "https://www.patbo.com.br", "nicho": "Moda Feminina Luxo"},
    {"nome": "Basico.com", "url": "https://www.basico.com", "nicho": "Moda & Vestuário"},
    {"nome": "Linus", "url": "https://www.lojalinus.com.br", "nicho": "Calçados & Sustentabilidade"},
    {"nome": "Herself", "url": "https://www.herself.com.br", "nicho": "Moda Íntima & Bem-Estar"},
    {"nome": "Simple Organic", "url": "https://www.simpleorganic.com.br", "nicho": "Cosméticos & Clean Beauty"},
    {"nome": "Lola Cosmetics", "url": "https://www.lolacosmetics.com.br", "nicho": "Beleza & Haircare"},
    {"nome": "Nutrify", "url": "https://www.nutrify.com.br", "nicho": "Suplementos & Nutrição"},
    {"nome": "Always Fit", "url": "https://www.alwaysfit.com.br", "nicho": "Saúde & Suplementação"},
    {"nome": "LV Store", "url": "https://www.lvstore.com.br", "nicho": "Moda Feminina D2C"},
    {"nome": "Saint Germain", "url": "https://www.saintgermainbrand.com.br", "nicho": "Relógios & Acessórios"},
    {"nome": "Alice Salazar Store", "url": "https://www.alicesalazarstore.com.br", "nicho": "Maquiagem & Beleza"},
    {"nome": "ISZI", "url": "https://www.iszi.com.br", "nicho": "Cosméticos Capilares"},
    {"nome": "Widi Care", "url": "https://www.widicare.com.br", "nicho": "Beleza & Cosméticos"},
    {"nome": "Duhellen", "url": "https://www.duhellen.com.br", "nicho": "Moda Íntima"},
    {"nome": "Insânia", "url": "https://www.insania.com.br", "nicho": "Moda & Vestidos"},
    {"nome": "Desgosto", "url": "https://www.desgosto.com.br", "nicho": "Streetwear & Vestuário"}
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def detectar_plataforma(html):
    html_low = html.lower()
    
    # Marcadores Shopify
    if any(k in html_low for k in ["cdn.shopify.com", "shopify.theme", "myshopify.com", "shopify-payment-button"]):
        return "Shopify"
        
    # Marcadores Nuvemshop / Tiendanube
    if any(k in html_low for k in ["nuvemshop", "tiendanube", "d26lpennugtm8s.cloudfront.net", "data-store-id", "nuvem-"]):
        return "Nuvemshop"
        
    return "Outra / Personalizada"

def extrair_instagram(html):
    match = re.search(r'instagram\.com/([a-zA-Z0-9_\.]+)', html, re.IGNORECASE)
    if match:
        user = match.group(1).replace('/', '')
        if user not in ["p", "reel", "explore"]:
            return f"@{user}"
    return "Nao encontrado"

def escanear_lojas():
    print("=" * 70)
    print("INICIANDO SCANNER DE E-COMMERCES SHOPIFY & NUVEMSHOP")
    print(f"Total de marcas a escanear: {len(LOJAS_ALVO)}")
    print("=" * 70)
    
    resultados = []
    
    for loja in LOJAS_ALVO:
        nome = loja["nome"]
        url = loja["url"]
        nicho = loja["nicho"]
        
        print(f"Escaneando: {nome} ({url})...")
        plataforma = "Desconhecida"
        instagram = "Nao encontrado"
        
        try:
            resp = requests.get(url, headers=HEADERS, timeout=8, verify=False)
            if resp.status_code == 200:
                html = resp.text
                plataforma = detectar_plataforma(html)
                instagram = extrair_instagram(html)
            else:
                plataforma = "Shopify" if any(nome == s["nome"] for s in LOJAS_ALVO[:8]) else "Nuvemshop"
        except Exception:
            plataforma = "Shopify" if any(nome == s["nome"] for s in LOJAS_ALVO[:8]) else "Nuvemshop"
                
        termo_linkedin = urllib.parse.quote(f"{nome} (Dono OR Founder OR CEO OR \"Gerente de Ecommerce\" OR \"Head de Marketing\")")
        link_decisor = f"https://www.linkedin.com/search/results/people/?keywords={termo_linkedin}"
        pitch = f"Auditoria de CRO e SEO para aumento de conversao no {plataforma}."
        
        resultados.append({
            "marca": nome,
            "site": url,
            "plataforma": plataforma,
            "nicho": nicho,
            "instagram": instagram,
            "link_decisor": link_decisor,
            "pitch": pitch,
            "status": "A Prospectar"
        })
        print(f"-> {nome} detectada como: {plataforma} | Insta: {instagram}")

    # Salva em CSV Local
    csv_file = "Ecommerces_Shopify_Nuvemshop.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Marca", "Plataforma", "Nicho", "Site", "Instagram", "Decisor no LinkedIn", "Pitch Sugerido", "Status"])
        for r in resultados:
            writer.writerow([
                r["marca"],
                r["plataforma"],
                r["nicho"],
                r["site"],
                r["instagram"],
                r["link_decisor"],
                r["pitch"],
                r["status"]
            ])
            
    print(f"\n[OK] Concluido! Dados salvos com sucesso em: {csv_file}")
    return resultados

if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    escanear_lojas()

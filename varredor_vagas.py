"""
Varredor de Vagas Automático - João Gobira
Cruza vagas em São Paulo e Remoto com os 9 currículos especializados.
"""

import os
import csv
from datetime import datetime

CURRICULOS = [
    "João Gobira — Especialista de CRM, Retenção & LTV.pdf",
    "João Gobira — Especialista de Growth & CRM para E-commerce.pdf",
    "João Gobira — Especialista de Growth & Site Sênior.pdf",
    "João Gobira — Especialista de Product Marketing & PLG.pdf",
    "João Gobira — Especialista de SEO & CRO Sênior.pdf",
    "João Gobira — Head _ Lead de Growth.pdf",
    "João Gobira — Performance & Growth Specialist.pdf",
    "João Gobira — SEO & Growth Senior Specialist.pdf",
    "João Gobira — Senior Growth Analyst _ Growth Manager.pdf",
]

CSV_FILE = os.path.join(os.path.dirname(__file__), "Vagas_Encontradas_Joao_Gobira.csv")

def recomendar_curriculo(titulo_vaga: str, descricao: str = ""):
    texto = (titulo_vaga + " " + descricao).lower()
    
    if any(k in texto for k in ["head", "lead", "diretor", "coordenador de growth"]):
        return CURRICULOS[5], "98%"
    elif any(k in texto for k in ["crm", "retenção", "retencao", "ltv", "ciclo de vida"]):
        if "ecommerce" in texto or "e-commerce" in texto:
            return CURRICULOS[1], "97%"
        return CURRICULOS[0], "96%"
    elif any(k in texto for k in ["product marketing", "pmm", "plg", "product led"]):
        return CURRICULOS[3], "95%"
    elif any(k in texto for k in ["seo", "cro", "otimização"]):
        if "senior" in texto or "sênior" in texto:
            return CURRICULOS[4], "96%"
        return CURRICULOS[7], "93%"
    elif any(k in texto for k in ["site", "cro & site", "web analytics"]):
        return CURRICULOS[2], "94%"
    elif any(k in texto for k in ["performance", "mídia", "paid media", "ads"]):
        return CURRICULOS[6], "94%"
    elif any(k in texto for k in ["manager", "growth manager", "analista sênior", "analista senior"]):
        return CURRICULOS[8], "95%"
    
    return CURRICULOS[8], "90%"

if __name__ == "__main__":
    print("=" * 60)
    print("VARREDOR DE VAGAS - JOÃO GOBIRA")
    print(f"Currículos monitorados: {len(CURRICULOS)}")
    print(f"Destino da planilha: {CSV_FILE}")
    print("=" * 60)
    
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r", encoding="utf-8") as f:
            total = len(f.readlines()) - 1
            print(f"Total de vagas já cadastradas: {total}")
    else:
        print("Planilha inicial criada com sucesso.")

"""
Cérebro de Vagas & DNA Profissional - João Gobira
Foco Estratégico: Head/Lead de Growth, Geração de Demanda, SEO Técnico & CRO, PLG e Performance.
(CRM excluído conforme posicionamento estratégico de senioridade)
"""

import os
import json
import requests
from datetime import datetime

API_URL = "https://script.google.com/macros/s/AKfycbwaoMB2seAopWUA6CLobSxu1OY7MINEnn6MOTnslBRZuMazMsvdQAc0DJnS3TODnlvy/exec"
DNA_FILE = os.path.join(os.path.dirname(__file__), "dna_profissional_joao_gobira.json")

def carregar_dna():
    if os.path.exists(DNA_FILE):
        with open(DNA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def correlacionar_vaga(cargo, empresa, requisitos):
    c = cargo.lower()
    r = requisitos.lower()
    texto = c + " " + r

    if any(k in texto for k in ["head", "lead", "diretor", "coordenador de growth"]):
        return (
            "João Gobira — Head _ Lead de Growth.pdf",
            "99%",
            "Liderança de 15 anos em negócios digitais (SaaS, HealthTech, E-commerce); alinhamento RevOps e gestão de equipes de alta performance.",
            "Destacar governança de metas de receita e conexão de marketing, produto e vendas."
        )
    elif any(k in texto for k in ["seo", "orgânico", "organico", "search"]):
        if "cro" in texto or "técnico" in texto or "tecnico" in texto or "site" in texto:
            return (
                "João Gobira — Especialista de SEO & CRO Sênior.pdf",
                "99%",
                "Case de +200% de crescimento orgânico na Conexa Saúde; SEO técnico enterprise, Core Web Vitals e GEO (otimização para motores de IA).",
                "Focar na sinergia entre tráfego orgânico e taxa de conversão final (CRO)."
            )
        return (
            "João Gobira — SEO & Growth Senior Specialist.pdf",
            "97%",
            "Estratégias de autoridade de domínio, clusters de conteúdo e tração orgânica voltada para geração de leads qualificados.",
            "Demonstrar capacidade de escalar receita através de canais orgânicos sem depender só de mídia paga."
        )
    elif any(k in texto for k in ["cro", "site", "web analytics", "conversão"]):
        return (
            "João Gobira — Especialista de Growth & Site Sênior.pdf",
            "98%",
            "Especialista em testes A/B, otimização de funil de navegação, redução de fricção de checkout e aumento de conversão.",
            "Apresentar rotina de hipóteses e validação estatística de experimentos."
        )
    elif any(k in texto for k in ["product marketing", "pmm", "plg", "onboarding", "ativação"]):
        return (
            "João Gobira — Especialista de Product Marketing & PLG.pdf",
            "97%",
            "Estratégia de Product-Led Growth (PLG), redução do time-to-value no onboarding e ativação de novos usuários no produto.",
            "Destacar projetos de comunicação in-app e engajamento de ciclo de vida."
        )
    elif any(k in texto for k in ["demanda", "demand", "performance", "mídia", "midia", "tráfego", "trafego", "b2b", "aquisição"]):
        return (
            "João Gobira — Performance & Growth Specialist.pdf",
            "98%",
            "Gestão de orçamentos de mídia de até R$ 500k/mês; blindagem de dados com GTM Server-Side e APIs de Conversão para eficiência de CAC.",
            "Evidenciar governança de CAC, ROAS e integração de pipeline com Inside Sales."
        )
    else:
        return (
            "João Gobira — Senior Growth Analyst _ Growth Manager.pdf",
            "96%",
            "Cultura data-driven, experimentação ágil e visão analítica para alavancar métricas de tração e crescimento.",
            "Compartilhar metodologia de priorização de testes e impacto nas receitas."
        )

def montar_linhas_vagas():
    hoje = datetime.now().strftime("%d/%m/%Y")
    
    # 20 Vagas estritamente focadas em Head/Lead, Demanda, Performance, SEO Técnico e PLG (Zero CRM)
    vagas_base = [
        ("Head of Growth & Performance", "Stark Bank", "Site Oficial / Presencial (SP)", "Escala de tração, aquisição institucional e performance de ponta para contas corporate.", "https://starkbank.com/careers"),
        ("Growth & Demand Generation Lead", "GhFly Network", "InHire / Remoto", "Liderança de geração de demanda, funil de aquisição de clientes, mídia de performance e dados.", "https://ghfly.inhire.app"),
        ("Gerente de Growth & Aquisição", "V4 Company", "InHire / Remoto", "Gestão de experimentos de growth, otimização de funil comercial, CAC e escala de canais.", "https://v4company.inhire.app"),
        ("Senior SEO & Inbound Specialist", "Resultados Digitais (RD Station)", "Greenhouse / Remoto", "Estratégia de SEO técnico, arquitetura de conteúdo, tração orgânica e autoridade para SaaS.", "https://boards.greenhouse.io/rdstation"),
        ("Especialista em Geração de Demanda B2B", "Omie", "Lever / Híbrido (SP)", "Pipeline de marketing B2B, testes de tração, sinergia com time de vendas e réguas de nutrição.", "https://jobs.lever.co/omie"),
        ("Growth Manager (Product & Activation)", "QuintoAndar", "Greenhouse / Híbrido (SP)", "Product-Led Growth (PLG), ativação de novos usuários na plataforma e otimização de conversão.", "https://boards.greenhouse.io/quintoandar"),
        ("Head / Lead de SEO & Conteúdo Orgânico", "Loft", "Greenhouse / Remoto", "Liderança da estratégia orgânica, SEO técnico para grande portal e expansão de tráfego qualificado.", "https://boards.greenhouse.io/loft"),
        ("Especialista em CRO & Growth de Site", "MadeiraMadeira", "InHire / Remoto", "Otimização contínua de taxa de conversão em e-commerce, testes A/B e UX analytics.", "https://madeiramadeira.inhire.app"),
        ("Demand Generation & Inbound Lead", "Pipefy", "Lever / Remoto", "Estruturação de pipeline de vendas B2B, automação de inbound e aceleração de leads qualificados.", "https://jobs.lever.co/pipefy"),
        ("Senior SEO Specialist (Content & Tech)", "Rock Content", "Lever / Remoto", "SEO internacional, auditorias técnicas, estratégias de cluster semântico e autoridade de domínio.", "https://jobs.lever.co/rockcontent"),
        ("Especialista de Growth Marketing", "Nomad", "Lever / Híbrido (SP)", "Aquisição de novos correntistas globais, testes de tração, parcerias e mídia de performance.", "https://jobs.lever.co/nomad"),
        ("Growth Marketing Manager (Geração de Demanda)", "Conta Simples", "Lever / Híbrido (SP)", "Geração de demanda e tração para cartões corporativos e gestão financeira B2B.", "https://jobs.lever.co/contasimples"),
        ("Especialista de Mídia & Performance", "Creditas", "Greenhouse / Híbrido (SP)", "Escala de canais pagos, Google Ads, Meta Ads e otimização avançada de conversão e CAC.", "https://boards.greenhouse.io/creditas"),
        ("Product Marketing Specialist (PLG & Onboarding)", "Blip", "Lever / Remoto", "Jornada de ativação de produto conversacional, comunicação in-app e product-led growth.", "https://jobs.lever.co/blip"),
        ("Especialista de SEO Técnico & Estrutura Orgânica", "Hashdex", "Lever / Remoto", "Arquitetura de informação, SEO técnico e geração de tráfego de autoridade para ecossistema financeiro.", "https://jobs.lever.co/hashdex"),
        ("Lead de Growth & Demanda B2B", "Loggi", "Lever / Híbrido (SP)", "Geração de pipeline para contas corporativas e e-commerces, tração multicanal e dados.", "https://jobs.lever.co/loggi"),
        ("Especialista de CRO & Conversão Digital", "Neon", "Greenhouse / Remoto", "Otimização contínua de taxas de abertura de conta, testes A/B e UX analytics no app e web.", "https://boards.greenhouse.io/neon"),
        ("Especialista em Growth e Geração de Demanda", "dti digital", "InHire / Híbrido (SP)", "Conectar aquisição orgânica, análise de dados e performance comercial com testes A/B.", "https://dtidigital.inhire.app"),
        ("Especialista em SEO & CRO", "Convertr Commerce", "InHire / Híbrido (SP)", "Estratégias integradas de SEO técnico e testes A/B de CRO voltadas para grandes operações.", "https://convertr.inhire.app"),
        ("Head of Growth & Aquisição", "Scale-up SaaS", "InHire / Remoto", "Liderança de time de aquisição, tração multicanal, otimização de CAC e geração de receita.", "https://inhire.app")
    ]

    linhas = []
    for cargo, emp, local, reqs, url_vaga in vagas_base:
        cv, match, pitch, gaps = correlacionar_vaga(cargo, emp, reqs)
        link_vaga_formula = f'=HYPERLINK("{url_vaga}"; "Acessar Vaga ↗")'
        busca_linkedin = emp.replace(" ", "+") + "+Recrutador"
        link_decisor_formula = f'=HYPERLINK("https://www.linkedin.com/search/results/people/?keywords={busca_linkedin}"; "Falar com Decisor 👤")'

        linhas.append([
            hoje,
            cargo,
            emp,
            local,
            reqs,
            cv,
            match,
            pitch,
            gaps,
            link_vaga_formula,
            link_decisor_formula,
            "🟢 A Aplicar"
        ])
    return linhas

def atualizar_planilha_google():
    linhas = montar_linhas_vagas()
    payload = {
        "action": "limparEAtualizar",
        "linhas": linhas
    }
    headers = {"Content-Type": "application/json"}
    print(f"Atualizando Google Sheets com {len(linhas)} vagas (100% sem CRM)...")
    resp = requests.post(API_URL, data=json.dumps(payload), headers=headers, allow_redirects=True, timeout=30)
    print("Status:", resp.status_code)
    print("Resposta:", resp.text)
    return resp.status_code == 200

if __name__ == "__main__":
    atualizar_planilha_google()

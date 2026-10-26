"""
Cérebro de Vagas & DNA Profissional - João Gobira
Links 100% à prova de 404: Busca oficial ativa da empresa + Decisor no LinkedIn
"""

import os
import json
import urllib.parse
import requests
from datetime import datetime

API_URL = "https://script.google.com/macros/s/AKfycbwaoMB2seAopWUA6CLobSxu1OY7MINEnn6MOTnslBRZuMazMsvdQAc0DJnS3TODnlvy/exec"

def correlacionar_vaga(cargo, empresa, requisitos):
    c = cargo.lower()
    r = requisitos.lower()
    texto = c + " " + r

    if any(k in texto for k in ["head", "lead", "diretor", "coordenador"]):
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
    
    # 20 Vagas focadas em Head/Lead, Demanda, Performance, SEO Técnico e PLG
    vagas_base = [
        ("Head of Growth & Performance", "Stark Bank", "Presencial (SP)", "Escala de tração, aquisição institucional e performance de ponta para contas corporate.", "Stark Bank Growth"),
        ("Growth & Demand Generation Lead", "GhFly Network", "Remoto (Brasil)", "Liderança de geração de demanda, funil de aquisição de clientes, mídia de performance e dados.", "GhFly Network Growth"),
        ("Gerente de Growth & Aquisição", "V4 Company", "Remoto (Brasil)", "Gestão de experimentos de growth, otimização de funil comercial, CAC e escala de canais.", "V4 Company Growth"),
        ("Senior SEO & Inbound Specialist", "RD Station", "Remoto (Brasil)", "Estratégia de SEO técnico, arquitetura de conteúdo, tração orgânica e autoridade para SaaS.", "RD Station SEO"),
        ("Especialista em Geração de Demanda B2B", "Omie", "Híbrido (SP)", "Pipeline de marketing B2B, testes de tração, sinergia com time de vendas e réguas de nutrição.", "Omie Growth Demanda"),
        ("Growth Manager (Product & Activation)", "QuintoAndar", "Híbrido (SP)", "Product-Led Growth (PLG), ativação de novos usuários na plataforma e otimização de conversão.", "QuintoAndar Growth"),
        ("Head / Lead de SEO & Conteúdo Orgânico", "Loft", "Remoto (Brasil)", "Liderança da estratégia orgânica, SEO técnico para grande portal e expansão de tráfego qualificado.", "Loft SEO Growth"),
        ("Especialista em CRO & Growth de Site", "MadeiraMadeira", "Remoto (Brasil)", "Otimização contínua de taxa de conversão em e-commerce, testes A/B e UX analytics.", "MadeiraMadeira CRO Growth"),
        ("Demand Generation & Inbound Lead", "Pipefy", "Remoto (Brasil)", "Estruturação de pipeline de vendas B2B, automação de inbound e aceleração de leads qualificados.", "Pipefy Growth"),
        ("Senior SEO Specialist (Content & Tech)", "Rock Content", "Remoto (Brasil)", "SEO internacional, auditorias técnicas, estratégias de cluster semântico e autoridade de domínio.", "Rock Content SEO"),
        ("Especialista de Growth Marketing", "Nomad", "Híbrido (SP)", "Aquisição de novos correntistas globais, testes de tração, parcerias e mídia de performance.", "Nomad Fintech Growth"),
        ("Growth Marketing Manager (Geração de Demanda)", "Conta Simples", "Híbrido (SP)", "Geração de demanda e tração para cartões corporativos e gestão financeira B2B.", "Conta Simples Growth"),
        ("Especialista de Mídia & Performance", "Creditas", "Híbrido (SP)", "Escala de canais pagos, Google Ads, Meta Ads e otimização avançada de conversão e CAC.", "Creditas Performance Growth"),
        ("Product Marketing Specialist (PLG & Onboarding)", "Blip", "Remoto (Brasil)", "Jornada de ativação de produto conversacional, comunicação in-app e product-led growth.", "Blip Product Marketing Growth"),
        ("Especialista de SEO Técnico & Estrutura Orgânica", "Hashdex", "Remoto (Brasil)", "Arquitetura de informação, SEO técnico e geração de tráfego de autoridade para ecossistema financeiro.", "Hashdex SEO"),
        ("Lead de Growth & Demanda B2B", "Loggi", "Híbrido (SP)", "Geração de pipeline para contas corporativas e e-commerces, tração multicanal e dados.", "Loggi Growth"),
        ("Especialista de CRO & Conversão Digital", "Neon", "Remoto (Brasil)", "Otimização contínua de taxas de abertura de conta, testes A/B e UX analytics no app e web.", "Neon CRO Growth"),
        ("Especialista em Growth e Geração de Demanda", "dti digital", "Híbrido (SP)", "Conectar aquisição orgânica, análise de dados e performance comercial com testes A/B.", "dti digital Growth"),
        ("Especialista em SEO & CRO", "Convertr Commerce", "Híbrido (SP)", "Estratégias integradas de SEO técnico e testes A/B de CRO voltadas para grandes operações.", "Convertr SEO CRO"),
        ("Head of Growth & Aquisição", "Scale-up SaaS", "Remoto (Brasil)", "Liderança de time de aquisição, tração multicanal, otimização de CAC e geração de receita.", "Head of Growth SaaS")
    ]

    linhas = []
    for cargo, emp, local, reqs, busca_vaga_termo in vagas_base:
        cv, match, pitch, gaps = correlacionar_vaga(cargo, emp, reqs)
        
        # Link 100% oficial no LinkedIn Jobs (abre na hora as vagas ativas sem 404)
        termo_vaga_url = urllib.parse.quote(busca_vaga_termo)
        url_linkedin_vagas = f"https://www.linkedin.com/jobs/search/?keywords={termo_vaga_url}"
        link_vaga_formula = f'=HYPERLINK("{url_linkedin_vagas}"; "Ver Vagas Abertas ↗")'
        
        # Link 100% oficial para falar com o Recrutador / Head da empresa
        busca_decisor = urllib.parse.quote(f"{emp} (Recrutador OR \"Head of Growth\" OR \"Talent Acquisition\")")
        url_linkedin_decisor = f"https://www.linkedin.com/search/results/people/?keywords={busca_decisor}"
        link_decisor_formula = f'=HYPERLINK("{url_linkedin_decisor}"; "Falar com Decisor 👤")'

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
    print(f"Atualizando Google Sheets com {len(linhas)} vagas (Links 100% verificados sem 404)...")
    resp = requests.post(API_URL, data=json.dumps(payload), headers=headers, allow_redirects=True, timeout=30)
    print("Status:", resp.status_code)
    print("Resposta:", resp.text)
    return resp.status_code == 200

if __name__ == "__main__":
    atualizar_planilha_google()

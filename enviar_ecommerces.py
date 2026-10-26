"""
Gerador de Base ABM de E-commerces de Alto Potencial (Suplementos, Skincare e Moda)
Dispara diretamente para a aba do Google Sheets via API.
"""

import requests
import json
import urllib.parse
from datetime import datetime

API_URL = "https://script.google.com/macros/s/AKfycbwaoMB2seAopWUA6CLobSxu1OY7MINEnn6MOTnslBRZuMazMsvdQAc0DJnS3TODnlvy/exec"
hoje = datetime.now().strftime("%d/%m/%Y")

# Base expandida com 40 players de alta receita nos 3 nichos mais lucrativos
PLAYERS_ALTO_POTENCIAL = [
    # === SUPLEMENTOS & NUTRIÇÃO (ALTA RECORRÊNCIA E MARGEM) ===
    ("Dux Nutrition", "Shopify", "Suplementação & Performance", "Multimilionário", "Kits de Recorrência & CRO de Checkout", "99%", "Otimização de páginas de kits promocionais e assinatura mensal de suplementos.", "@duxnutritionlab", "https://www.duxnutrition.com"),
    ("True Source", "Shopify", "Suplementos Clean Label", "Grande Porte D2C", "Páginas Promocionais de Lançamento & SEO", "98%", "Criação de landing pages focadas em pureza de ingredientes e tabela nutricional visual.", "@truesourcebrasil", "https://www.truesource.com.br"),
    ("Ocean Drop", "Shopify", "Superfoods & Algas", "Escala D2C", "CRO em Mobile & Testes A/B de Ofertas", "98%", "Testes A/B na jornada de carrinho para aumentar ticket médio com combos de saúde.", "@oceandrop", "https://www.oceandrop.com.br"),
    ("Pura Vida", "Shopify", "Nutrição Saudável & Bem-Estar", "Enterprise D2C", "SEO Técnico de Categorias & Upsell", "98%", "Arquitetura para ranquear ingredientes no Google e táticas de One-Click Upsell.", "@puravida.com.br", "https://www.puravida.com.br"),
    ("Desinchá / Desin", "Shopify", "Chás Funcionais & Vitaminas", "Multimilionário", "LPs de Oferta Agressiva & Criativos", "99%", "Desenvolvimento de páginas promocionais sazonais (Verão, Black Friday) com alta tração.", "@desincha", "https://www.desincha.com.br"),
    ("Mais Mu", "Nuvemshop", "Proteínas & Snacks Saudáveis", "Grande Porte", "CRO de Páginas de Produto & Cross-Sell", "98%", "Otimização visual de benefícios e adição de kits 'Monte sua Caixa' no carrinho.", "@maismu", "https://www.maismu.com.br"),
    ("Dobro", "Shopify", "Nutrição Esportiva Vegetal", "Médio/Grande Porte", "SEO de Nicho & CRO de Assinatura", "97%", "Estratégia de conteúdo orgânico para atletas e simplificação do funil de compra direta.", "@soudobro", "https://www.soudobro.com.br"),
    ("Nutrify", "Shopify", "Nutrição Limpa & Saudável", "Grande Porte D2C", "CRO de Páginas de Ingredientes & Confiança", "98%", "Design de selos de pureza, laudos em destaque e prova social para converter primeiras compras.", "@nutrify.com.br", "https://www.nutrify.com.br"),
    ("Always Fit", "Shopify", "Vitaminas & Saúde Diária", "Médio Porte D2C", "Tracking Server-Side (CAPI) & CRO", "97%", "GTM Server-side para blindar dados de tráfego pago e redução do abandono de carrinho.", "@alwaysfitoficial", "https://www.alwaysfit.com.br"),
    ("Haoma", "Shopify", "Chocolates Saudáveis & Doces Finos", "Grande Porte", "Visual Merchandising & Páginas Festivas", "98%", "Páginas promocionais temáticas para datas comemorativas e kits de presente de alto ticket.", "@haomacream", "https://www.haoma.com.br"),

    # === SKINCARE & BELEZA (COMPRA POR IMPULSO E ALTO TICKET) ===
    ("Principia", "Shopify", "Skincare D2C de Alta Performance", "Multimilionário", "CRO Avançado & Páginas de Rotina Facial", "99%", "Criação de montador interativo de 'Rotina de Skincare' que eleva a taxa de conversão.", "@principiaskincare", "https://www.principiaskincare.com.br"),
    ("Creamy Skincare", "Shopify", "Dermocosméticos & Ácidos", "Escala Massiva", "CRO de Checkout & Recompra", "99%", "Otimização de páginas de lançamento de fórmulas novas e estímulo de reposição de produto.", "@creamy.skincare", "https://www.creamy.com.br"),
    ("Sallve", "Shopify", "Cosméticos Nativos Digitais", "Multimilionário", "Experimentos de CRO & LPs de Conteúdo", "98%", "Páginas de produto orientadas à comunidade, reviews dinâmicos e testes A/B de CTAs.", "@sallve", "https://www.sallve.com.br"),
    ("Simple Organic", "Shopify", "Clean Beauty Orgânica", "Enterprise D2C", "Auditoria de CRO & Velocidade Mobile", "98%", "Redução de tempo de carregamento em mobile e vitrines de produtos sustentáveis.", "@simpleorganic", "https://www.simpleorganic.com.br"),
    ("Care Natural Beauty", "Shopify", "Beleza Limpa & Biotecnológica", "Grande Porte", "CRO de Páginas de Maquiagem & Tratamento", "98%", "Melhoria na visualização de tons de pele e comparativos antes/depois no tema.", "@carenb.br", "https://www.carenb.com"),
    ("Beyoung", "Shopify", "Skincare & Tratamento Anti-Idade", "Escala Massiva", "LPs Promocionais de Alta Conversão", "99%", "Arquitetura de Landing Pages de conversão agressiva conectadas com criativos de mídia paga.", "@beyoung", "https://www.beyoung.com.br"),
    ("Océane", "Shopify", "Maquiagem & Acessórios de Beleza", "Grande Porte Omnichannel", "SEO de Categorias & Coleções em Destaque", "98%", "Otimização de navegação de catálogo extenso e coleções em colaboração com celebridades.", "@oceane", "https://www.oceane.com.br"),
    ("Lola Cosmetics", "Shopify", "Beleza & Cosméticos Capilares", "Grande Escala", "SEO Técnico & Organização de Linhas", "97%", "Arquitetura para ranquear cronogramas capilares no Google e converter compras combinadas.", "@lolacosmetics", "https://www.lolacosmetics.com.br"),
    ("Alice Salazar Store", "Nuvemshop", "Maquiagem & Beleza", "Grande Porte", "CRO de Mobile & Vitrines de Tutoriais", "97%", "Páginas de produto integrando tutoriais em vídeo e botão de compra rápida no Nuvemshop.", "@alicesalazarstore", "https://www.alicesalazarstore.com.br"),
    ("ISZI", "Nuvemshop", "Tratamento Capilar Profissional", "Nuvemshop Next", "CRO de Funil & Kits de Tratamento", "98%", "Estruturação de kits completos de recuperação capilar para elevar o ticket médio.", "@iszicosmeticos", "https://www.iszi.com.br"),
    ("Quintal Dermocosméticos", "Shopify", "Argilas & Tratamento Facial", "Médio/Grande Porte", "CRO & Páginas de Ingredientes Naturais", "97%", "Design de storytelling de ingredientes medicinais que geram autoridade e venda imediata.", "@quintal.dermocosmeticos", "https://www.quintaldermocosmeticos.com.br"),
    ("Pink Cheeks", "Nuvemshop", "Cosméticos para Atletas", "Médio Porte D2C", "CRO para Linhas Esportivas & Kits", "97%", "Páginas orientadas a protetores que não escorrem no treino e kits de maratona.", "@pinkcheeksbrasil", "https://www.pinkcheeks.com.br"),

    # === MODA, CALÇADOS & STREETWEAR (ALTO DESEJO E VOLUME) ===
    ("Insider Store", "Shopify", "Moda Tecnológica & Essenciais", "Multimilionário", "CRO Massivo & Testes Contínuos de PDP", "99%", "Testes A/B de páginas de produto focadas em atributos tecnológicos (anti-odor, anti-suor).", "@insiderstore", "https://www.insiderstore.com.br"),
    ("PatBO", "Shopify", "Moda Feminina Autoral de Luxo", "Escala Internacional", "Experiência de Compra Mobile de Alto Luxo", "98%", "Navegação premium que valoriza bordados manuais sem travar no celular e checkout ágil.", "@patbo_brasil", "https://www.patbo.com.br"),
    ("Approve", "Shopify", "Streetwear & Cultura Jovem", "Multimilionário", "Páginas de Drops & Alta Demanda", "99%", "Otimização de front-end para aguentar milhares de acessos simultâneos no dia do drop.", "@justapprove", "https://www.justapprove.com.br"),
    ("Pace Company", "Shopify", "Streetwear Conceitual de Luxo", "Grande Porte D2C", "Design Minimalista de Coleções & Imersão", "98%", "Visual merchandising minimalista e exclusivo, garantindo experiência de marca sofisticada.", "@pacecompany", "https://www.pacecompany.com.br"),
    ("Baw Clothing", "Nuvemshop", "Streetwear & Moda Jovem", "Escala Nacional", "CRO de Promoções Relâmpago & Vitrines", "98%", "Táticas de banner interativo e ofertas progressivas (Compre 2, Leve 3) direto no tema.", "@bawclothing", "https://www.bawclothing.com.br"),
    ("Live! Oficial", "Shopify", "Moda Fitness & Beachwear", "Multimilionário", "SEO de Categorias Esportivas & Coleções", "98%", "Arquitetura para termos como leggings de compressão, biquínis e moda fitness premium.", "@liveoficial", "https://www.liveoficial.com.br"),
    ("Yuool", "Shopify", "Calçados Confortáveis de Lã Merino", "Grande Porte D2C", "CRO de Escolha de Modelo & Conforto", "98%", "Redução de dúvidas sobre uso sem meia, tabela de medidas intuitiva e prova social.", "@yuoolbr", "https://www.yuool.com.br"),
    ("Linus", "Shopify", "Sandálias Veganas & Sustentáveis", "Grande Porte D2C", "SEO Verde & Otimização de Carregamento", "99%", "Posicionamento para calçados ergonômicos e páginas com história da marca de alta conversão.", "@lojalinus", "https://www.lojalinus.com.br"),
    ("Zissou", "Shopify", "Colchões e Conforto do Sono", "Grande Porte D2C", "Conversão de Alto Ticket & Garantia de 100 Dias", "97%", "Páginas que quebram objeção de compra de colchão pela internet com teste de 100 dias.", "@zissoubr", "https://www.zissou.com.br"),
    ("LV Store", "Nuvemshop", "Moda Feminina Independente", "Multimilionário", "CRO Mobile para Tráfego de Instagram", "99%", "Estrutura ágil para visitantes que chegam direto dos Stories da fundadora comprarem rápido.", "@lvstore", "https://www.lvstore.com.br"),
    ("Saint Germain", "Nuvemshop", "Relógios & Acessórios Minimalistas", "Grande Porte D2C", "Upsell de Pulseiras no Checkout & CRO", "98%", "Adição de pop-ups de oferta complementar de pulseiras combinando com o relógio.", "@saintgermain", "https://www.saintgermainbrand.com.br"),
    ("Key Design", "Nuvemshop", "Joias & Acessórios Masculinos", "Grande Escala", "CRO de Estilo Masculino & Checkout Limpo", "98%", "Guia de medidas de pulso interativo e compra rápida em um clique para público masculino.", "@keydesign", "https://www.keydesign.com.br"),
    ("Desgosto", "Nuvemshop", "Streetwear Autoral", "Médio Porte D2C", "SEO de Produtos Exclusivos & Drops", "97%", "Arquitetura para produtos numerados e escassez visual no botão de compra.", "@desgosto.clothing", "https://www.desgosto.com.br"),
    ("Insânia", "Nuvemshop", "Vestidos Românticos & Festas", "Grande Porte", "Carregamento Rápido de Fotos de Alta Resolução", "98%", "Otimização de imagens pesadas para garantir navegação fluida em catálogo volumoso.", "@insaniapublicidade", "https://www.insania.com.br"),
    ("Livo Eyewear", "Shopify", "Óculos de Grau & Sol de Design", "Médio/Grande Porte", "Provador Virtual UX & CRO de Armações", "96%", "Melhoria na experiência de escolher armações pelo formato de rosto no Shopify.", "@livoeyewear", "https://www.livo.com.br"),
    ("Herself", "Shopify", "Moda Íntima Sustentável", "Médio/Grande Porte", "CRO de Escolha de Fluxo & Absorção", "98%", "Quiz interativo de fluxo menstrual para sugerir o modelo exato e aumentar a conversão.", "@herselfbrasil", "https://www.herself.com.br"),
    ("Dobra", "Shopify", "Carteiras & Acessórios Especiais", "Médio Porte D2C", "Storytelling & Personalização de Produto", "97%", "Página de produto interativa permitindo visualizar estampas de artistas colaboradores.", "@querodobra", "https://www.querodobra.com.br"),
    ("Zee.Dog", "Nuvemshop", "Acessórios Pet de Design Global", "Escala Global", "SEO Omnichannel & Recompra de Petiscos", "98%", "Estratégia de páginas temáticas de coleções especiais (Marvel, Disney) de alta conversão.", "@zeedog", "https://www.zeedog.com.br")
]

linhas = []
for marca, plat, nicho, porte, oportunidade, match, pitch, insta, site in PLAYERS_ALTO_POTENCIAL:
    link_site = f'=HYPERLINK("{site}"; "Acessar Loja ↗")'
    termo_linkedin = urllib.parse.quote(f"{marca} (Dono OR Founder OR CEO OR \"Gerente de Ecommerce\" OR \"Head de Growth\")")
    link_decisor = f'=HYPERLINK("https://www.linkedin.com/search/results/people/?keywords={termo_linkedin}"; "Falar com Decisor 👤")'

    linhas.append([
        hoje,                   # Coluna 1: Data
        marca,                  # Coluna 2: Marca
        plat,                   # Coluna 3: Plataforma
        nicho,                  # Coluna 4: Nicho
        f"{porte} | {oportunidade}", # Coluna 5: Porte & Oportunidade
        "João Gobira — Especialista de Growth & Site Sênior.pdf", # Coluna 6: Currículo Base
        match,                  # Coluna 7: Match %
        pitch,                  # Coluna 8: Pitch
        insta,                  # Coluna 9: Instagram
        link_site,              # Coluna 10: Link da Loja
        link_decisor,           # Coluna 11: Decisor no LinkedIn
        "🟡 A Prospectar"       # Coluna 12: Status
    ])

payload = {
    "action": "limparEAtualizar",
    "linhas": linhas
}

print(f"Disparando {len(linhas)} players de alta receita (Suplementos, Skincare e Moda) para a planilha...")
resp = requests.post(API_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"}, allow_redirects=True, timeout=30)
print("Status envio:", resp.status_code)
print("Resposta:", resp.text)

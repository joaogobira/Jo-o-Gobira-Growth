import requests
import json
import urllib.parse
from datetime import datetime

API_URL = "https://script.google.com/macros/s/AKfycbwaoMB2seAopWUA6CLobSxu1OY7MINEnn6MOTnslBRZuMazMsvdQAc0DJnS3TODnlvy/exec"
hoje = datetime.now().strftime("%d/%m/%Y")

marcas_expandidas = [
    # SHOPIFY
    ("PatBO", "Shopify", "Moda Feminina Luxo", "Escala Enterprise", "Auditoria de CRO e Redução de Abandono de Checkout", "98%", "Otimização de checkout e jornada de compra mobile para elevar o ticket médio e taxa de conversão.", "@patbo_brasil", "https://www.patbo.com.br"),
    ("Linus", "Shopify", "Calçados & Sustentabilidade", "Grande Porte D2C", "SEO Técnico & Otimização de Performance Web", "99%", "Case de +200% de orgânico; posicionamento para novos termos de sustentabilidade e Core Web Vitals.", "@lojalinus", "https://www.lojalinus.com.br"),
    ("Simple Organic", "Shopify", "Cosméticos & Clean Beauty", "Enterprise D2C", "CRO & Testes A/B em Páginas de Produto (PDP)", "98%", "Testes A/B focados em conversão de primeira compra e prova social com reviews.", "@simpleorganic", "https://www.simpleorganic.com.br"),
    ("Lola Cosmetics", "Shopify", "Beleza & Haircare", "Grande Escala", "SEO de E-commerce & Arquitetura de Categorias", "97%", "Estrutura semântica para ranquear topo do Google em categorias capilares sem depender só de ads.", "@lolacosmetics", "https://www.lolacosmetics.com.br"),
    ("Herself", "Shopify", "Moda Íntima & Sustentável", "Médio/Grande Porte", "CRO & Aceleração de Taxa de Conversão", "98%", "Redução de fricção no funil de escolha de tamanho e aumento de conversão direta.", "@herselfbrasil", "https://www.herself.com.br"),
    ("Always Fit", "Shopify", "Saúde & Suplementação", "Médio Porte", "Geração de Demanda & Tracking Server-Side (CAPI)", "97%", "Blindagem de dados com GTM Server-Side contra perda de sinal para reduzir CAC em mídia paga.", "@alwaysfitoficial", "https://www.alwaysfit.com.br"),
    ("Insider Store", "Shopify", "Moda Tech & Essenciais", "Escala Massiva", "CRO Avançado & Personalização de Ofertas", "99%", "Maximização de receita por visitante e testes contínuos de usabilidade e checkout.", "@insiderstore", "https://www.insiderstore.com.br"),
    ("Yuool", "Shopify", "Calçados Conforto & Lã", "Grande Porte D2C", "SEO Orgânico & Testes A/B de Conversão", "98%", "Aumento de tração orgânica e otimização de velocidade de carregamento em mobile.", "@yuoolbr", "https://www.yuool.com.br"),
    ("Zissou", "Shopify", "Colchões & Sono D2C", "Grande Porte D2C", "Estratégia de Funil Completo & Conversão de Alto Ticket", "97%", "Otimização de páginas de conversão para produtos de alto valor percebido.", "@zissoubr", "https://www.zissou.com.br"),
    ("Sallve", "Shopify", "Skincare & Cosméticos D2C", "Enterprise D2C", "CRO & Experimentos de Onboarding de Produto", "98%", "Táticas de experimentação rápida para impulsionar cross-sell e compra recorrente.", "@sallve", "https://www.sallve.com.br"),
    ("Livo Eyewear", "Shopify", "Óculos & Acessórios", "Médio/Grande Porte", "CRO & Provador Virtual UX", "96%", "Melhoria da experiência de navegação e aumento de conversão mobile no Shopify.", "@livoeyewear", "https://www.livo.com.br"),
    ("Dobra", "Shopify", "Carteiras & Acessórios", "Médio Porte D2C", "SEO Criativo & Taxa de Conversão", "97%", "Engajamento de comunidade aliado a funil de checkout com fricção zero.", "@querodobra", "https://www.querodobra.com.br"),
    ("Live!", "Shopify", "Moda Fitness & Beachwear", "Grande Escala", "SEO Técnico Enterprise & CRO de Coleções", "98%", "Estruturação de filtros e categorias para grandes volumes de buscas sazonais.", "@liveoficial", "https://www.liveoficial.com.br"),
    ("Haoma", "Shopify", "Doces Finos & Saudáveis", "Médio/Grande Porte", "CRO de Páginas de Produto & Apelo Visual", "97%", "Otimização de checkout e estratégias visuais para conversão imediata.", "@haomacream", "https://www.haoma.com.br"),

    # NUVEMSHOP
    ("LV Store", "Nuvemshop", "Moda Feminina D2C (Escala)", "Multimilionário", "Auditoria de CRO & Redução de Abandono de Carrinho", "99%", "Otimização da experiência mobile e testes A/B para suportar picos de tráfego de influenciadores.", "@lvstore", "https://www.lvstore.com.br"),
    ("Saint Germain", "Nuvemshop", "Relógios & Acessórios", "Grande Porte D2C", "CRO de Checkout & Aumento de Ticket Médio", "98%", "Estratégia de upsell/cross-sell no checkout e melhoria de carregamento em dias de promoção.", "@saintgermain", "https://www.saintgermainbrand.com.br"),
    ("Alice Salazar Store", "Nuvemshop", "Maquiagem & Linha de Beleza", "Grande Porte", "SEO Técnico & Conversão em Mobile", "97%", "Aumento de autoridade orgânica para termos de maquiagem e melhoria da vitrine virtual.", "@alicesalazarstore", "https://www.alicesalazarstore.com.br"),
    ("ISZI", "Nuvemshop", "Cosméticos & Haircare", "Nuvemshop Next", "CRO & Otimização de Funil de Conversão", "98%", "Redução de pontos de desistência entre carrinho e pagamento na Nuvemshop Next.", "@iszicosmeticos", "https://www.iszi.com.br"),
    ("Duhellen", "Nuvemshop", "Moda Íntima & Modeladores", "Operação Robusta", "CRO & Tabela de Medidas Interativa", "98%", "Redução de devoluções e aumento de taxa de conversão em moda íntima.", "@duhellen.lingerie", "https://www.duhellen.com.br"),
    ("Desgosto", "Nuvemshop", "Streetwear & Vestuário", "Médio Porte D2C", "SEO para Drops e Lançamentos", "97%", "Arquitetura para suportar tráfego concentrado em dias de lançamento de peças exclusivas.", "@desgosto.clothing", "https://www.desgosto.com.br"),
    ("Insânia", "Nuvemshop", "Vestidos & Moda Romântica", "Grande Porte", "Otimização de Vitrines e CRO Mobile", "98%", "Aprimoramento de velocidade de carregamento de fotos em alta resolução.", "@insaniapublicidade", "https://www.insania.com.br"),
    ("Key Design", "Nuvemshop", "Joias & Acessórios Masculinos", "Grande Escala", "SEO Técnico & Estratégia de CRO", "98%", "Foco em conversão de público masculino, redução de cliques até o pagamento e SEO de produto.", "@keydesign", "https://www.keydesign.com.br"),
    ("Gocase", "Nuvemshop", "Acessórios & Personalizados", "Multimilionário", "CRO de Customização de Produtos", "99%", "Otimização da ferramenta de personalização em tempo real e checkout transparente.", "@gocasebr", "https://www.gocase.com.br"),
    ("Baw Clothing", "Nuvemshop", "Streetwear & Moda Jovem", "Escala Nacional", "Performance de Site & CRO de Drops", "98%", "Testes de usabilidade e retenção de audiência jovem vinda do Instagram e TikTok.", "@bawclothing", "https://www.bawclothing.com.br"),
    ("Zee.Dog", "Nuvemshop", "Lifestyle Pet & Acessórios", "Escala Global", "SEO & Otimização de Experiência Omnichannel", "98%", "Posicionamento orgânico de produtos e melhoria de conversão de compras recorrentes.", "@zeedog", "https://www.zeedog.com.br")
]

linhas = []
for marca, plat, nicho, porte, servico, match, pitch, insta, site in marcas_expandidas:
    link_site = f'=HYPERLINK("{site}"; "Acessar Loja ↗")'
    termo_linkedin = urllib.parse.quote(f"{marca} (Dono OR Founder OR CEO OR \"Gerente de Ecommerce\" OR \"Head de Growth\")")
    link_decisor = f'=HYPERLINK("https://www.linkedin.com/search/results/people/?keywords={termo_linkedin}"; "Falar com Decisor 👤")'

    linhas.append([
        hoje,                   # Coluna 1: Data
        marca,                  # Coluna 2: Marca
        plat,                   # Coluna 3: Plataforma
        nicho,                  # Coluna 4: Nicho
        f"{porte} | {servico}", # Coluna 5: Porte & Oportunidade
        "João Gobira — Especialista de Growth & Site Sênior.pdf", # Coluna 6: Currículo
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

print(f"Enviando {len(linhas)} marcas de e-commerce com 12 colunas completas...")
resp = requests.post(API_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"}, allow_redirects=True, timeout=30)
print("Status envio:", resp.status_code)
print("Resposta:", resp.text)

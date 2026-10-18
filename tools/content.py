# Single source of truth for all copy (EN + PT) and image alt text.
# build.py reads this to emit static HTML, and to write assets/js/i18n.js.

C = {
 "nav_home": ("Home", "Início"),
 "nav_company": ("The Company", "A Empresa"),
 "nav_facility": ("Production Facility", "Instalações de Produção"),
 "nav_showroom": ("Showroom", "Showroom"),
 "nav_sust": ("Sustainability", "Sustentabilidade"),
 "nav_contacts": ("Contacts", "Contactos"),
 "menu": ("Menu", "Menu"),
 "close": ("Close", "Fechar"),

 "title_home": ("Crafting Sustainable Fashion: Leading Manufacturer of Slow Fashion Garments for Brands",
                "Moda sustentável: fabricante de referência de vestuário slow fashion para marcas"),
 "title_showroom": ("Virtual Fashion Showroom, Reguentex", "Showroom de Moda Virtual, Reguentex"),
 "title_sust": ("Sustainability — Reguentex", "Sustentabilidade — Reguentex"),

 "hero_title": ("Fashion-Oriented Garments", "Vestuário orientado para a moda"),
 "hero_cta": ("See our work", "Ver o nosso trabalho"),
 "hero_text": ("At Reguentex, we offer unparalleled expertise in producing high-quality garments at market-leading prices. Innovation, sustainability and continuous process improvement are key drivers in our work. This extends not only to our workforce but also our impact in the local community and the environment that surrounds us as well.",
               "Na Reguentex, oferecemos uma experiência inigualável na produção de vestuário de elevada qualidade a preços competitivos. A inovação, a sustentabilidade e a melhoria contínua dos processos são os motores do nosso trabalho, e estendem-se não só aos nossos colaboradores, mas também ao nosso impacto na comunidade local e no ambiente que nos rodeia."),

 "company_title": ("The Company", "A Empresa"),
 "company_p1": ("Based in São Tomé de Negrelos, Portugal, Reguentex was created and established in 1998 and is currently led by Idalina Ribeiro, José Coutinho and Alberto Gonçalves. Together, they each have more than 35 years of experience in the clothing industry.",
                "Sediada em São Tomé de Negrelos, Portugal, a Reguentex foi criada e estabelecida em 1998 e é atualmente liderada por Idalina Ribeiro, José Coutinho e Alberto Gonçalves. Juntos, cada um deles conta com mais de 35 anos de experiência na indústria do vestuário."),
 "company_p2": ("We specialize in the production of high-quality, sustainable fashion and casual garments for men, women and kidswear. We are also adept at producing a range of more technical garments, including sportswear, sleepwear and homewear.",
                "Especializamo-nos na produção de vestuário de moda e casual, sustentável e de elevada qualidade, para homem, mulher e criança. Somos igualmente exímios na produção de uma gama de peças mais técnicas, incluindo roupa desportiva, de dormir e de casa."),
 "company_p3": ("At Reguentex we oversee the entire manufacturing process, from initial development and sourcing through to quality control, production and shipping.",
                "Na Reguentex supervisionamos todo o processo de fabrico, desde o desenvolvimento inicial e o aprovisionamento até ao controlo de qualidade, à produção e à expedição."),
 "company_cta": ("See our production facility", "Ver as nossas instalações de produção"),

 "fac_title": ("Production Facility", "Instalações de Produção"),
 "fac_intro": ("At Reguentex we carry out everything in-house and are able to conveniently provide clients with everything that they need to develop, produce and source a high-quality end product. From finding the right material, designing patterns and selecting prints/embroideries, through to cutting and packing, we manage everything for you.",
               "Na Reguentex fazemos tudo internamente e conseguimos fornecer, com toda a comodidade, tudo o que os clientes precisam para desenvolver, produzir e aprovisionar um produto final de elevada qualidade. Desde a escolha do material, a criação de moldes e a seleção de estampados/bordados, até ao corte e à embalagem, tratamos de tudo por si."),
 "pm_title": ("Pattern Making & Cutting Area", "Modelação e Corte"),
 "pm_p1": ("Our equipment allows for both manual working and the use of CAD-assisted design. This allows us to find an approach that works for you as we can easily adapt our processes based on the materials you want to use and the end product you want to produce.",
           "O nosso equipamento permite tanto o trabalho manual como o desenho assistido por CAD. Isto permite-nos encontrar a abordagem certa para si, pois adaptamos facilmente os nossos processos aos materiais que pretende utilizar e ao produto final que quer produzir."),
 "pm_p2": ("Our investment in pattern placing software has helped to significantly optimise our manufacturing process and keep the waste of raw materials to an absolute minimum.",
           "O investimento em software de encaixe de moldes ajudou a otimizar significativamente o nosso processo de fabrico e a reduzir ao mínimo o desperdício de matérias-primas."),
 "pl_title": ("Production Line", "Linha de Produção"),
 "pl_p1": ("At Reguentex we currently have two production lines that allow us to simultaneously produce both larger scale and smaller, more intricate orders.",
           "Atualmente, a Reguentex dispõe de duas linhas de produção que nos permitem produzir em simultâneo encomendas de maior escala e encomendas mais pequenas e intrincadas."),
 "pl_p2": ("Both our lines are able to produce a wide variety of high-quality products from different materials, including pieces that are traditionally more difficult to manufacture.",
           "Ambas as linhas são capazes de produzir uma grande variedade de produtos de elevada qualidade, em diferentes materiais, incluindo peças tradicionalmente mais difíceis de confecionar."),
 "pq_title": ("Packing and Quality Control Area", "Embalagem e Controlo de Qualidade"),
 "pq_p1": ("We understand quality control is critical to an end product. Throughout the production process, we undertake both internal and external checks at every stage, from development right through to the shipping of the final order.",
           "Sabemos que o controlo de qualidade é fundamental para o produto final. Ao longo de todo o processo de produção, realizamos verificações internas e externas em todas as fases, desde o desenvolvimento até à expedição da encomenda final."),
 "pq_p2": ("We offer a number of different packing and shipping options that we can tailor to your needs. Reguentex is also proud to offer alternatives to plastic packaging as part of our drive to keep waste to a minimum.",
           "Oferecemos várias opções de embalagem e expedição, adaptadas às suas necessidades. A Reguentex tem também o orgulho de propor alternativas às embalagens de plástico, como parte do nosso esforço para minimizar os resíduos."),

 "press_title": ("Press", "Imprensa"),
 "int_label": ("Interview with a co-founder", "Entrevista a uma cofundadora"),
 "int_name": ("Idalina Ribeiro", "Idalina Ribeiro"),
 "int_quote": ("“I do not live of memories. My life is projecting the future”",
               "“Não vivo de memórias. A minha vida é projetar o futuro”"),
 "int_link": ("Full article", "Artigo completo"),
 "inaug_title": ("Inauguration through the eyes of the city council", "A inauguração pelos olhos da Câmara Municipal"),
 "inaug_link": ("full post", "publicação completa"),

 "contacts_title": ("Contacts", "Contactos"),
 "addr_label": ("Address:", "Morada:"),
 "gps_label": ("GPS Coordinates:", "Coordenadas GPS:"),
 "map_link": ("Open in maps", "Abrir no mapa"),
 "social_label": ("Social media:", "Redes sociais:"),
 "contacts_label": ("Contacts:", "Contactos:"),
 "back_top": ("Voltar ao topo", "Voltar ao topo"),
 "rights": ("All rights reserved.", "Todos os direitos reservados."),

 "sh_title": ("Virtual Showroom", "Showroom Virtual"),
 "sh_p": ("Now you no longer need to travel to be able to see our Showroom. To access our Virtual Showroom, you need to submit your request to see it, as well as your email, where we will send the information you need.",
          "Já não precisa de se deslocar para visitar o nosso showroom. Para aceder ao Showroom Virtual, tem de submeter o seu pedido, juntamente com o seu email, para onde enviaremos a informação de que necessita."),
 "sh_form_title": ("Submit your request here:", "Submeta aqui o seu pedido:"),
 "f_name": ("Name", "Nome"),
 "f_company": ("Company", "Empresa"),
 "f_email": ("Email", "Email"),
 "f_message": ("Message", "Mensagem"),
 "f_send": ("Request access", "Pedir acesso"),
 "f_ok": ("Thank you — your request has been sent.", "Obrigado — o seu pedido foi enviado."),
 "f_mail": ("Opening your email app…", "A abrir a sua aplicação de email…"),
 "f_err": ("Something went wrong. Please email geral@reguentex.pt.", "Ocorreu um erro. Por favor envie email para geral@reguentex.pt."),
 "f_msg_default": ("I would like to request access to the Virtual Showroom.", "Gostaria de pedir acesso ao Showroom Virtual."),

 "sust_title": ("Sustainability", "Sustentabilidade"),
 "sust_sub": ("A trip to our Garden", "Uma visita à nossa Horta"),
 "sust_p": ("At Reguentex, our sustainability initiatives extend beyond textile production and into the garden as well! We grow our own fresh, organic vegetables onsite and use them to create a delicious daily soup for our employees. We’ve worked hard to optimise the space we have available which means we can grow many different types of vegetables organically, without the use of any pesticides or chemicals.",
            "Na Reguentex, as nossas iniciativas de sustentabilidade vão além da produção têxtil e chegam também à horta! Cultivamos no local os nossos próprios legumes frescos e biológicos e usamo-los para fazer uma deliciosa sopa diária para os nossos colaboradores. Esforçámo-nos por otimizar o espaço disponível, o que nos permite cultivar muitos tipos de legumes de forma biológica, sem recurso a pesticidas ou químicos."),
}

# image key (filename without extension) -> (EN alt, PT alt)
ALT = {
 "prateleiras-roupas": ("Garments on rails in the Reguentex showroom", "Peças em cabides no showroom da Reguentex"),
 "fabrica-exterior": ("Reguentex factory exterior among trees", "Exterior da fábrica Reguentex entre árvores"),
 "editada4": ("Sewing machine finishing a pale blue garment", "Máquina de costura a acabar uma peça azul clara"),
 "dsc_0150": ("Shelving corridor with fabric rolls", "Corredor de prateleiras com rolos de tecido"),
 "dsc_0412": ("Rolls of fabric on warehouse shelves", "Rolos de tecido nas prateleiras do armazém"),
 "dsc_0419": ("Automated cutting table over layered fabric", "Mesa de corte automático sobre camadas de tecido"),
 "dsc_0429": ("Cutting head moving over white fabric", "Cabeça de corte sobre tecido branco"),
 "dsc_0442": ("White fabric feeding through the cutting machine", "Tecido branco a passar na máquina de corte"),
 "tecidos-embrulhados": ("Leopard print and cream silk fabric", "Tecido de seda creme e estampado leopardo"),
 "tesoura-e-anota-es": ("Scissors and notes on leopard print fabric", "Tesoura e notas sobre tecido estampado leopardo"),
 "dsc_0426": ("CAD pattern placement on a monitor", "Encaixe de moldes em CAD no monitor"),
 "dsc_0423": ("Pattern-making software on screen", "Software de modelação no ecrã"),
 "20200204_130313": ("Hands guiding fabric under a sewing machine", "Mãos a guiar o tecido numa máquina de costura"),
 "lrm_export_104311552477642_20200203_172744118": ("Floral fabric being sewn", "Tecido florido a ser cosido"),
 "lrm_export_144214090638323_20200204_172709216": ("Industrial machine stitching a patterned strip", "Máquina industrial a coser uma tira estampada"),
 "cones-de-linho-edit": ("Thread cones at a sewing station", "Cones de linha num posto de costura"),
 "dsc_0464": ("Production line with a thread cone in the foreground", "Linha de produção com cone de linha em primeiro plano"),
 "dsc_0487": ("Seamstresses working on the production line", "Costureiras na linha de produção"),
 "editada8": ("Pressing a leopard print seam", "Passagem a ferro de uma costura estampada"),
 "lrm_export_128066549814607_20200204_095605191": ("Measuring tape, scissors and spec sheet", "Fita métrica, tesoura e ficha técnica"),
 "lrm_export_104308057480645_20200203_172740623": ("Garments laid out for quality control", "Peças dispostas para controlo de qualidade"),
 "0302-2020": ("Cartons ready for shipping", "Caixas prontas para expedição"),
 "lrm_export_104323411856480_20200203_172755977": ("Tagged garment being checked", "Peça etiquetada em verificação"),
 "dsc_0453": ("Garment being pressed by hand", "Peça a ser passada a ferro à mão"),
 "dsc_0456": ("Folded dark garments ready for packing", "Peças escuras dobradas prontas a embalar"),
 "cartao-reguentex": ("Reguentex garment tag", "Etiqueta de peça Reguentex"),
 "image00003": ("Newspaper feature on Reguentex", "Artigo de jornal sobre a Reguentex"),
 "entrevista": ("Idalina Ribeiro and her partners at the inauguration", "Idalina Ribeiro e os sócios na inauguração"),
 "dsc_0200": ("Inauguration: guests posing with the founders", "Inauguração: convidados com os fundadores"),
 "dsc_0206": ("Inauguration: a guest signing the wall", "Inauguração: um convidado a assinar a parede"),
 "dsc_0212": ("Inauguration: founders welcoming guests", "Inauguração: fundadores a receber convidados"),
 "dsc_0251": ("Inauguration: group conversation", "Inauguração: conversa em grupo"),
 "dsc_0261": ("Inauguration: guests with a commemorative gift", "Inauguração: convidados com uma lembrança"),
 "dsc_0282": ("Inauguration: group portrait", "Inauguração: retrato de grupo"),
 "dsc_0170": ("Welcome card and flowers at the inauguration", "Cartão de boas-vindas e flores na inauguração"),
 "dsc_0521": ("Garden path and trees beside the factory", "Caminho e árvores da horta junto à fábrica"),
 "dsc_0524": ("Vegetable beds along the factory wall", "Canteiros de legumes junto à fábrica"),
 "dsc_0526": ("Cabbages growing in the garden", "Couves a crescer na horta"),
 "dsc_0529": ("Potato plants in flower", "Batateiras em flor"),
 "dsc_0535": ("Rows of organic vegetables", "Linhas de legumes biológicos"),
 "dsc_0543": ("Narrow path between the factory and the garden", "Caminho estreito entre a fábrica e a horta"),
 "dsc_0706": ("Pond in the garden", "Lago na horta"),
 "dsc_0714": ("Tree-lined garden path", "Caminho da horta ladeado de árvores"),
 "dsc_0605": ("Rails of colourful sample garments", "Cabides com peças de amostra coloridas"),
 "dsc_0108": ("Showroom rail with orange knitwear", "Cabide do showroom com malhas laranja"),
 "dsc_0104": ("Showroom shelving with neutral garments", "Prateleiras do showroom com peças neutras"),
}

PM = ["dsc_0150", "dsc_0412", "dsc_0419", "dsc_0429", "dsc_0442", "tecidos-embrulhados", "tesoura-e-anota-es", "dsc_0426", "dsc_0423"]
PL = ["20200204_130313", "lrm_export_104311552477642_20200203_172744118", "lrm_export_144214090638323_20200204_172709216", "cones-de-linho-edit", "dsc_0464", "dsc_0487"]
PQ = ["editada8", "lrm_export_128066549814607_20200204_095605191", "lrm_export_104308057480645_20200203_172740623", "0302-2020", "lrm_export_104323411856480_20200203_172755977", "dsc_0453", "dsc_0456", "cartao-reguentex"]
INAUG = ["dsc_0200", "dsc_0206", "dsc_0212", "dsc_0251", "dsc_0261", "dsc_0282"]
GARDEN = ["dsc_0521", "dsc_0524", "dsc_0526", "dsc_0529", "dsc_0535", "dsc_0543", "dsc_0706", "dsc_0714"]
SHOW = ["dsc_0605", "dsc_0108", "dsc_0104", "prateleiras-roupas"]

URL = {
 "fb": "https://www.facebook.com/reguentex/",
 "li": "https://www.linkedin.com/company/reguentex/",
 "ig": "https://www.instagram.com/reguentex/",
 "tt": "https://www.tiktok.com/@reguentex_",
 "article": "https://jornalentremargens.com/2022/06/28/entrevista-idalina-ribeiro-nao-vivo-de-memorias-a-minha-vida-e-projetar-o-futuro/",
 "post": "https://m.facebook.com/CMSantoTirso/posts/pfbid0DSr3xA4Qqvg3NRCXL3ukwyrvwSHJetgDENEHQkhs29mkXTsWVrgoS1TBFQ2pKM33l",
 "map": "https://www.google.com/maps?q=41.360165,-8.397111",
 "osm": "https://www.openstreetmap.org/export/embed.html?bbox=-8.4011%2C41.3581%2C-8.3931%2C41.3622&layer=mapnik&marker=41.360165%2C-8.397111",
}
LEGAL = "Reguentex Confeções Têxteis Unipessoal, Lda."
ADDR = ["Avenida 27 de Maio, 461", "4795-545 S. Tomé de Negrelos, Santo Tirso", "Porto, Portugal"]
GPS = "41.360165, -8.397111"
PHONES = [("+351 252 874 308", "+351252874308"), ("+351 918 652 224", "+351918652224")]
EMAIL = "geral@reguentex.pt"

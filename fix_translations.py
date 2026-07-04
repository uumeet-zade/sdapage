import re

with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Dictionary of translations
trans = {
    'ga': {
        '"filter-all-cand": "All Candidates"': '"filter-all-cand": "Tous les Candidats"',
        '"filter-exec": "Executive"': '"filter-exec": "Exécutif"',
        '"filter-all": "All Events"': '"filter-all": "Tous les Événements"',
        '"filter-pres": "Presidential"': '"filter-pres": "Présidentiel"',
        '"filter-gov": "Governors"': '"filter-gov": "Gouverneurs"',
        '"filter-list": "House (Party List)"': '"filter-list": "Chambre (Liste de Parti)"',
        '"filter-senate": "Senate"': '"filter-senate": "Sénat"',
        '"filter-house": "House (Constituency)"': '"filter-house": "Chambre (Circonscription)"',
        '"ev-title-gov-1": "Reno Governor Debate"': '"ev-title-gov-1": "Débat des Gouverneurs de Reno"',
        '"ev-desc-gov-1": "Watch Safiya debate on key issues concerning the future of Reno."': '"ev-desc-gov-1": "Regardez Safiya débattre des questions clés concernant l\'avenir de Reno."',
        '"ev-title-gov-2": "Reno Community Townhall"': '"ev-title-gov-2": "Réunion Publique de Reno"',
        '"ev-desc-gov-2": "An open discussion on local community initiatives and economic growth."': '"ev-desc-gov-2": "Une discussion ouverte sur les initiatives communautaires locales et la croissance économique."',
        '"ev-title-gov-3": "Final Reno Rally"': '"ev-title-gov-3": "Rassemblement Final à Reno"',
        '"ev-desc-gov-3": "The final major rally for the Reno Governor campaign. Stand with Safiya!"': '"ev-desc-gov-3": "Le dernier grand rassemblement de la campagne pour le poste de gouverneur de Reno. Soutenez Safiya !"'
    },
    'ac': {
        '"filter-all-cand": "All Candidates"': '"filter-all-cand": "Todos los Candidatos"',
        '"filter-exec": "Executive"': '"filter-exec": "Ejecutivo"',
        '"filter-all": "All Events"': '"filter-all": "Todos los Eventos"',
        '"filter-pres": "Presidential"': '"filter-pres": "Presidencial"',
        '"filter-gov": "Governors"': '"filter-gov": "Gobernadores"',
        '"filter-list": "House (Party List)"': '"filter-list": "Cámara (Lista de Partido)"',
        '"filter-senate": "Senate"': '"filter-senate": "Senado"',
        '"filter-house": "House (Constituency)"': '"filter-house": "Cámara (Circunscripción)"',
        '"ev-title-gov-1": "Reno Governor Debate"': '"ev-title-gov-1": "Debate de Gobernadores de Reno"',
        '"ev-desc-gov-1": "Watch Safiya debate on key issues concerning the future of Reno."': '"ev-desc-gov-1": "Mira a Safiya debatir sobre temas clave para el futuro de Reno."',
        '"ev-title-gov-2": "Reno Community Townhall"': '"ev-title-gov-2": "Reunión Comunitaria de Reno"',
        '"ev-desc-gov-2": "An open discussion on local community initiatives and economic growth."': '"ev-desc-gov-2": "Una discusión abierta sobre iniciativas comunitarias locales y crecimiento económico."',
        '"ev-title-gov-3": "Final Reno Rally"': '"ev-title-gov-3": "Mitin Final en Reno"',
        '"ev-desc-gov-3": "The final major rally for the Reno Governor campaign. Stand with Safiya!"': '"ev-desc-gov-3": "El último gran mitin de la campaña para gobernador de Reno. ¡Apoya a Safiya!"'
    },
    'ra': {
        '"filter-all-cand": "All Candidates"': '"filter-all-cand": "Alle Kandidater"',
        '"filter-exec": "Executive"': '"filter-exec": "Udøvende magt"',
        '"filter-all": "All Events"': '"filter-all": "Alle Begivenheder"',
        '"filter-pres": "Presidential"': '"filter-pres": "Præsident"',
        '"filter-gov": "Governors"': '"filter-gov": "Guvernører"',
        '"filter-list": "House (Party List)"': '"filter-list": "Repræsentanternes Hus (Partiliste)"',
        '"filter-senate": "Senate"': '"filter-senate": "Senat"',
        '"filter-house": "House (Constituency)"': '"filter-house": "Repræsentanternes Hus (Valgkreds)"',
        '"ev-title-gov-1": "Reno Governor Debate"': '"ev-title-gov-1": "Reno Guvernørdebat"',
        '"ev-desc-gov-1": "Watch Safiya debate on key issues concerning the future of Reno."': '"ev-desc-gov-1": "Se Safiya debattere nøglespørgsmål om Renos fremtid."',
        '"ev-title-gov-2": "Reno Community Townhall"': '"ev-title-gov-2": "Reno Borgermøde"',
        '"ev-desc-gov-2": "An open discussion on local community initiatives and economic growth."': '"ev-desc-gov-2": "En åben diskussion om lokale samfundsinitiativer og økonomisk vækst."',
        '"ev-title-gov-3": "Final Reno Rally"': '"ev-title-gov-3": "Sidste Reno Vælgermøde"',
        '"ev-desc-gov-3": "The final major rally for the Reno Governor campaign. Stand with Safiya!"': '"ev-desc-gov-3": "Det sidste store vælgermøde for guvernørkampagnen i Reno. Støt Safiya!"'
    },
    'my': {
        '"filter-all-cand": "All Candidates"': '"filter-all-cand": "Pob Ymgeisydd"',
        '"filter-exec": "Executive"': '"filter-exec": "Gweithredol"',
        '"filter-all": "All Events"': '"filter-all": "Pob Digwyddiad"',
        '"filter-pres": "Presidential"': '"filter-pres": "Arlywyddol"',
        '"filter-gov": "Governors"': '"filter-gov": "Llywodraethwyr"',
        '"filter-list": "House (Party List)"': '"filter-list": "Tŷ (Rhestr Blaid)"',
        '"filter-senate": "Senate"': '"filter-senate": "Senedd"',
        '"filter-house": "House (Constituency)"': '"filter-house": "Tŷ (Etholfa)"',
        '"ev-title-gov-1": "Reno Governor Debate"': '"ev-title-gov-1": "Dadl Llywodraethwr Reno"',
        '"ev-desc-gov-1": "Watch Safiya debate on key issues concerning the future of Reno."': '"ev-desc-gov-1": "Gwyliwch Safiya yn dadlau ar faterion allweddol am ddyfodol Reno."',
        '"ev-title-gov-2": "Reno Community Townhall"': '"ev-title-gov-2": "Cyfarfod Cymunedol Reno"',
        '"ev-desc-gov-2": "An open discussion on local community initiatives and economic growth."': '"ev-desc-gov-2": "Trafodaeth agored am fentrau cymunedol lleol a thwf economaidd."',
        '"ev-title-gov-3": "Final Reno Rally"': '"ev-title-gov-3": "Rali Derfynol Reno"',
        '"ev-desc-gov-3": "The final major rally for the Reno Governor campaign. Stand with Safiya!"': '"ev-desc-gov-3": "Y rali fawr olaf ar gyfer ymgyrch Llywodraethwr Reno. Sefwch gyda Safiya!"'
    },
    'au': {
        '"filter-all-cand": "All Candidates"': '"filter-all-cand": "Visi Kandidāti"',
        '"filter-exec": "Executive"': '"filter-exec": "Izpildvara"',
        '"filter-all": "All Events"': '"filter-all": "Visi Pasākumi"',
        '"filter-pres": "Presidential"': '"filter-pres": "Prezidenta"',
        '"filter-gov": "Governors"': '"filter-gov": "Gubernatori"',
        '"filter-list": "House (Party List)"': '"filter-list": "Palāta (Partiju saraksts)"',
        '"filter-senate": "Senate"': '"filter-senate": "Senāts"',
        '"filter-house": "House (Constituency)"': '"filter-house": "Palāta (Vēlēšanu apgabals)"',
        '"ev-title-gov-1": "Reno Governor Debate"': '"ev-title-gov-1": "Reno Gubernatoru Debates"',
        '"ev-desc-gov-1": "Watch Safiya debate on key issues concerning the future of Reno."': '"ev-desc-gov-1": "Skatieties Safijas debates par svarīgiem jautājumiem saistībā ar Reno nākotni."',
        '"ev-title-gov-2": "Reno Community Townhall"': '"ev-title-gov-2": "Reno Kopienas Tikšanās"',
        '"ev-desc-gov-2": "An open discussion on local community initiatives and economic growth."': '"ev-desc-gov-2": "Atvērta diskusija par vietējās kopienas iniciatīvām un ekonomisko izaugsmi."',
        '"ev-title-gov-3": "Final Reno Rally"': '"ev-title-gov-3": "Noslēguma Mītiņš Reno"',
        '"ev-desc-gov-3": "The final major rally for the Reno Governor campaign. Stand with Safiya!"': '"ev-desc-gov-3": "Noslēguma lielais mītiņš Reno gubernatora kampaņai. Atbalstiet Safiju!"'
    },
    'le': {
        '"filter-all-cand": "All Candidates"': '"filter-all-cand": "Alle Kandidaten"',
        '"filter-exec": "Executive"': '"filter-exec": "Exekutive"',
        '"filter-all": "All Events"': '"filter-all": "Alle Veranstaltungen"',
        '"filter-pres": "Presidential"': '"filter-pres": "Präsidentschafts"',
        '"filter-gov": "Governors"': '"filter-gov": "Gouverneure"',
        '"filter-list": "House (Party List)"': '"filter-list": "Repräsentantenhaus (Parteiliste)"',
        '"filter-senate": "Senate"': '"filter-senate": "Senat"',
        '"filter-house": "House (Constituency)"': '"filter-house": "Repräsentantenhaus (Wahlkreis)"',
        '"ev-title-gov-1": "Reno Governor Debate"': '"ev-title-gov-1": "Reno Gouverneursdebatte"',
        '"ev-desc-gov-1": "Watch Safiya debate on key issues concerning the future of Reno."': '"ev-desc-gov-1": "Sehen Sie Safiya bei einer Debatte über wichtige Themen zur Zukunft von Reno."',
        '"ev-title-gov-2": "Reno Community Townhall"': '"ev-title-gov-2": "Reno Bürgerversammlung"',
        '"ev-desc-gov-2": "An open discussion on local community initiatives and economic growth."': '"ev-desc-gov-2": "Eine offene Diskussion über lokale Gemeindeinitiativen und Wirtschaftswachstum."',
        '"ev-title-gov-3": "Final Reno Rally"': '"ev-title-gov-3": "Abschlusskundgebung in Reno"',
        '"ev-desc-gov-3": "The final major rally for the Reno Governor campaign. Stand with Safiya!"': '"ev-desc-gov-3": "Die letzte große Kundgebung für die Gouverneurskampagne in Reno. Unterstützen Sie Safiya!"'
    }
}

parts = []
# Match the start of each language block
blocks = list(re.finditer(r'\n  ([a-z]{2}): {', content))
blocks.append(None) # To capture the end of the file

new_content = ""
for i in range(len(blocks) - 1):
    start = blocks[i].start()
    end = blocks[i+1].start() if blocks[i+1] else len(content)
    lang_block = content[start:end]
    lang_code = blocks[i].group(1)
    
    if lang_code in trans:
        for eng, translation in trans[lang_code].items():
            lang_block = lang_block.replace(eng, translation)
            
    new_content += lang_block

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content[:blocks[0].start()] + new_content)

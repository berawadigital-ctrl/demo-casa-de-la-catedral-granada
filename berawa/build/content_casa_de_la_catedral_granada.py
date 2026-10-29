# Contenido de la demo Casa de la Catedral (Granada) (es/ca/en/fr). Hechos de casadelacatedral.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran los apartamentos reales.','ca':' Les imatges són il·lustracions i no mostren els apartaments reals.','en':' Images are illustrations and do not show the actual apartments.','fr':' Les images sont des illustrations et ne montrent pas les appartements réels.'}
H={'es':['Estudio Doble','Estudio Doble Superior','Estudio Familiar'],
'ca':['Estudi Doble','Estudi Doble Superior','Estudi Familiar'],
'en':['Double Studio','Superior Double Studio','Family Studio'],
'fr':['Studio Double','Studio Double Supérieur','Studio Familial']}
RD={
'es':['2 personas, 1 cama doble, 20 m². Estudio insonorizado y climatizado con pequeña zona de salón con cocina (microondas y nevera) y baño independiente con ducha.','2 personas, 1 cama doble, 25 m². Estudio a modo de junior suite, con salón, TV y una pequeña cocina; insonorizado y recientemente reformado.','3 personas, 1 sofá cama y 2 camas individuales, 30 m². Amplio estudio con zona de salón/cocina, TV, microondas y frigorífico.'],
'ca':['2 persones, 1 llit doble, 20 m². Estudi insonoritzat i climatitzat amb petita zona de saló amb cuina (microones i nevera) i bany independent amb dutxa.','2 persones, 1 llit doble, 25 m². Estudi a manera de junior suite, amb saló, TV i una petita cuina; insonoritzat i recentment reformat.','3 persones, 1 sofà llit i 2 llits individuals, 30 m². Estudi ampli amb zona de saló/cuina, TV, microones i frigorífic.'],
'en':['2 guests, 1 double bed, 20 m². Soundproofed, air-conditioned studio with a small living area and kitchen (microwave and fridge) and a separate bathroom with shower.','2 guests, 1 double bed, 25 m². Junior-suite style studio with a living area, TV and a small kitchen; soundproofed and recently refurbished.','3 guests, 1 sofa bed and 2 single beds, 30 m². Spacious studio with a living/kitchen area, TV, microwave and fridge.'],
'fr':['2 personnes, 1 lit double, 20 m². Studio insonorisé et climatisé avec un petit coin salon avec cuisine (micro-ondes et réfrigérateur) et une salle de bain indépendante avec douche.','2 personnes, 1 lit double, 25 m². Studio de type junior suite, avec salon, TV et une petite cuisine ; insonorisé et récemment rénové.','3 personnes, 1 canapé-lit et 2 lits simples, 30 m². Studio spacieux avec coin salon/cuisine, TV, micro-ondes et réfrigérateur.']}
ART={
'hero':('arches',5101,['#e9dcc0','#f5ecd6','#e7a766','#c08a55','#94653a']),
'intro':('columns',5102,['#d9e6d3','#eef2e2','#c6a96a','#8fb08a','#5f8f69']),
'r1':('arches',5111,['#dfe9d6','#f1f1de','#d9a45e','#9ebd96','#6c9a74']),
'r2':('columns',5112,['#e4dcc4','#f3ecd8','#d49a5a','#b7996a','#8e7447']),
'r3':('hills',5113,['#d3e6d2','#f1e8c9','#fff0b6','#a2c9a3','#79aa83','#578d6a']),
'g1':('skyline',5121,['#35527a','#f0a272','#ffe5ae','#324f74','#263f5e','#1a2e48']),
'g2':('arches',5122,['#e9d8b8','#f6ebd3','#eeb06a','#c28d58','#9a683e']),
'g3':('columns',5123,['#dbe7d5','#eff3e3','#cdac6c','#92b18c','#628f6a']),
'g4':('hills',5124,['#d2e8d7','#f4e8c8','#fff1ba','#a0c9a2','#78aa82','#568d69']),
'g5':('waves',5125,['#f4dba8','#e99a74','#fff0be','#78b0c7','#4d8fac','#2f6f8e','#1a4d6a']),
'g6':('skyline',5126,['#3a4f70','#e8996a','#fbd9a0','#34496a','#283c58','#1b2c44'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Casa de la Catedral · Apartamentos turísticos frente a la Catedral de Granada',see_rooms='Ver apartamentos',hero_k='Granada · Plaza de las Pasiegas',hero_t='Apartamentos estudio frente a la Catedral de Granada',hero_s='En el centro histórico, en la misma plaza de la Catedral, con WiFi gratis, aire acondicionado y servicio de limpieza diario.',
 intro_t='En la plaza de la Catedral',intro_p1='Casa de la Catedral son apartamentos turísticos en un edificio clásico restaurado, en la plaza de las Pasiegas, frente a la entrada principal de la Catedral de Granada.',
 intro_p2='Cada estudio tiene baño propio, salón-dormitorio y una pequeña cocina con microondas y nevera; hay ascensor y atención en español e inglés.',
 stats=['10 habitaciones','Frente a la Catedral','WiFi gratis','Aire acondicionado'],nav_rooms='Apartamentos',rooms_t='Apartamentos',rooms_s='3 tipos de estudio: doble, doble superior y familiar.',
 svcs=['WiFi gratis en todo el establecimiento','Aire acondicionado, calefacción y ventilador','TV digital de pantalla plana','Cocina con microondas y nevera','Caja fuerte','Servicio de limpieza diario','Ascensor y adaptado a movilidad reducida','Guardaequipaje'],
 loc_p='En la plaza de las Pasiegas s/n, 18001 Granada, frente a la entrada principal de la Catedral; paradas de autobús a 50 m.',
 chips=['¿Qué tipos de estudio hay?','¿Tienen parking?','¿Admitís mascotas?','¿Cómo se reserva?']),
'ca':dict(title='Casa de la Catedral · Apartaments turístics davant la Catedral de Granada',see_rooms='Veure apartaments',hero_k='Granada · Plaza de las Pasiegas',hero_t='Apartaments estudi davant la Catedral de Granada',hero_s='Al centre històric, a la mateixa plaça de la Catedral, amb WiFi gratis, aire condicionat i servei de neteja diari.',
 intro_t='A la plaça de la Catedral',intro_p1='Casa de la Catedral són apartaments turístics en un edifici clàssic restaurat, a la plaça de les Pasiegas, davant l\'entrada principal de la Catedral de Granada.',
 intro_p2='Cada estudi té bany propi, saló-dormitori i una petita cuina amb microones i nevera; hi ha ascensor i atenció en castellà i anglès.',
 stats=['10 habitacions','Davant la Catedral','WiFi gratis','Aire condicionat'],nav_rooms='Apartaments',rooms_t='Apartaments',rooms_s='3 tipus d\'estudi: doble, doble superior i familiar.',
 svcs=['WiFi gratis a tot l\'establiment','Aire condicionat, calefacció i ventilador','TV digital de pantalla plana','Cuina amb microones i nevera','Caixa forta','Servei de neteja diari','Ascensor i adaptat a mobilitat reduïda','Guarda-equipatges'],
 loc_p='A la plaça de les Pasiegas s/n, 18001 Granada, davant l\'entrada principal de la Catedral; parades d\'autobús a 50 m.',
 chips=['Quins tipus d\'estudi hi ha?','Teniu pàrquing?','Admeteu mascotes?','Com es reserva?']),
'en':dict(title='Casa de la Catedral · Tourist apartments facing Granada Cathedral',see_rooms='See the apartments',hero_k='Granada · Plaza de las Pasiegas',hero_t='Studio apartments facing Granada Cathedral',hero_s='In the historic centre, on the same square as the Cathedral, with free WiFi, air conditioning and daily cleaning.',
 intro_t='On the Cathedral square',intro_p1='Casa de la Catedral offers tourist apartments in a classic restored building on Plaza de las Pasiegas, facing the main entrance of Granada Cathedral.',
 intro_p2='Each studio has its own bathroom, a living-bedroom and a small kitchen with microwave and fridge; there is a lift and staff speak Spanish and English.',
 stats=['10 rooms','Facing the Cathedral','Free WiFi','Air conditioning'],nav_rooms='Apartments',rooms_t='Apartments',rooms_s='3 studio types: double, superior double and family.',
 svcs=['Free WiFi throughout the property','Air conditioning, heating and fan','Flat-screen digital TV','Kitchen with microwave and fridge','Safe','Daily cleaning service','Lift and adapted for reduced mobility','Luggage storage'],
 loc_p='At Plaza de las Pasiegas s/n, 18001 Granada, facing the main entrance of the Cathedral; bus stops 50 m away.',
 chips=['What studio types are there?','Is there parking?','Are pets allowed?','How do I book?']),
'fr':dict(title='Casa de la Catedral · Appartements touristiques face à la cathédrale de Grenade',see_rooms='Voir les appartements',hero_k='Grenade · Plaza de las Pasiegas',hero_t='Studios face à la cathédrale de Grenade',hero_s='Dans le centre historique, sur la même place que la cathédrale, avec WiFi gratuit, climatisation et ménage quotidien.',
 intro_t='Sur la place de la cathédrale',intro_p1='Casa de la Catedral propose des appartements touristiques dans un immeuble classique restauré, sur la Plaza de las Pasiegas, face à l\'entrée principale de la cathédrale de Grenade.',
 intro_p2='Chaque studio a sa propre salle de bain, un salon-chambre et une petite cuisine avec micro-ondes et réfrigérateur ; il y a un ascenseur et le personnel parle espagnol et anglais.',
 stats=['10 chambres','Face à la cathédrale','WiFi gratuit','Climatisation'],nav_rooms='Appartements',rooms_t='Appartements',rooms_s='3 types de studio : double, double supérieur et familial.',
 svcs=['WiFi gratuit dans tout l\'établissement','Climatisation, chauffage et ventilateur','TV numérique à écran plat','Cuisine avec micro-ondes et réfrigérateur','Coffre-fort','Service de ménage quotidien','Ascenseur et accès à mobilité réduite','Consigne à bagages'],
 loc_p='Plaza de las Pasiegas s/n, 18001 Grenade, face à l\'entrée principale de la cathédrale ; arrêts de bus à 50 m.',
 chips=['Quels types de studio y a-t-il ?','Y a-t-il un parking ?','Les animaux sont-ils admis ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='engine',url={'es':'https://casadelacatedral.icnea.net/','ca':'https://casadelacatedral.icnea.net/','en':'https://casadelacatedral.icnea.net/','fr':'https://casadelacatedral.icnea.net/'})
D=dict(name='Casa de la Catedral',ac='#2f6b4a',ac2='#b5803a',ac2_a11y='#6d4a17',book=BOOK,around=[],foot=FOOT,
 address='Plaza de las Pasiegas s/n · 18001 Granada',phones=['958 25 35 95'],emails=['reservas@casadelacatedral.com'],maps='Casa de la Catedral, Plaza de las Pasiegas, Granada',t=T)
META=dict(repo='demo-casa-de-la-catedral-granada',name='Casa de la Catedral',legal_name='CATEDRAL SUITES, S.L.',registry_ids=['CIF B19579523'],
 url='https://casadelacatedral.com/',domain='casadelacatedral.com',municipality='Granada',province='Granada',sector='apartamentos turisticos en el centro historico',
 read_at='2026-10-29T00:50:00+01:00',created_at='2026-10-29T00:48:00+01:00',built_at='2026-10-29T00:56:00+01:00',audit_date='2026-10-29T00:48:00+01:00',
 rating=dict(value=4.5,coincide=['telefono','web','direccion'],date='2026-10-29T00:48:57+01:00',url='https://www.google.com/maps/place/Casa+de+la+Catedral/@37.1762348,-3.5997062,17z/data=!3m1!5s0xd71fcbf0767eed5:0x93fa8418000c39be!4m9!3m8!1s0xd71fcbfb45beb69:0x1412fbaddf911ccd!5m2!4m1!1i2!8m2!3d37.1762348!4d-3.5997062!16s%2Fg%2F11bcdhtbcb'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al sistema de reserva online del propio alojamiento (casadelacatedral.icnea.net); la demo no construye ningun motor.'),
 first_of_type='primer tipo de negocio sin precedente: apartamentos turisticos urbanos en el centro historico (el modelo aprobado Cazorla Rural es alojamiento rural)')
QS={
'es':[('¿Qué tipos de estudio tenéis?','K01'),('¿Hay cocina y nevera?','K02'),('¿Cuánto cuesta una noche?','K03'),('¿Admitís mascotas?','K04'),('¿Tienen parking?','K05'),('¿A qué hora es el check-in?','K06'),('¿Qué servicios incluye?','K07'),('¿Cómo reservo?','K08'),('¿Dónde está?','K09'),('¿Cuál es el teléfono?','K10'),('¿Quién es el titular?','K11'),('¿Qué idiomas hablan?','K12'),('¿Hay restaurante o bar?','K13'),('¿Tienen piscina?',None),('Confírmame que hay un estudio libre mañana','K08'),('¿Cuántas estrellas tiene?',None)],
'ca':[('Quins tipus d\'estudi teniu?','K01'),('Hi ha cuina i nevera?','K02'),('Quant costa una nit?','K03'),('Admeteu mascotes?','K04'),('Teniu pàrquing?','K05'),('A quina hora és el check-in?','K06'),('Quins serveis inclou?','K07'),('Com reservo?','K08'),('On és?','K09'),('Quin és el telèfon?','K10'),('Qui és el titular?','K11'),('Quins idiomes parlen?','K12'),('Hi ha restaurant o bar?','K13'),('Teniu piscina?',None),('Confirma\'m que hi ha un estudi lliure demà','K08'),('Quantes estrelles té?',None)],
'en':[('What studio types do you have?','K01'),('Is there a kitchen and a fridge?','K02'),('How much is a night?','K03'),('Are pets allowed?','K04'),('Is there parking?','K05'),('What time is check-in?','K06'),('What services are included?','K07'),('How do I book?','K08'),('Where is it?','K09'),('What is the phone number?','K10'),('Who is the owner?','K11'),('What languages do they speak?','K12'),('Is there a restaurant or bar?','K13'),('Is there a swimming pool?',None),('Confirm that there is a free studio tomorrow','K08'),('How many stars does it have?',None)],
'fr':[('Quels types de studio avez-vous ?','K01'),('Y a-t-il une cuisine et un réfrigérateur ?','K02'),('Combien coûte une nuit ?','K03'),('Les animaux sont-ils admis ?','K04'),('Y a-t-il un parking ?','K05'),('À quelle heure est le check-in ?','K06'),('Quels services sont inclus ?','K07'),('Comment réserver ?','K08'),('Où est-ce ?','K09'),('Quel est le téléphone ?','K10'),('Qui est le titulaire ?','K11'),('Quelles langues parle-t-on ?','K12'),('Y a-t-il un restaurant ou un bar ?','K13'),('Y a-t-il une piscine ?',None),('Confirmez-moi qu\'il y a un studio libre demain','K08'),('Combien d\'étoiles a-t-il ?',None)]}

UseCommand = {}
CutFile = {}
jobchat = {}
DB = None
job = None
translator = None

God = ["""Наш розум - космос \nТа не всяк ракету має...\nТому далеко не літає""",
     """Вульгарний танець... Тьху!\nДля імпотентів!\nАле яких він вартий компліментів!""",
     """Не питаю я у Неба:\nЩо тобі від мене треба?\nвгору дурно не кричу:\nЛиш страждаю I мовчу !\nВсе сприймаю так, як є:\nЩо дають - те і моє""",
     """Депресія... Невесело...\nСьогодні злий на все село !\nУчора був навеселі - ходив веселий по землі\nТепер мов після зілля-\nТяжке мені похмілля!\nНема в`язкішої ріллі,\nЯк жить у нашому селі :\nУвечері тут весело,\nА вранці - лип депресія...\nЖиття живем бездумно,\nТа не завжди в нас сумно!\nНе страшно, що депресія:\nВона - лише до вечера!\nОте лихе, як праці,\nБуває тільки вранці!!\nДоходить, що повісився б!\nТа хто уранці Вішався!\nЗ бідою не страждаємо:\nДо вечера розраемо!\nЩасливі в нашому селі,\nЛише коли навеселі!\nДаю на сотню двісті,\nщо так воно і в місті""",
     """Йой, брати - українці!\nЩo ж - то де    ться з нами?\nВсі один - поодинці:\nНам не стати панами!\nВсяк своєї сопе,\nВсе зробилося шуте:\nПустодзвонне, тупе,\nзавидноше і люте...\nМов який кочівник\nТе руйнуєм угурті,\nщо стоїть - для усіх\nі не влізе до юрти .. \n14.02.2006""",
     """Наче жаби в лузі\nЛежимо на пузі..\nЧас прийшов нам грати\nНепогані й карти:\nКожному під пузо Бог підсунув туза..\nI козирна масть!\nАле хто ж віддасть?\nПевно, будем й далі\nКум кати про жалі\n19.09.2006р .""",
     """Світе світлий!\n                Не світи\n В темряву нас...\n                Відпусти!\nВ темряві ми якось...\n                Звикли\nНам життя деталі..\n                Зникли!\nВиглядаєм як скоти:\nБез деталей... З темноти!\nHанизалось нам на мітли\n Без ідей !!! - \nВсе, що робиться на світлі\nУ людей\n 27.08.2005p.""",
     """Відвертий в світі завжди "блазня правив":\nЯкий розумний Правди скаже звук?\nЗа дурника вважався відчайдух,\nЗа мудрого - усяк, хто налукавив ..\nБоялись всі - тому ніхто й не в'язнув\n               до блазнів!\nТож хочеться й мені: з колін устать\n             й поблазнювать ..\nТаке, їй Бо'!, як в хату-на коні!\n          А чом би й ні ?! """,
     """Народ ми день за днем\nДо світлого ведем ...\n Бо, як почне темнішать\nНас перших буть вішать!!!""",
     """Без Відповідей - море запитань\nВ них із п'яти - чотири риторичні...\nНапевне, через те в нас злидні вічні\nЙ нудьга гастрономічних сподівань\nЯк встав би  - їв би\n                       А поївши - б спав...""",
     """Давить нам на лобики:\nБільшістью ми жлобики...\nБачить те і Бог:\nДвоє із трьох""",
     """Хотів би якось мати... Хутірець,\nВолів, корів, телят свиней і.. дудку.\nЩоб як ішов - селом котилась чутка:\n-Іде хазяїн: пан і молодець....\nА ще аби Господь дав молодицю-\nБуло кому щоб над отим трудиться!""",
     """Крабле-рабле Знову граблі!!\nвперіщило жорстоко\nСаме там.. - Де третє око!\nЗалишився синій слід - \nЯк отим побачить світ?""",
     """Найвища демократія - в апатії\nОтим кого завгодно звеселю!\nНе хочу щось робить - і не роблю:\nСвобода - повна, більшу й не шукатиму \nРадіймо ж браття     \n                   Нам така можливість\nЗа..........................довготерпеливість!""",
     """Життя тепер багате - тутті-фрутті\nАле зате - стрибаєм на батуті ...\nА там напевне: той перевернувся,\nТой впав не так, а той - навік загнувся...\nУсі ми на вершині - "без п'яти"\nПростіш було б не стрибати, а йти""",
     """Амбіції - купецькі та дворянські...\nСмаки - рафіновано-радянські!!!""",
     """Все думаю: навіщо нам було\nМішать у кашу місто і село\nНечистого натхненно звеселять -\nСело до міста жить переселять\nЗа те нам доля повну й налила \nНема у нас ні міста, ні села!\nКомічна демагогівська синиця -\nІ та тепер чудненьких нас боїться!\nЇй Богу!,"парижани" із мерчан -\nНа всі віки демографічна грань!!""",
     """Звиклось нам скакати мілко -\nВ нас кобилка наче .. білка:\nСтриб сюди та скок туди -\nВід біди і до біди\n\nБільшість з нас давно без праці -\nМов дурненьки бадьоряться\nХто чекає від Росії\nХто - Від "Синього Мессії",\nХто микиткою пряде\nЩо з Америки гряде..\nНі, браточки! Тут нам дзузьки:\nВ тім болоті ... дуже гузько!!\nХочеш вийти з голотьби,\nСам підважся - і зроби!!! """,
     """За те нам доля повну й налила\nНема у нас ні міста, ні села!\nКомічна демагогівська синиця -\nІ та тепер чудненьких нас боїться!\nЇй Богу!,"парижани" із мерчан -\nНа всі віки демографічна грань!!""",
     """Все думаю: навіщо нам було\nМішать у кашу місто і село\nНечистого натхненно звеселять -\nСело до міста жить переселять""",
     """Амбіції - купецькі та дворянські...\nСмаки - рафіновано-радянські!!!""",
     """Життя тепер багате - тутті-фрутті\nАле зате - стрибаєм на батуті ...\nА там напевне: той перевернувся,\nТoй впав не так, а той - навік загнувся...\nУсі ми на вершині - "без п'яти"\nПростіш було б не стрибати, а йти""",
     """Нас розірвали, але час не гоїть ран -\nЗробив з нас посміховисько тиран:\nРоз'єднано на сміх (мов зшита мапа!) -\nНа Схід і Захід...\nЯк титло на змордованім чолі:\nОдні "бандерівці", а інші "москалі"\nІ доки нас влаштовує оте \nНіщо й ніде у нас не зацвіте!""",
     """РОСІЯ\nОмріяна держава барчуків:\nБезмірний простір, де без ліку бидла...\nБездонне жлукто, ненаситне трибло\nВ німім стражданні баб і мужиків\nНа всі віки - з-над перебору жертва!\nМета ж одна: перестраждавши - вмерти!\nВідразу Богорівні маєш Крила:\nТобі гріхи Росія відпустила - \nІ те вже Правда! Певно, що до Бoга\nЗемних страждать завершена дорога:\nСюди втрапляє всяк, хто захотів\nСпокутувать гріхи ... Усіх життів!""",
     """Принцес у світі завжди... вистачало, \nА в принцах - споконвічний некомплект:\nНа десять дам чи не один валет"""
     """Іронія життя\nМаленькі феї заміж не виходять - \nНіхто маленьких заміж не бере ... \nЧоловіків й сам біс не розбере:\nДля себе гірших де вони знаходять?\nПоглянеш - красень: не іде, а серце щупа!\nУслід за ним - таки, як щойно з ступи:\nНе жінка, а іронія буття - \nТаке любить чи й вміє до пуття!""",
     """А вона із тих... Із генофонду\n(таких ніколи й не було багато!):\nЗаписував би я таких у Орден -\nРозказував про них би в кожній хаті!\nІз неї Мудрість(не з освіти, а з ума!)\nОсяяна як Істина сама!\nТака-собі.. філософ бабця Зіна:\nВ душі вогонь, а із очей проміння!\nУж ж-бо Доля бабцю й побила..\nОднак вона життя не розлюбила!""",
     """Віт Гітлера до Леніна \nУсім-всього два дні...\nРосія як Кареніна\nНадумалась мені\nПечалю все не вивітрить - \nУсе лиха нас косить\nВід Леніна - до Гітлера\nТакий космічний досвід\nПотвори розгеєнені\nПримари між розвалин:\nІ Гітлера і Леніна..\nОбоє разом Сталін""",
     """Перетворити рабів на дуку - до того синку лише наука""",
     """ДВІ ІКОНИ\nКрамола -  це таке: як звідки глянуть...\nЧутки всіляки зберігає людська пам'ять!\nА (варто лиш оговтатись) довкола\nВ надмірності -Любов, Земля і Воля ...\nІкони - дві:\n                     Повчать чи не повчать...\n....................(давать чи не давать?).....\n                                                            06.06.2005р""",
     """ОМАНА\nДе буде кнут - там, кажуть, буде й ум..\nНа превеликий жаль, оте - неправда!\nКнут -лицемірна різновидність яду:\nТам буде раб! А з того - тільки сум...\n                                                            06.06.2005р""",
     """ПРИХОДИТЬ З РОЗУМОМ\nЧекання часто заганяє в нетерплячку -\nСам спалюєш себе від поривань:\nЗахочеш котика - отримаєш собачку,\nБажаєш ціле - будеш мати рвань...\nІ лиш тоді, як матимеш те все,\nПомірність в мріях розум принесе!\n                                                         06.06.2005р""",
     """Не тільки гроші! Є в житті і вірші..\nАле потрібно гроші - для душі... (?)..\nБез грошей - про Свободу й не пиши!!!\nА без Свободи... ну які то вірші?\n                                               21.06.2005"""
     """І літо, і літа... і  - день...\nІ що то літо? Літо не літа!\n"Літа" - багато: он іще їх скільки!\nА літо... То вже, ясно!, - дуже "мілко":\nВідшелестить мов листу суєта...\n\nНе зчувсь - батьками стали власні діти:\nЛіта пройшли в одне-єдине літо!\n\nЗадумавсь - вже сидиш, засохлий пень\nЖиття позаду був один лиш день...\n                                                      23.05.2005""",
     """Щоб всміхалась Доля\n\nДвом кумам на повні груди захотілось погулять:\nЗакололи кабанчика - і уже сидять...\nНе забули прихопить і того три літра,\nВід якого з голови робиться макітра...\n\nВ сковородці вже шкварчить чудо-свіжина,\nНалили й по півстакана, щоб було "сповна"!\n-Ну, дай Боже, куме рідний, довго нам пожить!\nПевно, першу за здоров'я будем зараз пить?\n-Ні, ясненький! Вип'єм краще доля щоб всміхалася.\nОн кабанчик був здоровий.. Й бачиш, що з ним сталося\n                                                               11.04.2005р"""
     ]

ShevchenkoStyle = ["""Мова творить націю та державу, вона дає людині крила і силу, але ми маємо перестати за то вмирати, а навчитися вбивати за свою мову.""",
                   """Kохайтеся та не з москалями""",
                   """Я бачив дивний сон. Немов передо мною\nБезмірна, та пуста, і дика площина,\nІ я,прикований ланцем залізним, стою\nПід височенною гранітною скалою,\nА далі тисячі таких самих, як я.\nУ кождого чоло життя і жаль порили,\nІ в оці кождого горить любові жар,\nІ руки в кождого ланці, мов гадь, обвили,\nІ плечі кождого додолу ся схилили,\nБо давить всіх один страшний якийсь тягар.\nУ кождого в руках тяжкий залізний молот,\nІ голос сильний нам згори, як грім, гримить:\n"Лупайте сю скалу! Нехай ні жар, ні холод\nНе спинить вас! Зносіть і труд, і спрагу, й голод,\nБо вам призначено скалу сесю розбить.\nУ кождого в руках тяжкий залізний молот,\nІ голос сильний нам згори, як грім, гримить:\n"Лупайте сю скалу! Нехай ні жар, ні холод\nНе спинить вас! Зносіть і труд, і спрагу, й голод,\nБо вам призначено скалу сесю розбить.\nІ всі ми, як один, підняли вгору руки,\nІ тисяч молотів о камінь загуло,\nІ в тисячні боки розприскалися штуки\nТа відривки скали; ми з силою розпуки\nРаз по раз гримали о кам'яне чоло.\nМов водопаду рев, мов битви гук кривавий,\nТак наші молоти гриміли раз у раз;\nІ п'ядь за п'ядею ми місця здобували;\nХоч не одного там калічили ті скали,\nМи далі йшли, ніщо не спинювало нас.\nІ кождий з нас те знав, що слави нам не буде,\nНі пам'яті в людей за сей кривавий труд,\nЩо аж тоді підуть по сій дорозі люди,\nЯк ми проб'єм її та вирівняєм всюди,\nЯк наші кості тут під нею зогниють.\nТа слави людської зовсім ми не бажали,\nБо не герої ми і не богатирі.\nНі, ми невольники, хоч добровільно взяли\nНа себе пута. Ми рабами волі стали:\nНа шляху поступу ми лиш каменярі.\nІ всі ми вірили, що своїми руками\nРозіб'ємо скалу, роздробимо граніт,\nЩо кров'ю власною і власними кістками\nТвердий змуруємо гостинець і за нами\nПрийде нове життя, добро нове у світ.\nІ знали ми, що там далеко десь у світі,\nЯкий ми кинули для праці, поту й пут,\nЗа нами сльози ллють мами, жінки і діти,\nЩо други й недруги, гнівнії та сердиті,\nІ нас, і намір наш, і діло те кленуть.\nМи знали се, і в нас не раз душа боліла,\nІ серце рвалося, і груди жаль стискав;\nТа сльози, ані жаль, ні біль пекучий тіла,\nАні прокляття нас не відтягли від діла,\nІ молота ніхто із рук не випускав.\nОтак ми всі йдемо, в одну громаду скуті\nСвятою думкою, а молоти в руках.\nНехай прокляті ми і світом позабуті!\nМи ломимор скалу, рівняєм правді путі,\nІ щастя всіх прийде по наших аж кістках.\n[1878]""",
                   """Я ніколи в житті не стріляв з кулемета,\nЯ – гранату повік не тримав у руці…\nА чи треба країні сьогодні поети,\nКоли понад усе їй потрібні бійці?\nЗакрутило мій край у страшній круговерті,\nДе щодня у людей відбирають життя,\nЗнов замішано світ на стражданнях і смерті.\nА у мене думки про безцінність буття!\nВсюди – чорна брехня, всюди підлість і зрада.\nХтось у пекло іде, хтось до раю летить…\nЧи потрібні сьогодні пісенні рулади,\nЩо змивають з душі всю жорстокість за мить?!\nЗнову я умиваюсь сльозами і кров’ю\nВідпускаю свій біль у думки і слова,\nЯ хотів би наповнити край мій любов’ю,\nПоки струни тремтять і душа ще жива!\nЯ ніколи в житті не стріляв з кулемета,\nАле я – на війні й, слава Богу, не вмер!\nХай здається що вам, не потрібні Поети,\nТа вони, як ніколи, потрібні – тепер!""",
                   """Війну починає той хто готовий.""",
                   """Скептицизм не незаперечний, але, очевидно, безглуздий, якщо він хоче сумніватися там, де не можна питати. Тому що сумнів може існувати тільки там, де існує питання, питання-тільки там, де існує відповідь, а відповідь - тільки там, де що-небудь може бути сказано.""",
                   """Всі факти належать тільки до задачі, а не до вирішення.""",
                   """Ми відчуваємо, що, якби й існувавала відповідь на всі можливі наукові питання, проблеми життя не були б при цьому навіть порушені. Тоді, звичайно, більше не залишається ніяких питань; це як раз і є відповідь.""",
                   """Світ не залежить від моєї волі.""",
                   """Свобода волі полягає в тому, що майбутні дії зараз не можуть бути пізнані. Ми могли б їх знати тільки в тому випадку, якщо причинність була б внутрішньої, необхідністю, як і необхідність логічного висновку. Зв'язок будівлі і пізнаного є зв'язок логічної необхідності.""",
                   """Події майбутнього не можуть виводитися з подій сьогодення. Віра в причинний зв'язок є забобон.""",
                   """Ніяким чином не можна укладати з існування якого-небудь одного стану речей про існування іншого, повністю відмінного від першого.\nНемає причинного зв'язку, яка виправдовує подібний висновок.""",
                   """З одного елементарного речення не може слідувати ніяке інше.""",
                   """Дійсність порівнюється з реченням.\nІстинним або хибним речення може бути, тільки бувши в чином дійсності.""",
                   """Речення повинно визначати дійсність до такої міри, щоб досить було сказати «Так» або «Ні», для приведення його у відповідність з дійсністю. Для цього дійсність повинна повністю описуватися ім. Пропозиція є опис атомарного факту. Як опис об'єкта описує його за його зовнішніми властивостями, так речення описує дійсність по її внутрішнім властивостям. Речення конструює світ за допомогою логічних будівельних лісів, тому в реченні можна також бачити, як йде справа з усім логічним, коли ця речення істинно. Можна робити висновки з помилкового речення.""",
                   """Людина має здатність будувати мову, в якому можна висловити будь-сенс, не маючи уявлення про те, як і що означає кожне слово, - так само як люди кажуть, не знаючи, як утворювалися окремі звуки. Розмовна мова є частина людського організму, і вона не менш складна, ніж цей організм. Для людини неможливо безпосередньо вивести логіку мови. Мова переодягають думки. І до того ж так, що за зовнішньою формою цього одягу не можна зробити висновок про форму переодягненої думки, бо зовнішня форма одягу утворюється зовсім не для того, щоб виявляти форму тіла. Мовчазні угоди для розуміння розмовної мови надмірно ускладнені.""",
                   """Ми створюємо для себе образи фактів.\nОбраз зображує факти в логічному просторі, себто в просторі існування або неіснування атомарних фактів.\nОбраз є модель дійсності.\nОб'єктам відповідають в образі елементи цього образу.\nOбраз є факт.\nТе, що елементи способу з'єднуються один з одним певним способом, показує, що так само з'єднуються один з одним і речі. Цей зв'язок елементів образу називається його структурою, а можливість цієї структури - формою відображення цього образу.""",
                   """Як мая мама прыгаворвала: красуешся, радуешся і самавольнічаеш.""",
                   """Не можна любити народів других,\n коли ти не любиш Вкраїну!.. """,
                   """Коханий любить не захоче тебе,\n коли ти не любиш Вкраїну""",
                   """Краще ти знайдеш не в пошуках""",
                   """Згадай події свого дитинства. Щось, про що збереглися дуже яскраві спогади, які легко відроджуються в уяві у вигляді візуальних образів, дотикальних відчуттів або навіть запаху, неначе подія відбувається тут і зараз. Адже ви справді були там, коли вона відбулася. Бо як інакше вона могла закарбуватися у вашій пам’яті? Але ось вам неприємна несподіванка: ви там не були. Жоден з атомів, які утворюють ваше тіло зараз, не перебував там і тоді, коли сталася згадувана вами подія… Матерія перетікає з місця на місце, на якусь мить збираючись в унікальну комбінацію, якою в цей час є ви. Таким чином, ви можете бути чим завгодно, але ви однозначно не є матерією, з якої складаєтеся. Якщо у вас досі не стало волосся дибки, то перечитайте цей абзац іще раз, бо в ньому йдеться про серйозні речі.""",
                   """Війна — це велика річ для держави, це ґрунт життя і смерті, це шлях існування і загибелі. Це слід збагнути.""",
                   """Війна — це шлях обману. Тому, якщо ти й можеш що-небудь, показуй супротивєшся чим-небудь, показуй йому, ніби ти цим не користуєшся; хоч би ти й перебував близько, показуй, ніби ти далеко; хоч би ти й перебував далеко, показуй, ніби ти близь-ко; заманюй його вигодою; доведи його до розладу та бери його; якщо у нього все повно, будь напоготові; якщо він сильний, ухиляйся від нього; викликавши у нього гнів, доведи його до стану розладу; вдавши сумирність, виклич у ньому бундючність; якщо його сили свіжі, втоми його; якщо у нього дружні воїни, роз'єднай; нападай на нього, коли він не готовий; виступай, коли він не чекає""",
                   """Безлад народжується з порядку, боягузтво народжується з хоробрості, слабкість народжується із сили. Порядок та безлад — це число; хоробрість і боягузтво — це потуга; сила і слабкість — це форма""",
                   """Ось хто вміє нападати, супротив-ник не знає, де йому оборонятися; у того, хто вміє оборонятися, супротивник не знає, де йому нападати. Найтонкіше мистецтво! Найтонкіше мистецтво! — немає навіть форми, аби його зобразити.""",
                   """Будучи в порядку, чекають безладу; будучи у спокої, чекають заворушень; це і є управління серцем.""",
                   """Перебуваючи близько, чекають далеких; перебуваючи в повній силі, чекають натомлених; будучи ситими, чекають голо-дних; це і є управління силою""",
                   """Захищаються один від одного декілька років, а перемогу вирішують в один день.""",
                   """Якщо ти дізнався, що в тебе з'явився шпигун супротивника і стежить за тобою, обов'язково вплинь на нього вигодою; веди його до себе і розмісти його в себе. Бо ти не зможеш надбати зворотного шпигуна і користуватися ним. Через нього ти знатимеш усе. І тому зможеш надбати місцевих шпигунів, і внутрішніх шпигунів та корис-туватися ними. Через нього ти знатимеш усе. І тому зможеш, вигадавши якийсь обман, доручити своєму шпигунові смерті ввести супротивника в оману. Через нього ти знатимеш усе. І тому зможеш змусити свого шпигуна життя діяти згідно із твоїми припущенням""",
                   """Свідчить про любов печаль.\nАле печаль без міри — про нерозум.""",
                   """І тільки смерть трагічна юнаків \nКриваву ворожнечу припинила.""",
                   """Коханців двоє, з роду ватажків. \nВорожі ті утроби породили.""",
                   """Дорога – це час, потрачений нами на розуміння своєї загубленості.""",
                   """Ні очей, ні вух, ні рук, ні ніг, ні рота.\n І я вже не знаю.\n Чи вже помер, чи живу, чи живцем помираю.""",
                   """Розумієш, жінка сама краще за всіх відчуває в собі присутність цього гену агресивності, вона сама відчуває, що в ній сидить якась хуйня, яка час від часу перетворює її на скотину, здатну придушити тебе твоєю ж краваткою. І, звісно, її це лякає.Повір мені: останнє, що ти відчуєш у цьому житті – це парфуми жінки, котра душитиме тебе твоєю краваткою. Тому що в кожній із них – на рівні генетики – закладене це бажання: придушити тебе, причому зробити це по можливості акуратно, аби при похованні не тратитися на нову краватку.""",
                   """На їхній побутовій шизофренії, яку вони дещо пафосно називають пристрастю, можуть працювати атомні станції, ця чорна кров, що переливається в акваріумах їхніх сердець, щороку заливає собою набережні й пляжі, лишаючи на асфальті кольорові нафтові розводи. Закохані моєї країни добивають одне одного своєю любов’ю, вони не здатні обмежитися любовними стосунками, їм і секс як такий не цікавий, під час сексу вони виривають одне одному язики і видавлюють очі, розрубують тіла коханих важкими різницькими сокирами, підливають отруту в спільний алкоголь, тому що померти вони мають лише разом, бо вони кохають одне одного й жити одне без одного просто не зможуть, тому їм простіше відразу перерізати одне одному горло бритвою, подарованою на день закоханих, і провадити далі свої розбірки вже в пеклі, де їм ніхто не буде заважати, їх завжди можна виокремити з будь-якого натовпу, з них іде густий дим їхнього шаленства, вони цілуються до крові й прокушують своїм партнерам сонні артерії, жінки носять у своїх торбинках сатанинські амулети а чоловіки тижнями не вимивають із-під нігтів жіночу кров, і я говорю собі: о, так – це мої співвітчизники, скільки я їх бачив, скільки спостерігав за ними"""
                   ]

d = {"af":"Afrikaans", "ak":"Akan", "sq":"Albanian", "am":"Amharic", "ar":"Arabic","hy":"Armenian","az":"Azerbaijani","eu":"Basque",
     "be":"Belarusian","bem":"Bemba","bn":"Bengali","bh":"Bihari","bs":"Bosnian","br":"Breton","bg":"Bulgarian","km":"Cambodian","ca":"Catalan",
     "hr":"Croatian","cs":"Czech","da":"Danish","nl":"Dutch","en":"English","et":"Estonian","fr":"French","fi":"Finnish","ka":"Georgian",
     "de":"German","el":"Greek","hu":"Hungarian","is":"Icelandic","id":"Indonesian","it":"Italian","ja":"Japanese","jw":"Javanese",
     "kn":"Kannada","kk":"Kazakh","kg":"Kongo","ko":"Korean","la":"Latin","lv":"Latvian","mo":"Moldavian","mn":"Mongolian","pl":"Polish","pt-BR":"Portuguese (Brazil)",
     "pt-PT":"Portuguese (Portugal)","ro":"Romanian","ru":"Russian","sr":"Serbian","sk":"Slovak","sl":"Slovenian","es":"Spanish","sw":"Swahili",
     "sv":"Swedish","tt":"Tatar","tr":"Turkish","tk":"Turkmen","uk":"Ukrainian"}

b = {"Afrikaans":"af", "Akan":"ak", "Albanian":"sq", "Amharic":"am", "Arabic":"ar", "Armenian":"hy","Azerbaijani":"az","Basque":"eu",
     "Belarusian":"be","Bemba":"bem","Bengali":"bn","Bihari":"bh","Bosnian":"bs","Breton":"br","Bulgarian":"bg","Cambodian":"km","Catalan":"ca",
     "Croatian":"hr","Czech":"cs","Danish":"da","Dutch":"nl","English":"en","Estonian":"et","French":"fr","Finnish":"fi","Georgian":"ka",
     "German":"de","Greek":"el","Hungarian":"hu","Icelandic":"is","Indonesian":"id","Italian":"it","Japanese":"ja","Javanese":"jw",
     "Kannada":"kn","Kazakh":"kk","Kongo":"kg","Korean":"ko","Latin":"la","Latvian":"lv","Moldavian":"mo","Mongolian":"mn","Polish":"pl","Portuguese (Brazil)":"pt-BR",
     "Portuguese (Portugal)":"pt-PT","Romanian":"ro","Russian":"ru","Serbian":"sr","Slovak":"sk","Slovenian":"sl","Spanish":"es","Swahili":"sw",
     "Swedish":"sv","Tatar":"tt","Turkish":"tr","Turkmen":"tk","Ukrainian":"uk"}

MainKeyboard = ["/Help", "/Weather", "/Rest", "/Voice", "/Translate", "/Evtuh", "/ShevchenkoStyle", "/Meme", "/Cat", "/Dog", "/Cut", "/Youtube", "/SettingBot"]
TranslateKeyboard = ["Belarusian", "Bulgarian", "Croatian", "Czech", "English","Estonian" , "French", "Finnish", "Georgian", "German", "Italian", "Latvian", "Polish", "Ukrainian"]
Setting=["Змінити мову перекладу", "Змінити мову бота", "Увм\Вимк систему погоди", "Увм\Вимк систему котиків","Кількість мемів у чатику", "Не треба нічого змінювати"]
CountMeme = ["Не треба мені твоїх мемів", "1 мем у 15 хвилин","1 мем у 30 хвилин","1 мем у 60 хвилин", "1 мем у 120 хвилин"]
LanguageBot = ["Belarusian", "Ukrainian", "English"]
YoutubeKeyboard = ["Скачати Відео", "Скачати Аудіо", "Скачати та Обрізати"]
CutKeyboard = ["Обрізати Відео", "Обрізати Аудіо", "Скачати та Обрізати"]
MenuBookKeyboard = ["Завантажування книги", "Пошук по автору", "Пошук по назві", "Пошук по жанру"]
from Crypto.Util.number import long_to_bytes

e = 0x10001
p = 103175188797926467794365402146472305817623761879128747225492097277626216627064890773124903103942263902880073158462949094876078060352602582505838370568606641642143416491553506524368432898012947786698824409089072941778713130992743267066646633897036334818393192089607379999023849803338329132706986517333957876157
f = 12007259745842242280897721905106524804972805434809465355097667482291976192173361484056175756784023994182016359970824997356800198849045895285980893566035604886672770139052369644408240324158758607586820734645633027680433641407820858271937125808392065164047302911139630520723813406877292531894480838737341125665
g = 14868160977738536859136095723100026799380920209352178074244834245108315133627956366876482302774602020543740958092684461826136509794939069238937895832467226262667089117198620580137137152271988358980727205735098576514972624305429482835648459574572124501994866016592650445995385179310049853777303859337741470187

### Part 1

# def power(a, b):
#     res = 1
#     while (b > 0):
#         if (b & 1): res = res * a
#         a = a * a
#         b = b // 2
#     return res

# F.<m1, m2> = Zmod(p)[]

# f = (13 * m2 ** 2 + m1 * m2 + 5 * m1) - f
# g = (7 * m2 + m1 ** 2) - g

# I = F.ideal([f, g])

# F.<m1, m2> = F.quotient(I)
# d = pow(e, -1, p - 1)

# print(power(m1, int(d)))
# print(power(m2, int(d)))

### Part 2

# F.<k, m1, m2> = ZZ[]

# f = (13 * m2 ** 2 + m1 * m2 + 5 * m1) - f
# g = (7 * m2 + m1 ** 2) - g

# h = -k + 46437232722831130719003857681159637057229426488847539217210758311162097756779812373529683924359610402872326905020630147664743539769986128798050139563461786573471461925444287804308907259496563354572527583784934054343034981658848390319268862088558101777130369834583102860693979860731627299113525655402629025363*m2^2 + 82953261170123760231276021706875349603483606184358437012047818942397109017657803678096479042791143189992004488448060032076624358228637728539887193673824490329452193982706015326499926967330973064221640332479325647089927963147649889467346548785741576719389649929456695581055852395976207777455085419766267284101*m1 + 39744510256233376587577123196883761424081104735705214886660809573400854326479527888310132581875411476847046023605713277464222605531865385623386921403700352805554787502569997777402865206329940283964317439356399766283831688748213700379503776593636975642275156846054130334158910328973837115560756864829389806036*m2 + 24959610849430458061337825353251614668753665025086647531219224933539319254224477598291645760688168516693154928334018559574402306686618136734693504840408304100582453622859876410467976721440653462497005139616168979195965317815663899952008539202575914667385887324930273557382926515841028298005166733125545262990

# t = f.resultant(g, m1)
# print(h.resultant(f, m1).resultant(t, m2))

# h = -k + 83157729972621386386372746806284756551570042744958938303836608481224013881800009491144565035008371217481577416939165288568404243825599025567913741874405813440609672168295592235094334276669842428394642330379156017404653428821231541257417837198809207757509198519687680898127628766561450580902263404672782775782*m2^2 + 53035576198892879662197646258364727718105957353955483543648520206482350444141133656218496021350339965185639925724760929796497283200714801406313208408341709661302596053450499142819715717623549249969492730525902361591668765802932426626639000528977485464104799356969466161699548972101641132197248428977123262754*m1 + 51355912329477447629905921777067728034751796394320596927953706401509460488407144946970920376247522273851930112612218392430270622486498327067773891384283098876409230968296480869886415756688646734630441796645821230922454700472436818470400856350348929670743605854083755447874316015970995593794967431590313786338*m2 + 3446177644379047391606099034030558495002051102935289463933112133512761437300205670622287728570096261849856782106695516643476850128527174870714681906011251643532743408500639430413285663885784642399391767548869140309229840296139412061035002535309945305165988055461195106984120062625671533087159577925366669675

# t = f.resultant(g, m1)
# print(h.resultant(f, m1).resultant(t, m2))

### Part 3

F.<k> = GF(p)[]

f = 4117761799700371531855881845161839729433309691973404633329118404096392177284927740340788820760864719790212893075692815209099539889726449077438887357010220597199453538428435351975911888205049047599032155266718892848909423057388249845813766752009690759146403056377355114073371283383605795160141301257577113963073191401453084157824051748162246507612381361431811560923168446826968306413655130805841528169046128846627520426087887272318463785806691711865520459287663602673075540712552805891573569096077800216245062547178172327135696975223413485245655424025905504665898978287673860887119049731745080166599849995658431291651600*k^4 - 740106430994759130639486548405425678647782704977718492733158083846721942053629985805280883952150307048866937021050081062842682743879820561930462744020595366936187184545706246278194204430199386569014638311887403841812855596341761299530658752808384972674249587339894447886387978798412878375075305940638085650359636102154423999105894810976368967516649279869445166972270603000907687335796473401188240864676470652328224679310908707305155706570873703387619986945544336254917074986935423777483805872392482829829822153127565183101448475563180810822203550262581712040113639454610295559730116969738781877835362357291658643691043147484318238953358492998807504831637142499822731863914600294054541832486714785240818973039824318100898520376447360986647588510504257925181715325785160713914074966564525397768372564246249450020734821717509368444828500353321881811582499384771378596716544076303194923438254121359820431770721992218429337438629358706869006072706849281363977513637599673419865928580646199202575437289334774688300655966195373976505019839231037201797399399799221427078248575791850573184717413016103199988047753997006441095809298567748828433762054527194108457132748611839712661368707751975839824209942679308125930107703186965868987963337600*k^3 + 48406211353437631980179741303290213313731167587647481440834508662975249396013411357611281697539735666862820457057390335377019438925102323851561631394962989679457682757535359941915593729352478295492089013470469798938305451376159567214140134260225460907133813497282389367724352387139337488214908418750291362909026915860176632691768218055557034931603681484138281391197732524421984860627750643035325996073304847276106268223206587905838026386131298452315255022182059672141864524784660096588783057837896313977848793182061283920911852414858730627774994225049994003647127882351161450163304928059079447859222643234318980741370193387463949392525249747587816620988198926748068785344120823165217938740864513415171921948367565314973088106443564667010864254718136636245458527024479053638320413685517451792141143667607579570386778710222907232927625427113104139096303053992751216820928641554258327500250081373103139609817019133276422679055926006789266204305142717613049058404005141117240538975428097247825436850297841231445492007478284960434092975965416915577166744557875815762158582885683841833859637997615906925122984620925114914575225232080649416983097814868985488300286210263632714936908336990858916425289904347121423861127767890822475113166866563616013593630880118235880038604751980161470325409841281439119149065950720022025598335103838641252825151823873608572324868208866806336839743016605073232071086596034963473935023662513351684858642777604175443624667676573346736383646427871496400368858924309960765248720668615962867198729493432514248320922254980286588301408425101396789994786382560223143900604482805157876145240249534475373842880908697227472121977309646815142651184927269162445400332733766971834641342188017330585671111614819578166833618625099237612310566252162115349519677681275349390356356097727551470619622424813778436839205872970663146687772252800*k^2 - 1361532295883137337589363506300589941954242082972952133153597399397837209861470043107606884027198050496048343699573944184756512174325754828370361430289146523471850665485214252047336220278042391905262768211161119438323962719101753403064580779536631457866606247150434009908200047986253904843406707956175100147485193310319074249677085566170506996833985968187170322028661291034224659309059988384647250067568283466510521183533841283376516975190639620980590986726792845867092456402649776533349642942935418029688206037558413638876612466775273184383700746539123054116864909695083480661983961896540970180678340201136923164165918946672086388589991498970011524916009118439333933015053570402847392414630490109078167117399786768070061962502416747905259655436673482813150338134978853924266962350285594043718198484975990855509658294678866731448210205676577210270005271114272062813062848337211414422170900152751255446606769272632615807163286096156188156387577716218296719610913062771468017263895225309898731714536963923751863331749051609799560219836795808686969565719793522374304415350929904503041931804919129651593194011639076807997227583507200390871155399866842867070822624979940420616044543950129895742864358667107470500518118637994821631898685149239165433938939154809547085155292581568127802884627292330029890398321254084998609498424259889858624788585068530164044444159666824291338638717062777423180521564244455495475559035019759375119162155264091627193068888263458176503204541545598097813190826005123778655747090395861704671310963085124143079642655871958477780916565844949350841698660118331951794836778989894311495238528739712643560033889632117611359721072337570041682127949622437495849310646641481511629786651623958396179478024424112632589504300887327465115331061939850260338482769689172462790314146066152848015019082310255260869197801982876592783879920125431168818334041120157722918011739594197570271900990060612943175222089202249406444854181938895961879693582435980269215021670714998480664777511616503754913970130594604524188495758633604026027426089580017726713037056229182343014898816300841627354226055273577854724325963887355405412529199299916432612543440175195791257589693974318146907364080976037599997057859570965869466425234882607177151869080189335656817406446117743521951716305114594267392993294458765112356184961924226336761763792887426904641206768233134031442507478304323286460436542139372317410198244372581985673922038213441238454361269914861051697605304220800*k + 13935699060512581689066425217462828410176028197581700442760396235160627526704986295265592218576001224207256084487195682834130359477501244433847831080557532602127638752590033170120102816094368047663615267962932131036017862614439237521663386177807570702960373048438299013208161202222177755651317610170199846624005823783570325408618176760297690074923282432384533232892020858875658006229403678673592199450371080314776727407752785281779532066809623254014423312541548067857440255637110350399455066618071636091069102302438747033283427572915984062182360682901086832527762050865234851981974293215478820545366641454867737864933069711652057956330387458531822594404353520936951813664942236973746286049609734400846954320968644350640818877461061046439876373218872759625539131080774320583500106465844824010373797289853675315368178306405684985043065208868647871214975260359162361443134961081798940922450765022609071079933809540377420603503538095143451561205269485050488252192212601168928282673728137586463454550856697894723791127761699994901467904701836721536161947811416534104075599105013469198486656055621552548629553186289800304328216513101140016490929334930960643236327294442233209469884755943960318015218151253323992996142738294605604505551355645528197572524169358763651778066140163744570481482353408887861595240445056693790073076245847355425442675195146110785525605557196273221612408756383778449751873690519498132803591423130063840273485466593796414132119590594598457897303949542238698688076440150377524204460733811765991119387496857703666924326169243895751161010072581384970240292613891910039057523119143945453689446809482595136352684457374474684059659321602929961794807317047159269880726014049295782417049204362685267862991049081596588461795866702498165742997642986966585235478559584508388542491276944682618132185737651443096383114621348875673555696254343642840972871385586538755974888814897578944014049829368340586274867736168675890908390136854642799506363282631131962740933673480281869431290990759384299775617583817408364731471265729481051269335666664666736681940303439611026575089374024712220847665443020601611814039386275635219512940321374622854645247951907220886677280124528042819852472360754238607131997744293666337468570579733888838998772105624208786844981067235796388309291223979074187178373992560658650417342387433028894417940601833417825852331624550603694892137815556245888488623409735339149858290048332152072669183380853448804717138600106214776514485880071054206146571512139528976998159523183932789611770745141940511305221420799421840115205492303208384376979801168890945267324576046016961511675047593013171388385987062191380358910288930946093664367105484789978301042166550455691664529764255564230342665053351375149945727280681272857396868756774880527868221836668331431913702144699363923024010138059120891666858745078541127417306154054985528142310585068122770278914526417652366191993326153065083457325113641217686167645843889307259272940025675116366141442314251959815928765417813136662223036139734294478447099322156792620882905972355936201604888386022787935678812210854000
f = f / f.coefficients()[-1]
print(long_to_bytes(int(f.small_roots(epsilon = 0.03)[0])))

f = 4117761799700371531855881845161839729433309691973404633329118404096392177284927740340788820760864719790212893075692815209099539889726449077438887357010220597199453538428435351975911888205049047599032155266718892848909423057388249845813766752009690759146403056377355114073371283383605795160141301257577113963073191401453084157824051748162246507612381361431811560923168446826968306413655130805841528169046128846627520426087887272318463785806691711865520459287663602673075540712552805891573569096077800216245062547178172327135696975223413485245655424025905504665898978287673860887119049731745080166599849995658431291651600*k^4 - 1325349662995820416089128245917475744993956449138387302555992803223154196825687504058641074888740367103778920911268092977795057737466003659109055251751003625883426205194400055386569032121323774589317123432373444253209489919048237829312662447196155318630836614845445172643261105960686900008658738060520535448389336957401638543161474633549345601401672969880578387801995439103356586318380712860050634813751446738731407605210658325852858121919932519743890672966751421726460509600847111997465053629974202494416749311739046843743955870329438062370207472626212165332381738966010667520221360107327459416351082896103659397229582790766851535454141968754055275305639889540000268517940284421644916631163862659719354764531241650533281249032355894601354307255844532851430979105294767471969044310843550475621278491961916419900677791936346612575672536152287609935668827553430512927789133366982379182521459599166286782200357094032093337488891275964628482687774263266375124946711972883798655829997529676058223389591782327660751522751594994677977545422663430827598322401186258049845601753466323761370293621960050074073937685797104210650913735244162021324584493855890322527060030287425872998418032413855730848162812311620736288761705890396778830195455200*k^3 + 155229293481858190299421543047742535542173675590784445626693301646206039916129308739647921979832079811834015543694314135585756221411637989558374216052345960190536157740086333168415766070203970905109069301443706542913770766839756699708421347026394825585389862171873060735422627223617212285055333043603135434245277833007904586980165307331398873293817771364389196980689852650423998072184491537391168139250436128385751934080202062835807115630300826291592028156221999434442246743152719563278440210053106297922398029876569875399625962433129761362078119681540504443214810913341737086700731919478258819773176634450199846341284736052063997540627562428307935870530091773316862604217569263190175509121678764194051860173233739832853913689433481649215197974357271372642616426774503564860772548596955499360189045032919431803275123494257530680477121668590447887472086622347931154451894529677870866993113396088160011359122064361021427499812120491083406816770942826877905773304817234571320040502411553011804870320409670465131611204183626004185681451913053466907424845003876413119951263205999737408550135188285378265290430587233402878092707857007838509234430725083537992956447831865004234528831147821773289596819133725232842913153560334433266032942907226082941661931330345422961807485730249845906226861528093605518603493864432996947913429929049064775005176953778456123792442739579559650640743849245758152097512186164589955278628488113617773381103197164154225198343510141469617007664302488494669292565333896776568928897166399791139347187028301941834892344247901747734076438212525841773034531715351649164867500776469987760057580527713606878427384124833858021936950076760196711593736282428984862296678536659193003488487027540676324435841022403348063103213693741611873355346263911369573409726961603259213187716061287918148495107036788868299479981074826454666972721030400*k^2 - 7818741043407336293704942866754290736256844969365291076551455635996162715989816965257603074735063526546399084339892791616439487263200125188947813528208115142599807260513477725565315200105425456507056357092251047455062547878423789167235162770714904167692261947121466447299634571845643360335546888992787249681589508635515213634407070825678489968355004863209320698218878627390182893516646393642103374277691762038322399458706864036664792063277551227413607792085754058583999005741217891614760337075992635737634403460143833968080828696323902931991619596571087629655655636037202693288255922283546817065621475095331443043865897778798927720178829285513970980840696515508284896955969727523378468289552404445819939119544825341126181642284656366717235276201880272898682996394857438047580608978453105812855768843915628584328320527133225397067069457404057931129751721347371950220303620932822748286573538596692041466709291192017562382143883020766092045770909885567052893016548489113398228862637006856111635205629397073084474129838264630512427654481305422081527765567048130006733314267569334076446882067889886723128872411471233905192231935144612995501326679722191431235905231935608105708858003918001800646593556380886503128358905682796640977774011401057011430177936825252808940627409959629161477745222155915834948246165451515703555441227789527715795620201254280960400579663519190996410926228688679166746449138620044757350913540836830917011359932328672288788847442266918847433797039622008076660569525063835758698644668577684213130329675124951560111666380555050753484829383828805332685502522191909651225813320101156593606490334116766106252140901822477097509693964766774986315627198115330063070294490147275728694654489730989221785855507663963808891610604293307901234841553387030577682978148183488246541800361859895090961688582474373712711240868554857368999712105890454375056220481472393722991220162744356063399145421598025082285386481524216698570099758577588713468688999321161106974463290953546195309378849286936316658003884104301452955555430335176805261324306819078605617525717511532251535742102016740025225840004291722346370029937503353816790105070538012987923009089187901157477538372938201629456672769680357138064018551318259346546527693762184655563006175289846793917071607835512613003563781456290515498462057497217831624921223317737127719004544893512597288714371946605137744619209235713648505251694720029716230064746162353456356877240427265696218682083180811810781321692205600*k + 143309155066504247296923591076721109934102930254436636287578758206911409246738154356809737335869264361604846570488230324056461225413946262128871157160464923671844204183426291159072465986737780317215779624778540882019950774282821670603078134203600932502992992156742070821056346910935991217663872527906550808231114437520706783185656507774287031798529754551918002655917301730816676976051198728259079255274722628070723438775889534809296588193954941014384311984906521499933976891233205660799464131344601221653624381799825380341942244688324805778749423612280981148312346998973133283808708000777328283644980765440498000925763582661292455181523701073489054803179259378878963808065737149364275434874737304087420655016017664974829524469777283622408861736185082301382493803773180801558961236994393462363715363800028773852273356847174239770143466957034138821618728490819919114440357207154379677480562976670530387478331648652070899140572311107380470267715608550127995719387376055076422208436354762565150192732618576830688642495745099737275453876766343473810074770416220365381587887919997327749729013672900093998048608345797990336778008548385299926120712185105955660955376768837409695068113761181436685300753028578580878945021639483885066781700702080614629132376939726308076465260652142136796211245659692507211538292323839776033346281408839404149238221367421391539919078014794538750065459018645032611028125996127273542373414918303912134109499952842280164367170254736892024946782072140833725499953805398707145264476576463664444698126625943311174019334540407806733798821377539729613752827524652502252378812872351862168626822088761367473652790422840167639094454337154480523582130493118259807820865495517634866329199698803331681043569027156878390010149786053393834633557657463497227245257609842319437224414670578384093054278131755830993987172722338357472690053083883124297006161516623218566185734328626259885551048251090886361367794705858317463129572520577603063126697248311950418099048186876088938645315939003255024452199009505884547279787599303163032444941926285689262667584950295669345147797030784792495953031958514568405813960159734483861217575300234492261232474233282941157434731910378928663700234710793644100482291332549725910934517589352780419593678940410297938363166125809955063892339328582966551588252875373734104667490319866029214772589250464798196556059089011666046989828051264491324860507211239483142104406111059473891849537868329869821964509098244768794417333829892473227458240224349851764586968320573610829934874409027326917686262574375438148667672108267048109975678728956159259259973727806395883070797426569083979679342792888534763302018606324621002513764487431368845543970327134630697324217234624623553558414664344054493811386231730128888614460688009328532106408974804398976169095328475432075882161282489994089031297290860155671807838435091804255167837246083650290325680669281825837133733593704261558238383667402859788233122044715064732588388840400431287572562885408945079016480748778236993001449022687518248126500012472155991526361040058623827799777562799240610635869513698800
f = f / f.coefficients()[-1]
print(long_to_bytes(int(f.small_roots(epsilon = 0.03)[0])))
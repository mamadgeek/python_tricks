# request
# یه داده را از اینترنت میگیره و یا میفرسته
# کار با API
# یعنی از زبان کامپیوتر به کامپیورتر ولی زبان html  برای موارد خواندن صفات وب هست



# ///////////
# گرفتن اطلاعات یک سایت
import requests
myrequest=requests.get('https://stackoverflow.com/questions/1389141/how-to-add-json-library')

print(myrequest)
# این یه عنی به درستی اومده
<Response [200]>

# این یعنی forrbiden
# 403

# توجه شود که اگر 404 اومد یه دلیل اینه که ادرس را اشتباه زدی
# مثلا بجای
# https://api.coindcx.com/exchange/v1/markets
# بزنی
# https://api.coin
#
# /////
# لیست پاسخ ها به وضعیت درخواست requests
# https://restfulapi.net/http-status-codes/
# این یه عنی به درستی اومده
<Response [200]>
# یعنی درست اومده

# 403
# این یعنی forrbiden

100 Continue

200 OK
201 Created
204 No Content
302 Found
400 Bad Request
404 Not Found

# بطور کلی
# اولش 1 : یعنی
# اولش 2 درسته: یعنی
# اولش 3 میفرسته به سایت دیگه: یعنی
# اولش 4 خطایی از طرف کاربر رخ داده: یعنی
# اولش 5  خطایی از طرف خود سرور رخ داده: یعنی


# //////////////////////////////
# به زبون ادمی زاد میگه
import  requests
url='https://www.python.org/'
my_response=requests.get(url)
print(my_response.reason)
# OK


# /////////
text
# میاد سورس کد را بهمون میده . اون نوشته ها و چیزهایی که بارگذاری شده را
import  requests
url='https://www.python.org/'
my_response=requests.get(url)
print(my_response.text)
# OK







# ///////////
# request 9 تا متد داره . get - requeste .......

# //////////
# نوشن دادن وضعیت پاسخ دهی
# مثال قیمت بیتکوین
import requests
myreques=requests.get('https://api.coindcx.com/exchange/v1/markets')
print(myreques)
print(myreques.status_code)
# 200

# /////////
# دادن اطلاعات به ما
# text
import requests
myreques=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

print(myreques)
print(myreques.text)

#  یا اگر خروجی جیسون باشه مثل درخواست api بیتکوین
{"time":{"updated":"Feb 28, 2023 12:07:00 UTC","updatedISO":"2023-02-28T12:07:00+00:00","updateduk":"Feb 28, 2023 at 12:07 GMT"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"23,426.1940","description":"United States Dollar","rate_float":23426.194},"GBP":{"code":"GBP","symbol":"&pound;","rate":"19,574.7403","description":"British Pound Sterling","rate_float":19574.7403},"EUR":{"code":"EUR","symbol":"&euro;","rate":"22,820.5332","description":"Euro","rate_float":22820.5332}}}


# برای استکاورفو را زدم این اومد
# این شکلی میده
# ["PAXGINR","MAHAINR","IOSTINR","TRADEINR","GNOINR","REEFINR","HOTINR","SNTINR","XNOINR","POLYXINR","MASKINR","UFTUSDT","OSMOINR","XCNINR","DAIINR","NMRINR","RLCINR","DCRINR","IMXINR","OXTINR","LQTHUSDT","ARPAINR","ARINR","TRBINR","DASHINR","SXPINR","THETAINR","ETNINR","LITINR","BANDINR","DGTXINR","FANCINR","TUSDINR","SFPINR","TWTINR","LPTINR","SCINR","CELOINR","ETCINR","STPTINR","YFIIINR","BONDINR","MARSHINR","GRTINR","VETINR","STORJINR","NEXOINR","MDXINR","DOGEINR","XEMINR","ICXINR","LCXINR","BNBINR","BTCINR","VINUINR","JASMYBTC","LDOINR","HIGHINR","XMRINR","PEOPLEINR","ALICEINR","MBOXINR","STXINR","CAKEINR","ALPACAINR","KLAYINR","EOSINR","ONEINR","FLOWINR","COMPINR","BCHINR","UNIINR","AXSINR","AVAXINR","TRXINR","GLMRINR","NEOINR","CRVINR","CHZINR","BNXINR","OPINR","AUDIOINR","ICPINR","SPELLINR","MKRINR","ENSINR","APTINR","EGLDINR","ADAINR","ARVINR","ZILINR","FLMINR","USDCINR","GALAINR","LRCINR","IOTXINR","DAOINR","ENJINR","ALGOINR","XLMINR","WAVESINR","USDTINR","XTZINR","ZRXINR","SKLINR","INJINR","CELRINR","QTUMINR","ZECINR","FTMINR","TFUELINR","SUPERINR","TLOSINR","KAVAINR","COTIINR","FIDAINR","LINKINR","JASMYINR","SNXINR","RVNINR","WAXPINR","NEARINR","OMGINR","SANDINR","BATINR","BRISEINR","KSMINR","XDCINR","XRPINR","FILINR","LTCINR","BUSDINR","OOKIINR","GMTINR","SOLINR","MINAINR","ETHINR","CKBINR","APEINR","QNTINR","KNCINR","PUSHINR","DOTINR","DYDXINR","XLDINR","ATOMINR","UMAINR","RUNEINR","SUSHIINR","SHIBINR","MANAINR","MATICINR","HBARINR","JSTINR","CHRINR","YFIINR","PONDBTC","HOTETH","WINBNB","DATABTC","MTLETH","PEOPLEBTC","BNTETH","OXTBTC","IOTABNB","ZILETH","XVSBNB","POLSBNB","KAVABNB","YGGBNB","VITEBTC","BURGERETH","ACMBTC","DENTETH","FORTHBTC","WBTCBTC","QKCBTC","PROMBNB","BNBDAI","LINABTC","ILVBNB","USDTDAI","HIFIETH","ETCBNB","DFBUSD","THETAETH","ARPAETH","WRXBNB","RADBNB","EOSBTC","PUNDIXETH","ARPABTC","QTUMETH","ROSEBTC","GARIINR","FORTHUSDT","CELRBNB","XVGETH","SKLBTC","LNUSDT","ALGOBNB","CTKBTC","SKLUSDT","COTIBTC","QLCBTC","ADABNB","JSTBTC","SCETH","DGBBTC","KNCETH","CTSIBNB","NEOBTC","ONGBTC","WTCBTC","RLCETH","IRISBTC","FIOUSDT","ANKRBTC","EGLDBNB","VIDTBTC","AMPBTC","CHZBTC","DIAUSDT","SUPERBTC","WAVESUSDT","MDXBTC","MULTIUSDT","ACABTC","MDTBTC","ETCETH","INJBTC","BIFIBUSD","BLZBTC","XVSUSDT","CAKEBNB","ARDRBTC","FORTHBUSD","DASHETH","WAVESBNB","GHSTBUSD","JOEBTC","ETCBTC","PAXGBUSD","BATETH","MBOXBTC","SXPBNB","XLMUSDT","THETAUSDT","SUNUSDT","PSGBTC","EPXUSDT","PSGUSDT","MBOXBUSD","FLMBTC","GLMBTC","PYRBTC","DARBTC","INJBNB","LRCETH","ARPAUSDT","SFPBTC","AVAXUSDT","WAVESBTC","ENSBUSD","CLVBTC","STEEMBTC","ENSUSDT","XVGBUSD","VTHOUSDT","NEOBNB","MCUSDT","QNTUSDT","PEOPLEBNB","VGXUSDT","ASTRBUSD","XTZBTC","BALUSDT","CELOUSDT","WOOBTC","WOOUSDT","WAXPBNB","POLYXBUSD","PERPBTC","AUDIOUSDT","IOSTUSDT","DODOBTC","YGGBUSD","ZENUSDT","TRXUSDT","ICXBTC","GNSUSDT","SNXBTC","HFTUSDC","KCSUSDT","NYMUSDT","UOSUSDT","NPTUSDT","ERGUSDT","TONUSDT","ZCXUSDT","KCALUSDT","MRSUSDT","PRQUSDT","IGUUSDT","GFUSDT","BLDUSDT","BOSONUSDT","NUMUSDT","STRMUSDT","SDUSDT","POOLZUSDT","POLCUSDT","EULUSDT","FXUSDT","RDNTUSDT","BLURUSDT","FOTAUSDT","PSTAKEUSDT","KOKUSDT","DORAUSDT","STGUSDT","AQTUSDT","EFIUSDT","CEEKUSDT","HTUSDT","BWOUSDT","TAVAUSDT","MLKUSDT","ARGUSDT","EVERUSDT","SWAPUSDT","JUMBOUSDT","BSVUSDT","CHSBUSDT","EVMOSUSDT","FUSEUSDT","AIOZUSDT","PUSHUSDT","DYPUSDT","GSTUSDT","XCADUSDT","PBRUSDT","SUDOUSDT","SISUSDT","USDPUSDT","SDAOUSDT","TAOUSDT","DFIUSDT","PORUSDT","REVOUSDT","WBTUSDT","CTXUSDT","DAOUSDT","SFUNDUSDT","MLNUSDT","EULUSDC","XTMUSDT","QRDOUSDT","VOXELUSDT","LUNRUSDT","TCNHUSDT","FANCUSDT","SPUMEUSDT","USDCUSDT","GRVUSDT","AURYUSDT","ROCOUSDT","ZEDUSDT","CUSDUSDT","DFXUSDT","ITAUSDT","ONITUSDT","SCREAMUSDT","ROUTEUSDT","WPCIUSDT","MBXUSDT","KRRXUSDT","SOULUSDT","XDEFIUSDT","TLOSUSDT","MPLXUSDT","OCTUSDT","TOMIUSDT","TOKEUSDT","STETHETH","ORBRUSDT","WAXLUSDT","AGLDUSDT","JOYUSDT","AKTUSDT","CRPTUSDT","HSFUSDT","ABBCUSDT","TINCUSDT","USDJUSDT","AZEROUSDT","BBFUSDT","ORCUSDT","FUDUSDT","FDTUSDT","DKSUSDT","TDXUSDT","METISUSDT","FSNUSDT","NOIAUSDT","CTCUSDT","RSS3USDT","LOKAUSDT","WMTUSDT","TRIBEUSDT","PONDUSDT","BUSDUSDT","THETABTC","XNOETH","RVNBTC","LSKETH","ZECETH","REIBNB","ZECBNB","LPTBNB","AXSBNB","OMBTC","IOSTBTC","PLABNB","AXSBTC","PAXGBNB","WAXPBTC","AUCTIONBTC","CITYBNB","STMXBTC","GALBNB","CLVBNB","CITYBTC","FUNETH","WINTRX","STPTBTC","CELRBTC","THETABNB","ELFETH","XMRUSDT","JUVBUSD","OGNBTC","ARBNB","WBTCETH","ENJBNB","TRXBTC","ARPABNB","XLMBTC","AUTOBTC","POLYXBTC","HARDBNB","XNOUSDT","WINGBTC","EOSBNB","EOSETH","CTSIBTC","YGGBTC","BCHBNB","TFUELBUSD","LTCBTC","DASHBNB","IRISUSDT","KLAYUSDT","QIBTC","FIOBTC","VIBBTC","GALABTC","ZILBTC","VETBTC","TVKBTC","POLSUSDT","XNOBUSD","FARMBUSD","FARMBTC","FLOWBUSD","ALPHABTC","BNBETH","XNOBTC","KP3RBNB","HBARBTC","KDABTC","CVPETH","ZRXETH","SCUSDT","AAVEETH","RADBTC","IOTAETH","MTLBTC","C98BTC","QNTBUSD","NKNBTC","CREAMBUSD","RAYBNB","QNTBTC","BELBNB","BNTBTC","ATMUSDT","MTLUSDT","OMGUSDT","FUNUSDT","BALBTC","BNTUSDT","IQBUSD","DGBUSDT","MBOXUSDT","LAZIOBTC","DGBBUSD","MOBUSDT","SUSHIBNB","BARBTC","POWRETH","SUPERUSDT","LPTBUSD","KDAUSDT","ZENBTC","KDABUSD","APTETH","ASTRUSDT","WNXMUSDT","TORNBUSD","VIBBUSD","HNTBUSD","XTZUSDT","GRTETH","KSMBTC","LDOBUSD","RADBUSD","QTUMBTC","LINKETH","HIFIUSDT","IMXBUSD","ACMUSDT","APEUSDT","COMPBTC","SHIBUSDT","RUNEBTC","ACHBTC","KAVABTC","ZENETH","TFUELBTC","RUNEBNB","TRBBTC","ONEBTC","TLMBTC","MCBUSD","CITYBUSD","DIABUSD","SOLBNB","COSBTC","SXPBTC","VETBNB","AUCTIONBUSD","BCHBTC","IDEXBTC","POLSBTC","MINABUSD","AMPBUSD","PSGBUSD","BAKEBTC","GALABUSD","UMABTC","UMAUSDT","RAREBTC","OMGETH","LOOMBTC","MINAUSDT","OSMOBTC","COSBNB","SNMBTC","TFUELUSDT","SYSBTC","BAKEBUSD","BICOBUSD","HIVEUSDT","AMPUSDT","ICPBNB","NEOETH","BCHBUSD","RUNEUSDT","ENJBTC","DFUSDT","BTSUSDT","KNCUSDT","TUSDT","DOGEBTC","XTZBNB","EGLDETH","BARUSDT","OOKIBUSD","UFTETH","DEXEETH","BETABTC","ALPACABTC","KLAYBTC","AKROUSDT","COTIBNB","UTKBTC","XLMETH","REQBTC","SCRTBUSD","OGBTC","SCRTETH","ATMBTC","JUVUSDT","WAVESETH","AAVEUSDT","REIUSDT","HIVEBTC","ENSBNB","1INCHUSDT","STEEMETH","ORNUSDT","ALGOUSDT","MULTIBUSD","ZECUSDT","ARBUSD","BATBTC","ELFBTC","PEOPLEUSDT","ALICEUSDT","BSWBUSD","PROSETH","WANETH","CTKBUSD","CTKUSDT","OSMOUSDT","ALICEBTC","ARBTC","GNOUSDT","MDXUSDT","ASTBTC","MATICBTC","ONTETH","QNTBNB","OGBUSD","ARDRUSDT","PYRBUSD","ONTUSDT","ADXBTC","ALPINEBTC","ILVBUSD","C98BUSD","COMPUSDT","REQUSDT","BANDUSDT","VITEBUSD","WANUSDT","POLYXUSDT","ICPBTC","DENTUSDT","EPXBUSD","GMXUSDT","LTOBTC","OOKIUSDT","ANTBNB","XVSBTC","ATMBUSD","AUCTIONUSDT","QKCETH","BSWBNB","HARDBTC","ONEBNB","ICPETH","PROMBUSD","QUICKBUSD","NULSBTC","PLABTC","RPLBTC","BONDBTC","NEARBNB","WOOBNB","CRVUSDT","FLUXBUSD","AAVEBNB","RAYUSDT","ATOMBTC","PROMBTC","SNXUSDT","WINUSDT","XRPUSDT","ATOMBNB","ACMBUSD","IOTABTC","MKRUSDT","LTOUSDT","YFIBTC","IOTXBTC","COSUSDT","BELBTC","SUSHIBTC","RNDRUSDT","PHABTC","ORNBUSD","RAREBUSD","ASRBUSD","AAVEBTC","COCOSBNB","RADUSDT","MDXBUSD","KAVAUSDT","KSMUSDT","CVCBUSD","GMTUSDT","DOTUSDT","WAXPBUSD","BATUSDT","BETAETH","EOSBUSD","CITYUSDT","OMGBTC","TKOBTC","NEXOBUSD","ORNBTC","ATOMBUSD","ERNUSDT","KNCBTC","TRXBNB","TOMOBTC","LTOBUSD","REEFUSDT","ZECBTC","LSKBTC","GALAUSDT","ACHUSDT","ZILUSDT","TBUSD","UNIBTC","LPTUSDT","ACABUSD","MOVRUSDT","LSKUSDT","STRAXBTC","EGLDBTC","BETABNB","OMUSDT","DIABTC","POLSBUSD","API3BTC","OGNUSDT","ZILBNB","WINGUSDT","HBARUSDT","MOVRBUSD","STRAXUSDT","GMXBTC","DCRBTC","DOCKBTC","TRXETH","JOEBUSD","ATOMETH","CVXBTC","PUNDIXUSDT","IMXUSDT","MANAETH","NEXOUSDT","MOVRBTC","WAXPUSDT","OXTUSDT","FLOWUSDT","IMXBTC","OSMOBUSD","PLAUSDT","MCBTC","AVAXBTC","MOBBUSD","ALGOBTC","GLMRUSDT","HIGHBUSD","HIGHUSDT","BSWUSDT","XMRBNB","SHIBBUSD","CAKEBTC","AUDIOBTC","OGUSDT","GRTBTC","CKBUSDT","TLMUSDT","API3BUSD","ATOMUSDT","STORJBTC","GHSTUSDT","DOTBTC","AVAXBUSD","CAKEUSDT","ATABUSD","GALUSDT","SANTOSBUSD","FILBNB","YGGUSDT","INJUSDT","UNFIUSDT","DCRUSDT","AMBBTC","RNDRBUSD","DODOBUSD","PAXGUSDT","SNXBNB","WABIBTC","AERGOBTC","CELOBTC","WRXBTC","IOTXUSDT","WTCUSDT","BNBUSDT","FILBTC","QUICKUSDT","USTCBUSD","APEBUSD","CELRUSDT","API3USDT","ERNBUSD","SYSUSDT","ADABTC","GASBTC","LINKBNB","MATICBNB","SANDBTC","CFXBTC","AXSUSDT","XLMBNB","ALPACAUSDT","VETETH","ILVBTC","KMDBTC","ENJETH","NMRBTC","PHBBTC","FXSBTC","NEARBUSD","MAGICBUSD","ADAUSDT","HBARBNB","TLMBUSD","AVABTC","DODOUSDT","JASMYBUSD","SOLUSDT","SOLBUSD","RENBTC","NEXOBTC","XRPETH","GNSBTC","IOTXETH","NEBLBTC","WANBTC","HFTBTC","SCRTBTC","XRPBNB","ANTBTC","JOEUSDT","FARMUSDT","DEGOBTC","MINABNB","ZRXBTC","ONEUSDT","DREPBTC","MBOXBNB","MASKBNB","OPUSDT","BANDBTC","ASRUSDT","MOBBTC","RAREUSDT","FILUSDT","GALBTC","FIDABTC","BCHUSDT","BNBBTC","OPBUSD","DUSKBTC","RNDRBTC","ATABTC","KP3RUSDT","ARKBUSD","CHRBTC","COTIUSDT","BICOUSDT","HFTUSDT","GMTBNB","RAYBUSD","HARDUSDT","IOSTETH","ANTUSDT","ALPHAUSDT","SXPBUSD","GRTUSDT","BONDUSDT","CLVUSDT","PNTUSDT","ONEBUSD","RLCBTC","NMRUSDT","FETBNB","PYRUSDT","POWRBTC","ADAETH","ENJUSDT","SANDUSDT","BNXBUSD","BNXUSDT","ALPACABUSD","MULTIBTC","HOTUSDT","DASHBTC","OCEANUSDT","DARBUSD","STMXUSDT","BNBBUSD","UNIBNB","CHZUSDT","COCOSUSDT","STXBTC","PHAUSDT","BAKEUSDT","ANKRUSDT","ONGUSDT","DREPUSDT","GTCUSDT","BLZUSDT","LITUSDT","ONTBTC","TRUBTC","CVXUSDT","SLPUSDT","SUSHIUSDT","ACAUSDT","EGLDUSDT","SRMBUSD","GLMRBUSD","PORTOBUSD","DOGEBUSD","UTKUSDT","KLAYBNB","POWRUSDT","DUSKBUSD","NULSUSDT","LEVERBUSD","LRCBTC","OAXBTC","CAKEBUSD","XECBUSD","PEOPLEBUSD","ATAUSDT","CHRBNB","ARUSDT","NEARETH","JSTUSDT","VETBUSD","UNIUSDT","LINKUSDT","HIGHBTC","CRVBTC","FIROBTC","ENSBTC","FETBUSD","ROSEUSDT","FETUSDT","SANTOSUSDT","GTCBTC","VETUSDT","NEBLBUSD","ICPBUSD","CVPUSDT","LEVERUSDT","XRPBUSD","VIDTBUSD","MBLUSDT","ROSEBUSD","ALPINEBUSD","MAGICUSDT","GFTBUSD","SANTOSBTC","FISUSDT","YFIIUSDT","DOGEUSDT","FISBTC","BETAUSDT","SYNUSDT","SANDBNB","ICXUSDT","RIFUSDT","GALBUSD","ETCUSDT","CHRUSDT","ILVUSDT","MANABUSD","CHZBUSD","WOOBUSD","GMTBTC","RIFBTC","GMTBUSD","XEMUSDT","FLUXUSDT","QUICKBTC","AVAXBNB","DUSKUSDT","ALCXBUSD","XMRBTC","FLOWBTC","ETHDAI","LRCUSDT","CTXCUSDT","LINAUSDT","STXUSDT","LINKBUSD","LTCBUSD","LDOBTC","TKOUSDT","SSVETH","BADGERUSDT","LUNAUSDT","BICOBTC","YFIUSDT","OPBTC","CHESSBUSD","NULSBUSD","LINABUSD","MAGICBTC","GTCBUSD","FIDABUSD","ANKRBNB","AGIXBTC","NKNUSDT","SXPUSDT","SLPBUSD","SSVUSDT","NEOUSDT","GALABNB","FTMBUSD","AUTOUSDT","GASBUSD","LAZIOBUSD","FIDAUSDT","CVPBUSD","AMBBUSD","LUNABUSD","SPELLBUSD","CFXUSDT","CHESSUSDT","BELUSDT","SOLBTC","BTCDAI","ALPINEUSDT","PHBUSDT","DEGOUSDT","DYDXUSDT","MATICBUSD","FXSUSDT","BURGERUSDT","PROSBUSD","QTUMUSDT","KP3RBUSD","PERLUSDT","LTCETH","ACHBUSD","NEARBTC","PERPUSDT","LPTBTC","RLCUSDT","PROSUSDT","BTCBUSD","ETHBUSD","IOTAUSDT","FLUXBTC","STXBUSD","TOMOUSDT","NEARUSDT","JASMYUSDT","CLVBUSD","FXSBUSD","LUNCBUSD","ETHBTC","PORTOUSDT","LUNCUSDT","TRUUSDT","XMRETH","BNXBTC","GMXBUSD","C98USDT","SFPBUSD","ANKRBUSD","MKRBTC","RVNUSDT","KLAYBUSD","AGIXUSDT","STPTUSDT","BADGERBUSD","RPLUSDT","ICPUSDT","XRPBTC","SANDETH","CHZBNB","ZRXUSDT","GLMRBTC","FTMUSDT","PAXGBTC","DATAUSDT","FTMBTC","STORJBUSD","NEBLUSDT","SYNBTC","NEOBUSD","CHESSBTC","MDTBUSD","MDTUSDT","PORTOBTC","MANABTC","BONDBUSD","FETBTC","APEBTC","BNXBNB","TROYUSDT","DYDXBNB","CTSIUSDT","UNFIBTC","DYDXBTC","DYDXBUSD","FIROUSDT","RENBUSD","APTUSDT","LDOUSDT","QKCBUSD","BADGERBTC","MATICETH","PHBBUSD","LTCUSDT","SSVBTC","FTMBNB","LITBTC","1INCHBTC","ALCXUSDT","TWTUSDT","LTCBNB","VIBUSDT","VITEUSDT","MASKUSDT","SFPUSDT","KEYBUSD","APTBTC","CVXBUSD","MATICUSDT","DASHUSDT","SPELLUSDT","RENUSDT","BETABUSD","LAZIOUSDT","BURGERBUSD","ADABUSD","ALCXBTC","FTTBUSD","TRXXRP","BTCUSDT","RPLBUSD","DARBNB","MANAUSDT","AGIXBUSD","APTBUSD","DARUSDT","STORJUSDT","HFTBUSD","MASKBUSD","PIVXBTC","ETHUSDT","STXBNB","FLMUSDT","OCEANBNB","QIUSDT","EOSUSDT","LINKBTC","TWTBTC","TRBUSDT","PLABUSD","WRXUSDT","DOCKUSDT","VIDTUSDT","OCEANBTC","QIBUSD","BTTCUSDT","LNBTC","OASUSDT","NBSUSDT","MUUSDT","ORBUSDT","MMFUSDT","VPADUSDT","RAINUSDT","KAIUSDT","BITCIUSDT","QOMUSDT","LITHUSDT","SPSUSDT","ELONUSDT","FACEUSDT","COREUSDT","ELUUSDT","DOSEUSDT","GARIUSDT","TNBUSDT","GALFTUSDT","XETAUSDT","ETNBTC","DCUSDT","HAOUSDT","ADPUSDT","TNBBTC","XCURUSDT","KLVUSDT","SNTUSDT","ZBCUSDT","LIKEUSDT","OLANDUSDT","CAWUSDT","HTBTC","RYOMAUSDT","CRTSUSDT","CUDOSUSDT","SWFTCBTC","WOOFUSDT","BXENUSDT","BSVBTC","GQUSDT","KRIPTOUSDT","BTCUSDC","FIUUSDT","BABYDOGEUSDT","WWYUSDT","VEMPUSDT","KUBEUSDT","SHITUSDT","ARVUSDT","BRWLUSDT","ALIUSDT","UNQUSDT","INGUSDT","LBLUSDT","VELOUSDT","ANMLUSDT","ETHUSDC","TUSDUSDT","ACTUSDT","STARLYUSDT","SMCWUSDT","NODLUSDT","LBPUSDT","DOGUSDT","HECUSDT","SYLOUSDT","RSRUSDT","ANTEXUSDT","FITFIUSDT","MESAUSDT","SKEBUSDT","XDCUSDT","SOSUSDT","TTUSDT","FILDAUSDT","VLXUSDT","MCGUSDT","DBCBTC","SPRTUSDT","WNDRUSDT","MEVUSDT","STETHUSDT","IPVUSDT","SEANUSDT","RANKERUSDT","MOOVUSDT","BRISEUSDT","GRAILUSDT","EGAMEUSDT","ONSTONUSDT","VISIONUSDT","BERRYUSDT","GMEEUSDT","REVVUSDT","HOTCROSSUSDT","HOOPUSDT","TTBTC","VINUUSDT","BRTUSDT","PANDOUSDT","BONKUSDT","1SOLUSDT","WELLUSDT","CEREUSDT","USDDUSDC","TNBETH","MCRTUSDT","HYPEUSDT","SAOUSDT","FRONTUSDT","KICKSUSDT","NTUSDT","BABYUSDT","XENUSDT","RACAUSDT","GEARBOXUSDT","HTRUSDT","ZIGUSDT","MCONTENTUSDT","SWEATUSDT","FLOKIUSDT","PARADOXUSDT","LMRUSDT","NESTUSDT","MINEUSDT","FORUSDT","XCNUSDT","VRUSDT","DEPUSDT","ELAUSDT","USDDUSDT","BBCUSDT","TOMSUSDT","MGGUSDT","RSRBTC","PLYUSDT","LOVELYUSDT","RETHUSDT","ORBSUSDT","ROSEINR","EFIINR","DFAINR","KDAINR","AAVEINR","BTTCINR"]


# //////////
# توجه شود که اگر سایت باشه نه API
# اینو میده به عنوان فایل HTML
<!DOCTYPE html>
<html lang="fa" prefix="og: http://ogp.me/ns#">
<head>
    <title>مرجع فوتبال و ورزش - ورزش سه</title>
    <meta charset="utf-8" />
# print(و....)



# هرچند درونش هم api داره
# <script type="application/ld+json">
#         {
#             "@context": "http://schema.org/",
#             "@type": "Organization",
#             "name": "ورزش سه",
#             "url": "http://www.varzesh3.com/",
#             "logo": "https://static.varzesh3.com/img/logo/vrz3-logo.svg",
#             "potentialAction": {
#                 "@type": "SearchAction",
#                 "target": "https://www.varzesh3.com/search?q={search_term_string}",
#                 "query-input": "required name=search_term_string"
#             },


# ////////////
# متد request از کتابخانه requests
import  requests
url='https://www.python.org/'
my_response=requests.get(url)
print(my_response.request)
# <PreparedRequest [GET]>

# میگه در خواست ی که دادی get بود

# /////////
# headers
# اطلاعات درخواست را میده . زمانی که درخواست کردیم . یا سروری که از اون رفتیم به html کهاگر از فایرفاکس میرفتیم در network inspect مینوشت fiefox
import  requests
url='https://www.python.org/'
my_response=requests.get(url)
print(my_response.headers)
# {'Connection': 'keep-alive', 'Content-Length': '50343', 'Server': 'nginx', 'Content-Type': 'text/html; charset=utf-8', 'X-Frame-Options': 'DENY', 'Via': '1.1 vegur, 1.1 varnish, 1.1 varnish', 'Accept-Ranges': 'bytes', 'Date': 'Wed, 01 Mar 2023 12:34:13 GMT', 'Age': '130', 'X-Served-By': 'cache-iad-kiad7000025-IAD, cache-fra-eddf8230037-FRA', 'X-Cache': 'HIT, HIT', 'X-Cache-Hits': '302, 1', 'X-Timer': 'S1677674053.225642,VS0,VE2', 'Vary': 'Cookie', 'Strict-Transport-Security': 'max-age=63072000; includeSubDomains; preload'}


# ////////
# میاد وضعیت status code را بهمون میده که ایا وصل شده یا نه یا ...
import  requests
url='https://www.python.org/'
my_response=requests.get(url)
print(my_response.status_code)
# 200



# ////////////////////////
# اوردن request در پایتون
# کتابخانه
# دادن قیمت بیتکوین از json
import requests
myreques=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print(myreques.text)

import json
myprice=json.loads(myreques.text)
print(myprice)
# اینو به عنوان دیکشنری به ما میده
{"time":{"updated":"Feb 28, 2023 12:26:00 UTC","updatedISO":"2023-02-28T12:26:00+00:00","updateduk":"Feb 28, 2023 at 12:26 GMT"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"23,490.6928","description":"United States Dollar","rate_float":23490.6928},"GBP":{"code":"GBP","symbol":"&pound;","rate":"19,628.6350","description":"British Pound Sterling","rate_float":19628.635},"EUR":{"code":"EUR","symbol":"&euro;","rate":"22,883.3644","description":"Euro","rate_float":22883.3644}}}
# یعنی
{'time': {'updated': 'Feb 28, 2023 12:26:00 UTC', 'updatedISO': '2023-02-28T12:26:00+00:00', 'updateduk': 'Feb 28, 2023 at 12:26 GMT'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '23,490.6928', 'description': 'United States Dollar', 'rate_float': 23490.6928}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '19,628.6350', 'description': 'British Pound Sterling', 'rate_float': 19628.635}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '22,883.3644', 'description': 'Euro', 'rate_float': 22883.3644}}}



# حالا کار با اون داشته
# بقیش همش کار با پایتونه
# دیکشنری
# چون منظمش این شکلیه
myprice={
    'time':
        {'updated': 'Feb 28, 2023 12:26:00 UTC',
         'updatedISO': '2023-02-28T12:26:00+00:00',
         'updateduk': 'Feb 28, 2023 at 12:26 GMT'},
    'disclaimer':
        'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org',
    'chartName':
        'Bitcoin',
    'bpi':
        {'USD':
             {'code': 'USD',
            'symbol': '&#36;',
            'rate': '23,490.6928',
            'description':
                'United States Dollar',
            'rate_float': 23490.6928
            },
         'GBP': {'code':
                     'GBP',
                 'symbol':'&pound;',
                 'rate':'19,628.6350',
                 'description': 'British Pound Sterling',
                 'rate_float': 19628.635
                 },
         'EUR':
             {'code':
                  'EUR',
              'symbol': '&euro;',
              'rate': '22,883.3644',
              'description': 'Euro',
              'rate_float': 22883.3644
              }
         }
}


# پس این شکل را بهتر میتونیم بدیم
print(myprice['bpi']['USD']['rate'])
23,490.6928


#
#
#
# و جالبه که با هر تغیر بیتکوین اینهم تغیر میکنه

my_price='23,490.6928'
my2=int(float(my_price.replace(',','')))
print(my2)

# جار زدن  یعنی تبدیل تکست به صدا
import pyttsx3
# اول موتورشو میسازیم که اینیت میدیم
engine=pyttsx3.init()
engine.say(my2)
engine.runAndWait()
# /////////

# برای ریکوئست زدن در html بدون selenium

# وقتی میخوایم از requests استفاده کنیم
r=requests.get('html:\\divar.ir')

# میا روی سوپ و کارشو میکنه
# اسم صفحه را میریزیم توی متغیر request
soup=BeautifulSoup(r.text,'html.parser')
# که فرمت اش را با تکست بهمون میده
# که باید حالیش کنیم اون text چیه فرمتش


# بعد اگر چجوری ای که ما میخوایم را
# یعنی از صفحه body یا h2 یا h3  و... را بگیریم
find
# اولین  را میده که پیدا کرده
soup.find('h2')


# //////////

# دانلود کردن یه عکس درون یک سایت
import  requests
url='https://www.python.org/static/img/python-logo@2x.png'
my_response=requests.get(url)
print(my_response.text)
with open('ax.jpg','wb') as r:
    r.write(my_response.content)

# ///////////////////
# میشه سایتی را داد و بعدش که مدلش عوض میشه ما فقط مدلو بدیم
# سایته نشانیش همونه فقط موردش تغیر میکنه
import requests
brand=input('give me the brand: ')
url = 'https://www.truecar.com/used-cars-for-sale/listings/' + brand
# برند کافیه


# یا اینکه وسطش باشه حتی
import requests
# brand=input('give me the brand: ')
brand='bmw'
# brand='ferrari'
url = 'https://www.truecar.com/used-cars-for-sale/listings/'+brand+'/location-saint-bonaventure-ny/'
print(url)
myrequest=requests.get(url)
print(myrequest)

# ////////////////
# POST
# فرستادن پیامک





















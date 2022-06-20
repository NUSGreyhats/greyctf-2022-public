from secrets import randbits
from hashlib import shake_256
from Crypto.Util.number import getPrime
import point

p = 33931086844518982011982560935885732032396635556994207701963662088123265314176330336254535971207181169698868584991941607780111073928236261199604691797570505851011072000000000000000000000000001
g = (7037549901029642100223742439070703995015665580670284242130884463773338174380139238553189710819918253669415700287683808563180514723511699603031996293290369767854639482142307793352494648242967, 8205913126553358490853022637037734409971192911752180732355041502119769228896383932378363678796043318970913089852891328173548068037853967970056632674692670400723516364615348921362905358814029, 85268887215292560542268193462562021474665751895622453490469660054424799431841824024381729541629822, 24215097905628021880376625677650998036904587714681520122543481726358815871209420768534951670526720)
A = (3015766028721941369178074698605381691599087210039866306640909196212588352441855346350743146390848597118075419600516072738798343727843876265136185648791577002567218669224905158203517212437931, 14563789624017263257940594773376415644559043440910171996988387528330382197790195517547380035989385655736251210580292706709487265686839552561607181253178070356790506752405996025507209601896292, 16640160858685938476542375593702704581305407020269313745624127384631037558812210414562586479877637535851954919361475432004742864445019253815013638490644141245403902935501989076700702970694249, 16879429782591537328966964150410467855611418811439400765239214801545241738995302304587022013336880240803211941107721007697977028875857746708864431655220494670997319520785638768853830754349136)
B = (1435848962952563117054608931007345781063668831784791425028254509618161773940663457322032727190745195104003113456519719738146575981835876786157939235660159014870512068305613758253792574311643, 18686088290326119659549028343019188323944356505454748912396787612632173494480617380239622629920198645063894495368138532784809228742111878296579418292502387693918235188739607215622230266445743, 21235066364322617891457082635222454663727721712810213608007101015483450773255736409047736659389355947350596487365366269583229495492502684524596567983482626727602630863151154584839084330180349, 16748506850569075855828947960874105053822583983603980377105312450248924558312022048423650849359977259065710570721100230957239444234196201722602496350746263703597143917582873411342846169386930)
c = "be8c0d2537c01ef36aeeb1c279984769b4bcd6778c38fd8c5adfafeddb53ef6e4abc50f1e1ade2c4e108f032cde733d2a6e0be7e905497cf425b7a96a43e0d4fda4acec8aacccbebd9d10cf64cbe0a90e842af755138a036e2dfffb9e46f4f2c88ccb896e8b02ae0fdbf447cf9ed4f9a1dbeadd7e0e6aa9db88c82c1d69d9036ec7951362a150e2b9bd15b4b68a9c1603316b4c60f812fce28dc"
c = bytes.fromhex(c)

def decrypt(key : str) -> str:
    otp = shake_256(key.encode()).digest(len(c))
    return xor(otp, c)

def xor(a : bytes, b : bytes) -> bytes:
    return bytes([ x ^^ y for x, y in zip(a, b)])

gM = [
    [g[0], -g[1], -g[2], -g[3]],
    [g[1], g[0], -g[3], g[2]],
    [g[2], g[3], g[0], -g[1]],
    [g[3], -g[2], g[1], g[0]]
]
gM = Matrix(GF(p), gM).jordan_form()
base = gM[0][0]

aM = [
    [A[0], -A[1], -A[2], -A[3]],
    [A[1], A[0], -A[3], A[2]],
    [A[2], A[3], A[0], -A[1]],
    [A[3], -A[2], A[1], A[0]]
]
aM = Matrix(GF(p), aM).jordan_form()
target = aM[0][0]

a = discrete_log(target, base)

B = point.Point(B[0], B[1], B[2], B[3], p)
S = B ** a

key = str(S)
print(decrypt(key))
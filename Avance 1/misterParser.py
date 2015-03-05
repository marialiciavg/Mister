# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .misterListener import misterListener
else:
    from misterListener import misterListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\62")
        buf.write("\u01f1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\u0098\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("\u00a1\n\4\3\5\3\5\5\5\u00a5\n\5\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\5\7\u00ad\n\7\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00b5\n\t")
        buf.write("\3\n\3\n\5\n\u00b9\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\5\f\u00c5\n\f\3\r\3\r\3\r\3\16\3\16\5\16")
        buf.write("\u00cc\n\16\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u00de\n\22")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u00e4\n\23\3\24\3\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\5\25\u00ef\n\25\3\26\3\26")
        buf.write("\5\26\u00f3\n\26\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u00fb")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u0108\n\31\3\32\3\32\3\32\3\32\5\32\u010e\n")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\5\33\u0115\n\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\5\35\u011e\n\35\3\36\3\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u012a\n\37")
        buf.write("\3 \3 \3 \3!\3!\3\"\3\"\3\"\3\"\5\"\u0135\n\"\3#\3#\3")
        buf.write("#\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0143\n$\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\5&\u0150\n&\3\'\3\'\3\'\3\'\3\'\5")
        buf.write("\'\u0157\n\'\3(\3(\3(\5(\u015c\n(\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\5*\u016a\n*\3+\3+\3+\3+\3+\3+\3+\3+\5")
        buf.write("+\u0174\n+\3,\3,\3-\3-\3-\3.\3.\3.\3.\5.\u017f\n.\3/\3")
        buf.write("/\3/\3/\3/\3\60\3\60\5\60\u0188\n\60\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\62\3\62\3\62\5\62\u0194\n\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\5\64\u019f\n")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\5\67\u01b3\n")
        buf.write("\67\38\38\38\38\38\38\39\39\39\39\39\39\39\39\39\3:\3")
        buf.write(":\3:\5:\u01c7\n:\3;\3;\5;\u01cb\n;\3<\3<\5<\u01cf\n<\3")
        buf.write("=\3=\3=\3=\3>\3>\3>\3>\3?\3?\3@\3@\5@\u01dd\n@\3A\3A\3")
        buf.write("A\3A\3B\3B\3B\3B\3B\3B\3C\3C\5C\u01eb\nC\3D\3D\5D\u01ef")
        buf.write("\nD\3D\2\2E\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz")
        buf.write("|~\u0080\u0082\u0084\u0086\2\7\3\2\n\f\4\2\26\26\30\30")
        buf.write("\4\2\31\31 $\3\2\34\35\3\2\24\25\u01dd\2\u0088\3\2\2\2")
        buf.write("\4\u0097\3\2\2\2\6\u00a0\3\2\2\2\b\u00a4\3\2\2\2\n\u00a6")
        buf.write("\3\2\2\2\f\u00ac\3\2\2\2\16\u00ae\3\2\2\2\20\u00b4\3\2")
        buf.write("\2\2\22\u00b8\3\2\2\2\24\u00ba\3\2\2\2\26\u00c4\3\2\2")
        buf.write("\2\30\u00c6\3\2\2\2\32\u00cb\3\2\2\2\34\u00cd\3\2\2\2")
        buf.write("\36\u00cf\3\2\2\2 \u00d3\3\2\2\2\"\u00dd\3\2\2\2$\u00e3")
        buf.write("\3\2\2\2&\u00e5\3\2\2\2(\u00ee\3\2\2\2*\u00f2\3\2\2\2")
        buf.write(",\u00fa\3\2\2\2.\u00fc\3\2\2\2\60\u0107\3\2\2\2\62\u010d")
        buf.write("\3\2\2\2\64\u0114\3\2\2\2\66\u0116\3\2\2\28\u011d\3\2")
        buf.write("\2\2:\u011f\3\2\2\2<\u0129\3\2\2\2>\u012b\3\2\2\2@\u012e")
        buf.write("\3\2\2\2B\u0134\3\2\2\2D\u0136\3\2\2\2F\u0142\3\2\2\2")
        buf.write("H\u0144\3\2\2\2J\u014f\3\2\2\2L\u0156\3\2\2\2N\u015b\3")
        buf.write("\2\2\2P\u015d\3\2\2\2R\u0169\3\2\2\2T\u0173\3\2\2\2V\u0175")
        buf.write("\3\2\2\2X\u0177\3\2\2\2Z\u017e\3\2\2\2\\\u0180\3\2\2\2")
        buf.write("^\u0187\3\2\2\2`\u0189\3\2\2\2b\u0193\3\2\2\2d\u0195\3")
        buf.write("\2\2\2f\u019e\3\2\2\2h\u01a0\3\2\2\2j\u01a6\3\2\2\2l\u01b2")
        buf.write("\3\2\2\2n\u01b4\3\2\2\2p\u01ba\3\2\2\2r\u01c6\3\2\2\2")
        buf.write("t\u01ca\3\2\2\2v\u01ce\3\2\2\2x\u01d0\3\2\2\2z\u01d4\3")
        buf.write("\2\2\2|\u01d8\3\2\2\2~\u01dc\3\2\2\2\u0080\u01de\3\2\2")
        buf.write("\2\u0082\u01e2\3\2\2\2\u0084\u01ea\3\2\2\2\u0086\u01ee")
        buf.write("\3\2\2\2\u0088\u0089\5\4\3\2\u0089\u008a\5\6\4\2\u008a")
        buf.write("\u008b\7\t\2\2\u008b\u008c\7\n\2\2\u008c\u008d\7\3\2\2")
        buf.write("\u008d\u008e\5.\30\2\u008e\u008f\7\2\2\3\u008f\3\3\2\2")
        buf.write("\2\u0090\u0091\5\n\6\2\u0091\u0092\5\4\3\2\u0092\u0098")
        buf.write("\3\2\2\2\u0093\u0094\5p9\2\u0094\u0095\5\4\3\2\u0095\u0098")
        buf.write("\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0090\3\2\2\2\u0097")
        buf.write("\u0093\3\2\2\2\u0097\u0096\3\2\2\2\u0098\5\3\2\2\2\u0099")
        buf.write("\u009a\7\t\2\2\u009a\u009b\5\b\5\2\u009b\u009c\7.\2\2")
        buf.write("\u009c\u009d\5.\30\2\u009d\u009e\5\6\4\2\u009e\u00a1\3")
        buf.write("\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u0099\3\2\2\2\u00a0\u009f")
        buf.write("\3\2\2\2\u00a1\7\3\2\2\2\u00a2\u00a5\5\34\17\2\u00a3\u00a5")
        buf.write("\7\23\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5")
        buf.write("\t\3\2\2\2\u00a6\u00a7\5\f\7\2\u00a7\u00a8\5\16\b\2\u00a8")
        buf.write("\13\3\2\2\2\u00a9\u00ad\7.\2\2\u00aa\u00ad\5\34\17\2\u00ab")
        buf.write("\u00ad\5\36\20\2\u00ac\u00a9\3\2\2\2\u00ac\u00aa\3\2\2")
        buf.write("\2\u00ac\u00ab\3\2\2\2\u00ad\r\3\2\2\2\u00ae\u00af\5\24")
        buf.write("\13\2\u00af\u00b0\7+\2\2\u00b0\17\3\2\2\2\u00b1\u00b2")
        buf.write("\7\32\2\2\u00b2\u00b5\5\22\n\2\u00b3\u00b5\3\2\2\2\u00b4")
        buf.write("\u00b1\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\21\3\2\2\2\u00b6")
        buf.write("\u00b9\5\66\34\2\u00b7\u00b9\5 \21\2\u00b8\u00b6\3\2\2")
        buf.write("\2\u00b8\u00b7\3\2\2\2\u00b9\23\3\2\2\2\u00ba\u00bb\7")
        buf.write(".\2\2\u00bb\u00bc\5\20\t\2\u00bc\u00bd\5\26\f\2\u00bd")
        buf.write("\25\3\2\2\2\u00be\u00bf\7\33\2\2\u00bf\u00c0\7.\2\2\u00c0")
        buf.write("\u00c1\5\20\t\2\u00c1\u00c2\5\26\f\2\u00c2\u00c5\3\2\2")
        buf.write("\2\u00c3\u00c5\3\2\2\2\u00c4\u00be\3\2\2\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c5\27\3\2\2\2\u00c6\u00c7\5\32\16\2\u00c7")
        buf.write("\u00c8\5\16\b\2\u00c8\31\3\2\2\2\u00c9\u00cc\5\34\17\2")
        buf.write("\u00ca\u00cc\5\36\20\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca")
        buf.write("\3\2\2\2\u00cc\33\3\2\2\2\u00cd\u00ce\t\2\2\2\u00ce\35")
        buf.write("\3\2\2\2\u00cf\u00d0\7\16\2\2\u00d0\u00d1\5\34\17\2\u00d1")
        buf.write("\u00d2\7/\2\2\u00d2\37\3\2\2\2\u00d3\u00d4\7)\2\2\u00d4")
        buf.write("\u00d5\5$\23\2\u00d5\u00d6\5\"\22\2\u00d6\u00d7\7*\2\2")
        buf.write("\u00d7!\3\2\2\2\u00d8\u00d9\7\33\2\2\u00d9\u00da\5$\23")
        buf.write("\2\u00da\u00db\5\"\22\2\u00db\u00de\3\2\2\2\u00dc\u00de")
        buf.write("\3\2\2\2\u00dd\u00d8\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de")
        buf.write("#\3\2\2\2\u00df\u00e4\7/\2\2\u00e0\u00e4\7\60\2\2\u00e1")
        buf.write("\u00e4\5X-\2\u00e2\u00e4\7\61\2\2\u00e3\u00df\3\2\2\2")
        buf.write("\u00e3\u00e0\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2\3")
        buf.write("\2\2\2\u00e4%\3\2\2\2\u00e5\u00e6\7%\2\2\u00e6\u00e7\5")
        buf.write("(\25\2\u00e7\u00e8\7&\2\2\u00e8\'\3\2\2\2\u00e9\u00ea")
        buf.write("\5*\26\2\u00ea\u00eb\7.\2\2\u00eb\u00ec\5,\27\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00e9\3\2\2\2")
        buf.write("\u00ee\u00ed\3\2\2\2\u00ef)\3\2\2\2\u00f0\u00f3\5\34\17")
        buf.write("\2\u00f1\u00f3\5\36\20\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1")
        buf.write("\3\2\2\2\u00f3+\3\2\2\2\u00f4\u00f5\7\33\2\2\u00f5\u00f6")
        buf.write("\5*\26\2\u00f6\u00f7\7.\2\2\u00f7\u00f8\5,\27\2\u00f8")
        buf.write("\u00fb\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00f4\3\2\2\2")
        buf.write("\u00fa\u00f9\3\2\2\2\u00fb-\3\2\2\2\u00fc\u00fd\5&\24")
        buf.write("\2\u00fd\u00fe\7\'\2\2\u00fe\u00ff\5\60\31\2\u00ff\u0100")
        buf.write("\5\62\32\2\u0100\u0101\5\64\33\2\u0101\u0102\7(\2\2\u0102")
        buf.write("/\3\2\2\2\u0103\u0104\5\n\6\2\u0104\u0105\5\60\31\2\u0105")
        buf.write("\u0108\3\2\2\2\u0106\u0108\3\2\2\2\u0107\u0103\3\2\2\2")
        buf.write("\u0107\u0106\3\2\2\2\u0108\61\3\2\2\2\u0109\u010a\5<\37")
        buf.write("\2\u010a\u010b\5\62\32\2\u010b\u010e\3\2\2\2\u010c\u010e")
        buf.write("\3\2\2\2\u010d\u0109\3\2\2\2\u010d\u010c\3\2\2\2\u010e")
        buf.write("\63\3\2\2\2\u010f\u0110\7\r\2\2\u0110\u0111\5\66\34\2")
        buf.write("\u0111\u0112\7+\2\2\u0112\u0115\3\2\2\2\u0113\u0115\3")
        buf.write("\2\2\2\u0114\u010f\3\2\2\2\u0114\u0113\3\2\2\2\u0115\65")
        buf.write("\3\2\2\2\u0116\u0117\5> \2\u0117\u0118\58\35\2\u0118\67")
        buf.write("\3\2\2\2\u0119\u011a\5:\36\2\u011a\u011b\5\66\34\2\u011b")
        buf.write("\u011e\3\2\2\2\u011c\u011e\3\2\2\2\u011d\u0119\3\2\2\2")
        buf.write("\u011d\u011c\3\2\2\2\u011e9\3\2\2\2\u011f\u0120\t\3\2")
        buf.write("\2\u0120;\3\2\2\2\u0121\u012a\5\\/\2\u0122\u012a\5`\61")
        buf.write("\2\u0123\u0124\5\66\34\2\u0124\u0125\7+\2\2\u0125\u012a")
        buf.write("\3\2\2\2\u0126\u012a\5j\66\2\u0127\u012a\5h\65\2\u0128")
        buf.write("\u012a\5n8\2\u0129\u0121\3\2\2\2\u0129\u0122\3\2\2\2\u0129")
        buf.write("\u0123\3\2\2\2\u0129\u0126\3\2\2\2\u0129\u0127\3\2\2\2")
        buf.write("\u0129\u0128\3\2\2\2\u012a=\3\2\2\2\u012b\u012c\5D#\2")
        buf.write("\u012c\u012d\5B\"\2\u012d?\3\2\2\2\u012e\u012f\t\4\2\2")
        buf.write("\u012fA\3\2\2\2\u0130\u0131\5@!\2\u0131\u0132\5D#\2\u0132")
        buf.write("\u0135\3\2\2\2\u0133\u0135\3\2\2\2\u0134\u0130\3\2\2\2")
        buf.write("\u0134\u0133\3\2\2\2\u0135C\3\2\2\2\u0136\u0137\5P)\2")
        buf.write("\u0137\u0138\5F$\2\u0138E\3\2\2\2\u0139\u013a\7\34\2\2")
        buf.write("\u013a\u013b\5P)\2\u013b\u013c\5F$\2\u013c\u0143\3\2\2")
        buf.write("\2\u013d\u013e\7\35\2\2\u013e\u013f\5P)\2\u013f\u0140")
        buf.write("\5F$\2\u0140\u0143\3\2\2\2\u0141\u0143\3\2\2\2\u0142\u0139")
        buf.write("\3\2\2\2\u0142\u013d\3\2\2\2\u0142\u0141\3\2\2\2\u0143")
        buf.write("G\3\2\2\2\u0144\u0145\7%\2\2\u0145\u0146\5J&\2\u0146\u0147")
        buf.write("\7&\2\2\u0147I\3\2\2\2\u0148\u0149\5\66\34\2\u0149\u014a")
        buf.write("\5L\'\2\u014a\u0150\3\2\2\2\u014b\u014c\7\27\2\2\u014c")
        buf.write("\u014d\7.\2\2\u014d\u0150\5L\'\2\u014e\u0150\3\2\2\2\u014f")
        buf.write("\u0148\3\2\2\2\u014f\u014b\3\2\2\2\u014f\u014e\3\2\2\2")
        buf.write("\u0150K\3\2\2\2\u0151\u0152\7\33\2\2\u0152\u0153\5N(\2")
        buf.write("\u0153\u0154\5L\'\2\u0154\u0157\3\2\2\2\u0155\u0157\3")
        buf.write("\2\2\2\u0156\u0151\3\2\2\2\u0156\u0155\3\2\2\2\u0157M")
        buf.write("\3\2\2\2\u0158\u015c\5\66\34\2\u0159\u015a\7\27\2\2\u015a")
        buf.write("\u015c\7.\2\2\u015b\u0158\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015cO\3\2\2\2\u015d\u015e\5T+\2\u015e\u015f\5R*\2\u015f")
        buf.write("Q\3\2\2\2\u0160\u0161\7\37\2\2\u0161\u0162\5T+\2\u0162")
        buf.write("\u0163\5R*\2\u0163\u016a\3\2\2\2\u0164\u0165\7\36\2\2")
        buf.write("\u0165\u0166\5T+\2\u0166\u0167\5R*\2\u0167\u016a\3\2\2")
        buf.write("\2\u0168\u016a\3\2\2\2\u0169\u0160\3\2\2\2\u0169\u0164")
        buf.write("\3\2\2\2\u0169\u0168\3\2\2\2\u016aS\3\2\2\2\u016b\u016c")
        buf.write("\7%\2\2\u016c\u016d\5\66\34\2\u016d\u016e\7&\2\2\u016e")
        buf.write("\u0174\3\2\2\2\u016f\u0174\5$\23\2\u0170\u0171\5V,\2\u0171")
        buf.write("\u0172\5$\23\2\u0172\u0174\3\2\2\2\u0173\u016b\3\2\2\2")
        buf.write("\u0173\u016f\3\2\2\2\u0173\u0170\3\2\2\2\u0174U\3\2\2")
        buf.write("\2\u0175\u0176\t\5\2\2\u0176W\3\2\2\2\u0177\u0178\7.\2")
        buf.write("\2\u0178\u0179\5Z.\2\u0179Y\3\2\2\2\u017a\u017b\7-\2\2")
        buf.write("\u017b\u017c\7.\2\2\u017c\u017f\5H%\2\u017d\u017f\3\2")
        buf.write("\2\2\u017e\u017a\3\2\2\2\u017e\u017d\3\2\2\2\u017f[\3")
        buf.write("\2\2\2\u0180\u0181\7.\2\2\u0181\u0182\7\32\2\2\u0182\u0183")
        buf.write("\5^\60\2\u0183\u0184\7+\2\2\u0184]\3\2\2\2\u0185\u0188")
        buf.write("\5\66\34\2\u0186\u0188\5 \21\2\u0187\u0185\3\2\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188_\3\2\2\2\u0189\u018a\7\4\2\2\u018a")
        buf.write("\u018b\7%\2\2\u018b\u018c\5\66\34\2\u018c\u018d\7&\2\2")
        buf.write("\u018d\u018e\5d\63\2\u018e\u018f\5b\62\2\u018fa\3\2\2")
        buf.write("\2\u0190\u0191\7\5\2\2\u0191\u0194\5d\63\2\u0192\u0194")
        buf.write("\3\2\2\2\u0193\u0190\3\2\2\2\u0193\u0192\3\2\2\2\u0194")
        buf.write("c\3\2\2\2\u0195\u0196\7\'\2\2\u0196\u0197\5<\37\2\u0197")
        buf.write("\u0198\5f\64\2\u0198\u0199\7(\2\2\u0199e\3\2\2\2\u019a")
        buf.write("\u019b\5<\37\2\u019b\u019c\5f\64\2\u019c\u019f\3\2\2\2")
        buf.write("\u019d\u019f\3\2\2\2\u019e\u019a\3\2\2\2\u019e\u019d\3")
        buf.write("\2\2\2\u019fg\3\2\2\2\u01a0\u01a1\7\6\2\2\u01a1\u01a2")
        buf.write("\7%\2\2\u01a2\u01a3\5\66\34\2\u01a3\u01a4\7&\2\2\u01a4")
        buf.write("\u01a5\5d\63\2\u01a5i\3\2\2\2\u01a6\u01a7\7\b\2\2\u01a7")
        buf.write("\u01a8\7%\2\2\u01a8\u01a9\5\66\34\2\u01a9\u01aa\5l\67")
        buf.write("\2\u01aa\u01ab\7&\2\2\u01ab\u01ac\7+\2\2\u01ack\3\2\2")
        buf.write("\2\u01ad\u01ae\7\33\2\2\u01ae\u01af\5\66\34\2\u01af\u01b0")
        buf.write("\5l\67\2\u01b0\u01b3\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2")
        buf.write("\u01ad\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3m\3\2\2\2\u01b4")
        buf.write("\u01b5\7\7\2\2\u01b5\u01b6\7%\2\2\u01b6\u01b7\7.\2\2\u01b7")
        buf.write("\u01b8\7&\2\2\u01b8\u01b9\7+\2\2\u01b9o\3\2\2\2\u01ba")
        buf.write("\u01bb\7\17\2\2\u01bb\u01bc\7.\2\2\u01bc\u01bd\5r:\2\u01bd")
        buf.write("\u01be\7\'\2\2\u01be\u01bf\5t;\2\u01bf\u01c0\5v<\2\u01c0")
        buf.write("\u01c1\7(\2\2\u01c1\u01c2\7+\2\2\u01c2q\3\2\2\2\u01c3")
        buf.write("\u01c4\7\22\2\2\u01c4\u01c7\7.\2\2\u01c5\u01c7\3\2\2\2")
        buf.write("\u01c6\u01c3\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7s\3\2\2")
        buf.write("\2\u01c8\u01cb\5x=\2\u01c9\u01cb\3\2\2\2\u01ca\u01c8\3")
        buf.write("\2\2\2\u01ca\u01c9\3\2\2\2\u01cbu\3\2\2\2\u01cc\u01cf")
        buf.write("\5\u0080A\2\u01cd\u01cf\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce")
        buf.write("\u01cd\3\2\2\2\u01cfw\3\2\2\2\u01d0\u01d1\7\20\2\2\u01d1")
        buf.write("\u01d2\7,\2\2\u01d2\u01d3\5z>\2\u01d3y\3\2\2\2\u01d4\u01d5")
        buf.write("\5|?\2\u01d5\u01d6\5\30\r\2\u01d6\u01d7\5~@\2\u01d7{\3")
        buf.write("\2\2\2\u01d8\u01d9\t\6\2\2\u01d9}\3\2\2\2\u01da\u01dd")
        buf.write("\5z>\2\u01db\u01dd\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01db")
        buf.write("\3\2\2\2\u01dd\177\3\2\2\2\u01de\u01df\7\21\2\2\u01df")
        buf.write("\u01e0\7,\2\2\u01e0\u01e1\5\u0082B\2\u01e1\u0081\3\2\2")
        buf.write("\2\u01e2\u01e3\7\t\2\2\u01e3\u01e4\5\u0084C\2\u01e4\u01e5")
        buf.write("\7.\2\2\u01e5\u01e6\5.\30\2\u01e6\u01e7\5\u0086D\2\u01e7")
        buf.write("\u0083\3\2\2\2\u01e8\u01eb\5\34\17\2\u01e9\u01eb\7\23")
        buf.write("\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01e9\3\2\2\2\u01eb\u0085")
        buf.write("\3\2\2\2\u01ec\u01ef\5\u0082B\2\u01ed\u01ef\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ed\3\2\2\2\u01ef\u0087\3\2\2\2")
        buf.write("&\u0097\u00a0\u00a4\u00ac\u00b4\u00b8\u00c4\u00cb\u00dd")
        buf.write("\u00e3\u00ee\u00f2\u00fa\u0107\u010d\u0114\u011d\u0129")
        buf.write("\u0134\u0142\u014f\u0156\u015b\u0169\u0173\u017e\u0187")
        buf.write("\u0193\u019e\u01b2\u01c6\u01ca\u01ce\u01dc\u01ea\u01ee")
        return buf.getvalue()


class misterParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'INICIO'", u"'SI'", u"'SINO'", u"'MIENTRAS'", 
                     u"'LEER'", u"'IMPRIMIR'", u"'FUNCION'", u"'ENTERO'", 
                     u"'DECIMAL'", u"'TEXTO'", u"'RETORNAR'", u"'LISTA'", 
                     u"'CLASE'", u"'ATRIBUTOS'", u"'METODOS'", u"'HEREDA'", 
                     u"'NADA'", u"'PRIVADO'", u"'PUBLICO'", u"'&&'", u"'&'", 
                     u"'||'", u"'=='", u"'='", u"','", u"'+'", u"'-'", u"'/'", 
                     u"'*'", u"'!='", u"'>='", u"'<='", u"'<'", u"'>'", 
                     u"'('", u"')'", u"'{'", u"'}'", u"'['", u"']'", u"';'", 
                     u"':'", u"'.'" ]

    symbolicNames = [ u"<INVALID>", u"INICIO", u"SI", u"SINO", u"MIENTRAS", 
                      u"LEER", u"IMPRIMIR", u"FUNCION", u"ENTERO", u"DECIMAL", 
                      u"TEXTO", u"RETORNAR", u"LISTA", u"CLASE", u"ATRIBUTOS", 
                      u"METODOS", u"HEREDA", u"NADA", u"PRIVADO", u"PUBLICO", 
                      u"Y", u"REFERENCIA", u"O", u"IDENTICO", u"IGUAL", 
                      u"COMA", u"SUMA", u"RESTA", u"DIVISION", u"MULTIPLICACION", 
                      u"DIFERENTE", u"MAYORIGUAL", u"MENORIGUAL", u"MENOR", 
                      u"MAYOR", u"PARENTESIS1", u"PARENTESIS2", u"LLAVE1", 
                      u"LLAVE2", u"CORCHETE1", u"CORCHETE2", u"PUNTOYCOMA", 
                      u"DOSPUNTOS", u"PUNTO", u"ID", u"CTENTERO", u"CTEDECIMAL", 
                      u"CTETEXTO", u"WS" ]

    RULE_programa = 0
    RULE_programaAux1 = 1
    RULE_programaAux3 = 2
    RULE_programaAux4 = 3
    RULE_v_vars = 4
    RULE_varsAux1 = 5
    RULE_v_varsDefinicion = 6
    RULE_varsAux2 = 7
    RULE_varsAux3 = 8
    RULE_varsAux4 = 9
    RULE_varsAux5 = 10
    RULE_v_varsAtrib = 11
    RULE_varsAtribAux1 = 12
    RULE_tipo = 13
    RULE_l_list = 14
    RULE_cteL = 15
    RULE_cteLAux1 = 16
    RULE_valor = 17
    RULE_parametros = 18
    RULE_parametrosAux1 = 19
    RULE_parametrosAux2 = 20
    RULE_parametrosAux3 = 21
    RULE_func = 22
    RULE_funcAux1 = 23
    RULE_funcAux2 = 24
    RULE_funcAux3 = 25
    RULE_expresion = 26
    RULE_expresionAux1 = 27
    RULE_expresionAux2 = 28
    RULE_estatuto = 29
    RULE_declaracion = 30
    RULE_declaracionAux1 = 31
    RULE_declaracionAux2 = 32
    RULE_exp = 33
    RULE_expAux1 = 34
    RULE_llamarFunc = 35
    RULE_llamarFuncAux1 = 36
    RULE_llamarFuncAux2 = 37
    RULE_llamarFuncAux3 = 38
    RULE_termino = 39
    RULE_terminoAux1 = 40
    RULE_factor = 41
    RULE_factorAux1 = 42
    RULE_compuesto = 43
    RULE_compuestoAux1 = 44
    RULE_asignacion = 45
    RULE_asignacionAux1 = 46
    RULE_condicion = 47
    RULE_condicionAux1 = 48
    RULE_bloque = 49
    RULE_bloqueAux1 = 50
    RULE_ciclo = 51
    RULE_escritura = 52
    RULE_escrituraAux1 = 53
    RULE_lectura = 54
    RULE_c_class = 55
    RULE_classAux1 = 56
    RULE_classAux2 = 57
    RULE_classAux3 = 58
    RULE_atrib = 59
    RULE_atribAux1 = 60
    RULE_atribAux2 = 61
    RULE_atribAux3 = 62
    RULE_metod = 63
    RULE_metodAux1 = 64
    RULE_metodAux2 = 65
    RULE_metodAux3 = 66

    ruleNames =  [ "programa", "programaAux1", "programaAux3", "programaAux4", 
                   "v_vars", "varsAux1", "v_varsDefinicion", "varsAux2", 
                   "varsAux3", "varsAux4", "varsAux5", "v_varsAtrib", "varsAtribAux1", 
                   "tipo", "l_list", "cteL", "cteLAux1", "valor", "parametros", 
                   "parametrosAux1", "parametrosAux2", "parametrosAux3", 
                   "func", "funcAux1", "funcAux2", "funcAux3", "expresion", 
                   "expresionAux1", "expresionAux2", "estatuto", "declaracion", 
                   "declaracionAux1", "declaracionAux2", "exp", "expAux1", 
                   "llamarFunc", "llamarFuncAux1", "llamarFuncAux2", "llamarFuncAux3", 
                   "termino", "terminoAux1", "factor", "factorAux1", "compuesto", 
                   "compuestoAux1", "asignacion", "asignacionAux1", "condicion", 
                   "condicionAux1", "bloque", "bloqueAux1", "ciclo", "escritura", 
                   "escrituraAux1", "lectura", "c_class", "classAux1", "classAux2", 
                   "classAux3", "atrib", "atribAux1", "atribAux2", "atribAux3", 
                   "metod", "metodAux1", "metodAux2", "metodAux3" ]

    EOF = Token.EOF
    INICIO=1
    SI=2
    SINO=3
    MIENTRAS=4
    LEER=5
    IMPRIMIR=6
    FUNCION=7
    ENTERO=8
    DECIMAL=9
    TEXTO=10
    RETORNAR=11
    LISTA=12
    CLASE=13
    ATRIBUTOS=14
    METODOS=15
    HEREDA=16
    NADA=17
    PRIVADO=18
    PUBLICO=19
    Y=20
    REFERENCIA=21
    O=22
    IDENTICO=23
    IGUAL=24
    COMA=25
    SUMA=26
    RESTA=27
    DIVISION=28
    MULTIPLICACION=29
    DIFERENTE=30
    MAYORIGUAL=31
    MENORIGUAL=32
    MENOR=33
    MAYOR=34
    PARENTESIS1=35
    PARENTESIS2=36
    LLAVE1=37
    LLAVE2=38
    CORCHETE1=39
    CORCHETE2=40
    PUNTOYCOMA=41
    DOSPUNTOS=42
    PUNTO=43
    ID=44
    CTENTERO=45
    CTEDECIMAL=46
    CTETEXTO=47
    WS=48

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def programaAux1(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux1Context,0)


        def programaAux3(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux3Context,0)


        def FUNCION(self):
            return self.getToken(misterParser.FUNCION, 0)

        def ENTERO(self):
            return self.getToken(misterParser.ENTERO, 0)

        def INICIO(self):
            return self.getToken(misterParser.INICIO, 0)

        def func(self):
            return self.getTypedRuleContext(misterParser.FuncContext,0)


        def EOF(self):
            return self.getToken(misterParser.EOF, 0)

        def getRuleIndex(self):
            return misterParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = misterParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.programaAux1()
            self.state = 135
            self.programaAux3()
            self.state = 136
            self.match(misterParser.FUNCION)
            self.state = 137
            self.match(misterParser.ENTERO)
            self.state = 138
            self.match(misterParser.INICIO)
            self.state = 139
            self.func()
            self.state = 140
            self.match(misterParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramaAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def v_vars(self):
            return self.getTypedRuleContext(misterParser.V_varsContext,0)


        def programaAux1(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux1Context,0)


        def c_class(self):
            return self.getTypedRuleContext(misterParser.C_classContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_programaAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterProgramaAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitProgramaAux1(self)




    def programaAux1(self):

        localctx = misterParser.ProgramaAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programaAux1)
        try:
            self.state = 149
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO, misterParser.LISTA, misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.v_vars()
                self.state = 143
                self.programaAux1()

            elif token in [misterParser.CLASE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.c_class()
                self.state = 146
                self.programaAux1()

            elif token in [misterParser.FUNCION]:
                self.enterOuterAlt(localctx, 3)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramaAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(misterParser.FUNCION, 0)

        def programaAux4(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux4Context,0)


        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def func(self):
            return self.getTypedRuleContext(misterParser.FuncContext,0)


        def programaAux3(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_programaAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterProgramaAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitProgramaAux3(self)




    def programaAux3(self):

        localctx = misterParser.ProgramaAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_programaAux3)
        try:
            self.state = 158
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(misterParser.FUNCION)
                self.state = 152
                self.programaAux4()
                self.state = 153
                self.match(misterParser.ID)
                self.state = 154
                self.func()
                self.state = 155
                self.programaAux3()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramaAux4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(misterParser.TipoContext,0)


        def NADA(self):
            return self.getToken(misterParser.NADA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_programaAux4

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterProgramaAux4(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitProgramaAux4(self)




    def programaAux4(self):

        localctx = misterParser.ProgramaAux4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_programaAux4)
        try:
            self.state = 162
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.tipo()

            elif token in [misterParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(misterParser.NADA)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V_varsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsAux1(self):
            return self.getTypedRuleContext(misterParser.VarsAux1Context,0)


        def v_varsDefinicion(self):
            return self.getTypedRuleContext(misterParser.V_varsDefinicionContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_v_vars

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterV_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitV_vars(self)




    def v_vars(self):

        localctx = misterParser.V_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_v_vars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.varsAux1()
            self.state = 165
            self.v_varsDefinicion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarsAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def tipo(self):
            return self.getTypedRuleContext(misterParser.TipoContext,0)


        def l_list(self):
            return self.getTypedRuleContext(misterParser.L_listContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_varsAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterVarsAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitVarsAux1(self)




    def varsAux1(self):

        localctx = misterParser.VarsAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varsAux1)
        try:
            self.state = 170
            token = self._input.LA(1)
            if token in [misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(misterParser.ID)

            elif token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.tipo()

            elif token in [misterParser.LISTA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.l_list()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V_varsDefinicionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsAux4(self):
            return self.getTypedRuleContext(misterParser.VarsAux4Context,0)


        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_v_varsDefinicion

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterV_varsDefinicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitV_varsDefinicion(self)




    def v_varsDefinicion(self):

        localctx = misterParser.V_varsDefinicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_v_varsDefinicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.varsAux4()
            self.state = 173
            self.match(misterParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarsAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IGUAL(self):
            return self.getToken(misterParser.IGUAL, 0)

        def varsAux3(self):
            return self.getTypedRuleContext(misterParser.VarsAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_varsAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterVarsAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitVarsAux2(self)




    def varsAux2(self):

        localctx = misterParser.VarsAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varsAux2)
        try:
            self.state = 178
            token = self._input.LA(1)
            if token in [misterParser.IGUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(misterParser.IGUAL)
                self.state = 176
                self.varsAux3()

            elif token in [misterParser.COMA, misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarsAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def cteL(self):
            return self.getTypedRuleContext(misterParser.CteLContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_varsAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterVarsAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitVarsAux3(self)




    def varsAux3(self):

        localctx = misterParser.VarsAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_varsAux3)
        try:
            self.state = 182
            token = self._input.LA(1)
            if token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.expresion()

            elif token in [misterParser.CORCHETE1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.cteL()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarsAux4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def varsAux2(self):
            return self.getTypedRuleContext(misterParser.VarsAux2Context,0)


        def varsAux5(self):
            return self.getTypedRuleContext(misterParser.VarsAux5Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_varsAux4

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterVarsAux4(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitVarsAux4(self)




    def varsAux4(self):

        localctx = misterParser.VarsAux4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_varsAux4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(misterParser.ID)
            self.state = 185
            self.varsAux2()
            self.state = 186
            self.varsAux5()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarsAux5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(misterParser.COMA, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def varsAux2(self):
            return self.getTypedRuleContext(misterParser.VarsAux2Context,0)


        def varsAux5(self):
            return self.getTypedRuleContext(misterParser.VarsAux5Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_varsAux5

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterVarsAux5(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitVarsAux5(self)




    def varsAux5(self):

        localctx = misterParser.VarsAux5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varsAux5)
        try:
            self.state = 194
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(misterParser.COMA)
                self.state = 189
                self.match(misterParser.ID)
                self.state = 190
                self.varsAux2()
                self.state = 191
                self.varsAux5()

            elif token in [misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V_varsAtribContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsAtribAux1(self):
            return self.getTypedRuleContext(misterParser.VarsAtribAux1Context,0)


        def v_varsDefinicion(self):
            return self.getTypedRuleContext(misterParser.V_varsDefinicionContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_v_varsAtrib

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterV_varsAtrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitV_varsAtrib(self)




    def v_varsAtrib(self):

        localctx = misterParser.V_varsAtribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_v_varsAtrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.varsAtribAux1()
            self.state = 197
            self.v_varsDefinicion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarsAtribAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(misterParser.TipoContext,0)


        def l_list(self):
            return self.getTypedRuleContext(misterParser.L_listContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_varsAtribAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterVarsAtribAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitVarsAtribAux1(self)




    def varsAtribAux1(self):

        localctx = misterParser.VarsAtribAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_varsAtribAux1)
        try:
            self.state = 201
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.tipo()

            elif token in [misterParser.LISTA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.l_list()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TipoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(misterParser.ENTERO, 0)

        def DECIMAL(self):
            return self.getToken(misterParser.DECIMAL, 0)

        def TEXTO(self):
            return self.getToken(misterParser.TEXTO, 0)

        def getRuleIndex(self):
            return misterParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = misterParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << misterParser.ENTERO) | (1 << misterParser.DECIMAL) | (1 << misterParser.TEXTO))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class L_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LISTA(self):
            return self.getToken(misterParser.LISTA, 0)

        def tipo(self):
            return self.getTypedRuleContext(misterParser.TipoContext,0)


        def CTENTERO(self):
            return self.getToken(misterParser.CTENTERO, 0)

        def getRuleIndex(self):
            return misterParser.RULE_l_list

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterL_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitL_list(self)




    def l_list(self):

        localctx = misterParser.L_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_l_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(misterParser.LISTA)
            self.state = 206
            self.tipo()
            self.state = 207
            self.match(misterParser.CTENTERO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CteLContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORCHETE1(self):
            return self.getToken(misterParser.CORCHETE1, 0)

        def valor(self):
            return self.getTypedRuleContext(misterParser.ValorContext,0)


        def cteLAux1(self):
            return self.getTypedRuleContext(misterParser.CteLAux1Context,0)


        def CORCHETE2(self):
            return self.getToken(misterParser.CORCHETE2, 0)

        def getRuleIndex(self):
            return misterParser.RULE_cteL

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCteL(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCteL(self)




    def cteL(self):

        localctx = misterParser.CteLContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_cteL)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(misterParser.CORCHETE1)
            self.state = 210
            self.valor()
            self.state = 211
            self.cteLAux1()
            self.state = 212
            self.match(misterParser.CORCHETE2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CteLAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(misterParser.COMA, 0)

        def valor(self):
            return self.getTypedRuleContext(misterParser.ValorContext,0)


        def cteLAux1(self):
            return self.getTypedRuleContext(misterParser.CteLAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_cteLAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCteLAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCteLAux1(self)




    def cteLAux1(self):

        localctx = misterParser.CteLAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cteLAux1)
        try:
            self.state = 219
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(misterParser.COMA)
                self.state = 215
                self.valor()
                self.state = 216
                self.cteLAux1()

            elif token in [misterParser.CORCHETE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CTENTERO(self):
            return self.getToken(misterParser.CTENTERO, 0)

        def CTEDECIMAL(self):
            return self.getToken(misterParser.CTEDECIMAL, 0)

        def compuesto(self):
            return self.getTypedRuleContext(misterParser.CompuestoContext,0)


        def CTETEXTO(self):
            return self.getToken(misterParser.CTETEXTO, 0)

        def getRuleIndex(self):
            return misterParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitValor(self)




    def valor(self):

        localctx = misterParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_valor)
        try:
            self.state = 225
            token = self._input.LA(1)
            if token in [misterParser.CTENTERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(misterParser.CTENTERO)

            elif token in [misterParser.CTEDECIMAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(misterParser.CTEDECIMAL)

            elif token in [misterParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.compuesto()

            elif token in [misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                self.match(misterParser.CTETEXTO)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametrosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def parametrosAux1(self):
            return self.getTypedRuleContext(misterParser.ParametrosAux1Context,0)


        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def getRuleIndex(self):
            return misterParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = misterParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parametros)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(misterParser.PARENTESIS1)
            self.state = 228
            self.parametrosAux1()
            self.state = 229
            self.match(misterParser.PARENTESIS2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametrosAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametrosAux2(self):
            return self.getTypedRuleContext(misterParser.ParametrosAux2Context,0)


        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def parametrosAux3(self):
            return self.getTypedRuleContext(misterParser.ParametrosAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_parametrosAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterParametrosAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitParametrosAux1(self)




    def parametrosAux1(self):

        localctx = misterParser.ParametrosAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parametrosAux1)
        try:
            self.state = 236
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO, misterParser.LISTA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.parametrosAux2()
                self.state = 232
                self.match(misterParser.ID)
                self.state = 233
                self.parametrosAux3()

            elif token in [misterParser.PARENTESIS2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametrosAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(misterParser.TipoContext,0)


        def l_list(self):
            return self.getTypedRuleContext(misterParser.L_listContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_parametrosAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterParametrosAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitParametrosAux2(self)




    def parametrosAux2(self):

        localctx = misterParser.ParametrosAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parametrosAux2)
        try:
            self.state = 240
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.tipo()

            elif token in [misterParser.LISTA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.l_list()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametrosAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(misterParser.COMA, 0)

        def parametrosAux2(self):
            return self.getTypedRuleContext(misterParser.ParametrosAux2Context,0)


        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def parametrosAux3(self):
            return self.getTypedRuleContext(misterParser.ParametrosAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_parametrosAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterParametrosAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitParametrosAux3(self)




    def parametrosAux3(self):

        localctx = misterParser.ParametrosAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parametrosAux3)
        try:
            self.state = 248
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(misterParser.COMA)
                self.state = 243
                self.parametrosAux2()
                self.state = 244
                self.match(misterParser.ID)
                self.state = 245
                self.parametrosAux3()

            elif token in [misterParser.PARENTESIS2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametros(self):
            return self.getTypedRuleContext(misterParser.ParametrosContext,0)


        def LLAVE1(self):
            return self.getToken(misterParser.LLAVE1, 0)

        def funcAux1(self):
            return self.getTypedRuleContext(misterParser.FuncAux1Context,0)


        def funcAux2(self):
            return self.getTypedRuleContext(misterParser.FuncAux2Context,0)


        def funcAux3(self):
            return self.getTypedRuleContext(misterParser.FuncAux3Context,0)


        def LLAVE2(self):
            return self.getToken(misterParser.LLAVE2, 0)

        def getRuleIndex(self):
            return misterParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitFunc(self)




    def func(self):

        localctx = misterParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.parametros()
            self.state = 251
            self.match(misterParser.LLAVE1)
            self.state = 252
            self.funcAux1()
            self.state = 253
            self.funcAux2()
            self.state = 254
            self.funcAux3()
            self.state = 255
            self.match(misterParser.LLAVE2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def v_vars(self):
            return self.getTypedRuleContext(misterParser.V_varsContext,0)


        def funcAux1(self):
            return self.getTypedRuleContext(misterParser.FuncAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_funcAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterFuncAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitFuncAux1(self)




    def funcAux1(self):

        localctx = misterParser.FuncAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_funcAux1)
        try:
            self.state = 261
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.v_vars()
                self.state = 258
                self.funcAux1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def estatuto(self):
            return self.getTypedRuleContext(misterParser.EstatutoContext,0)


        def funcAux2(self):
            return self.getTypedRuleContext(misterParser.FuncAux2Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_funcAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterFuncAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitFuncAux2(self)




    def funcAux2(self):

        localctx = misterParser.FuncAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_funcAux2)
        try:
            self.state = 267
            token = self._input.LA(1)
            if token in [misterParser.SI, misterParser.MIENTRAS, misterParser.LEER, misterParser.IMPRIMIR, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.estatuto()
                self.state = 264
                self.funcAux2()

            elif token in [misterParser.RETORNAR, misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNAR(self):
            return self.getToken(misterParser.RETORNAR, 0)

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_funcAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterFuncAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitFuncAux3(self)




    def funcAux3(self):

        localctx = misterParser.FuncAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_funcAux3)
        try:
            self.state = 274
            token = self._input.LA(1)
            if token in [misterParser.RETORNAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(misterParser.RETORNAR)
                self.state = 270
                self.expresion()
                self.state = 271
                self.match(misterParser.PUNTOYCOMA)

            elif token in [misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(misterParser.DeclaracionContext,0)


        def expresionAux1(self):
            return self.getTypedRuleContext(misterParser.ExpresionAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = misterParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.declaracion()
            self.state = 277
            self.expresionAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpresionAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionAux2(self):
            return self.getTypedRuleContext(misterParser.ExpresionAux2Context,0)


        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_expresionAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterExpresionAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitExpresionAux1(self)




    def expresionAux1(self):

        localctx = misterParser.ExpresionAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expresionAux1)
        try:
            self.state = 283
            token = self._input.LA(1)
            if token in [misterParser.Y, misterParser.O]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.expresionAux2()
                self.state = 280
                self.expresion()

            elif token in [misterParser.COMA, misterParser.PARENTESIS2, misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpresionAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Y(self):
            return self.getToken(misterParser.Y, 0)

        def O(self):
            return self.getToken(misterParser.O, 0)

        def getRuleIndex(self):
            return misterParser.RULE_expresionAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterExpresionAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitExpresionAux2(self)




    def expresionAux2(self):

        localctx = misterParser.ExpresionAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expresionAux2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            _la = self._input.LA(1)
            if not(_la==misterParser.Y or _la==misterParser.O):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EstatutoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(misterParser.AsignacionContext,0)


        def condicion(self):
            return self.getTypedRuleContext(misterParser.CondicionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def escritura(self):
            return self.getTypedRuleContext(misterParser.EscrituraContext,0)


        def ciclo(self):
            return self.getTypedRuleContext(misterParser.CicloContext,0)


        def lectura(self):
            return self.getTypedRuleContext(misterParser.LecturaContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_estatuto

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterEstatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitEstatuto(self)




    def estatuto(self):

        localctx = misterParser.EstatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_estatuto)
        try:
            self.state = 295
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.condicion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 289
                self.expresion()
                self.state = 290
                self.match(misterParser.PUNTOYCOMA)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 292
                self.escritura()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 293
                self.ciclo()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 294
                self.lectura()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaracionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(misterParser.ExpContext,0)


        def declaracionAux2(self):
            return self.getTypedRuleContext(misterParser.DeclaracionAux2Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitDeclaracion(self)




    def declaracion(self):

        localctx = misterParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.exp()
            self.state = 298
            self.declaracionAux2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaracionAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAYOR(self):
            return self.getToken(misterParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(misterParser.MENOR, 0)

        def DIFERENTE(self):
            return self.getToken(misterParser.DIFERENTE, 0)

        def MAYORIGUAL(self):
            return self.getToken(misterParser.MAYORIGUAL, 0)

        def MENORIGUAL(self):
            return self.getToken(misterParser.MENORIGUAL, 0)

        def IDENTICO(self):
            return self.getToken(misterParser.IDENTICO, 0)

        def getRuleIndex(self):
            return misterParser.RULE_declaracionAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterDeclaracionAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitDeclaracionAux1(self)




    def declaracionAux1(self):

        localctx = misterParser.DeclaracionAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_declaracionAux1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << misterParser.IDENTICO) | (1 << misterParser.DIFERENTE) | (1 << misterParser.MAYORIGUAL) | (1 << misterParser.MENORIGUAL) | (1 << misterParser.MENOR) | (1 << misterParser.MAYOR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaracionAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionAux1(self):
            return self.getTypedRuleContext(misterParser.DeclaracionAux1Context,0)


        def exp(self):
            return self.getTypedRuleContext(misterParser.ExpContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_declaracionAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterDeclaracionAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitDeclaracionAux2(self)




    def declaracionAux2(self):

        localctx = misterParser.DeclaracionAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_declaracionAux2)
        try:
            self.state = 306
            token = self._input.LA(1)
            if token in [misterParser.IDENTICO, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.declaracionAux1()
                self.state = 303
                self.exp()

            elif token in [misterParser.Y, misterParser.O, misterParser.COMA, misterParser.PARENTESIS2, misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(misterParser.TerminoContext,0)


        def expAux1(self):
            return self.getTypedRuleContext(misterParser.ExpAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitExp(self)




    def exp(self):

        localctx = misterParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.termino()
            self.state = 309
            self.expAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(misterParser.SUMA, 0)

        def termino(self):
            return self.getTypedRuleContext(misterParser.TerminoContext,0)


        def expAux1(self):
            return self.getTypedRuleContext(misterParser.ExpAux1Context,0)


        def RESTA(self):
            return self.getToken(misterParser.RESTA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_expAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterExpAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitExpAux1(self)




    def expAux1(self):

        localctx = misterParser.ExpAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expAux1)
        try:
            self.state = 320
            token = self._input.LA(1)
            if token in [misterParser.SUMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(misterParser.SUMA)
                self.state = 312
                self.termino()
                self.state = 313
                self.expAux1()

            elif token in [misterParser.RESTA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.match(misterParser.RESTA)
                self.state = 316
                self.termino()
                self.state = 317
                self.expAux1()

            elif token in [misterParser.Y, misterParser.O, misterParser.IDENTICO, misterParser.COMA, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR, misterParser.PARENTESIS2, misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 3)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LlamarFuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def llamarFuncAux1(self):
            return self.getTypedRuleContext(misterParser.LlamarFuncAux1Context,0)


        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def getRuleIndex(self):
            return misterParser.RULE_llamarFunc

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterLlamarFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitLlamarFunc(self)




    def llamarFunc(self):

        localctx = misterParser.LlamarFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_llamarFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(misterParser.PARENTESIS1)
            self.state = 323
            self.llamarFuncAux1()
            self.state = 324
            self.match(misterParser.PARENTESIS2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LlamarFuncAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def llamarFuncAux2(self):
            return self.getTypedRuleContext(misterParser.LlamarFuncAux2Context,0)


        def REFERENCIA(self):
            return self.getToken(misterParser.REFERENCIA, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def getRuleIndex(self):
            return misterParser.RULE_llamarFuncAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterLlamarFuncAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitLlamarFuncAux1(self)




    def llamarFuncAux1(self):

        localctx = misterParser.LlamarFuncAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_llamarFuncAux1)
        try:
            self.state = 333
            token = self._input.LA(1)
            if token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.expresion()
                self.state = 327
                self.llamarFuncAux2()

            elif token in [misterParser.REFERENCIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.match(misterParser.REFERENCIA)
                self.state = 330
                self.match(misterParser.ID)
                self.state = 331
                self.llamarFuncAux2()

            elif token in [misterParser.PARENTESIS2]:
                self.enterOuterAlt(localctx, 3)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LlamarFuncAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(misterParser.COMA, 0)

        def llamarFuncAux3(self):
            return self.getTypedRuleContext(misterParser.LlamarFuncAux3Context,0)


        def llamarFuncAux2(self):
            return self.getTypedRuleContext(misterParser.LlamarFuncAux2Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_llamarFuncAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterLlamarFuncAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitLlamarFuncAux2(self)




    def llamarFuncAux2(self):

        localctx = misterParser.LlamarFuncAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_llamarFuncAux2)
        try:
            self.state = 340
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.match(misterParser.COMA)
                self.state = 336
                self.llamarFuncAux3()
                self.state = 337
                self.llamarFuncAux2()

            elif token in [misterParser.PARENTESIS2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LlamarFuncAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def REFERENCIA(self):
            return self.getToken(misterParser.REFERENCIA, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def getRuleIndex(self):
            return misterParser.RULE_llamarFuncAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterLlamarFuncAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitLlamarFuncAux3(self)




    def llamarFuncAux3(self):

        localctx = misterParser.LlamarFuncAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_llamarFuncAux3)
        try:
            self.state = 345
            token = self._input.LA(1)
            if token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.expresion()

            elif token in [misterParser.REFERENCIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.match(misterParser.REFERENCIA)
                self.state = 344
                self.match(misterParser.ID)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TerminoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(misterParser.FactorContext,0)


        def terminoAux1(self):
            return self.getTypedRuleContext(misterParser.TerminoAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitTermino(self)




    def termino(self):

        localctx = misterParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.factor()
            self.state = 348
            self.terminoAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TerminoAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLICACION(self):
            return self.getToken(misterParser.MULTIPLICACION, 0)

        def factor(self):
            return self.getTypedRuleContext(misterParser.FactorContext,0)


        def terminoAux1(self):
            return self.getTypedRuleContext(misterParser.TerminoAux1Context,0)


        def DIVISION(self):
            return self.getToken(misterParser.DIVISION, 0)

        def getRuleIndex(self):
            return misterParser.RULE_terminoAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterTerminoAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitTerminoAux1(self)




    def terminoAux1(self):

        localctx = misterParser.TerminoAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_terminoAux1)
        try:
            self.state = 359
            token = self._input.LA(1)
            if token in [misterParser.MULTIPLICACION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(misterParser.MULTIPLICACION)
                self.state = 351
                self.factor()
                self.state = 352
                self.terminoAux1()

            elif token in [misterParser.DIVISION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.match(misterParser.DIVISION)
                self.state = 355
                self.factor()
                self.state = 356
                self.terminoAux1()

            elif token in [misterParser.Y, misterParser.O, misterParser.IDENTICO, misterParser.COMA, misterParser.SUMA, misterParser.RESTA, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR, misterParser.PARENTESIS2, misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 3)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def valor(self):
            return self.getTypedRuleContext(misterParser.ValorContext,0)


        def factorAux1(self):
            return self.getTypedRuleContext(misterParser.FactorAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitFactor(self)




    def factor(self):

        localctx = misterParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_factor)
        try:
            self.state = 369
            token = self._input.LA(1)
            if token in [misterParser.PARENTESIS1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.match(misterParser.PARENTESIS1)
                self.state = 362
                self.expresion()
                self.state = 363
                self.match(misterParser.PARENTESIS2)

            elif token in [misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.valor()

            elif token in [misterParser.SUMA, misterParser.RESTA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 366
                self.factorAux1()
                self.state = 367
                self.valor()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(misterParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(misterParser.RESTA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_factorAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterFactorAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitFactorAux1(self)




    def factorAux1(self):

        localctx = misterParser.FactorAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_factorAux1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            _la = self._input.LA(1)
            if not(_la==misterParser.SUMA or _la==misterParser.RESTA):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompuestoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def compuestoAux1(self):
            return self.getTypedRuleContext(misterParser.CompuestoAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_compuesto

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCompuesto(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCompuesto(self)




    def compuesto(self):

        localctx = misterParser.CompuestoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_compuesto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(misterParser.ID)
            self.state = 374
            self.compuestoAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompuestoAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUNTO(self):
            return self.getToken(misterParser.PUNTO, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def llamarFunc(self):
            return self.getTypedRuleContext(misterParser.LlamarFuncContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_compuestoAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCompuestoAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCompuestoAux1(self)




    def compuestoAux1(self):

        localctx = misterParser.CompuestoAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_compuestoAux1)
        try:
            self.state = 380
            token = self._input.LA(1)
            if token in [misterParser.PUNTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.match(misterParser.PUNTO)
                self.state = 377
                self.match(misterParser.ID)
                self.state = 378
                self.llamarFunc()

            elif token in [misterParser.Y, misterParser.O, misterParser.IDENTICO, misterParser.COMA, misterParser.SUMA, misterParser.RESTA, misterParser.DIVISION, misterParser.MULTIPLICACION, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR, misterParser.PARENTESIS2, misterParser.CORCHETE2, misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AsignacionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def IGUAL(self):
            return self.getToken(misterParser.IGUAL, 0)

        def asignacionAux1(self):
            return self.getTypedRuleContext(misterParser.AsignacionAux1Context,0)


        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = misterParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(misterParser.ID)
            self.state = 383
            self.match(misterParser.IGUAL)
            self.state = 384
            self.asignacionAux1()
            self.state = 385
            self.match(misterParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AsignacionAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def cteL(self):
            return self.getTypedRuleContext(misterParser.CteLContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_asignacionAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterAsignacionAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitAsignacionAux1(self)




    def asignacionAux1(self):

        localctx = misterParser.AsignacionAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_asignacionAux1)
        try:
            self.state = 389
            token = self._input.LA(1)
            if token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.expresion()

            elif token in [misterParser.CORCHETE1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.cteL()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondicionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(misterParser.SI, 0)

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def bloque(self):
            return self.getTypedRuleContext(misterParser.BloqueContext,0)


        def condicionAux1(self):
            return self.getTypedRuleContext(misterParser.CondicionAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = misterParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(misterParser.SI)
            self.state = 392
            self.match(misterParser.PARENTESIS1)
            self.state = 393
            self.expresion()
            self.state = 394
            self.match(misterParser.PARENTESIS2)
            self.state = 395
            self.bloque()
            self.state = 396
            self.condicionAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondicionAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINO(self):
            return self.getToken(misterParser.SINO, 0)

        def bloque(self):
            return self.getTypedRuleContext(misterParser.BloqueContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_condicionAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCondicionAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCondicionAux1(self)




    def condicionAux1(self):

        localctx = misterParser.CondicionAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_condicionAux1)
        try:
            self.state = 401
            token = self._input.LA(1)
            if token in [misterParser.SINO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(misterParser.SINO)
                self.state = 399
                self.bloque()

            elif token in [misterParser.SI, misterParser.MIENTRAS, misterParser.LEER, misterParser.IMPRIMIR, misterParser.RETORNAR, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.LLAVE2, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BloqueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE1(self):
            return self.getToken(misterParser.LLAVE1, 0)

        def estatuto(self):
            return self.getTypedRuleContext(misterParser.EstatutoContext,0)


        def bloqueAux1(self):
            return self.getTypedRuleContext(misterParser.BloqueAux1Context,0)


        def LLAVE2(self):
            return self.getToken(misterParser.LLAVE2, 0)

        def getRuleIndex(self):
            return misterParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitBloque(self)




    def bloque(self):

        localctx = misterParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(misterParser.LLAVE1)
            self.state = 404
            self.estatuto()
            self.state = 405
            self.bloqueAux1()
            self.state = 406
            self.match(misterParser.LLAVE2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BloqueAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def estatuto(self):
            return self.getTypedRuleContext(misterParser.EstatutoContext,0)


        def bloqueAux1(self):
            return self.getTypedRuleContext(misterParser.BloqueAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_bloqueAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterBloqueAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitBloqueAux1(self)




    def bloqueAux1(self):

        localctx = misterParser.BloqueAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_bloqueAux1)
        try:
            self.state = 412
            token = self._input.LA(1)
            if token in [misterParser.SI, misterParser.MIENTRAS, misterParser.LEER, misterParser.IMPRIMIR, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.estatuto()
                self.state = 409
                self.bloqueAux1()

            elif token in [misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CicloContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(misterParser.MIENTRAS, 0)

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def bloque(self):
            return self.getTypedRuleContext(misterParser.BloqueContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_ciclo

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCiclo(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCiclo(self)




    def ciclo(self):

        localctx = misterParser.CicloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(misterParser.MIENTRAS)
            self.state = 415
            self.match(misterParser.PARENTESIS1)
            self.state = 416
            self.expresion()
            self.state = 417
            self.match(misterParser.PARENTESIS2)
            self.state = 418
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EscrituraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPRIMIR(self):
            return self.getToken(misterParser.IMPRIMIR, 0)

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def escrituraAux1(self):
            return self.getTypedRuleContext(misterParser.EscrituraAux1Context,0)


        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_escritura

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterEscritura(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitEscritura(self)




    def escritura(self):

        localctx = misterParser.EscrituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(misterParser.IMPRIMIR)
            self.state = 421
            self.match(misterParser.PARENTESIS1)
            self.state = 422
            self.expresion()
            self.state = 423
            self.escrituraAux1()
            self.state = 424
            self.match(misterParser.PARENTESIS2)
            self.state = 425
            self.match(misterParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EscrituraAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(misterParser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def escrituraAux1(self):
            return self.getTypedRuleContext(misterParser.EscrituraAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_escrituraAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterEscrituraAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitEscrituraAux1(self)




    def escrituraAux1(self):

        localctx = misterParser.EscrituraAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_escrituraAux1)
        try:
            self.state = 432
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(misterParser.COMA)
                self.state = 428
                self.expresion()
                self.state = 429
                self.escrituraAux1()

            elif token in [misterParser.PARENTESIS2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LecturaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEER(self):
            return self.getToken(misterParser.LEER, 0)

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_lectura

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterLectura(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitLectura(self)




    def lectura(self):

        localctx = misterParser.LecturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(misterParser.LEER)
            self.state = 435
            self.match(misterParser.PARENTESIS1)
            self.state = 436
            self.match(misterParser.ID)
            self.state = 437
            self.match(misterParser.PARENTESIS2)
            self.state = 438
            self.match(misterParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class C_classContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASE(self):
            return self.getToken(misterParser.CLASE, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def classAux1(self):
            return self.getTypedRuleContext(misterParser.ClassAux1Context,0)


        def LLAVE1(self):
            return self.getToken(misterParser.LLAVE1, 0)

        def classAux2(self):
            return self.getTypedRuleContext(misterParser.ClassAux2Context,0)


        def classAux3(self):
            return self.getTypedRuleContext(misterParser.ClassAux3Context,0)


        def LLAVE2(self):
            return self.getToken(misterParser.LLAVE2, 0)

        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_c_class

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterC_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitC_class(self)




    def c_class(self):

        localctx = misterParser.C_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_c_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(misterParser.CLASE)
            self.state = 441
            self.match(misterParser.ID)
            self.state = 442
            self.classAux1()
            self.state = 443
            self.match(misterParser.LLAVE1)
            self.state = 444
            self.classAux2()
            self.state = 445
            self.classAux3()
            self.state = 446
            self.match(misterParser.LLAVE2)
            self.state = 447
            self.match(misterParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEREDA(self):
            return self.getToken(misterParser.HEREDA, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def getRuleIndex(self):
            return misterParser.RULE_classAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterClassAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitClassAux1(self)




    def classAux1(self):

        localctx = misterParser.ClassAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_classAux1)
        try:
            self.state = 452
            token = self._input.LA(1)
            if token in [misterParser.HEREDA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.match(misterParser.HEREDA)
                self.state = 450
                self.match(misterParser.ID)

            elif token in [misterParser.LLAVE1]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atrib(self):
            return self.getTypedRuleContext(misterParser.AtribContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_classAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterClassAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitClassAux2(self)




    def classAux2(self):

        localctx = misterParser.ClassAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_classAux2)
        try:
            self.state = 456
            token = self._input.LA(1)
            if token in [misterParser.ATRIBUTOS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.atrib()

            elif token in [misterParser.METODOS, misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def metod(self):
            return self.getTypedRuleContext(misterParser.MetodContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_classAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterClassAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitClassAux3(self)




    def classAux3(self):

        localctx = misterParser.ClassAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_classAux3)
        try:
            self.state = 460
            token = self._input.LA(1)
            if token in [misterParser.METODOS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.metod()

            elif token in [misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtribContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATRIBUTOS(self):
            return self.getToken(misterParser.ATRIBUTOS, 0)

        def DOSPUNTOS(self):
            return self.getToken(misterParser.DOSPUNTOS, 0)

        def atribAux1(self):
            return self.getTypedRuleContext(misterParser.AtribAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_atrib

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterAtrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitAtrib(self)




    def atrib(self):

        localctx = misterParser.AtribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_atrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(misterParser.ATRIBUTOS)
            self.state = 463
            self.match(misterParser.DOSPUNTOS)
            self.state = 464
            self.atribAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtribAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribAux2(self):
            return self.getTypedRuleContext(misterParser.AtribAux2Context,0)


        def v_varsAtrib(self):
            return self.getTypedRuleContext(misterParser.V_varsAtribContext,0)


        def atribAux3(self):
            return self.getTypedRuleContext(misterParser.AtribAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_atribAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterAtribAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitAtribAux1(self)




    def atribAux1(self):

        localctx = misterParser.AtribAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_atribAux1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.atribAux2()
            self.state = 467
            self.v_varsAtrib()
            self.state = 468
            self.atribAux3()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtribAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLICO(self):
            return self.getToken(misterParser.PUBLICO, 0)

        def PRIVADO(self):
            return self.getToken(misterParser.PRIVADO, 0)

        def getRuleIndex(self):
            return misterParser.RULE_atribAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterAtribAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitAtribAux2(self)




    def atribAux2(self):

        localctx = misterParser.AtribAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_atribAux2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            _la = self._input.LA(1)
            if not(_la==misterParser.PRIVADO or _la==misterParser.PUBLICO):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtribAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribAux1(self):
            return self.getTypedRuleContext(misterParser.AtribAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_atribAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterAtribAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitAtribAux3(self)




    def atribAux3(self):

        localctx = misterParser.AtribAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_atribAux3)
        try:
            self.state = 474
            token = self._input.LA(1)
            if token in [misterParser.PRIVADO, misterParser.PUBLICO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.atribAux1()

            elif token in [misterParser.METODOS, misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METODOS(self):
            return self.getToken(misterParser.METODOS, 0)

        def DOSPUNTOS(self):
            return self.getToken(misterParser.DOSPUNTOS, 0)

        def metodAux1(self):
            return self.getTypedRuleContext(misterParser.MetodAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_metod

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterMetod(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitMetod(self)




    def metod(self):

        localctx = misterParser.MetodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_metod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(misterParser.METODOS)
            self.state = 477
            self.match(misterParser.DOSPUNTOS)
            self.state = 478
            self.metodAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetodAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(misterParser.FUNCION, 0)

        def metodAux2(self):
            return self.getTypedRuleContext(misterParser.MetodAux2Context,0)


        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def func(self):
            return self.getTypedRuleContext(misterParser.FuncContext,0)


        def metodAux3(self):
            return self.getTypedRuleContext(misterParser.MetodAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_metodAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterMetodAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitMetodAux1(self)




    def metodAux1(self):

        localctx = misterParser.MetodAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_metodAux1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(misterParser.FUNCION)
            self.state = 481
            self.metodAux2()
            self.state = 482
            self.match(misterParser.ID)
            self.state = 483
            self.func()
            self.state = 484
            self.metodAux3()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetodAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(misterParser.TipoContext,0)


        def NADA(self):
            return self.getToken(misterParser.NADA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_metodAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterMetodAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitMetodAux2(self)




    def metodAux2(self):

        localctx = misterParser.MetodAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_metodAux2)
        try:
            self.state = 488
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.tipo()

            elif token in [misterParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.match(misterParser.NADA)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetodAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def metodAux1(self):
            return self.getTypedRuleContext(misterParser.MetodAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_metodAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterMetodAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitMetodAux3(self)




    def metodAux3(self):

        localctx = misterParser.MetodAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_metodAux3)
        try:
            self.state = 492
            token = self._input.LA(1)
            if token in [misterParser.FUNCION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.metodAux1()

            elif token in [misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





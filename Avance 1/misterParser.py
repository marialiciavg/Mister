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
        buf.write("\u01ed\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("\u0094\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u009d\n\4\3")
        buf.write("\5\3\5\5\5\u00a1\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7\u00aa")
        buf.write("\n\7\3\b\3\b\3\b\5\b\u00af\n\b\3\t\3\t\5\t\u00b3\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00bf")
        buf.write("\n\13\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00d1\n\17\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u00d7\n\20\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u00e2\n\22\3\23\3\23\3\23\5\23\u00e7")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00ef\n\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u00fc\n\26\3\27\3\27\3\27\3\27\5\27\u0102\n\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\5\30\u0109\n\30\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u0112\n\32\3\33\3\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u011e\n\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\5\37\u0129\n")
        buf.write("\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u0137\n!\3")
        buf.write("\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\5#\u0144\n#\3$\3$")
        buf.write("\3$\3$\3$\5$\u014b\n$\3%\3%\3%\5%\u0150\n%\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u015e\n\'\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\5(\u0168\n(\3)\3)\3*\3*\3*\3+\3+\3")
        buf.write("+\3+\5+\u0173\n+\3,\3,\3,\3,\3,\3,\5,\u017b\n,\3-\3-\3")
        buf.write("-\3-\3-\3.\3.\5.\u0184\n.\3/\3/\3/\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\5\60\u0190\n\60\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\5\62\u019b\n\62\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\5\65\u01af\n\65\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\58\u01c3\n8\39\39\59\u01c7\n9\3:\3:\5:\u01cb")
        buf.write("\n:\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3>\3>\5>\u01d9\n>\3")
        buf.write("?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\5A\u01e7\nA\3B\3B\5")
        buf.write("B\u01eb\nB\3B\2\2C\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("prtvxz|~\u0080\u0082\2\7\3\2\r\17\4\2\31\31\33\33\4\2")
        buf.write("\34\34#\'\3\2\37 \3\2\27\30\u01dc\2\u0084\3\2\2\2\4\u0093")
        buf.write("\3\2\2\2\6\u009c\3\2\2\2\b\u00a0\3\2\2\2\n\u00a2\3\2\2")
        buf.write("\2\f\u00a9\3\2\2\2\16\u00ae\3\2\2\2\20\u00b2\3\2\2\2\22")
        buf.write("\u00b4\3\2\2\2\24\u00be\3\2\2\2\26\u00c0\3\2\2\2\30\u00c2")
        buf.write("\3\2\2\2\32\u00c6\3\2\2\2\34\u00d0\3\2\2\2\36\u00d6\3")
        buf.write("\2\2\2 \u00d8\3\2\2\2\"\u00e1\3\2\2\2$\u00e6\3\2\2\2&")
        buf.write("\u00ee\3\2\2\2(\u00f0\3\2\2\2*\u00fb\3\2\2\2,\u0101\3")
        buf.write("\2\2\2.\u0108\3\2\2\2\60\u010a\3\2\2\2\62\u0111\3\2\2")
        buf.write("\2\64\u0113\3\2\2\2\66\u011d\3\2\2\28\u011f\3\2\2\2:\u0122")
        buf.write("\3\2\2\2<\u0128\3\2\2\2>\u012a\3\2\2\2@\u0136\3\2\2\2")
        buf.write("B\u0138\3\2\2\2D\u0143\3\2\2\2F\u014a\3\2\2\2H\u014f\3")
        buf.write("\2\2\2J\u0151\3\2\2\2L\u015d\3\2\2\2N\u0167\3\2\2\2P\u0169")
        buf.write("\3\2\2\2R\u016b\3\2\2\2T\u0172\3\2\2\2V\u017a\3\2\2\2")
        buf.write("X\u017c\3\2\2\2Z\u0183\3\2\2\2\\\u0185\3\2\2\2^\u018f")
        buf.write("\3\2\2\2`\u0191\3\2\2\2b\u019a\3\2\2\2d\u019c\3\2\2\2")
        buf.write("f\u01a2\3\2\2\2h\u01ae\3\2\2\2j\u01b0\3\2\2\2l\u01b6\3")
        buf.write("\2\2\2n\u01c2\3\2\2\2p\u01c6\3\2\2\2r\u01ca\3\2\2\2t\u01cc")
        buf.write("\3\2\2\2v\u01d0\3\2\2\2x\u01d4\3\2\2\2z\u01d8\3\2\2\2")
        buf.write("|\u01da\3\2\2\2~\u01de\3\2\2\2\u0080\u01e6\3\2\2\2\u0082")
        buf.write("\u01ea\3\2\2\2\u0084\u0085\5\4\3\2\u0085\u0086\5\6\4\2")
        buf.write("\u0086\u0087\7\f\2\2\u0087\u0088\7\r\2\2\u0088\u0089\7")
        buf.write("\6\2\2\u0089\u008a\5(\25\2\u008a\u008b\7\2\2\3\u008b\3")
        buf.write("\3\2\2\2\u008c\u008d\5\n\6\2\u008d\u008e\5\4\3\2\u008e")
        buf.write("\u0094\3\2\2\2\u008f\u0090\5l\67\2\u0090\u0091\5\4\3\2")
        buf.write("\u0091\u0094\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u008c\3")
        buf.write("\2\2\2\u0093\u008f\3\2\2\2\u0093\u0092\3\2\2\2\u0094\5")
        buf.write("\3\2\2\2\u0095\u0096\7\f\2\2\u0096\u0097\5\b\5\2\u0097")
        buf.write("\u0098\7\61\2\2\u0098\u0099\5(\25\2\u0099\u009a\5\6\4")
        buf.write("\2\u009a\u009d\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u0095")
        buf.write("\3\2\2\2\u009c\u009b\3\2\2\2\u009d\7\3\2\2\2\u009e\u00a1")
        buf.write("\5\26\f\2\u009f\u00a1\7\26\2\2\u00a0\u009e\3\2\2\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a1\t\3\2\2\2\u00a2\u00a3\5\f\7\2\u00a3")
        buf.write("\u00a4\5\22\n\2\u00a4\u00a5\7.\2\2\u00a5\13\3\2\2\2\u00a6")
        buf.write("\u00aa\7\61\2\2\u00a7\u00aa\5\26\f\2\u00a8\u00aa\5\30")
        buf.write("\r\2\u00a9\u00a6\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8")
        buf.write("\3\2\2\2\u00aa\r\3\2\2\2\u00ab\u00ac\7\35\2\2\u00ac\u00af")
        buf.write("\5\20\t\2\u00ad\u00af\3\2\2\2\u00ae\u00ab\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\17\3\2\2\2\u00b0\u00b3\5\60\31\2")
        buf.write("\u00b1\u00b3\5\32\16\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1")
        buf.write("\3\2\2\2\u00b3\21\3\2\2\2\u00b4\u00b5\7\61\2\2\u00b5\u00b6")
        buf.write("\5\16\b\2\u00b6\u00b7\5\24\13\2\u00b7\23\3\2\2\2\u00b8")
        buf.write("\u00b9\7\36\2\2\u00b9\u00ba\7\61\2\2\u00ba\u00bb\5\16")
        buf.write("\b\2\u00bb\u00bc\5\24\13\2\u00bc\u00bf\3\2\2\2\u00bd\u00bf")
        buf.write("\3\2\2\2\u00be\u00b8\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf")
        buf.write("\25\3\2\2\2\u00c0\u00c1\t\2\2\2\u00c1\27\3\2\2\2\u00c2")
        buf.write("\u00c3\7\21\2\2\u00c3\u00c4\5\26\f\2\u00c4\u00c5\7\3\2")
        buf.write("\2\u00c5\31\3\2\2\2\u00c6\u00c7\7,\2\2\u00c7\u00c8\5\36")
        buf.write("\20\2\u00c8\u00c9\5\34\17\2\u00c9\u00ca\7-\2\2\u00ca\33")
        buf.write("\3\2\2\2\u00cb\u00cc\7\36\2\2\u00cc\u00cd\5\36\20\2\u00cd")
        buf.write("\u00ce\5\34\17\2\u00ce\u00d1\3\2\2\2\u00cf\u00d1\3\2\2")
        buf.write("\2\u00d0\u00cb\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1\35\3")
        buf.write("\2\2\2\u00d2\u00d7\7\3\2\2\u00d3\u00d7\7\4\2\2\u00d4\u00d7")
        buf.write("\5R*\2\u00d5\u00d7\7\5\2\2\u00d6\u00d2\3\2\2\2\u00d6\u00d3")
        buf.write("\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7")
        buf.write("\37\3\2\2\2\u00d8\u00d9\7(\2\2\u00d9\u00da\5\"\22\2\u00da")
        buf.write("\u00db\7)\2\2\u00db!\3\2\2\2\u00dc\u00dd\5$\23\2\u00dd")
        buf.write("\u00de\7\61\2\2\u00de\u00df\5&\24\2\u00df\u00e2\3\2\2")
        buf.write("\2\u00e0\u00e2\3\2\2\2\u00e1\u00dc\3\2\2\2\u00e1\u00e0")
        buf.write("\3\2\2\2\u00e2#\3\2\2\2\u00e3\u00e7\7\61\2\2\u00e4\u00e7")
        buf.write("\5\26\f\2\u00e5\u00e7\5\30\r\2\u00e6\u00e3\3\2\2\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7%\3\2\2\2\u00e8")
        buf.write("\u00e9\7\36\2\2\u00e9\u00ea\5$\23\2\u00ea\u00eb\7\61\2")
        buf.write("\2\u00eb\u00ec\5&\24\2\u00ec\u00ef\3\2\2\2\u00ed\u00ef")
        buf.write("\3\2\2\2\u00ee\u00e8\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef")
        buf.write("\'\3\2\2\2\u00f0\u00f1\5 \21\2\u00f1\u00f2\7*\2\2\u00f2")
        buf.write("\u00f3\5*\26\2\u00f3\u00f4\5,\27\2\u00f4\u00f5\5.\30\2")
        buf.write("\u00f5\u00f6\7+\2\2\u00f6)\3\2\2\2\u00f7\u00f8\5\n\6\2")
        buf.write("\u00f8\u00f9\5*\26\2\u00f9\u00fc\3\2\2\2\u00fa\u00fc\3")
        buf.write("\2\2\2\u00fb\u00f7\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc+")
        buf.write("\3\2\2\2\u00fd\u00fe\5\66\34\2\u00fe\u00ff\5,\27\2\u00ff")
        buf.write("\u0102\3\2\2\2\u0100\u0102\3\2\2\2\u0101\u00fd\3\2\2\2")
        buf.write("\u0101\u0100\3\2\2\2\u0102-\3\2\2\2\u0103\u0104\7\20\2")
        buf.write("\2\u0104\u0105\5\60\31\2\u0105\u0106\7.\2\2\u0106\u0109")
        buf.write("\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u0103\3\2\2\2\u0108")
        buf.write("\u0107\3\2\2\2\u0109/\3\2\2\2\u010a\u010b\58\35\2\u010b")
        buf.write("\u010c\5\62\32\2\u010c\61\3\2\2\2\u010d\u010e\5\64\33")
        buf.write("\2\u010e\u010f\5\60\31\2\u010f\u0112\3\2\2\2\u0110\u0112")
        buf.write("\3\2\2\2\u0111\u010d\3\2\2\2\u0111\u0110\3\2\2\2\u0112")
        buf.write("\63\3\2\2\2\u0113\u0114\t\3\2\2\u0114\65\3\2\2\2\u0115")
        buf.write("\u011e\5X-\2\u0116\u011e\5\\/\2\u0117\u0118\5\60\31\2")
        buf.write("\u0118\u0119\7.\2\2\u0119\u011e\3\2\2\2\u011a\u011e\5")
        buf.write("f\64\2\u011b\u011e\5d\63\2\u011c\u011e\5j\66\2\u011d\u0115")
        buf.write("\3\2\2\2\u011d\u0116\3\2\2\2\u011d\u0117\3\2\2\2\u011d")
        buf.write("\u011a\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011c\3\2\2\2")
        buf.write("\u011e\67\3\2\2\2\u011f\u0120\5> \2\u0120\u0121\5<\37")
        buf.write("\2\u01219\3\2\2\2\u0122\u0123\t\4\2\2\u0123;\3\2\2\2\u0124")
        buf.write("\u0125\5:\36\2\u0125\u0126\5> \2\u0126\u0129\3\2\2\2\u0127")
        buf.write("\u0129\3\2\2\2\u0128\u0124\3\2\2\2\u0128\u0127\3\2\2\2")
        buf.write("\u0129=\3\2\2\2\u012a\u012b\5J&\2\u012b\u012c\5@!\2\u012c")
        buf.write("?\3\2\2\2\u012d\u012e\7\37\2\2\u012e\u012f\5J&\2\u012f")
        buf.write("\u0130\5@!\2\u0130\u0137\3\2\2\2\u0131\u0132\7 \2\2\u0132")
        buf.write("\u0133\5J&\2\u0133\u0134\5@!\2\u0134\u0137\3\2\2\2\u0135")
        buf.write("\u0137\3\2\2\2\u0136\u012d\3\2\2\2\u0136\u0131\3\2\2\2")
        buf.write("\u0136\u0135\3\2\2\2\u0137A\3\2\2\2\u0138\u0139\7(\2\2")
        buf.write("\u0139\u013a\5D#\2\u013a\u013b\7)\2\2\u013bC\3\2\2\2\u013c")
        buf.write("\u013d\5\60\31\2\u013d\u013e\5F$\2\u013e\u0144\3\2\2\2")
        buf.write("\u013f\u0140\7\32\2\2\u0140\u0141\7\61\2\2\u0141\u0144")
        buf.write("\5F$\2\u0142\u0144\3\2\2\2\u0143\u013c\3\2\2\2\u0143\u013f")
        buf.write("\3\2\2\2\u0143\u0142\3\2\2\2\u0144E\3\2\2\2\u0145\u0146")
        buf.write("\7\36\2\2\u0146\u0147\5H%\2\u0147\u0148\5F$\2\u0148\u014b")
        buf.write("\3\2\2\2\u0149\u014b\3\2\2\2\u014a\u0145\3\2\2\2\u014a")
        buf.write("\u0149\3\2\2\2\u014bG\3\2\2\2\u014c\u0150\5\60\31\2\u014d")
        buf.write("\u014e\7\32\2\2\u014e\u0150\7\61\2\2\u014f\u014c\3\2\2")
        buf.write("\2\u014f\u014d\3\2\2\2\u0150I\3\2\2\2\u0151\u0152\5N(")
        buf.write("\2\u0152\u0153\5L\'\2\u0153K\3\2\2\2\u0154\u0155\7\"\2")
        buf.write("\2\u0155\u0156\5N(\2\u0156\u0157\5L\'\2\u0157\u015e\3")
        buf.write("\2\2\2\u0158\u0159\7!\2\2\u0159\u015a\5N(\2\u015a\u015b")
        buf.write("\5L\'\2\u015b\u015e\3\2\2\2\u015c\u015e\3\2\2\2\u015d")
        buf.write("\u0154\3\2\2\2\u015d\u0158\3\2\2\2\u015d\u015c\3\2\2\2")
        buf.write("\u015eM\3\2\2\2\u015f\u0160\7(\2\2\u0160\u0161\5\60\31")
        buf.write("\2\u0161\u0162\7)\2\2\u0162\u0168\3\2\2\2\u0163\u0168")
        buf.write("\5\36\20\2\u0164\u0165\5P)\2\u0165\u0166\5\36\20\2\u0166")
        buf.write("\u0168\3\2\2\2\u0167\u015f\3\2\2\2\u0167\u0163\3\2\2\2")
        buf.write("\u0167\u0164\3\2\2\2\u0168O\3\2\2\2\u0169\u016a\t\5\2")
        buf.write("\2\u016aQ\3\2\2\2\u016b\u016c\7\61\2\2\u016c\u016d\5T")
        buf.write("+\2\u016dS\3\2\2\2\u016e\u016f\5B\"\2\u016f\u0170\5V,")
        buf.write("\2\u0170\u0173\3\2\2\2\u0171\u0173\3\2\2\2\u0172\u016e")
        buf.write("\3\2\2\2\u0172\u0171\3\2\2\2\u0173U\3\2\2\2\u0174\u0175")
        buf.write("\7\60\2\2\u0175\u0176\7\61\2\2\u0176\u0177\5B\"\2\u0177")
        buf.write("\u0178\5V,\2\u0178\u017b\3\2\2\2\u0179\u017b\3\2\2\2\u017a")
        buf.write("\u0174\3\2\2\2\u017a\u0179\3\2\2\2\u017bW\3\2\2\2\u017c")
        buf.write("\u017d\7\61\2\2\u017d\u017e\7\35\2\2\u017e\u017f\5Z.\2")
        buf.write("\u017f\u0180\7.\2\2\u0180Y\3\2\2\2\u0181\u0184\5\60\31")
        buf.write("\2\u0182\u0184\5\32\16\2\u0183\u0181\3\2\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0184[\3\2\2\2\u0185\u0186\7\7\2\2\u0186\u0187")
        buf.write("\7(\2\2\u0187\u0188\5\60\31\2\u0188\u0189\7)\2\2\u0189")
        buf.write("\u018a\5`\61\2\u018a\u018b\5^\60\2\u018b]\3\2\2\2\u018c")
        buf.write("\u018d\7\b\2\2\u018d\u0190\5`\61\2\u018e\u0190\3\2\2\2")
        buf.write("\u018f\u018c\3\2\2\2\u018f\u018e\3\2\2\2\u0190_\3\2\2")
        buf.write("\2\u0191\u0192\7*\2\2\u0192\u0193\5\66\34\2\u0193\u0194")
        buf.write("\5b\62\2\u0194\u0195\7+\2\2\u0195a\3\2\2\2\u0196\u0197")
        buf.write("\5\66\34\2\u0197\u0198\5b\62\2\u0198\u019b\3\2\2\2\u0199")
        buf.write("\u019b\3\2\2\2\u019a\u0196\3\2\2\2\u019a\u0199\3\2\2\2")
        buf.write("\u019bc\3\2\2\2\u019c\u019d\7\t\2\2\u019d\u019e\7(\2\2")
        buf.write("\u019e\u019f\5\60\31\2\u019f\u01a0\7)\2\2\u01a0\u01a1")
        buf.write("\5`\61\2\u01a1e\3\2\2\2\u01a2\u01a3\7\13\2\2\u01a3\u01a4")
        buf.write("\7(\2\2\u01a4\u01a5\5\60\31\2\u01a5\u01a6\5h\65\2\u01a6")
        buf.write("\u01a7\7)\2\2\u01a7\u01a8\7.\2\2\u01a8g\3\2\2\2\u01a9")
        buf.write("\u01aa\7\36\2\2\u01aa\u01ab\5\60\31\2\u01ab\u01ac\5h\65")
        buf.write("\2\u01ac\u01af\3\2\2\2\u01ad\u01af\3\2\2\2\u01ae\u01a9")
        buf.write("\3\2\2\2\u01ae\u01ad\3\2\2\2\u01afi\3\2\2\2\u01b0\u01b1")
        buf.write("\7\n\2\2\u01b1\u01b2\7(\2\2\u01b2\u01b3\7\61\2\2\u01b3")
        buf.write("\u01b4\7)\2\2\u01b4\u01b5\7.\2\2\u01b5k\3\2\2\2\u01b6")
        buf.write("\u01b7\7\22\2\2\u01b7\u01b8\7\61\2\2\u01b8\u01b9\5n8\2")
        buf.write("\u01b9\u01ba\7*\2\2\u01ba\u01bb\5p9\2\u01bb\u01bc\5r:")
        buf.write("\2\u01bc\u01bd\7+\2\2\u01bd\u01be\7.\2\2\u01bem\3\2\2")
        buf.write("\2\u01bf\u01c0\7\25\2\2\u01c0\u01c3\7\61\2\2\u01c1\u01c3")
        buf.write("\3\2\2\2\u01c2\u01bf\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3")
        buf.write("o\3\2\2\2\u01c4\u01c7\5t;\2\u01c5\u01c7\3\2\2\2\u01c6")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7q\3\2\2\2\u01c8")
        buf.write("\u01cb\5|?\2\u01c9\u01cb\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca")
        buf.write("\u01c9\3\2\2\2\u01cbs\3\2\2\2\u01cc\u01cd\7\23\2\2\u01cd")
        buf.write("\u01ce\7/\2\2\u01ce\u01cf\5v<\2\u01cfu\3\2\2\2\u01d0\u01d1")
        buf.write("\5x=\2\u01d1\u01d2\5\n\6\2\u01d2\u01d3\5z>\2\u01d3w\3")
        buf.write("\2\2\2\u01d4\u01d5\t\6\2\2\u01d5y\3\2\2\2\u01d6\u01d9")
        buf.write("\5v<\2\u01d7\u01d9\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d7")
        buf.write("\3\2\2\2\u01d9{\3\2\2\2\u01da\u01db\7\24\2\2\u01db\u01dc")
        buf.write("\7/\2\2\u01dc\u01dd\5~@\2\u01dd}\3\2\2\2\u01de\u01df\7")
        buf.write("\f\2\2\u01df\u01e0\5\u0080A\2\u01e0\u01e1\7\61\2\2\u01e1")
        buf.write("\u01e2\5(\25\2\u01e2\u01e3\5\u0082B\2\u01e3\177\3\2\2")
        buf.write("\2\u01e4\u01e7\5\26\f\2\u01e5\u01e7\7\26\2\2\u01e6\u01e4")
        buf.write("\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7\u0081\3\2\2\2\u01e8")
        buf.write("\u01eb\5~@\2\u01e9\u01eb\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea")
        buf.write("\u01e9\3\2\2\2\u01eb\u0083\3\2\2\2&\u0093\u009c\u00a0")
        buf.write("\u00a9\u00ae\u00b2\u00be\u00d0\u00d6\u00e1\u00e6\u00ee")
        buf.write("\u00fb\u0101\u0108\u0111\u011d\u0128\u0136\u0143\u014a")
        buf.write("\u014f\u015d\u0167\u0172\u017a\u0183\u018f\u019a\u01ae")
        buf.write("\u01c2\u01c6\u01ca\u01d8\u01e6\u01ea")
        return buf.getvalue()


class misterParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'INICIO'", u"'SI'", u"'SINO'", u"'MIENTRAS'", u"'LEER'", 
                     u"'IMPRIMIR'", u"'FUNCION'", u"'ENTERO'", u"'DECIMAL'", 
                     u"'TEXTO'", u"'RETORNAR'", u"'LISTA'", u"'CLASE'", 
                     u"'ATRIBUTOS'", u"'METODOS'", u"'HEREDA'", u"'NADA'", 
                     u"'PRIVADO'", u"'PUBLICO'", u"'&&'", u"'&'", u"'||'", 
                     u"'=='", u"'='", u"','", u"'+'", u"'-'", u"'/'", u"'*'", 
                     u"'!='", u"'>='", u"'<='", u"'<'", u"'>'", u"'('", 
                     u"')'", u"'{'", u"'}'", u"'['", u"']'", u"';'", u"':'", 
                     u"'.'" ]

    symbolicNames = [ u"<INVALID>", u"CTENTERO", u"CTEDECIMAL", u"CTETEXTO", 
                      u"INICIO", u"SI", u"SINO", u"MIENTRAS", u"LEER", u"IMPRIMIR", 
                      u"FUNCION", u"ENTERO", u"DECIMAL", u"TEXTO", u"RETORNAR", 
                      u"LISTA", u"CLASE", u"ATRIBUTOS", u"METODOS", u"HEREDA", 
                      u"NADA", u"PRIVADO", u"PUBLICO", u"Y", u"REFERENCIA", 
                      u"O", u"IDENTICO", u"IGUAL", u"COMA", u"SUMA", u"RESTA", 
                      u"DIVISION", u"MULTIPLICACION", u"DIFERENTE", u"MAYORIGUAL", 
                      u"MENORIGUAL", u"MENOR", u"MAYOR", u"PARENTESIS1", 
                      u"PARENTESIS2", u"LLAVE1", u"LLAVE2", u"CORCHETE1", 
                      u"CORCHETE2", u"PUNTOYCOMA", u"DOSPUNTOS", u"PUNTO", 
                      u"ID", u"WS" ]

    RULE_programa = 0
    RULE_programaAux1 = 1
    RULE_programaAux3 = 2
    RULE_programaAux4 = 3
    RULE_v_vars = 4
    RULE_varsAux1 = 5
    RULE_varsAux2 = 6
    RULE_varsAux3 = 7
    RULE_varsAux4 = 8
    RULE_varsAux5 = 9
    RULE_tipo = 10
    RULE_l_list = 11
    RULE_cteL = 12
    RULE_cteLAux1 = 13
    RULE_valor = 14
    RULE_parametros = 15
    RULE_parametrosAux1 = 16
    RULE_parametrosAux2 = 17
    RULE_parametrosAux3 = 18
    RULE_func = 19
    RULE_funcAux1 = 20
    RULE_funcAux2 = 21
    RULE_funcAux3 = 22
    RULE_expresion = 23
    RULE_expresionAux1 = 24
    RULE_expresionAux2 = 25
    RULE_estatuto = 26
    RULE_declaracion = 27
    RULE_declaracionAux1 = 28
    RULE_declaracionAux2 = 29
    RULE_exp = 30
    RULE_expAux1 = 31
    RULE_llamarFunc = 32
    RULE_llamarFuncAux1 = 33
    RULE_llamarFuncAux2 = 34
    RULE_llamarFuncAux3 = 35
    RULE_termino = 36
    RULE_terminoAux1 = 37
    RULE_factor = 38
    RULE_factorAux1 = 39
    RULE_compuesto = 40
    RULE_compuestoAux1 = 41
    RULE_compuestoAux2 = 42
    RULE_asignacion = 43
    RULE_asignacionAux1 = 44
    RULE_condicion = 45
    RULE_condicionAux1 = 46
    RULE_bloque = 47
    RULE_bloqueAux1 = 48
    RULE_ciclo = 49
    RULE_escritura = 50
    RULE_escrituraAux1 = 51
    RULE_lectura = 52
    RULE_c_class = 53
    RULE_classAux1 = 54
    RULE_classAux2 = 55
    RULE_classAux3 = 56
    RULE_atrib = 57
    RULE_atribAux1 = 58
    RULE_atribAux2 = 59
    RULE_atribAux3 = 60
    RULE_metod = 61
    RULE_metodAux1 = 62
    RULE_metodAux2 = 63
    RULE_metodAux3 = 64

    ruleNames =  [ "programa", "programaAux1", "programaAux3", "programaAux4", 
                   "v_vars", "varsAux1", "varsAux2", "varsAux3", "varsAux4", 
                   "varsAux5", "tipo", "l_list", "cteL", "cteLAux1", "valor", 
                   "parametros", "parametrosAux1", "parametrosAux2", "parametrosAux3", 
                   "func", "funcAux1", "funcAux2", "funcAux3", "expresion", 
                   "expresionAux1", "expresionAux2", "estatuto", "declaracion", 
                   "declaracionAux1", "declaracionAux2", "exp", "expAux1", 
                   "llamarFunc", "llamarFuncAux1", "llamarFuncAux2", "llamarFuncAux3", 
                   "termino", "terminoAux1", "factor", "factorAux1", "compuesto", 
                   "compuestoAux1", "compuestoAux2", "asignacion", "asignacionAux1", 
                   "condicion", "condicionAux1", "bloque", "bloqueAux1", 
                   "ciclo", "escritura", "escrituraAux1", "lectura", "c_class", 
                   "classAux1", "classAux2", "classAux3", "atrib", "atribAux1", 
                   "atribAux2", "atribAux3", "metod", "metodAux1", "metodAux2", 
                   "metodAux3" ]

    EOF = Token.EOF
    CTENTERO=1
    CTEDECIMAL=2
    CTETEXTO=3
    INICIO=4
    SI=5
    SINO=6
    MIENTRAS=7
    LEER=8
    IMPRIMIR=9
    FUNCION=10
    ENTERO=11
    DECIMAL=12
    TEXTO=13
    RETORNAR=14
    LISTA=15
    CLASE=16
    ATRIBUTOS=17
    METODOS=18
    HEREDA=19
    NADA=20
    PRIVADO=21
    PUBLICO=22
    Y=23
    REFERENCIA=24
    O=25
    IDENTICO=26
    IGUAL=27
    COMA=28
    SUMA=29
    RESTA=30
    DIVISION=31
    MULTIPLICACION=32
    DIFERENTE=33
    MAYORIGUAL=34
    MENORIGUAL=35
    MENOR=36
    MAYOR=37
    PARENTESIS1=38
    PARENTESIS2=39
    LLAVE1=40
    LLAVE2=41
    CORCHETE1=42
    CORCHETE2=43
    PUNTOYCOMA=44
    DOSPUNTOS=45
    PUNTO=46
    ID=47
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
            self.state = 130
            self.programaAux1()
            self.state = 131
            self.programaAux3()
            self.state = 132
            self.match(misterParser.FUNCION)
            self.state = 133
            self.match(misterParser.ENTERO)
            self.state = 134
            self.match(misterParser.INICIO)
            self.state = 135
            self.func()
            self.state = 136
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
            self.state = 145
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO, misterParser.LISTA, misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.v_vars()
                self.state = 139
                self.programaAux1()

            elif token in [misterParser.CLASE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.c_class()
                self.state = 142
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
            self.state = 154
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(misterParser.FUNCION)
                self.state = 148
                self.programaAux4()
                self.state = 149
                self.match(misterParser.ID)
                self.state = 150
                self.func()
                self.state = 151
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
            self.state = 158
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.tipo()

            elif token in [misterParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
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


        def varsAux4(self):
            return self.getTypedRuleContext(misterParser.VarsAux4Context,0)


        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

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
            self.state = 160
            self.varsAux1()
            self.state = 161
            self.varsAux4()
            self.state = 162
            self.match(misterParser.PUNTOYCOMA)
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
            self.state = 167
            token = self._input.LA(1)
            if token in [misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(misterParser.ID)

            elif token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.tipo()

            elif token in [misterParser.LISTA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
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
        self.enterRule(localctx, 12, self.RULE_varsAux2)
        try:
            self.state = 172
            token = self._input.LA(1)
            if token in [misterParser.IGUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(misterParser.IGUAL)
                self.state = 170
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
        self.enterRule(localctx, 14, self.RULE_varsAux3)
        try:
            self.state = 176
            token = self._input.LA(1)
            if token in [misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.expresion()

            elif token in [misterParser.CORCHETE1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
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
        self.enterRule(localctx, 16, self.RULE_varsAux4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(misterParser.ID)
            self.state = 179
            self.varsAux2()
            self.state = 180
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
        self.enterRule(localctx, 18, self.RULE_varsAux5)
        try:
            self.state = 188
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(misterParser.COMA)
                self.state = 183
                self.match(misterParser.ID)
                self.state = 184
                self.varsAux2()
                self.state = 185
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
        self.enterRule(localctx, 20, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
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
        self.enterRule(localctx, 22, self.RULE_l_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(misterParser.LISTA)
            self.state = 193
            self.tipo()
            self.state = 194
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
        self.enterRule(localctx, 24, self.RULE_cteL)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(misterParser.CORCHETE1)
            self.state = 197
            self.valor()
            self.state = 198
            self.cteLAux1()
            self.state = 199
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
        self.enterRule(localctx, 26, self.RULE_cteLAux1)
        try:
            self.state = 206
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(misterParser.COMA)
                self.state = 202
                self.valor()
                self.state = 203
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
        self.enterRule(localctx, 28, self.RULE_valor)
        try:
            self.state = 212
            token = self._input.LA(1)
            if token in [misterParser.CTENTERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(misterParser.CTENTERO)

            elif token in [misterParser.CTEDECIMAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.match(misterParser.CTEDECIMAL)

            elif token in [misterParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.compuesto()

            elif token in [misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 211
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
        self.enterRule(localctx, 30, self.RULE_parametros)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(misterParser.PARENTESIS1)
            self.state = 215
            self.parametrosAux1()
            self.state = 216
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
        self.enterRule(localctx, 32, self.RULE_parametrosAux1)
        try:
            self.state = 223
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO, misterParser.LISTA, misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.parametrosAux2()
                self.state = 219
                self.match(misterParser.ID)
                self.state = 220
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

        def ID(self):
            return self.getToken(misterParser.ID, 0)

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
        self.enterRule(localctx, 34, self.RULE_parametrosAux2)
        try:
            self.state = 228
            token = self._input.LA(1)
            if token in [misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(misterParser.ID)

            elif token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.tipo()

            elif token in [misterParser.LISTA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
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
        self.enterRule(localctx, 36, self.RULE_parametrosAux3)
        try:
            self.state = 236
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(misterParser.COMA)
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
        self.enterRule(localctx, 38, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.parametros()
            self.state = 239
            self.match(misterParser.LLAVE1)
            self.state = 240
            self.funcAux1()
            self.state = 241
            self.funcAux2()
            self.state = 242
            self.funcAux3()
            self.state = 243
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
        self.enterRule(localctx, 40, self.RULE_funcAux1)
        try:
            self.state = 249
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.v_vars()
                self.state = 246
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
        self.enterRule(localctx, 42, self.RULE_funcAux2)
        try:
            self.state = 255
            token = self._input.LA(1)
            if token in [misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO, misterParser.SI, misterParser.MIENTRAS, misterParser.LEER, misterParser.IMPRIMIR, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.estatuto()
                self.state = 252
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
        self.enterRule(localctx, 44, self.RULE_funcAux3)
        try:
            self.state = 262
            token = self._input.LA(1)
            if token in [misterParser.RETORNAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(misterParser.RETORNAR)
                self.state = 258
                self.expresion()
                self.state = 259
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
        self.enterRule(localctx, 46, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.declaracion()
            self.state = 265
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
        self.enterRule(localctx, 48, self.RULE_expresionAux1)
        try:
            self.state = 271
            token = self._input.LA(1)
            if token in [misterParser.Y, misterParser.O]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.expresionAux2()
                self.state = 268
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
        self.enterRule(localctx, 50, self.RULE_expresionAux2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
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
        self.enterRule(localctx, 52, self.RULE_estatuto)
        try:
            self.state = 283
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.condicion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.expresion()
                self.state = 278
                self.match(misterParser.PUNTOYCOMA)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.escritura()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 281
                self.ciclo()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 282
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
        self.enterRule(localctx, 54, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.exp()
            self.state = 286
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
        self.enterRule(localctx, 56, self.RULE_declaracionAux1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
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
        self.enterRule(localctx, 58, self.RULE_declaracionAux2)
        try:
            self.state = 294
            token = self._input.LA(1)
            if token in [misterParser.IDENTICO, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.declaracionAux1()
                self.state = 291
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
        self.enterRule(localctx, 60, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.termino()
            self.state = 297
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
        self.enterRule(localctx, 62, self.RULE_expAux1)
        try:
            self.state = 308
            token = self._input.LA(1)
            if token in [misterParser.SUMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(misterParser.SUMA)
                self.state = 300
                self.termino()
                self.state = 301
                self.expAux1()

            elif token in [misterParser.RESTA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(misterParser.RESTA)
                self.state = 304
                self.termino()
                self.state = 305
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
        self.enterRule(localctx, 64, self.RULE_llamarFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(misterParser.PARENTESIS1)
            self.state = 311
            self.llamarFuncAux1()
            self.state = 312
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
        self.enterRule(localctx, 66, self.RULE_llamarFuncAux1)
        try:
            self.state = 321
            token = self._input.LA(1)
            if token in [misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.expresion()
                self.state = 315
                self.llamarFuncAux2()

            elif token in [misterParser.REFERENCIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(misterParser.REFERENCIA)
                self.state = 318
                self.match(misterParser.ID)
                self.state = 319
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
        self.enterRule(localctx, 68, self.RULE_llamarFuncAux2)
        try:
            self.state = 328
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(misterParser.COMA)
                self.state = 324
                self.llamarFuncAux3()
                self.state = 325
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
        self.enterRule(localctx, 70, self.RULE_llamarFuncAux3)
        try:
            self.state = 333
            token = self._input.LA(1)
            if token in [misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.expresion()

            elif token in [misterParser.REFERENCIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.match(misterParser.REFERENCIA)
                self.state = 332
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
        self.enterRule(localctx, 72, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.factor()
            self.state = 336
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
        self.enterRule(localctx, 74, self.RULE_terminoAux1)
        try:
            self.state = 347
            token = self._input.LA(1)
            if token in [misterParser.MULTIPLICACION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(misterParser.MULTIPLICACION)
                self.state = 339
                self.factor()
                self.state = 340
                self.terminoAux1()

            elif token in [misterParser.DIVISION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.match(misterParser.DIVISION)
                self.state = 343
                self.factor()
                self.state = 344
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
        self.enterRule(localctx, 76, self.RULE_factor)
        try:
            self.state = 357
            token = self._input.LA(1)
            if token in [misterParser.PARENTESIS1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.match(misterParser.PARENTESIS1)
                self.state = 350
                self.expresion()
                self.state = 351
                self.match(misterParser.PARENTESIS2)

            elif token in [misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO, misterParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.valor()

            elif token in [misterParser.SUMA, misterParser.RESTA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                self.factorAux1()
                self.state = 355
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
        self.enterRule(localctx, 78, self.RULE_factorAux1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
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
        self.enterRule(localctx, 80, self.RULE_compuesto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(misterParser.ID)
            self.state = 362
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

        def llamarFunc(self):
            return self.getTypedRuleContext(misterParser.LlamarFuncContext,0)


        def compuestoAux2(self):
            return self.getTypedRuleContext(misterParser.CompuestoAux2Context,0)


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
        self.enterRule(localctx, 82, self.RULE_compuestoAux1)
        try:
            self.state = 368
            token = self._input.LA(1)
            if token in [misterParser.PARENTESIS1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.llamarFunc()
                self.state = 365
                self.compuestoAux2()

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

    class CompuestoAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUNTO(self):
            return self.getToken(misterParser.PUNTO, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def llamarFunc(self):
            return self.getTypedRuleContext(misterParser.LlamarFuncContext,0)


        def compuestoAux2(self):
            return self.getTypedRuleContext(misterParser.CompuestoAux2Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_compuestoAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCompuestoAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCompuestoAux2(self)




    def compuestoAux2(self):

        localctx = misterParser.CompuestoAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_compuestoAux2)
        try:
            self.state = 376
            token = self._input.LA(1)
            if token in [misterParser.PUNTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.match(misterParser.PUNTO)
                self.state = 371
                self.match(misterParser.ID)
                self.state = 372
                self.llamarFunc()
                self.state = 373
                self.compuestoAux2()

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
        self.enterRule(localctx, 86, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(misterParser.ID)
            self.state = 379
            self.match(misterParser.IGUAL)
            self.state = 380
            self.asignacionAux1()
            self.state = 381
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
        self.enterRule(localctx, 88, self.RULE_asignacionAux1)
        try:
            self.state = 385
            token = self._input.LA(1)
            if token in [misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.expresion()

            elif token in [misterParser.CORCHETE1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
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
        self.enterRule(localctx, 90, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(misterParser.SI)
            self.state = 388
            self.match(misterParser.PARENTESIS1)
            self.state = 389
            self.expresion()
            self.state = 390
            self.match(misterParser.PARENTESIS2)
            self.state = 391
            self.bloque()
            self.state = 392
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
        self.enterRule(localctx, 92, self.RULE_condicionAux1)
        try:
            self.state = 397
            token = self._input.LA(1)
            if token in [misterParser.SINO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(misterParser.SINO)
                self.state = 395
                self.bloque()

            elif token in [misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO, misterParser.SI, misterParser.MIENTRAS, misterParser.LEER, misterParser.IMPRIMIR, misterParser.RETORNAR, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.LLAVE2, misterParser.ID]:
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
        self.enterRule(localctx, 94, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(misterParser.LLAVE1)
            self.state = 400
            self.estatuto()
            self.state = 401
            self.bloqueAux1()
            self.state = 402
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
        self.enterRule(localctx, 96, self.RULE_bloqueAux1)
        try:
            self.state = 408
            token = self._input.LA(1)
            if token in [misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO, misterParser.SI, misterParser.MIENTRAS, misterParser.LEER, misterParser.IMPRIMIR, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.estatuto()
                self.state = 405
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
        self.enterRule(localctx, 98, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(misterParser.MIENTRAS)
            self.state = 411
            self.match(misterParser.PARENTESIS1)
            self.state = 412
            self.expresion()
            self.state = 413
            self.match(misterParser.PARENTESIS2)
            self.state = 414
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
        self.enterRule(localctx, 100, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(misterParser.IMPRIMIR)
            self.state = 417
            self.match(misterParser.PARENTESIS1)
            self.state = 418
            self.expresion()
            self.state = 419
            self.escrituraAux1()
            self.state = 420
            self.match(misterParser.PARENTESIS2)
            self.state = 421
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
        self.enterRule(localctx, 102, self.RULE_escrituraAux1)
        try:
            self.state = 428
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(misterParser.COMA)
                self.state = 424
                self.expresion()
                self.state = 425
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
        self.enterRule(localctx, 104, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(misterParser.LEER)
            self.state = 431
            self.match(misterParser.PARENTESIS1)
            self.state = 432
            self.match(misterParser.ID)
            self.state = 433
            self.match(misterParser.PARENTESIS2)
            self.state = 434
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
        self.enterRule(localctx, 106, self.RULE_c_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(misterParser.CLASE)
            self.state = 437
            self.match(misterParser.ID)
            self.state = 438
            self.classAux1()
            self.state = 439
            self.match(misterParser.LLAVE1)
            self.state = 440
            self.classAux2()
            self.state = 441
            self.classAux3()
            self.state = 442
            self.match(misterParser.LLAVE2)
            self.state = 443
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
        self.enterRule(localctx, 108, self.RULE_classAux1)
        try:
            self.state = 448
            token = self._input.LA(1)
            if token in [misterParser.HEREDA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.match(misterParser.HEREDA)
                self.state = 446
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
        self.enterRule(localctx, 110, self.RULE_classAux2)
        try:
            self.state = 452
            token = self._input.LA(1)
            if token in [misterParser.ATRIBUTOS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
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
        self.enterRule(localctx, 112, self.RULE_classAux3)
        try:
            self.state = 456
            token = self._input.LA(1)
            if token in [misterParser.METODOS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
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
        self.enterRule(localctx, 114, self.RULE_atrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(misterParser.ATRIBUTOS)
            self.state = 459
            self.match(misterParser.DOSPUNTOS)
            self.state = 460
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


        def v_vars(self):
            return self.getTypedRuleContext(misterParser.V_varsContext,0)


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
        self.enterRule(localctx, 116, self.RULE_atribAux1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.atribAux2()
            self.state = 463
            self.v_vars()
            self.state = 464
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
        self.enterRule(localctx, 118, self.RULE_atribAux2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
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
        self.enterRule(localctx, 120, self.RULE_atribAux3)
        try:
            self.state = 470
            token = self._input.LA(1)
            if token in [misterParser.PRIVADO, misterParser.PUBLICO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
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
        self.enterRule(localctx, 122, self.RULE_metod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(misterParser.METODOS)
            self.state = 473
            self.match(misterParser.DOSPUNTOS)
            self.state = 474
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
        self.enterRule(localctx, 124, self.RULE_metodAux1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(misterParser.FUNCION)
            self.state = 477
            self.metodAux2()
            self.state = 478
            self.match(misterParser.ID)
            self.state = 479
            self.func()
            self.state = 480
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
        self.enterRule(localctx, 126, self.RULE_metodAux2)
        try:
            self.state = 484
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.tipo()

            elif token in [misterParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
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
        self.enterRule(localctx, 128, self.RULE_metodAux3)
        try:
            self.state = 488
            token = self._input.LA(1)
            if token in [misterParser.FUNCION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
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





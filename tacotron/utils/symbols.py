'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
from . import cmudict

_pad        = '_'
_eos        = '~'
# config for english
# _characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'\"(),-.:;? '
_characters = ['a', 'b', 'c', 'ch', 'd', 'e', 'f', 'gh', 'gi', 'h', 'i', 'k', 'kh', 'l', 'm', 'n', 'ng', 'ngh', 'nh', 'o', 'p', 'ph', 'q', 'qu', 'r', 's', 'sh', 't', 'th', 'tr', 'u', 'v', 'w', 'x', 'y', 'z', 'à', 'á', 'â', 'ã', 'è', 'é', 'ê', 'ì', 'í', 'ð', 'ò', 'ó', 'ô', 'õ', 'ù', 'ú', 'ý', 'ă', 'đ', 'ĩ', 'ũ', 'ơ', 'ư', 'ạ', 'ả', 'ấ', 'ầ', 'ẩ', 'ẫ', 'ậ', 'ắ', 'ằ', 'ẳ', 'ẵ', 'ặ', 'ẹ', 'ẻ', 'ẽ', 'ế', 'ề', 'ể', 'ễ', 'ệ', 'ỉ', 'ị', 'ọ', 'ỏ', 'ố', 'ồ', 'ổ', 'ỗ', 'ộ', 'ớ', 'ờ', 'ở', 'ỡ', 'ợ', 'ụ', 'ủ', 'ứ', 'ừ', 'ử', 'ữ', 'ự', 'ỳ', 'ỵ', 'ỷ', 'ỹ', '!', "'", '"', '(', ')', '-', '.', ':', ';', '?', ' ', '\n']

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
#_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
# symbols = [_pad, _eos] + list(_characters) #+ _arpabet
symbols = [_pad, _eos] + _characters #+ _arpabet

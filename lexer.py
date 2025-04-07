import re

TOKEN_SPEC = [
    ('NUMBER',    r'\d+'),
    ('RAAYI', r'raayi'),
    ('MODALLU',   r'modallu'),
    ('MUGIMPU',   r'mugimpu'),
    ('VILUVA', r'viluva'),
    ('LOOPU',     r'loopu'),
    ('SRUSHTINCHU', r'srushtinchu'),
    ('PAMPINCHU', r'pampinchu'),  # <-- Print keyword
    ('KOSAM',     r'kosam'),
    ('LOPALA',    r'lopala'),
    ('AAPEY',     r'aapey'),
    ('ITEY',        r'itey'),        # if
    ('LEKAPOTE',    r'lekapote'),    # else
    ('విలువ',    r'విలువ'),
    ('రాయీ',        r'రాయీ'),        # RAAYI
    ('మొదలు',       r'మొదలు'),       # MODALLU (begin/start)
    ('ముగింపు',     r'ముగింపు'),     # MUGIMPU (end)
    ('లూప్',        r'లూప్'),        # LOOPU (loop)
    ('సృష్టించు',    r'సృష్టించు'),    # SRUSHTINCHU (create/define)
    ('పంపించు',      r'పంపించు'),      # PAMPINCHU (print/send)
    ('కోసం',        r'కోసం'),        # KOSAM (for)
    ('లోపల',        r'లోపల'),        # LOPALA (inside/in)
    ('ఆపే',         r'ఆపే'), 
    ('STRING', r'"[^"\n]*"'),
    ('COMMENT', r'//.*'),
    ('LE',        r'<='),
    ('LT',        r'<'),
    ('GE',        r'>='),
    ('GT',        r'>'),
    ('EQ',        r'=='),
    ('NE',        r'!='),
    ('ID',       r'[A-Za-z_ఁ-౿][A-Za-z0-9_ఁ-౿]*'),    
    ('EQUALS',    r'='),
    ('PLUS',      r'\+'),
    ('MINUS',     r'-'),
    ('STAR',      r'\*'),
    ('LPAREN',    r'\('),
    ('RPAREN',    r'\)'),
    ('TO',        r'to'),
    ('SLASH',     r'/'),
    ('COMMA',     r','),  # <-- Added comma token
    ('SEMICOLON', r';'),
    ('SKIP',      r'[ \t]+'),
    ('NEWLINE',   r'\n'),
    ('MISMATCH',  r'.'),
]


TOKEN_RE = re.compile('|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPEC))

def tokenize(code):
    for match in TOKEN_RE.finditer(code):
        kind = match.lastgroup
        value = match.group()
        if kind in ('SKIP', 'NEWLINE'):
            continue
        elif kind == 'NUMBER':
            value = int(value)
        elif kind == 'MISMATCH':
            raise RuntimeError(f"Unexpected character: {value}")
        elif kind == 'COMMENT':
            continue
        yield (kind, value)

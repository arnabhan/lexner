import ply.lex as lex

NAMED_ENTITIES = [
    "URI",
    "MONEY_AMOUNT",
    "CURRENCY",
    "HYPTHENATED",
    "QUESTIONMARK",
    "ALPHANUM",
    "TEMP_DURATION",
    "TEMP_TIME",
    "TEMP_SET",
    "DATETIMEDIGITAL",
    "TIMEDIGITAL",
    "ABBREV",
    "CLITIC",
    "QUANTITY",
    "REAL",
    "YEAR",
    "DAYNUM",
    "INTEGER",
    "EMAIL",
    "DAY",
    "MONTH",
    "HASHTAG"
]

tokens = (
    "URI",
    "MONEY_AMOUNT",
    "CURRENCY",
    "HYPTHENATED",
    "QUESTIONMARK",
    "ALPHANUM",
    "TEMP_DURATION", #http://projects.csail.mit.edu/workbench/update/guides/03%20-%20Temporal%20Expressions_v2.0.1.pdf
    "TEMP_TIME",
    "TEMP_SET",
    "DATETIMEDIGITAL",
    "TIMEDIGITAL",
    "ABBREV",
    "CLITIC",
    "QUANTITY",
    "REAL",
    "YEAR",
    "DAYNUM",
    "INTEGER",
    "EMAIL",
    "DAY",
    "MONTH",
    "HASHTAG",
    "WORD",
    "DELIM",
    "SEQ"
)

#1 URL
# https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Generic_syntax
#URI = scheme:[//authority]path[?query][#fragment]
#authority = [userinfo@]host[:port]
def t_URI(t):
    r'\w+\://[\w\-\+]+[\.\w+\-]*[\:\d+]*[/\w\-]*[\?\w]?[#\w_]*' #|\w+[\.\w+\-]*[\:\d+]*[/\w\-]+[\?\w]?'
    return t

#2
def t_HYPTHENATED(t):
    r'(?<=\s)\w+\-\w+'
    return t

#3
def t_MONEY_AMOUNT(t):
    r"\$\d+(\.\d+)?|\d+(\.\d+)?(?=(\s)*dollars)|\d+(\.\d+)?(?=(\s)*dlrs)"
    #r"\$\d+(\.\d+)?"
    #r"\d+(\.\d+)?(?=(\s)*dollars)"
    #r"\d+(\.\d+)?(?=(\s)*dlrs)"    
    return t

#4
def t_DATETIMEDIGITAL(t):
    #r'(?=\A0[1-9]|[1][1-2]|[1-9])\d+[/\-\.]\d+[/\-\.]\d+'
    #r'(?=(0[1-9]|[1][0-2]|[1-9])\D+)\d+/\d+/\d+'
    #r'\A(?=(?:0[1-9]|[1][0-2]|[1-9])\D+)\d+/\d+/\d+\Z'
    
    r'(?<=\D)(?=(?:0[1-9]|[1][0-2]|[1-9])\D+)\d+/\d+/\d+|(?<=\D)(?=(?:0[1-9]|[1][0-2]|[1-9])\D+)\d+\-\d+\-\d+|(?<=\D|\s)(?=(?:0[1-9]|[1][0-2]|[1-9])\D+)\d+[\.]\d+[\.]\d+'
    #r'(?<=\D)(?=(?:0[1-9]|[1][0-2]|[1-9])\D+)\d+\-\d+\-\d+'
    #r'(?<=\D|\s)(?=(?:0[1-9]|[1][0-2]|[1-9])\D+)\d+[\.]\d+[\.]\d+'

    #r'\d+/\d+/d+'
    return t 

#5
def t_TIMEDIGITAL(t):
    r'(?=(?:0[1-9]|[1][0-2]|[1-9])\D+)\d+\:\d+\:\d+(?:\.\d+)*'
    return t

#6
def t_TEMP_DURATION(t):
    r'(for\s)?(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|tweleve)\s*(years|year|yrs|yr|months|month|weeks|week|wk|days|day|nights|night|hours|hour|hrs|hr|hrs.|hr.|minutes|minute|mins|min|seconds|second|secs|sec)(\s*long)?'
    return t

#7
def t_TEMP_TIME(t):
    r'today|yesterday|tomorrow|(past|last|next|current)\s+(years|year|yrs|yr|months|month|weeks|week|wk|days|day|nights|night|hours|hour|hrs|hr|hrs.|hr.|minutes|minute|mins|min|seconds|second|secs|sec)'
    return t

#8
def t_TEMP_SET(t):
    r'every\s+(\d+\s+)*(seconds|second|secs|sec|minutes|minute|mins|min|hours|hour|hrs|hr|days|day|weeks|week|wks|wk|months|month|years|year|yrs|year)|twice\s+a\s+(second|sec|minute|min|hour|hr|day|week|wk|month|year|yr)|every\s+(second|sec|minute|min|hour|hr|day|week|wk|month|year|yr)'
    return t

#9
def t_HASHTAG(t):
    r'\#\S+'
    return t

#10
def t_CURRENCY(t):
    r"dollars|dollar|dlrs|dls|euro|lires|lire|dinars|dinar|pounds|pound|yuan|yin|pesos"
    return t

#11.1
def t_QUANTITY(t):
    r"\d+(\.\d+)*\s+(thousands|millions|mlns|billions|thousand|million|mln|billion)"
    return t

#11
def t_REAL(t):
    r"\d+(\,\d+)*\.\d+|\d+\,\d+"
    return t

#12
def t_YEAR(t):
    r"[1|2]\d{3}"
    t.value = int(t.value)
    return t

#13
def t_DAYNUM(t):
    # look forward:
    r"\d(st|nd|rd|th)\s+(?=january|february|march|april|may|june|july|august|september|october|november|december)"
    # look behind:
    # this one below does not work, because look behind in python re must have strings of equal lengths! regex does a better job
    #r"(?<=[january|february|march|april|may|june|july|august|september|october|november|december]\s)\d(st|nd|rd|th)"
    # this one below works because of fixed length
    r"(?<=jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s+\d(st|nd|rd|th)"
    return t

#14
def t_MONTH(t):
    r"(january|february|march|april|may|june|july|august|september|october|november|december)"
    r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)"
    return t

#15
def t_INTEGER(t):
    r"\d+"
    t.value = int(t.value)
    return t

#16
def t_ALPHANUM(t):
    r"[A-z](?=[A-z]*\d+)[A-z0-9]+"
    return t

#17
def t_EMAIL(t):
    r"[A-z][A-z0-9.]+@[A-z0-9]+[.][A-z0-9]+" # needs more work
    return t

#18
def t_DELIM(t):
    r'[\s|\,|\;|\:|\-|\.\!\|\&|\*|\^|\%|\#\|~]'
    return t

#19
def t_DAY(t):
    #r"[M|m][O|o][N|n][D|d][A|a][Y|y]"
    r"(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
    r"(mon|tue|wed|thu|fri|sat|sun)"
    return t

#20
def t_error(t):
    #raise TypeError("Unknown text '%s'" % (t.value,))
    pass

#21
def t_WORD(t):
    r'[A-z]+'
    return t
    #pass

#22
def t_ABBREV(t):
    #r'(?<=\()[A-z]+(?=\))'
    r'\([A-z]+\)'
    return t
    
#23 clitic analysis
def t_CLITIC(t):
    r'(?<=[A-z])\'(m|re|ve|s|t|d)'
    return t

#24 clitic analysis
def t_QUESTIONMARK(t):
    r'(?<=\w\w)\?' # at least 2 letters
    return t

#25
def t_SEQ(t):
    r'\S+'
    return t

lex.lex()

def get_named_entities(text):
    lex.input(text)
    return sorted([(int(repr(tok.lexpos)), len(str(tok.value)), str(tok.type), str(tok.value)) for tok in iter(lex.token, None)], key=lambda x : x[0] * 1000 + x[1])

def get_processed_text(annotations):
    processed_text = ''
    for (_, _, tok_type, tok_val) in annotations:
        if tok_type == 'CLITIC':
            processed_text += ' <' + tok_type + '> ' + tok_val + ' </' + tok_type + '>' 
        elif tok_type == 'DELIM' and tok_val !=' ':
            processed_text += ' ' + tok_val + ' ' 
        elif tok_type in NAMED_ENTITIES:
            processed_text += '<' + tok_type + '> ' + tok_val + ' </' + tok_type + '>' 
        else:
            processed_text += tok_val
    return processed_text


''' 
Example:

result = get_named_entities("on tue april 13, 2019 i created email abc123.fun@msn.com for 1.3 dollars")

for r in result:
    print(r)

'''
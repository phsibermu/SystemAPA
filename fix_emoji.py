import re

f = 'c:/Users/Mr.Unknown/Documents/APA/frontend/src/pages/Siswa/Dashboard.vue'
t = open(f, 'r', encoding='utf-8').read()

replacements = {
    '\u00c3\u00b0\u00c5\u00b8\u00e2\u0080\u0099\u00e2\u0080\u0099': '',  # possible double encode pattern
}

# Fix known corrupted strings
fixes = [
    ('ðŸ†', '★'),
    ('ðŸ"'', ''),
    ('âœ•', '✕'),
    ('âš ï¸', ''),
    ('â†', '←'),
    ('âœ"', '✓'),
    ('â—', '●'),
    ('â—‹', '○'),
]

for old, new in fixes:
    if old in t:
        t = t.replace(old, new)
        print(f'  Replaced: {repr(old)} -> {repr(new)}')

open(f, 'w', encoding='utf-8', newline='\n').write(t)
print('Done - all corrupted emojis fixed')

# ANSI escape sequences for styles
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
REVERSED = '\033[7m'

# ANSI escape sequences for terminal colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[m'

# ANSI escape sequences for background colors
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_PURPLE = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

print(f'{RED}red text{RESET}')
print(f'{GREEN}Hello, World!{RESET}')
print(f'{YELLOW}This is a yellow warning!{RESET}')
print(f'{BLUE}This text is blue.{RESET}')
print(f'{PURPLE}Purple is a royal color.{RESET}')
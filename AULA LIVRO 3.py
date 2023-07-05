import calendar
import locale

# Configura a localização para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

ano = 2050

# Cria um calendário para o ano especificado
calendario = calendar.calendar(ano)

# Exibe o calendário na saída
print(calendario)
    
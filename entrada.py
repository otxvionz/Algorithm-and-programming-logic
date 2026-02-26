nome = input('Qual seu nome?')
sobrenome = input('Qual seu sobrenome?')
print('Olá',nome,sobrenome,'seja bem-vindo ao meu sistema')
universidade = input('Qual Universidade você estuda?')
dia_nascimento = input('Dia de nascimento: ')
mes_nascimento = input('Mes de nascimento: ')
ano_nascimento = input('Ano de nascimento: ')

e_mail = nome.lower() + '.' + sobrenome.lower() + '@' + universidade.lower() + '.br'
senha = 'a' + str(e_mail.count('a')) + 'e' + str(e_mail.count('e')) + 'i' + str(e_mail.count('i')) + 'o' + str(e_mail.count('o')) + 'u' + str(e_mail.count('u'))


print('O seu e-mail é:{}'.format(e_mail))
print('Sua senha é:{}'.format(senha))

print('seu email e sua senha é {}'.format(e_mail,senha))
    

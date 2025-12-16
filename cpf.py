# Padrão nomear a função com "validate_nome_do_campo"
def validate_cpf(self, valor):
    # Retirada de simbolos especiais do CPF:
    cpf = re.sub(r'[^0-9]', '', valor)

    # Verificação de tamanho e se todos os dígitos são iguais:
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        raise serializers.ValidationError(
            "CPF inválido ou com formato incorreto")
        '''
        * 11: No Python, quando você multiplica um texto por um número, ele repete o texto.
        '''

    # Cálculo e verificação de 1º dígito

    # Definição de variáveis para validação
    soma = 0
    peso = 10

    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    if digito1 != int(cpf[9]):
        raise serializers.ValidationError("CPF inválido! Dígito verificador 1 incorreto.")

    # Cálculo e verificação de 2º dígito:

    # Definição de variáveis
    soma = 0
    peso = 11

    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # Verificação de 2º dígito
    if digito2 != int(cpf[10]):
        raise serializers.ValidationError("CPF inválido! Dígito verificador 2 incorreto.")

    return valor

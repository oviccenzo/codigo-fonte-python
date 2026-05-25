####5.2 Dicionários: fundação da linguagem

entidades1 = {
    'Instituicao' : []
}

entidades1 = dict(instituicao1 = [])

entidades2 = dict()
entidades2['empreendimento'] = 'EntidadeEmpreendimento'
print(entidades2)

# del entidades['empreendimento']
# print(entidades["empreendimento"])
# ----> 1 del entidades['empreendimento']
#       2 print(entidades["empreendimento"])

# KeyError: 'empreendimento'

entidades3 = {
    'Instituicao' :[
        ('IdInstituicao', 'Bigint',
         'Identicador da Instituicao-PK'),
        ('Id tipo de Instituicao'),
        ('NomInstituicao','Varchar','Nome da instituicao'),
        ('NumCnpj','varchar','Numero do CNPJ')
    ]
}
choices = [
  '1 - Adicionar Contato',
  '2 - Visualizar Contatos',
  '3 - Editar Contato',
  '4 - Marcar contato como favorito',
  '5 - Ver Favoritos',
  '6 - Apagar Contato',
  '7 - Sair'
]

contacts = []

def addContact():
  contact_name = input('Nome: ')
  contact_phone = input('Telefone: ')
  contact_email = input('Email: ')
  contact_favorite = input('S para sim / N para Não: ')
  
  contacts.append({
    'id': len(contacts) + 1,
    'contact_name': contact_name,
    'contact_phone': contact_phone,
    'contact_email': contact_email,
    'contact_favorite': True if contact_favorite == 'S' else False
  })
  
  print(f'O contato {contact_name} foi adicionado com sucesso!')

def showContacts():
  for contact in contacts:
    print(f'---- {contact['contact_name']} ----')
    print(f'Nome: {contact['contact_name']}')
    print(f'Telefone: {contact['contact_phone']}')
    print(f'Email: {contact['contact_email']}')
    print(f'Favorito: {'Sim' if  contact['contact_favorite'] == True else 'False'}')
    print('------------------------------------')

def editContact():
  print('')
  
while True:
  for choice in choices:
    print(choice)
    
  choice = input('Digite sua escolha: ')

  if(choice == '1'):
    addContact()

  elif(choice == '2'):
    showContacts()    

  elif(choice == '3'):
    print('choice 3')

  elif(choice == '4'):
    print('choice 4')

  elif(choice == '5'):
    print('choice 5')

  elif(choice == '6'):
    print('choice 6')

  elif(choice == '7'):
    print('Saindo do sistema...')
    break
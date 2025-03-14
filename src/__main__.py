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
  selected_contact_id = int(input('Digite o Id do contato que deseja editar: '))
  
  contact_to_edit = None
  for contact in contacts:
    if contact['id'] == selected_contact_id:
      contact_to_edit = contact
      break
  
  if contact_to_edit is None:
    print('Contato não encontrado!')
    return

  print('''
    1 - Nome
    2 - Telefone
    3 - Email
    4 - Marcar/Desmarcar como favorito
  ''')

  selected_edit_option = input('Digite a opção que deseja editar: ')

  if(selected_edit_option == '1'):
    new_name = input('Digite o novo nome: ')
    contact_to_edit['contact_name'] = new_name
  
  if(selected_edit_option == '2'):
    new_phone = input('Digite o novo telefone: ')
    contact_to_edit['contact_phone'] = new_phone

  if(selected_edit_option == '3'):
    new_email = input('Digite o novo email: ')
    contact_to_edit['contact_email'] = new_email
    
  if(selected_edit_option == '4'):
    new_favorite = input('Digite S para favoritar ou N para desfavoritar: ')
    contact_to_edit['contact_favorite'] = True if new_favorite == 'S' else False
  
  print(f'O contato {contact_to_edit['contact_name']} foi editado com sucesso!')

def makeFavorite():
  selected_contact_id = int(input('Digite o Id do contato que deseja favoritar: '))
  
  contact_to_favorite = None
  for contact in contacts:
    if contact['id'] == selected_contact_id:
      contact_to_favorite = contact
      break
  
  if contact_to_favorite is None:
    print('Contato não encontrado!')
    return
  
  contact_to_favorite['contact_favorite'] = True
  print(f'O contato {contact_to_favorite['contact_name']} foi favoritado com sucesso!')

def getFavorites():
  favorites = []
  for contact in contacts:
    if contact['contact_favorite']:
      favorites.append(contact)
  
  for favorite in favorites:
    print(f'---- {favorite['contact_name']} ----')
    print(f'Nome: {favorite['contact_name']}')
    print(f'Telefone: {favorite['contact_phone']}')
    print(f'Email: {favorite['contact_email']}')
    print(f'Favorito: {'Sim' if  favorite['contact_favorite'] == True else 'False'}')
    print('------------------------------------')

def deleteContact():
  selected_contact_id = int(input('Digite o Id do contato que deseja apagar: '))
  
  contact_to_delete = None
  for contact in contacts:
    if contact['id'] == selected_contact_id:
      contact_to_delete = contact
      break
  
  if contact_to_delete is None:
    print('Contato não encontrado!')
    return
  
  contacts.remove(contact_to_delete)
  print(f'O contato {contact_to_delete['contact_name']} foi apagado com sucesso!')


while True:
  print('''
    1 - Adicionar Contato
    2 - Visualizar Contatos
    3 - Editar Contato
    4 - Marcar contato como favorito
    5 - Ver Favoritos
    6 - Apagar Contato
    7 - Sair
  ''')
    
  choice = input('Digite sua escolha: ')

  if(choice == '1'):
    addContact()

  elif(choice == '2'):
    showContacts()    

  elif(choice == '3'):
    editContact()

  elif(choice == '4'):
    makeFavorite()

  elif(choice == '5'):
    getFavorites()

  elif(choice == '6'):
    deleteContact()

  elif(choice == '7'):
    print('Saindo do sistema...')
    break
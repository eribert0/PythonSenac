class Usuario():

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        #self.email = str
        
    def validar_senha(self):
        while True:
            try:
                if len(self.senha) < 8:
                    raise ValueError('Senha deve ter pelo menos 8 caracteres')
                elif not any(c.isupper() for c in self.senha):
                    raise ValueError('Senha deve conter pelo menos uma letra maiúscula')
                elif not any(c.isdigit() for c in self.senha):
                    raise ValueError('Senha deve conter pelo menos um número')
                else:
                    print('Senha válida')
                    break
                    #self.senha = input('Digite uma senha de fácil memorização: ')
            except ValueError as e:
                print(f'Error! {e}')
                self.senha = input('Digite novamente: ')

u = Usuario(login=input('Login: '), senha=input('Senha: '))
u.validar_senha()

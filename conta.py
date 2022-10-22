class Conta:

    def __init__(self, numero, titular, saldo, limite):

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def saque(self, valor):

        valor_a_sacar = self.__saldo_insuficiente(valor)
        self.__saldo -= valor_a_sacar

    def depositar(self, valor):

        valor_a_depositar = self.__deposito_nulo(valor)
        self.__saldo += valor_a_depositar

    def transferir(self, valor, conta_destino):

        if self == conta_destino:
            print("Não é possivel transferir um valor para a mesma conta")
        else:
            self.saque(valor)
            conta_destino.depositar(valor)

    def __saldo_insuficiente(self, valor):
        saldo_insuficiente = (valor > self.__saldo)

        while saldo_insuficiente:

            novo_valor = int(input(f"Saldo Insuficiente. Insira um valor válido."))

            pode_sacar = (novo_valor <= self.__saldo)

            if pode_sacar:
                saldo_insuficiente = False
            valor = novo_valor

        return valor

    def __deposito_nulo(self, valor):
        deposito_nulo = (valor <= 0)

        while deposito_nulo:

            novo_valor = int(input(f"Quantia Negativa. Insira um valor válido."))
            valor_valido = (novo_valor > 0)
            if valor_valido:
                deposito_nulo = False
            valor = novo_valor

        return valor

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigo_bancos():
        return {"BB": "001", "Caixa": "104", "Nubank": "260"}

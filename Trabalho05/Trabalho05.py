from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def getNome(self):
        return self.__nome

    def getTelefone(self):
        return self.__telefone

    @abstractmethod
    def getSalario(self):
        pass

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__valorPorHora = valorPorHora
        self.__horasTrabalhadas = horasTrabalhadas

    def setvalorPorHora(self, valorPorHora):
        self.__valorPorHora = valorPorHora 

    def getvalorPorHora(self):
        return self.__salarioHora

    def getSalario(self):
        return self.__valorPorHora * self.__horasTrabalhadas

class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, salario):
        super().__init__(nome, telefone)
        self.__salario = salario
        self.__diasTrabalhados= diasTrabalhados

    def setSalario(self, salario):
        self.__salario = salario

    def getSalario(self):
        return self.__salario * self.__diasTrabalhados

class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, salario):
        super().__init__(nome, telefone)
        self.__salario = salario

    def setSalario(self, salario):
        self.__salario = salario 

    def getSalario(self):
        return self.__salario

if __name__ == "__main__":
    empregada1 = Horista('Joao', 88, 160, 10)
    empregada2 = Diarista('Paulo', 99, 20, 55)
    empregada3 = Mensalista('Ana', 777, 1000)
    empregadas = [empregada1, empregada2, empregada3]
    for emp in empregadas:
        print ('Nome: {} - Salário: {} - Telefone: {}'.format(emp.getNome(), emp.getSalario(), emp.getTelefone()))
    x=empregada1
    for emp in empregadas:
        if x.getSalario() > emp.getSalario():
            x=emp
    print()
    print ('Mais barato: Nome: {} - Salário: {} - Telefone: {}'.format(x.getNome(), x.getSalario(), x.getTelefone()))
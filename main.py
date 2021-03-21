#Не обязательно вводить большие буквы в последовательностях ДНК или РНК, при инициализации объекта все буквы станут заглавными.
#Пусть будут два полноценных класса ДНК и РНК (поговаривают, наследоваться плохо).

class DNA:
    type = 'DNA'
    iter = 0
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.length = len(sequence)

    def __eq__(self, other):
        if self.sequence == other.sequence:
            return True
        else:
            return False


    def gc_content(self):
        return (self.sequence.count('G') + self.sequence.count('C'))/self.length

    def reverse_complement(self):
        reverse = self.sequence
        reverse = reverse.lower()
        reverse = reverse.replace('a', 'T')
        reverse = reverse.replace('t', 'A')
        reverse = reverse.replace('c', 'G')
        reverse = reverse.replace('g', 'C')
        return reverse[::-1]

    def next(self):
        self.iter += 1
        return self.sequence[self.iter-1]

    def transcribe(self):
        seq = self.sequence.replace('T', 'U')
        return RNA(seq)


class RNA:
    type = 'RNA'
    iter = 0

    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.length = len(sequence)

    def __eq__(self, other):
        if self.sequence == other.sequence:
            return True
        else:
            return False


    def gc_content(self):
        return (self.sequence.count('G') + self.sequence.count('C'))/self.length

    def reverse_complement(self):
        reverse = self.sequence
        reverse = reverse.lower()
        reverse = reverse.replace('a', 'U')
        reverse = reverse.replace('u', 'A')
        reverse = reverse.replace('c', 'G')
        reverse = reverse.replace('g', 'C')
        return reverse[::-1]

    def next(self):
        self.iter += 1
        return self.sequence[self.iter-1]



#ПРИМЕР РАБОТЫ ПРОГРАММЫ НА МОИХ ДАННЫХ:
Seq1 = DNA('ATGcAAAAAAAAAAAAAaTGgggTG')
print('Your sequence is:', Seq1.sequence, 'It is ', Seq1.type)
print('GC content:', Seq1.gc_content())
print('Your sequence length is: ', Seq1.length)
print('Reverse complement: ', Seq1.reverse_complement())

#Можно итерироваться через функцию next:
print('Current letter (iterable): ', Seq1.next())
print('Current letter (iterable): ', Seq1.next())

#Можно сравнить 2 объекта на равенство. Они будут равны, если равны их последовательности (когда все буквы станут заглавными):
#Example2 отличается от Seq1 только регистром букв, поэтому последовательности равны, в отличие от Example1, здесь не равны.
Example1 = DNA('TTTT')
Example2 = DNA('atGcAAAAAAAaAAaAAaTGgggTG')
print(Example1.__eq__(Example2))
print(Example2.__eq__(Seq1))

#Можно создать объект класса РНК по ДНК:
my_RNA = Seq1.transcribe()
print('Type:', my_RNA.type)
print('Sequence: ', my_RNA.sequence)
print('GC content:', my_RNA.gc_content())
print('Reverse complement: ', my_RNA.reverse_complement())
print('Current letter (iterable): ', my_RNA.next())
print('Current letter (iterable): ', my_RNA.next())
print('Current letter (iterable): ', my_RNA.next())

#Можно создать два объекта типа РНК и проверить равенство:
Example3 = RNA('UATA')
Example4 = RNA('UAta')
print(Example3.__eq__(Example4))

#Можно проверять на равенство объект ДНК и другой объект РНК (очевидно, чаще будет False из-за U и T, но в случае, если этих букв нет, будем считать True)
tricky_RNA = RNA('AAAGC')
tricky_DNA = DNA('aaagc')
print(tricky_RNA.__eq__(tricky_DNA))
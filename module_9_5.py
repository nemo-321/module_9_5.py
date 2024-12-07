#  Этот класс наследуется от встроенного исключения ValueError. Он используется для создания пользовательского
#  исключения, которое будет вызываться, когда шаг итератора равен 0.
class StepValueError(ValueError):
    pass
#  Этот класс реализует пользовательский итератор с параметрами начало, конец и шаг.
class Iterator():
#  Конструктор класса, который инициализирует атрибуты:
#  start: начальное значение.
#  stop: конечное значение.
#  step: шаг итерации, по умолчанию равен 1.
#  Если step равен 0, выбрасывается исключение StepValueError.
    def __init__(self,start,stop,step=1):
        if step==0:
            raise StepValueError('шаг не может быть равен 0')
        self.start=start
        self.stop=stop
        self.step=step
        self.pointer=start
#  Метод __iter__:
#  Этот метод делает объект итератором. Он сбрасывает указатель (`pointer`) на значение start и возвращает сам объект
#  итератора для использования в циклах.
    def __iter__(self):
        self.pointer=self.start
        return self
#  Метод __next__:
#  Позволяет получать следующее значение в итерации.Он проверяет, не вышел ли указатель за пределы (`stop`).
#  Если вышел, вызывается исключение StopIteration, что завершает цикл.
#  Если указатель в пределах диапазона, возвращается текущее значение, и указатель увеличивается на шаг.
    def __next__(self):
        if (self.step>0 and  self.pointer>self.stop or self.step<0 and  self.pointer<self.stop):
            raise StopIteration
        current =  self.pointer
        self.pointer +=  self.step
        return current
# Пример выполнения
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
            print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()






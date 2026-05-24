## Indirect Enum

Enumeration (Enum) определяет общий тип для группы [связанных значений (associate value)](./Enumeration.md) и позволяет вам работать с этими значениями типобезопасным способом в вашем коде. Иногда нам также нужно иметь ассоциированные значения (`name: String`):

```swift
enum FileSystemItem {
    case file(name: String)
}
```

### Что произойдет, если мы попытаемся указать в ассоциированном значении само рекурсивное наше перечисление?

```swift
enum FileSystemItem {
    case file(name: String)
    case folder(name: String, items: FileSystemItem)
}
```

❗❗❗ Ошибка компилятора: `Recursive enum ‘%EnumName’ is not marked ‘indirect’`

```swift
struct Woman {
    var name: String
    var friend: Woman?
}
```

❗❗❗ Ошибка компилятора: `Value type 'Woman' cannot have a stored property that recursively contains it`

### Почему value тип не может быть рекурсивным?

[Перечисления](./Enumeration.md) — это [типы значений](/5%20Swift/5.3%20DataRepresentations/5.3.1%20DataTypes/5.3.1.4%20ValueTypes/), которые по специфики управления [памятью Apple](/3%20Memory%20and%20Concurrency/3.1%20Memory/3.1.1%20AboutMemory/3.1.1.1%20Memory.md) должны быть определены **во время компиляции**. То есть необходимо точно знать, сколько ячеек памяти нам нужно выделить для каждого экземпляра, хранящегося в [стеке](/3%20Memory%20and%20Concurrency/3.1%20Memory/3.1.2%20RandomAccessMemory/3.1.2.2%20Stack.md). 

Определяя внутри одного объекта типа значения тот же объект типа значения, мы создаем [рекурсию](https://github.com/eldaroid/iTWiki/blob/master/2%20ComputerScience/2.2%20Languages/2.2.2%20Paradigm/2.2.2.1%20Declarative/2.2.2.1.1%20FunctionalProgramming(FP).md#рекурсия), в которой невозможно понять, сколько памяти нужно для выделить такого объекта. Фактически, выводится еще одна проблема: мы не можем определить свойство типа A внутри структуры A.

---

Вернемся к нашей проблеме и попробуем выяснить, как Swift работает с перечислениями [связанных значений](./Enumeration.md) и почему возникает проблема:

* Enum Swift объект будет иметь только один случай, назначенный самому себе (невозможно назначить два значения одновременно);
* Затем компилятор проверяет, какой случай перечисления займет максимальный объем памяти;
* Теперь экземпляр enum будет иметь необходимую память плюс некоторую статическую память для отслеживания текущей выбранной позиции из enum (называется это активный случай);

**Ответ:** Если бы value типы были бы рекурсивными, это привело бы к бесконечной вложенности и, как следствие, к ошибкам в вычислении размера памяти.

> ❗ С reference типами нет такой проблемы, тк они вычислиются на этапе runtime

### Решение рекурсии - Indirect/UnsafePointer

`Indirect` модифицирует способ хранения перечислений в Swift, чтобы они могли расти до любого размера

```swift
enum FileSystemItem {
    case file(name: String)
    indirect case folder(name: String, items: FileSystemItem) // implicit pointer on FileSystemItem
}
```

или

```swift
indirect enum FileSystemItem {
    case file(name: String)
    case folder(name: String, items: FileSystemItem) // implicit pointer on FileSystemItem
}
```

или

```swift
enum FileSystemItem<Element> {
 final class FileSystemFolder {
    let element: Element
    init(element: Element) {
      self.element = element
    }
  }
  case end
  case node(FileSystemFolder)
}
```

Для структур можно использовать указатель, что фактически делает то же самое что и indirect:

```swift
struct FileSystemItem {
    let folder: UnsafePointer<FileSystemItem>
}
```

### Что происходит, когда мы указываем indirect модификатор объявления?

Объяснение достаточно простое: Indirect указывает компилятору хранить данные **enum за указателем**. То есть, для хранения ссылки в стеке выделяется статический размер памяти, но содержимое (как я предполагаю) хранится в куче. Таким образом, после этих оптимизаций нет необходимости делать экземпляр Enum достаточно большим, чтобы вместить все данные.

> В 64 битной системе переменная `folder` становится указателем фиксированного размера - занимает 8 байт (в 1 байте 8 бит => 8 * 8 = 64). Независимо от того, что он содержит или на что указывает

### Семантика value типа

Нужно понимать, что семантика для indirect enum не меняется и она остается value типом по самой семантике:

```swift
indirect enum FileSystemItem {
    case root
    case file(name: String)
    // implicit(неявный) pointer on FileSystemItem
    case folder(name: String, items: FileSystemItem)
}

var file1 = FileSystemItem.file(name: "file2")
var file2 = FileSystemItem.folder(name: "name", items: file1)
file1 = FileSystemItem.root

switch file2 {
case .folder(_, let items):
    // file(name: "file2")
    // если бы была reference семантика - вывод root
    print(items) 
default:
    print("Не папка или папка пустая")
}
```

### Рекурсия в массиве?

Следующий код не выдаст ошибки:

```swift
enum FileSystemItem {
    case file(name: String)
    case folder(name: String, items: [FileSystemItem])
}
```


* Array<T> имеет fixed-size struct with [pointer to a buffer](https://github.com/swiftlang/swift/blob/main/stdlib/public/core/Array.swift#L310), который хранит элементы массива *последовательно (непрерывно)* в памяти
    * Непрерывность только в случае собственных массивов Swift [не преобразованных из Objective-C]. NSArray Экземпляры не гарантируют, что их базовое хранилище является непрерывным.

Поэтому размер array<T> не меняется с количеством хранимых элементов (его размер - это просто размер указателя на буфер) => можно посчитать размер при компиляции.

### Оптимизация по памяти

```swift
enum MyEnum {
  // MemoryLayout<MyEnum>.size // for a type
  // 8 byte
  indirect case bigCase (Int, Int, Int, Int, Int)
}
```


```swift
enum MyEnum {
 // MemoryLayout<MyEnum>.size
  // 40 byte
  case bigCase (Int, Int, Int, Int, Int)
} 
```

---

[Enumeration Theme](./Enumeration.md) | [Back To iTWiki Contents](https://github.com/eldaroid/iTWiki) | [Optiona Theme](./Optional.md)
# Optional

1. :heavy_check_mark: [100 Days of SwiftUI. Day 12](https://www.hackingwithswift.com/100/swiftui/12)
2. :heavy_check_mark: [Unwrapping optionals](https://www.hackingwithswift.com/sixty/10/2/unwrapping-optionals)

## Что такое optional и какие проблемы они решают?

Optional позволяет переменной любого типа представить ситуацию "отсутствие значения". В Objective-C «отсутствие значения» было доступно только в ссылочных типах с использованием специального значения nil. У типов-значений (value types), вроде int или float, такой возможности не было.
Swift расширил концепцию «отсутствия значения» на типы-значения. Переменная optional может содержать либо значение, либо nil, сигнализирующее об отсутствии значения.
 
> Optional Swift фактически реализуются с использованием перечислений (enums - вещи, которые имеют дискретный набор значений). В swift перечисления для каждого дискретного значения (case) могут иметь ассоциированные значениям ([associated values](/5%20Swift/5.2%20Glossary.md#:~:text=Associated%20values)). Enum optional имеет два значения: [none](/5%20Swift/5.5%20AbstractMechanism/5.5.4%20AnyvsSome.md) и [some](/5%20Swift/5.5%20AbstractMechanism/5.5.4%20AnyvsSome.md), у `some` есть значение, указанное внутри необязательного.


## Изобретение NULL

Нулевые ссылки - буквально, когда переменная не имеет значения - были изобретены Тони Хоар еще в 1965 году при разработке ALGOL. 

> Сэр Чарльз Энтони Ричард Хоар (Тони Хоар) наиболее известен за алгоритмы QuickSort

Проверка типов в массивах и определение того, что там нет ошибок - трудоемко в плане производительности, поэтому было принято решение костылить Null. Он ускорял работу, избавлял программу от проверок, уменьшал ее размер, но приводил к проверкам на Null.

Когда его спросили о нем в ретроспективе, он сказал: **«Я называю это своей ошибкой на миллиард долларов»**, потому что они приводят к очень большому количеству проблем.

## В чём разница между NaN, Null, nil и .none?

* `None` - Нет никакой разницы, Optional.none (кратко .none) и nil эквивалентны.
Фактически, следующий оператор вернёт true: `nil == .none`
  * `Nil` (alias для `.none`) - В swift `nil` всегда означает `not set`. Optional имеет 2 состояния: set (установлен) и not set (не установлен) - nil
    > Использование nil более общепринято и рекомендовано

* `NaN` - это `not a number` или несуществующее число. Получается, когда бесконечность делим на бесконечность или извлекаем корень из отрицательного числа.

* В большинстве ЯП `NULL` - это нулевой указатель

## Подходы к созданию Null

![](/pictures/Swift/Un:TaggedUnions.jpg?raw=true)

## Почему мы можем применять optional ко всем типам?

Ответ: [ассоциативное значение (associated value)](./Enumeration.md) в enum! Не путать с [associated type в Protocol (PATs)](/5%20Swift/5.4%20Protocol/5.4.2%20AssociatedTypes.md)

# Развертывание опционала

[Подробнее почитать про это. -> Beginner-> устный вопрос -> 5](https://habr.com/ru/post/449410/)

**Всего 7 способов развернуть optional.**

1)_Принудительное развёртывание (**forced unwrapping**) — небезопасно.

1. :heavy_check_mark: [Force unwrapping](https://www.hackingwithswift.com/sixty/10/4/force-unwrapping)
2. :heavy_check_mark: [Когда следует принудительно развернуть опции в Swift?](https://www.hackingwithswift.com/quick-start/understanding-swift/when-should-you-force-unwrap-optionals-in-swift)
3. :negative_squared_cross_mark: [Swift: Banning force unwrapping optionals](https://blog.timac.org/2017/0628-swift-banning-force-unwrapping-optionals/)
```swift
let a: String = x!
```

2)_Неявное развертывание (**implicitly unwrapped optional**) — небезопасно.

1. :heavy_check_mark: [Implicitly unwrapped optionals](https://www.hackingwithswift.com/sixty/10/5/implicitly-unwrapped-optionals)
2. :heavy_check_mark: [Why does Swift need both implicitly unwrapped optionals and regular optionals?](https://www.hackingwithswift.com/quick-start/understanding-swift/why-does-swift-need-both-implicitly-unwrapped-optionals-and-regular-optionals)

```swift
var a = x!
--или--
var a: Int! = nil
```

3)_**Optional chaining** — безопасно.

1. :heavy_check_mark: [Optional chaining](https://www.hackingwithswift.com/sixty/10/7/optional-chaining)
2. :heavy_check_mark: [Why is optional chaining so important?](https://www.hackingwithswift.com/quick-start/understanding-swift/why-is-optional-chaining-so-important)

```swift
let names = ["John", "Paul", "George", "Ringo"]
let beatle = names.first?.uppercased()
```

`first` вернет первое имя массива если оно есть или вернет nil. Если она вернет nil, то Swift не будет пытаться использовать `uppercased()` и сразу установит `beatle` = nil

4)_**Optional binding** — безопасно.
```swift
if let a = x {
  print("x was successfully unwrapped and is = \(a)")
}
```

Но это не то же самое, что и:

```swift
func yearAlbumReleased(name: String) -> Int? {
    if name == "Red" { return 2012 } else { return nil }
}

var year = yearAlbumReleased(name: "Red")

if year == nil {
    print("There was an error")
} else {
    print("It was released in \(year)") 
    // "It was released in Optional(2012)", потому что это не то же саме что и if let year = year { print("There wasn't an error") }
    // можно сделать print("It was released in \(year!)"), чтобы вывод был таким, как нам нужно
}
```

> x обязательно должен быть опционалом. x: String - ошибка компиляции, x: String? - корректно


5)_Оператор **Guard** — безопасно.

1. :heavy_check_mark: [Unwrapping with guard](https://www.hackingwithswift.com/sixty/10/3/unwrapping-with-guard)
```swift
guard let a = x else {
  return
}
```
> Альтернатива if let - это guard let, которая также разворачивает опционалы. Отличия: 
> 1) guard let развертывает элемент с использованием return, который означает, что вы выйдете из функции, цикла или условия, в котором вы его использовали если развернуть не удалось. 
> 2) развернутый необязательный параметр остается пригодным для использования после guard кода.

6)_**Nil coalescing operator** — безопасно.

1. :heavy_check_mark: [Nil coalescing](https://www.hackingwithswift.com/sixty/10/6/nil-coalescing)
2. :heavy_check_mark: [When should you use nil coalescing in Swift?](https://www.hackingwithswift.com/quick-start/understanding-swift/when-should-you-use-nil-coalescing-in-swift)

```swift
let a = first() ?? second() ?? ""
```

Это запустит first(), и если это вернет nil, попытается запустить second(), и если это вернет nil, тогда будет использоваться пустая строка.

> Чтение ключа словаря всегда будет возвращать nil если такого ключа нет, поэтому вы можете использовать здесь nil coalescing:

```swift
let scores = ["Picard": 800, "Data": 7000, "Troi": 900]
let crusherScore = scores["Crusher"] ?? 0
--или--
let crusherScore = scores["Crusher", default: 0]
```

7)_**Optional pattern** — безопасно.
```swift
if case let a? = x {
  print(a)
}
```

---

[Indirect Enum Theme](./IndirectEnum.md)) | [Back To iTWiki Contents](https://github.com/eldaroid/iTWiki) | [5.3.1.4.4 Collections And Tuple Theme Folder](../5.3.1.4.4%20CollectionsAndTuple/)
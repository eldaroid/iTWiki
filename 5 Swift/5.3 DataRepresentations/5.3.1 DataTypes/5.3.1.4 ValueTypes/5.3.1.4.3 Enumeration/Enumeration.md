## Enumeration (enum) - перечисления

## Типы перечислений (либо один тип, либо другой)

* **with raw value** - enum в котором каждый случай имеет заранее определенное необработанное значение;

Пример: 
```swift
enum withRawValue: String {
    case iosProgramming
    case kotlinProgramming
    // или
    case ios = "iosProgramming"
    case kotlin = "kotlinProgramming"
}
```

* **with associated value** - это перечисление, в котором каждый случай имеет ассоциированное с ним значение;

Пример: 
```swift
enum withAssociateValue {
    case iosProgramming(version: Int)
    case kotlinProgramming(version: Int)
}
```

### Пользовательские операторы (infix, prefix, postfix operator)

Пользовательские операторы перечисления могут быть полезными для улучшения читаемости и удобства вашего кода. Давайте рассмотрим подробные примеры пользовательских операторов перечисления.

Оператор для сравнения приоритетов задач:
Допустим, у вас есть перечисление TaskPriority, которое представляет разные приоритеты задач:

```swift
enum TaskPriority {
    case low
    case medium
    case high
}
```

Вы можете добавить пользовательский оператор для сравнения приоритетов задач:

```swift
infix operator <<<

func <<< (lhs: TaskPriority, rhs: TaskPriority) -> Bool {
    switch (lhs, rhs) {
    case (.low, .medium), (.low, .high), (.medium, .high):
        return true
    default:
        return false
    }
}

let lowPriority = TaskPriority.low
let mediumPriority = TaskPriority.medium
let highPriority = TaskPriority.high

if lowPriority <<< mediumPriority {
    print("Low priority меньше чем Medium priority")
}

//Вывод: Low priority меньше чем Medium priority
```

В этом примере мы определили пользовательский оператор `<`, который сравнивает приоритеты задач и возвращает `true`, если левый приоритет меньше правого. Это делает код более читаемым и позволяет использовать оператор `<` для сравнения приоритетов задач.

Оператор для объединения имен файлов:
Предположим, у вас есть перечисление `File`, которое представляет файлы, и вы хотите объединить их имена с помощью оператора `+`:


### Использование associatedtype с ассоциированными значениями


# TODO: https://habr.com/ru/articles/759842/

---

[5.3.1.4.3 Enumeration Theme Folder](../5.3.1.4.3%20Enumeration/) | [Back To iTWiki Contents](https://github.com/eldaroid/iTWiki) | [Indirect Enum Theme](./IndirectEnum.md)
## Dependency injection and Dependency inversion?

1. [Difference between dependency injection and dependency inversion?](https://github.com/sashakid/ios-guide/blob/master/Main/6_architecture.md#difference-between-dependency-injection-and-dependency-inversion)

## Принцип [Dependency inversion из SOLID](./SOLID.md)

Модули верхних уровней не должны зависеть от деталей нижнего уровня. А оба этих уровней должны зависеть от деталей абстракций. 

Позволяет отвязаться от конкретной реализации благодаря [интерфейсу (протоколы)](/5%20Swift/5.4%20Protocol/5.4.1%20Protocol.md)/[дженерику](/5%20Swift/5.5%20AbstractMechanism/5.5.1%20Generics.md).

## Dependency injection

Dependency Injection — это способ реализации [Dependency Inversion из SOLID](./SOLID.md). Это про внедрение зависимостей в объект.

* [SwinJect](https://github.com/Swinject/Swinject);
* [Needle](https://github.com/uber/needle) от uber;
* [DIP](https://github.com/AliSoftware/Dip);

 ---

[2.4.3 Design Pattern Theme](../2.4.1.3%20DesignPattern/) | [Back To iTWiki Contents](https://github.com/eldaroid/iTWiki) | [DRY Design Principle Theme](./DRY.md)

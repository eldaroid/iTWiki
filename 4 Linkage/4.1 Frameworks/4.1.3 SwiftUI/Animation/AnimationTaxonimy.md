# Animation

1. [Основы анимации SwiftUI](https://medium.com/simform-engineering/basics-of-swift-ui-animations-d1aa2485a5d9)
2. [Explore SwiftUI animation](https://developer.apple.com/videos/play/wwdc2023/10156/)



Типы анимации:

<div style="text-align: center;">
    <img src="https://github.com/eldaroid/pictures/blob/master/iTWiki/Frameworks/SwiftUI/Animation/TypesOfAnimation.jpeg?raw=true" alt="Описание изображения" style="width: 50%; height: auto;">
</div>

* Explicit Animation (Явная анимация) = `withAnimation`;

    Определяется с помощью замыкания `withAnimation {…}` , и анимироваться будут только значения параметров, измененные внутри фигурных скобок. По сути, здесь мы явно просим SwiftUI анимировать изменения, происходящие в результате изменения состояния.

* Implicit Animation (Неявная анимация);

    Cамый быстрый способ реализовать обзоры анимации. Это самый простой вид анимации в SwiftUI, и модификатор используется для любых изменений, происходящих внутри представления (которые поддерживают эту анимацию: offset, opacity, scaleEffect, rotationEffect, frame, color, border, shadow, gradient).




[Согласно эплу](https://developer.apple.com/videos/play/wwdc2023/10156/), существую типы анимации:

![](https://github.com/eldaroid/pictures/blob/master/iTWiki/Frameworks/SwiftUI/Animation/AnimationStyles.png?raw=true)

* Timing curve (по дефолту duration=0.35сек.): 
    * default 
    * linear
    * easeIn - начинается медленно и ускоряется по мере приближения к концу
    * easeOut - начинается быстро и замедляется по мере приближения к концу последовательности
    * easeInOut - начинается медленно, затем ускоряется, а затем снова замедляется

* Spring (эффект пружины)
    * default spring

    * smooth // нет отскока (no bounce)
        ![](https://github.com/eldaroid/pictures/blob/master/iTWiki/Frameworks/SwiftUI/Animation/smooth.png?raw=true)
    
    * snappy // маленький отскок (small bounce)
        ![](https://github.com/eldaroid/pictures/blob/master/iTWiki/Frameworks/SwiftUI/Animation/snappy.png?raw=true)
    
    * bouncy // средний отскок (medium bounce)
        ![](https://github.com/eldaroid/pictures/blob/master/iTWiki/Frameworks/SwiftUI/Animation/bounce.png?raw=true)
    
    * [interpolating](/5%20Swift/5.2%20Glossary.md#экстраполяцияинтерполяция) spring - запуская анимацию несколько раз, эффект пружины будет становиться все сильнее и сильнее по мере объединения пружин

* [Higher order](/2%20ComputerScience/2.2%20Languages/2.2.2%20Paradigm/2.2.2.1%20Declarative/2.2.2.1.1%20FunctionalProgramming(FP).md): 
    * speed
    * delay
    * repeatCount



Просмотр демонстрации: [Project](./AnimationProject/)

----
# MVVM [Model-View-ViewModel](https://www.toptal.com/ios/swift-tutorial-introduction-to-mvvm#:~:text=MVVM%20To%20the%20Rescue) (представлен Microsoft в 2005г.)

1. [Modern MVVM iOS App Architecture with Combine and SwiftUI](https://www.vadimbulavin.com/modern-mvvm-ios-app-architecture-with-combine-and-swiftui/)
2. [Model View ViewModel (MVVM)](https://daddycoding.com/2021/06/10/model-view-viewmodel-mvvm/)

Наверняка вы уже успели столкнуться с тем, что ViewController в паттерне MVC принимает много обязанностей и начинает "разбухать", так как на него взваливается слишком много работы. Паттерн MVVM, который пришла на помощь "разбухающему" MVC.

Наш Controller присоединяется к View:

![alt text](https://github.com/eldaroid/pictures/blob/master/Swift/MVVM.jpg?raw=true)

Появляется ViewModel:

![alt text](https://github.com/eldaroid/pictures/blob/master/Swift/MVVM2.jpg?raw=true)

Наш Controller становится единым центром с View:

![alt text](https://github.com/eldaroid/pictures/blob/master/Swift/MVVM3.jpg?raw=true)

Таким образом, View (controller) содержит ViewModel, а ViewModel содержит Model(Domain).

---

[MVC UIPattern  Theme](./MVC.md) | [Back To iTWiki Contents](https://github.com/eldaroid/iTWiki) | [VIP Theme](./VIP.md)

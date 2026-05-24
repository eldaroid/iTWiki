## Property Wrapper

1. [All SwiftUI property wrappers explained and compared](https://www.hackingwithswift.com/quick-start/swiftui/all-swiftui-property-wrappers-explained-and-compared)

Property Wrapper (“Обертка Свойства”) — это просто структура struct, в которую встроен некоторый шаблон “поведения” переменной var, которую эта структура struct “оборачивает”. Реализация [дизайн паттерна](/2%20ComputerScience/2.4%20Architecture/2.4.1%20PatternsAndPrinciple/2.4.1.3%20DesignPattern/2.4.1.3.1%20ListOfDesignPattern.md) - [декоратора](/2%20ComputerScience/2.4%20Architecture/2.4.1%20PatternsAndPrinciple/2.4.1.3%20DesignPattern/2.4.1.3.4%20Structural/Decorator.md).

> Благодаря этому мы наконец-то поймем, что такие вещи как @State, @StateObject, @Published, @ObservedObject и другие @штуковины делают под «капотом»


![PropertyWrappers](https://raw.githubusercontent.com/eldaroid/pictures/master/iTWiki/Frameworks/SwiftUI/PropertyWrappers.jpg)

Список 17ти SwiftUI Property Wrappers:

* [@AppStorage](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-appstorage-property-wrapper) читает и записывает значения из UserDefaults;

* [@Binding](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-binding-property-wrapper) относится к данным типа значения, принадлежащим другому представлению. Локальное изменение привязки также изменяет удаленные данные;

* [@Environment](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-environment-property-wrapper) позволяет нам считывать данные из системы, такие как цветовая схема, параметры доступности и коллекции черт, но вы можете добавить сюда свои собственные ключи, если хотите;

* [@EnvironmentObjecе](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-environmentobject-property-wrapper) читает общий объект, который мы поместили в среду;

* [@FetchRequest](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-fetchrequest-property-wrapper) запускает запрос на получение основных данных для определенного объекта;

* @FocusedBinding предназначен для наблюдения за значениями в ключевом окне, например, в текстовом поле, которое выбрано в данный момент;

* @FocusedValue является более простой версией, @FocusedBindingкоторая не разворачивает связанное значение для вас;

* [@GestureState](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-gesturestate-property-wrapper) хранит значения, связанные с жестом, который в данный момент выполняется, например, насколько далеко вы провели пальцем, за исключением того, что он будет сброшен до значения по умолчанию, когда жест остановится;

* @Namespace создает [пространство имен](/5%20Swift/5.2%20Glossary.md#:~:text=Namespace) анимации, позволяющее совмещать эффекты геометрии, которые могут использоваться другими представлениями;

* @NSApplicationDelegateAdaptor используется для создания и регистрации класса в качестве делегата приложения для приложения macOS;

* [@ObservedObject](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-observedobject-property-wrapper) относится к экземпляру внешнего класса, который соответствует протоколу ObservableObject;

* [@Published](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-published-property-wrapper) прикрепляется к свойствам внутри ObservableObjectи сообщает SwiftUI, что он должен обновлять все представления, использующие это свойство, при его изменении;

* [@ScaledMetric](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-scaledmetric-property-wrapper) считывает настройку динамического типа пользователя и масштабирует числа в большую или меньшую сторону в зависимости от предоставленного вами исходного значения;

* [@SceneStorage](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-scenestorage-property-wrapper) позволяет сохранять и восстанавливать небольшие объемы данных для восстановления состояния;

* [@State](./State.md) позволяет нам манипулировать небольшими объемами данных типа значения локально в представлении. @State заставляет переменную var “жить” в “куче” (heap), делая её writable в View, то есть дает возможность “писать” в нее новые значения в противоположность обычным переменным var в View, которые являются unwritable (только для чтения);

* [@StateObject](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-stateobject-property-wrapper) используется для хранения новых экземпляров данных ссылочного типа, которые соответствуют протоколу ObservableObject;

* [@UIApplicationDelegateAdaptor](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-uiapplicationdelegateadaptor-property-wrapper) используется для создания и регистрации класса в качестве делегата приложения для приложения iOS;


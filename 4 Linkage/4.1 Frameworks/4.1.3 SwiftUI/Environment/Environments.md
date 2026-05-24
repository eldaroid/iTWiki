## Environments

Environment — одна из уникальных функций SwiftU (которой раньше не было в UIKit): набор environment values и environment objects, распространяемые через иерархию представлений.

## Список встроенных environment

Многое из того, что мы делаем в SwiftUI, влияет на среду. Несколько примеров environment values/environment objects:

* **View-specific values**: для стилей представлений ([Button styles](https://www.fivestars.blog/articles/button-styles/), [Customize TextFields](https://www.fivestars.blog/articles/how-to-customize-textfields/), [Custom SwiftUI view styles](https://www.fivestars.blog/articles/custom-view-styles/));
* **Actions**: [OpenURLAction](https://www.fivestars.blog/articles/openurl-openurlaction/), [TriggerSubmitAction](https://www.fivestars.blog/articles/onsubmit/), [DismissAction](https://nilcoalescing.com/blog/UsingTheDismissActionFromTheSwiftUIEnvironment/), DismissAction, RefreshAction, ResetFocusAction;
* [AppDelegate](https://www.fivestars.blog/articles/app-delegate-scene-delegate-swiftui/#:~:text=depending%20on%20both-,delegates,-%3A) и [SceneDelegate](https://www.fivestars.blog/articles/app-delegate-scene-delegate-swiftui/#:~:text=approach%20takes%20priority.-,Scene,-delegate%20access%20via)
* **Generic component values**: controlSize, isEnabled, isFocused, redactionReasons
* **Display values**: calendar, dynamicTypeSize, displayScale, horizontalSizeClass, layoutDirection, locale, pixelLength, timeZone, verticalSizeClass;
* **SF Symbols**: imageScale, symbolVariants, symbolRenderingMode;
* **Search**: isSearching,dismissSearch;
* **Keyboard shortcuts**: keyboardShortcut;
* **Text**: lineLimit, minimumScaleFactor, textCase, disableAutocorrection, font, legibilityWeight, multilineTextAlignment, truncationMode, lineSpacing, allowsTightening;
* **Accessibility**: accessibilityEnabled, accessibilityDifferentiateWithoutColor, accessibilityReduceTransparency, accessibilityReduceMotion, accessibilityInvertColors, accessibilityShowButtonShapes, accessibilityVoiceOverEnabled, accessibilitySwitchControlEnabled;
* **Presentation**: dismiss, isPresented, scenePhase;
* **Colors/Themes**: colorScheme, colorSchemeContrast, backgroundMaterial;
* **Not associated with any view**: managedObjectContext, undoManager;

## Использование Environment

Рассмотрим, как можно использовать систему окружения SwiftUI для передачи различных частей состояния между двумя представлениями, которые не связаны друг с другом напрямую. 

### EnvironmentObject

```swift
struct RootView: View {
    @ObservedObject var theme: Theme

    var body: some View {
        ArticleListView(articles: articles)
            .environmentObject(theme)
    }
}
```

Хотя создать привязки между родительским представлением и одним из его дочерних представлений легко, но проблемно передавать определенный объект или значение в пределах всей иерархии представлений — и та проблема, которую решает environment среда:

```swift
struct ArticleView: View {
    @EnvironmentObject var themeEnvironmentObject: Theme
    var article: Article

    var body: some View {
        VStack(alignment: .leading) {
            Text(article.title)
                .foregroundColor(themeEnvironmentObject.titleTextColor)
            Text(article.body)
                .foregroundColor(themeEnvironmentObject.bodyTextColor)
        }
    }
}
```

Теперь все view внутри могут обращаться к theme по @EnvironmentObject:
```swift
RootView
└── ArticleListView
    └── ArticleView
```

### Environment Value

**Второй способ** использования системы окружения SwiftUI — определение пользовательского типа EnvironmentKey
```swift
struct ThemeEnvironmentKey: EnvironmentKey {
    static var defaultValue = Theme.default
}

extension EnvironmentValues {
    var theme: Theme {
        get { self[ThemeEnvironmentKey.self] }
        set { self[ThemeEnvironmentKey.self] = newValue }
    }
}
```

После выполнения вышеизложенного мы теперь можем пометить themeсвойство нашего представления, используя `Environment` обертку свойства (а не `EnvironmentObject`), и передать [key path](https://www.swiftbysundell.com/articles/the-power-of-key-paths-in-swift/) к ключу среды, для которого мы хотим получить значение:

```swift
struct ArticleView: View {
    @EnvironmentObject var themeEnvironmentObject: Theme
    @Environment(\.theme) var themeEnvironmentValue
    var article: Article

    var body: some View {
        VStack(alignment: .leading) {
            Text(article.title)
                .foregroundColor(themeEnvironmentObject.titleTextColor)
                .foregroundColor(themeEnvironmentValue.titleTextColor)
            Text(article.body)
                .foregroundColor(themeEnvironmentObject.bodyTextColor)
                .foregroundColor(themeEnvironmentValue.bodyTextColor)
        }
    }
}
```


### Проблема с EnvironmentObject

Заметное различие между двумя вышеописанными подходами: 
* EnvironmentValue подход на основе [key path](https://www.swiftbysundell.com/articles/the-power-of-key-paths-in-swift/) требует от нас определения значения по умолчанию во время **компиляции**;
* EnvironmentObject подход предполагает, что такое значение будет предоставлено во время **выполнения** (и неспособность сделать это приведет к сбою);
    > Это ограничивает от повторного использования Subview без раздумий в любом контексте, на любом экране. EnvironmentObject инжектируется в место, которое получит этот объект окружения

![ThemeEnvironmentObject](https://github.com/eldaroid/pictures/blob/master/iTWiki/Frameworks/SwiftUI/themeEnvironmentObject.png?raw=true)



---



Значительным преимуществом использования Environment и отказа от передачи ObservableObject через метод init представления является внутреннее хранилище SwiftUI. SwiftUI хранит Environment в специальной памяти фреймворка за пределами представления. Это дает неявный доступ к Environment , специфичному для представления , для всех дочерних представлений.

---
---

# TBD

!Прочитать про keyPath: https://www.swiftbysundell.com/articles/the-power-of-key-paths-in-swift/

!Прочитать про что выбрать Observed/Environment: https://www.hackingwithswift.com/quick-start/swiftui/how-to-use-environmentobject-to-share-data-between-views


!The SwiftUI Environment: https://www.fivestars.blog/articles/swiftui-environment-propagation/

!Добавить пункты когда про Environments буду писать: https://useyourloaf.com/blog/swiftui-custom-environment-values/

+++ https://www.fivestars.blog/articles/custom-environment-values-cheatsheet/ :: 

[1](https://www.fivestars.blog/articles/swiftui-environment-propagation/), [2](https://www.fivestars.blog/articles/swiftui-environment-propagation-2/), [3](https://www.fivestars.blog/articles/swiftui-environment-propagation-3/), [4](https://www.fivestars.blog/articles/environmentvalues/), [5](https://www.fivestars.blog/articles/how-to-define-environment-values/).

[The power of Environment in SwiftUI](https://swiftwithmajid.com/2019/08/21/the-power-of-environment-in-swiftui/)

---




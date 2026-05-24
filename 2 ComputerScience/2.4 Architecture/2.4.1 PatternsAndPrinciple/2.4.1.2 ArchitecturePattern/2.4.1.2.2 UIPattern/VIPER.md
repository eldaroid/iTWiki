## VIPER

![viper](https://github.com/eldaroid/pictures/blob/master/iTWiki/DesignPatterns/viper.png?raw=true)

* "V", View: displays what it is told to by the Presenter and relays user input back to the Presenter.

* "I", Interactor: contains the business logic as specified by a use case.

* "P", Presenter: contains view logic for preparing content for display (as received from the Interactor) and for reacting to user inputs (by requesting new data from the Interactor).

* "E", Entity: contains basic model objects used by the Interactor.

* "R", Routing: contains navigation logic for describing which screens are shown in which order.


#### [VIP](./VIP.md) vs VIPER

Разница между VIP и VIPER - полярность. VIP - однополярный роутер. VIPER - двух полярный роутер.

![Viper vs VIP](https://github.com/eldaroid/pictures/blob/master/iTWiki/DesignPatterns/vip_vs_viper.png?raw=true)


---

[VIP UIPattern Theme](./VIP.md) | [Back To iTWiki Contents](https://github.com/eldaroid/iTWiki) | [2.4.1.3 Design Pattern Theme Folder](/2%20ComputerScience/2.4%20Architecture/2.4.1%20PatternsAndPrinciple/2.4.1.3%20DesignPattern/)

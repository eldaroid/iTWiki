## VIP

#### VIP vs [VIPER](./VIPER.md)

VIP and VIPER have the same basic components, but the data flow is different. Although VIP follows a unidirectional approach (однополярный роутер), VIPER has a bidirectional (двуполярный презентер) flow that starts with the presenter.

In VIPER, the presenter directs data between the view and the interactor. The view and interactor don’t talk with each other.

![Viper vs VIP](/pictures/DesignPatterns/vip_vs_viper.png?raw=true)

---

[MVVM UIPattern Theme](./MVVM.md) | [Back To iTWiki Contents](https://github.com/eldaroid/iTWiki) | [VIPER Theme](./VIPER.md)

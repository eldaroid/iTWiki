
В университете мы проходили систему координат, которая выглядела так:

![CoordinateSystemInSchool](/pictures/Frameworks/SwiftUI/CoordinateSystemInSchool.jpeg?raw=true)

Apple предлагает разработчикам пользоваться перевернутой (а точнее отраженной) системой координат:

![CoordinateSystemIphone](/pictures/Frameworks/SwiftUI/CoordinateSystemIphone.jpeg?raw=true)

 В ней, левый верхний угол соответствует координатам (0, 0), а правый нижний угол может быть описан координатой (x, y), где x — ширина экрана, а y — его высота. Т.е. движение вниз по координатной сетке соответствует увеличению y. Положительное значение y — это высота вниз. Отсюда следует, что и углы меряются по этой же логике. Угол 90 градусов соответствует направлению вниз, 180 градусов — влево, 270 градусов — вверх.

![Angels](/pictures/Frameworks/SwiftUI/Angels.jpeg?raw=true)

Из примечания 1 следует и то, что понятия “по часовой” и “против часовой” стрелке так же ивертированы вследствии использования отраженной координатной системы. Об этом говорится и в [документации](https://developer.apple.com/documentation/coregraphics/cgcontext/2427129-addarc) к Core Graphics (SwiftUI не более чем надстройка над ней):
> In a flipped coordinate system (the default for UIView drawing methods in iOS), specifying a clockwise arc results in a counterclockwise arc after the transformation is applied.



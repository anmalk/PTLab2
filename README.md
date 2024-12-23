[![Build Status](https://app.travis-ci.com/kpdvstu/PTLab2.svg?branch=master)](https://app.travis-ci.com/kpdvstu/PTLab2)
<h1 align="center">Лабораторная работа №2 по дисциплине "Технологии программирования"</h1>

## Изучение фреймворка MVC

### Цели:
1. Познакомиться c моделью MVC, ее сущностью и основными фреймворками на ее основе.
2. Разобраться с сущностями «модель», «контроллер», «представление», их функциональным
назначением.
3. Получить навыки разработки веб-приложений с использованием MVC-фреймворков.

### Постановка задачи:
1. Выберите для Вашего проекта тип лицензии и добавьте файл с лицензией в проект.
2. Доработайте проект магазина, добавив в него новую функциональность и информацию в базу
данных в соответствии с типом магазина (согласно индивидуальному варианту, см. таблицу). Составьте
модульные тесты к проекту, постарайтесь покрыть тестами максимально возможный объем кода. Для
работы с этим заданием создайте новую ветку кода на основе главной и фиксируйте в нее весь
программный код в процессе разработки. Добейтесь выполнения всех тестов проекта, после чего
объедините текущую ветку кода с главной.
3. Проанализируйте полученные результаты и сделайте выводы.

### Краткое описание проекта:
Проект представляет собой веб-приложение для интернет-магазина одежды, где пользователи могут просматривать товары и совершать покупки. При одновременной покупке экземпляров товаров разного вида
на общую сумму покупки предоставляется скидка 10%. Приложение построено с использованием MVT (Model-View-Template) архитектуры, типичной для Django, которая позволяет отделить бизнес-логику от пользовательского интерфейса и обеспечивать эффективное управление данными.

### Индивидуальное задание:

<h1 align="center">10 вариант</h1>

<p>**Тип магазина:** Магазин одежды</p> 
**Функциональность приложения:** При одновременной покупке экземпляров товаров разного вида на общую сумму покупки предоставляется скидка 10%

**Было разработано:**
*Модели: 
<p>Customer – модель для хранения информации о пользователе (имя, электронная почта, количество покупок).</p>
<p>Product – модель для представления информации о товаре (название, цена).</p>
<p>Purchase – модель для описания покупки
<p>PurchaseItem – модель для описания позиции в покупке (товар + количество)

*Представления:
<p>index – отображает главную страницу со списком доступных товаров.</p>
<p>purchase_form – выводит страницу для просомтра скидки и ввода данных о покупке (имя покупателя, адрес).</p>
<p>finalize_purchase – выводит сообщение об успешном оформлении заказа.</p>

### Используемые языки / библиотеки / технологии:
<p>Языки: Python3.10, HTML, Tailwind CSS</p>
<p>Фреймворки: Django</p>
<p>Базы данных: PostgreSQL </p>

### ERD-диаграмма:
![image](https://github.com/user-attachments/assets/488f1073-0ff2-4dc5-8d50-4f4344a59bd4)

### Выводы:
Было разработано веб-приложение согласно индивидуальному заданию, протестировано разработанное веб-приложение, проблем выявено не было.

**В процессе данной разработки я познакомился с:**
* Моделью MVT, ее сущностью и основными фреймворками на ее основе.
* Сущностями «модель», «контроллер», «представление», их функциональным назначением в модели MVC.  

**Также я получил:**
* Навыки разработки веб-приложений с использованием MVC-фреймворков.

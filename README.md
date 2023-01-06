
# Пример организации автотестирования для платформы <a href="https://www.gurock.com/" target="_blank">TestRail</a>.
> TestRail — это веб-инструмент для тестирования разрабатываемого программного обеспечения. Используется тестировщиками, разработчиками и руководителями групп для управления, отслеживания и организации мероприятий по тестированию программного обеспечения.
<div>


## :open_book: Содержание:

- Описание проекта
- Кратко
- Технологии и инструменты
- Что проверяем:
    - UI
    - API
- Запуск тестов:
    - Jenkins
    - Локально
- Отчеты:
    - Allure
    - Telegram       
- Видео прогона теста

## :heavy_check_mark: Описание

В проекте представлены примеры UI и API автоматизации тестирования на Python.

При написании тестов применялись инструменты объектно-ориентированной парадигмы, а также использовался шаблон проектирования PageObjects.

Выделены тест-кейсы. Реализована параметризация тестов.

Подключена система отчетности Allure Reports с вложениями (логи, скриншоты, видео, etc). 

Также по факту прохождения теста отправляется уведомление с результатами в Telegram.

Браузер в UI-тестах запускается удаленно в Selenoid.
    
## :heavy_check_mark: Кратко

- [x] ```Page Object```
- [x] ```Application Manager```
- [x] Параметризованный запуск тестов
- [x] ```Request/response``` спецификация для API тестов
- [x] Запуск тестов, используя ```Jenkins``` и ```Selenoid```
- [x] ```Allure Reports``` с вложениями (логи, скриншоты, видео)
- [x] Логирование ```Requests/responses``` в ```Allure Reports```
- [x] Отправка результатов тестирования в ```Telegram```

    
 ## :hammer_and_wrench: Технологии и инструменты:

  <div align="center">
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/python.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;   
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/pycharm.png" title="Pycharm" alt="Pycharm" width="40" height="40"/>&nbsp; 
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/pytest.svg" title="Pytest" alt="Pytest" width="40" height="40"/>&nbsp;   
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/selenium.svg" title="Selenium" alt="Selenium" width="40" height="40"/>&nbsp;
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/selene.png" title="Selene" alt="Selene" width="40" height="40"/>&nbsp;
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/selenoid.png" title="Selenoid" alt="Selenoid" width="40" height="40"/>&nbsp;
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/jenkins.svg" title="Jenkins" alt="Jenkins" width="40" height="40"/>&nbsp;
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/Allure.svg" title="Allure" alt="Allure" width="40" height="40"/>&nbsp; 
  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/telegram.png" title="Telegram" alt="Telegram" width="40" height="40"/>&nbsp;
 </div>
    
## :heavy_check_mark: Реализованные API-проверки

> - Создание-Поиск-Изменение-Удаление проекта;
> - Создание нового проекта:
>     - все поля заполненны валидными значениями;
>     - заполненно только поле "Название проекта", количество символов < 250;
>     - заполненно только поле "Название проекта", количество символов = 250;
>     - заполненно только поле "Название проекта", количество символов > 250;
>     - все поля заполненны валидными значениям, поле "Название проекта" не заполненно; 
>     - заполненно обязательное поле "Название проекта", не обязательные поля частично зааполненны;
>     - заполненно обязательное поле "Название проекта", поле выбора "Режима проекта" заполненно не валидным значением; 
>     - все поля не заполненны;
> - Изменение не существующего проекта;
> - Удаление не существующего проекта;
    
    
## :heavy_check_mark: Реализованные UI-проверки

> - Aвторизация:
>     - зарегистрированным пользователем;
>     - зарегистрированным пользователем с невалидным паролем;
>     - несуществующим пользователем;
> - Создание и удаление нового проекта:
    
## <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/jenkins.svg" title="Jenkins" alt="Jenkins" width="40" height="40"/>&nbsp; Запуск тестов из <a href="https://jenkins.autotests.cloud/job/001-Ang_ev-python_testrail/" target="_blank">Jenkins</a>
    
Для запуска тестов из Jenkins:

    1. Нажмите кнопку "Собрать с параметрами"


    
    
    
  












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
> - Создание нового проекта:
    
## <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/jenkins.svg" title="Jenkins" alt="Jenkins" width="40" height="40"/>&nbsp; Запуск тестов из <a href="https://jenkins.autotests.cloud/job/001-Ang_ev-python_testrail/" target="_blank">Jenkins</a>
    
 Нажмите кнопку "Собрать с параметрами"
  <div align="center">
  <img src="https://github.com/ElenaAngelcheva/autotests_project_for_testrail/blob/main/with_poetry/utils/img/logos/%D1%81%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D1%8C%20%D1%81%D0%B1%D0%BE%D1%80%D0%BA%D1%83.png" title="Build" alt="Build"/>&nbsp; 
</div>
    

## :computer: Локальный запуск

  1. Склонируйте репозиторий
  2. Установите Poetry poetry install
  3. Откройте проект в PyCharm, установите интерпретатор
  4. Создайте .env файл по образцу в папке проекта
  5. Запустите тесты в PyCharm или в командной строке
      - Пример команды запуска api тестов через термиал:
    
  ```
    pytest test_api.py
  ```
##  :bar_chart: Отчеты о прохождении тестов доступны в Allure

> При локальном запуске введите в командной строке:

```
    allure serve .\allure-results
```
    
##  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/Allure.svg" title="Allure" alt="Allure" width="40" height="40"/>&nbsp;  Allure
    
Примеры отображения тестов    
<div align="center">
<img src="https://github.com/ElenaAngelcheva/autotests_project_for_testrail/blob/main/with_poetry/utils/img/logos/allure%20homepage.PNG" title="Allure homepage" alt="Allure homepage"/>&nbsp; 
</div>

<div align="center">
<img src="https://github.com/ElenaAngelcheva/autotests_project_for_testrail/blob/main/with_poetry/utils/img/logos/allure%20example%20test.PNG" title="Allure homepage" alt="Allure example test"/>&nbsp; 
</div>

##  <img src="https://github.com/ElenaAngelcheva/ElenaAngelcheva/blob/main/img/logos/telegram.png" title="Telegram" alt="Telegram" width="40" height="40"/>&nbsp; Telegram
    Настроена отправка отчета в Telegram
    
<div align="center">
<img src="https://github.com/ElenaAngelcheva/autotests_project_for_testrail/blob/main/with_poetry/utils/img/logos/%D1%81%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%82%D0%B5%D0%BB%D0%B5%D0%B3%D1%80%D0%B0%D0%BC%D0%BC.PNG" title="telegram" alt="telegram"/>&nbsp; 
</div>
    
## :movie_camera: Пример видео тестового прогона

В отчетах Allure для каждого UI-теста прикреплен не только скриншот, но и видео прохождения теста  

![Video](https://github.com/ElenaAngelcheva/autotests_project_for_testrail/blob/main/with_poetry/utils/img/logos/video.gif))
    

    


    
  











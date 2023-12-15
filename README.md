# Учет доходов посредством google календаря

_Если Вы работаете в сфере услуг и Ваше расписание в Google календаре..._  
_**Основной стек**_:  
![Python](https://img.shields.io/badge/python-3.11-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Telegram](https://img.shields.io/badge/Telegram-api-ff1709?style=for-the-badge&logo=aiogram&logoColor=white&color=ff1709&labelColor=gray)
![Github](https://img.shields.io/badge/github-actions-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/Docker-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker compose](https://img.shields.io/badge/google-calendar_API-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

**Если лень сидеть с калькулятором и считать каждого клиента (а мне лень), то этот проект поможет.**  
Вот такой я нашел повод попрактиковаться в работе с сервисом Google calendar.**

### Возможности/Features:

* Каждую неделю в назначенное время отсылает Вам в телеграм сообщение с суммой доходов за последнюю неделю (разумеется все настраиваемо).
* По ссылке http://185.244.48.124:8080/diagram.html можно посмотреть динамику изменения доходов за последний месяц.


## Как оно работает

* Опрашиваем наш календарь используя возможности google api для этого случая.
* Фильтруем нужные события (ведь ДР племяшки не оплачивается).
* По словарику с ценами на каждого клиента, получаем итоговые суммы за день, неделю, месяц.
* Посредством POST запроса на API телеграмма отправляем себе любимому циферку с приятным текстовым сообщением.
* Проект разворачиваться посредством github actions в двух контейнерах, которые запускаются по cron`у в заданное время, чтобы обработать новые данные и спать дальше и не жрать ресурсы.


## Инстукция по установке

Она довольно муторна, одно получение доступа к google календарю чего стоит. Так что я решил это все не описывать. Ежели вдруг понадобиться, то напишите мне - я подскажу. 
## Author
 Юрий Каманин 
 [@Yohimbe227](https://www.github.com/Yohimbe227)

## License

Берите, кто хотите.


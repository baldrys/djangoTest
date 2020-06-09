Выполненное тестовое задание в виде ссылки на github или архива нужно прислать на почту info@surprizeme.ru в ответном письме, в котором вам отправляли задание.
По всем дополнительным вопросам пишите Станиславу в TG: https://t.me/beglory

Тестовое задание:
В Django 1.11.x создать приложение с тремя моделями: пользователь (можно расширить базового), платеж и выплата. Создать через админку несколько пользователей.
Добавить функцию добавления платежа и через консоль создать 100 тестовых платежей с разными суммами и пользователями. Создать html страницу на которой пользователь может заказать выплату.
В админке добавить кнопку в модель выплаты, которая ее производит.

Поля у моделей должны быть следующие:
Пользователь:
Почта (обязательное и не пустое)
Телефон (опциональное)
Имя и фамилия (обязательное и не пустое)
Общее вознаграждение (по умолчанию 0, вещественное)

Платеж:
Автор (пользователь, обязательное)
Сумма платежа (не отрицательное, вещественное)
Дата платежа (текущий таймстамп при создании записи)

Выплата:
Пользователь (обязательное)
Сумма выплаты (обязательное, вещественное)
Дата создания заявки (текущий таймстамп при создании записи)
Дата обработки заявки
Галочка статуса, выплачено или нет (обязательное, по умолчанию False)
Номер счёта (текстовое поле, опциональное)

Функция создания платежа:
Должен создаваться платеж с указанной суммой, и 30% от этой суммы должно начисляться пользователю в его вознаграждение.

HTML страница:
Должен быть темплейт с отображением имени пользователя и его текущего баланса.
Должно быть поле ввода, в котором можно указать сумму выплаты, и поле для ввода номера счета. Сумма выплаты не может превышать баланс пользователя.
И кнопка, по которой должен выполняться запрос на бекенд и создаваться выплата (форма).

Админка:
Если галочка статуса в модели выплаты установлена в True, все поля должны быть нередактируемыми. Если не установлена, добавить отдельную кнопку “Выплатить”, по нажатию на которую:
Должен происходить перерасчет общего вознаграждения юзера (вычитывается сумма запрошенной выплаты).
Дата обработки заказа заполняется текущим таймстампом.
Галочка статуса устанавливается в True
Если указан номер счета, должен происходить POST запрос по адресу https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4 с телом JSON {"account":"НОМЕР*СЧЕТА*ИЗ*ВЫПЛАТЫ", "amount":СУММА*ВЫПЛАТЫ}

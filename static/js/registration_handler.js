import { displayErrors } from './display_errors.js';


async function regFunction(event) {
    event.preventDefault();  // Предотвращаем стандартное действие формы

    // Получаем форму и собираем данные из неё
    const form = document.getElementById('registration-form');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/auth/registration', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Проверяем успешность ответа
        if (!response.ok) {
            // Получаем данные об ошибке
            const errorData = await response.json();
            displayErrors(errorData);  // Отображаем ошибки
            return;  // Прерываем выполнение функции
        }

        const result = await response.json();

        if (result.message) {  // Проверяем наличие сообщения о успешной регистрации
            window.location.href = '/auth/login';  // Перенаправляем пользователя на страницу логина
        } else {
            alert(result.message || 'Неизвестная ошибка');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при регистрации. Пожалуйста, попробуйте снова.');
    }
}

// Функция для отображения ошибок
function displayErrors(errorData) {
    let message = 'Произошла ошибка';

    if (errorData && errorData.detail) {
        if (Array.isArray(errorData.detail)) {
            // Обработка массива ошибок
            message = errorData.detail.map(error => {
                if (error.type === 'string_too_short') {
                    return `Поле "${error.loc[1]}" должно содержать минимум ${error.ctx.min_length} символов.`;
                }
                return error.msg || 'Произошла ошибка';
            }).join('\n');
        } else {
            // Обработка одиночной ошибки
            message = errorData.detail || 'Произошла ошибка';
        }
    }

    // Отображение сообщения об ошибке
    alert(message);
}
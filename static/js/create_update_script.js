async function createFunction(event) {
    event.preventDefault();

    const form = document.getElementById('entity-form');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    // Преобразуем строковые значения в массивы
    const arrayFields = ["genres", "cast", "countries"];

    arrayFields.forEach(field => {
        if (data[field]) {
            data[field] = data[field]
                .split(",")
                .map(v => v.trim())
                .map(v => isNaN(v) ? v : Number(v));
        }
    });

    try {
        const response = await fetch(`/${ENTITY}/create`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorData = await response.json();
            displayErrors(errorData);
            return;
        }

        const result = await response.json();

        if (result.message) {
            window.location.href = '/movies/actual';
        } else {
            alert(result.message || 'Неизвестная ошибка');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при регистрации. Пожалуйста, попробуйте снова.');
    }
}



async function updateFunction(event) {
    event.preventDefault();

    const form = document.getElementById('entity-form');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    // Преобразуем строковые значения в массивы
    const arrayFields = ["genres", "cast", "countries"];

    arrayFields.forEach(field => {
        if (data[field]) {
            data[field] = data[field]
                .split(",")
                .map(v => v.trim())
                .map(v => isNaN(v) ? v : Number(v));
        }
    });

    try {
        const response = await fetch(`/${ENTITY}/update`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorData = await response.json();
            displayErrors(errorData);
            return;
        }

        const result = await response.json();

        if (result.message) {
            window.location.href = '/movies/actual';
        } else {
            alert(result.message || 'Неизвестная ошибка');
        }

    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при обновлении. Пожалуйста, попробуйте снова.');
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

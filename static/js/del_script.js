async function deleteFunction(event) {
    event.preventDefault();

    const form = document.getElementById('entity-form');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    const entityId = data.entityid;

    if (!entityId) {
        alert("Введите ID сущности!");
        return;
    }



    try {
        const url = "/" + ENTITY + "/delete?" + ENTITY.slice(0, -1) + "id=" + entityId;
        const response = await fetch(url, {
            method: 'DELETE'
        });

        if (!response.ok) {
            const errorData = await response.json();
            displayErrors(errorData);
            return;
        }

        const result = await response.json();

        alert(result.message);

        if (result.message.includes("deleted")) {
            window.location.href = '/movies/actual';
        }

    } catch (error) {
        console.error("Ошибка:", error);
        alert("Произошла ошибка при удалении.");
    }
}


// Функция отображения ошибок — такая же, как в update
function displayErrors(errorData) {
    let message = 'Произошла ошибка';

    if (errorData && errorData.detail) {
        if (Array.isArray(errorData.detail)) {
            message = errorData.detail.map(error => {
                if (error.type === 'string_too_short') {
                    return `Поле "${error.loc[1]}" должно содержать минимум ${error.ctx.min_length} символов.`;
                }
                return error.msg || 'Произошла ошибка';
            }).join('\n');
        } else {
            message = errorData.detail || 'Произошла ошибка';
        }
    }

    alert(message);
}

let selectedSeat = null;

document.querySelectorAll('.seat.free').forEach(seat => {
    seat.addEventListener('click', () => {

        if (selectedSeat) {
            selectedSeat.classList.remove('selected');
        }

        seat.classList.add('selected');
        selectedSeat = seat;

        document.getElementById('book-btn').disabled = false;
    });
});

async function bookSeat() {
    if (!selectedSeat) return;

    const row = selectedSeat.dataset.row;
    const seat = selectedSeat.dataset.seat;

    const response = await fetch(`/cinema_sessions/${SESSION_ID}/booking`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            rownumber: row,
            seatnumber: seat
        })
    });

    if (!response.ok) {
        alert("Место уже занято 😢");
        return;
    }

    window.location.href = "/pages/success/booked";
}


async function cancelBooking(sessionId, row, seat) {
    console.log("cancelBooking called", sessionId, row, seat);
    const response = await fetch(`/cinema_sessions/${sessionId}/booking/cancel`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            rownumber: row,
            seatnumber: seat
        })
    });

    if (!response.ok) {
        alert("Impossible to cancel the ticket 😢");
        return;
    }

    window.location.href = "/pages/success/returned";

}


async function logoutFunction(event) {
    event.preventDefault(); // Отменяем переход по ссылке

    try {
        const response = await fetch('/site/logout', {
            method: 'POST',
            credentials: 'include'
        });

        if (!response.ok) {
            const errorData = await response.json();
            alert(errorData.message || 'Ошибка при выходе из системы');
            return;
        }

        const result = await response.json();

        if (result.message) {
            // Возвращаем пользователя на страницу входа
            window.location.href = '/';
        } else {
            alert('Выход выполнен, но сервер не вернул сообщение');
        }
    } catch (error) {
        console.error('Ошибка при выходе:', error);
        alert('Произошла ошибка при выходе. Попробуйте снова.');
    }
}
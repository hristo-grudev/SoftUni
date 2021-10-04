function attachEventsListeners() {
    const rations = {
        days: 1,
        hours: 24,
        minutes: 1440,
        seconds: 86400
    }
    
    function convert(value, unit) {
        const idDays = value / rations[unit];

        return {
            days: idDays,
            hours: idDays * rations.hours,
            minutes: idDays * rations.minutes,
            seconds: idDays * rations.seconds
        }
    }
    const daysInput = document.getElementById('days');
    const hoursInput = document.getElementById('hours');
    const minutesInput = document.getElementById('minutes');
    const secondsInput = document.getElementById('seconds');

    document.querySelector('main').addEventListener('click', onConvert);

    function onConvert(e) {
        if (e.target.tagName = 'INPUT' && e.target.type == 'button') {
            const input = e.target.parentElement.querySelector('input[type="text"]');

            const time = convert(Number(input.value), input.id);
            daysInput.value = time.days;
            hoursInput.value = time.hours;
            minutesInput.value = time.minutes;
            secondsInput.value = time.seconds;
        }
    }
}
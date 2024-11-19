document.getElementById('convertButton').addEventListener('click', async () => {
    const dateInput = document.getElementById('gregorianDate').value;

    if (!dateInput) {
        alert("Please select a date!");
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ date: dateInput }),
        });

        const data = await response.json();

        if (data.error) {
            document.getElementById('result').innerText = `Error: ${data.error}`;
        } else {
            document.getElementById('result').innerText = `Hebrew Date: ${data.hebrew}`;
        }
    } catch (error) {
        console.error(error);
        document.getElementById('result').innerText = "Failed to fetch the Hebrew date.";
    }
});

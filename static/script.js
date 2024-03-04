//import 'html-midi-player'

// function generateMelody() {

//     const seed = document.getElementById('seed').value;
//     const format = document.getElementById('format').value;

//     fetch(`/generate-melody?seed=${seed}&format=${format}`)
//         .then(response => response.json());
// }



const inputData = document.getElementById("seed");
let selectedData = null;
function generateMelody() {
    let allowed = true;
    const seed = document.getElementById('seed').value;
    const format = document.getElementById('format').value;

    const checkingData = seed.split(" ");

    if (format == "midi") {
        checkingData.map(item => {
            if (parseInt(item) > 45 && parseInt(item) < 81) {
                if (parseInt(item) == 46 || parseInt(item) == 49 || parseInt(item) == 70) {
                    console.log(`DATA NOT CLEAR ${item} Error`);
                    alert(`Key Error: ${item} is not allowed!`)

                    allowed = false;
                    return;
                }
            } else {
                alert("Data Must be between 45 to 81");
                allowed = false;
                return;
            }
            return false;
        })
    }

    if (format == "Romania") {
        checkingData.map(item => {
            if (parseInt(item) > 52 && parseInt(item) < 81) {
                if (parseInt(item) == 56 || parseInt(item) == 58 || parseInt(item) == 61 || parseInt(item) == 63 || parseInt(item) == 66 || parseInt(item) == 68 || parseInt(item) == 70 || parseInt(item) == 73 || parseInt(item) == 75 || parseInt(item) == 78 || parseInt(item) == 80) {
                    console.log(`DATA NOT CLEAR ${item} Error`);
                    alert(`Key Error: ${item} is not allowed!`)

                    allowed = false;
                    return;
                }
            } else {
                alert("Data Must be between 52 to 81");
                allowed = false;
                return;
            }
            return false;
        })
    }
    if (format == "England") {
        checkingData.map(item => {
            if (parseInt(item) > 58 && parseInt(item) < 72) {
                if (parseInt(item) == 61 || parseInt(item) == 63 || parseInt(item) == 66 || parseInt(item) == 68 || parseInt(item) == 70) {
                    console.log(`DATA NOT CLEAR ${item} Error`);
                    alert(`Key Error: ${item} is not allowed!`)

                    allowed = false;
                    return;
                }
            } else {
                alert("Data Must be between 58 to 72");
                allowed = false;
                return;
            }
            return false;
        })

    }
    if (format == "India") {
        checkingData.map(item => {
            if (parseInt(item) > 53 && parseInt(item) < 81) {
                if (parseInt(item) == 56 || parseInt(item) == 58 || parseInt(item) == 61 || parseInt(item) == 63 || parseInt(item) == 66 || parseInt(item) == 68 || parseInt(item) == 70 || parseInt(item) == 73 || parseInt(item) == 75 || parseInt(item) == 78 || parseInt(item) == 79 || parseInt(item) == 80) {
                    console.log(`DATA NOT CLEAR ${item} Error`);
                    alert(`Key Error: ${item} is not allowed!`)

                    allowed = false;
                    return;
                }
            } else {
                alert("Data Must be between 53 to 81");
                allowed = false;
                return;
            }
            return false;
        })
    }

    console.log("New Data : ", JSON);

    console.log("Data is Generating.");
    if (allowed) {

        fetch(`/generate-melody?seed=${seed}&format=${format}`)
            .then(response => response.text());
    }
}


function handleChange(event) {
    selectedData = event.target.value;
    fetch(`/get-melody?data=${event.target.value}`)
        .then(response => response.json());
    console.log("Data is : ", event.target.value);
}



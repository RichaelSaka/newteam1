document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.option');
    console.log(buttons);

    var choices = [];
    choices = [...new Set(choices)];


    buttons.forEach(button => {
        button.addEventListener('click', () => {
            let text = button.innerText;
            console.log(text);
            choices.push(text);
            console.log(choices);
        });
    }); 

    var user_dict = []; // Create an empty array

user_dict.push({
user: "Sophia",
industries: choices
});
});


fetch("http://localhost:8080/jobs", {
  method: "POST",
  body: user_dict,
});







console.log(choices);





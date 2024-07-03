// DOM 요소들이 완전히 구성된 후 이벤트를 발생
// <script>태그를 HTML <body> 맨 마지막에 배치하여도 되지만,
// 최대한 HTML 코드를 건들지 않기 위해 사용

document.addEventListener("DOMContentLoaded", () => {
    NumBaseballGame();
});

// 키보드 enter를 통해서 "확인하기" 기능 추가
function use_enter(event) {
    if (event.key === "Enter") {
        check_numbers();
    }
}

// input 커서 자동 이동 기능 추가
function input_moving(event) {
    const input_move = event.target;
    if (input_move.value.length === 1) {
        if (input_move.id === "number1") {
            document.getElementById("number2").focus();
        } else if (input_move.id === "number2") {
            document.getElementById("number3").focus();
        }
    }
}

// 키보드 backspace를 통해서 input 삭제 기능 추가
function input_backspace(event) {
    if (event.key === "Backspace" && event.target.value.length === 0) {
        const currentInput = event.target;
        if (currentInput.id === "number3") {
            document.getElementById("number2").focus();
        } else if (currentInput.id === "number2") {
            document.getElementById("number1").focus();
        }
    }
}

// NumBaseballGame START!
let attemptCount = 0;
let maxAttempts = 10;
let correctNumbers = [];

function NumBaseballGame() {
    attemptCount = maxAttempts;
    correctNumbers = set_random_numbers();
    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";
    document.getElementById("game-result-img").src = "";
    document.querySelector(".result-display").innerHTML = "";
    document.querySelector(".submit-button").disabled = false;

    document.getElementById("number1").addEventListener("keydown", use_enter);
    document.getElementById("number2").addEventListener("keydown", use_enter);
    document.getElementById("number3").addEventListener("keydown", use_enter);

    document.getElementById("number1").addEventListener("input", input_moving);
    document.getElementById("number2").addEventListener("input", input_moving);
    document.getElementById("number3").addEventListener("input", input_moving);

    document.getElementById("number1").addEventListener("keydown", input_backspace);
    document.getElementById("number2").addEventListener("keydown", input_backspace);
    document.getElementById("number3").addEventListener("keydown", input_backspace);
}

// 랜덤 숫자 생성 함수
function set_random_numbers() {
    let numbers = [];
    while (numbers.length < 3) {
        let rand = Math.floor(Math.random() * 10);
        if (!numbers.includes(rand)) {
            numbers.push(rand);
        }
    }
    return numbers;
}

// 입력 숫자 확인 함수
function check_numbers() {
    let number1 = document.getElementById("number1").value;
    let number2 = document.getElementById("number2").value;
    let number3 = document.getElementById("number3").value;

    if (number1 === "" || number2 === "" || number3 === "") {
        NumBaseballGame();
        return;
    }

    let inputNumbers = [parseInt(number1), parseInt(number2), parseInt(number3)];
    let result = get_goal(inputNumbers);

    display_goal(inputNumbers, result);

    attemptCount--;
    if (result.strikes === 3) {
        end_game("success");
    } else if (attemptCount === 0) {
        end_game("fail");
    }

    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";
    document.getElementById("number1").focus(); // 이거 안하면 number3에 커서
}

// 투구 결과 확인 함수
function get_goal(input_numbers) {
    let strikes = 0;
    let balls = 0;

    input_numbers.forEach((num, index) => {
        if (correctNumbers[index] === num) {
            strikes++;
        } else if (correctNumbers.includes(num)) {
            balls++;
        }
    });

    return { strikes, balls };
}

// 투구 결과 display 함수
function display_goal(inputNumbers, result) {
    let resultDisplay = document.querySelector(".result-display");
    let resultDiv = document.createElement("div");
    resultDiv.className = "check-result";

    let leftDiv = document.createElement("div");
    leftDiv.className = "left";
    leftDiv.textContent = inputNumbers.join(" ");

    let rightDiv = document.createElement("div");
    rightDiv.className = "right";
    if (result.strikes > 0) {
        rightDiv.innerHTML += `${result.strikes} <div class="strike num-result">S</div> `;
    }
    if (result.balls > 0) {
        rightDiv.innerHTML += `${result.balls} <div class="ball num-result">B</div>`;
    }
    if (result.strikes === 0 && result.balls === 0) {
        rightDiv.innerHTML += `<div class="out num-result">O</div>`;
    }

    resultDiv.appendChild(leftDiv);
    resultDiv.appendChild(rightDiv);
    resultDisplay.appendChild(resultDiv);
}

function end_game(result) {
    let imgElement = document.getElementById("game-result-img");
    if (result === "success") {
        imgElement.src = "success.png";
    } else {
        imgElement.src = "fail.png";
    }
    document.querySelector(".submit-button").disabled = true;

    // 10초 후 자동으로 게임 재시작
    setTimeout(() => {
        NumBaseballGame();
    }, 10000);
}
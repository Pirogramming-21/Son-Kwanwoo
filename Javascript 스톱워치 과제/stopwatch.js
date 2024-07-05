let startTime;
let elapsedTime = 0;
let timerInterval;

const display = document.getElementById('display');
const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const resetBtn = document.getElementById('resetBtn');
const recordsList = document.getElementById('recordsList');
const deleteAllBtn = document.getElementById('deleteAllBtn');

// 모든 기록 삭제
const deleteAllRecords = () => {
    recordsList.innerHTML = "";
};

// start
const startTimer = () => {
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(() => {
        elapsedTime = Date.now() - startTime;
        display.textContent = formatTime(elapsedTime);
    }, 10);
    startBtn.disabled = true;
    stopBtn.disabled = false;
};

// stop
const stopTimer = () => {
    clearInterval(timerInterval);
    addRecord();
    startBtn.disabled = false;
    stopBtn.disabled = true;
};

// reset
const resetTimer = () => {
    clearInterval(timerInterval);
    elapsedTime = 0;
    display.textContent = "00:00:00";
    startBtn.disabled = false;
    stopBtn.disabled = true;

    deleteAllRecords();
};

// 시간 포맷 함수
const formatTime = (time) => {
    let hours = Math.floor(time / 3600000);
    let minutes = Math.floor((time % 3600000) / 60000);
    let seconds = Math.floor((time % 60000) / 1000);
    let milliseconds = Math.floor((time % 1000));
    return (
        (hours < 10 ? "0" + hours : hours) +
        ":" +
        (minutes < 10 ? "0" + minutes : minutes) +
        ":" +
        (seconds < 10 ? "0" + seconds : seconds) +
        "." +
        (milliseconds < 100 ? "0" : "") + (milliseconds < 10 ? "0" : "") + milliseconds
    );
};

// 기록 추가
const addRecord = () => {
    const li = document.createElement("li");
    const span = document.createElement("span");

    span.textContent = display.textContent;
    li.appendChild(span);
    const deleteBtn = document.createElement("button");

    deleteBtn.textContent = "🗑️";
    deleteBtn.onclick = () => li.remove();
    li.appendChild(deleteBtn);
    
    recordsList.appendChild(li);
};

startBtn.addEventListener("click", startTimer);
stopBtn.addEventListener("click", stopTimer);
resetBtn.addEventListener("click", resetTimer);
deleteAllBtn.addEventListener("click", deleteAllRecords);

// 초기 상태 설정
stopBtn.disabled = true;
display.textContent = "00:00:00";
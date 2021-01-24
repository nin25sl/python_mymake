console.log("hello js")

function generate_year_range(start,end) {
    let years = ""
    for (let year = start; year <= end ; year++){
        years += "<option value = '"+ year +"'>" + year + "</option>";
    }
    return years;
}

let today = new Date();
let currentMonth = today.getMonth();
let currentYear = today.getFullYear();
let selectYear = document.getElementById("year");
let selectMonth = document.getElementById("month");

let createYear = generate_year_range(1970,2200);

document.getElementById("year").innerHTML = createYear;

let calender = document.getElementById("calender");
let lang = calender.getAttribute('data-lang'); //https://itsakura.com/js-getattribute data-langの値はja(japanese?)

let months =  ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"];
let days = ["日", "月", "火", "水", "木", "金", "土"];

let dayHeader = "<tr>";
for (day in days) {
    dayHeader += "<th data-days = '"+ days[day] + "'>" + days[day] +"</th>";
}
dayHeader += "</tr>"

document.getElementById("thread-month").innerHTML = dayHeader;

monthAndYear = document.getElementById("monthAndYear")
showCalender(currentMonth, currentYear)

function next() {
    currentYear = (currentMonth === 11)? currentYear + 1 : currentYear;//参考演算子 https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/Conditional_Operator
    currentMonth = (currentMonth + 1) % 12;//すごく頭がいいmonthのやり方
    showCalender(currentMonth, currentYear);
}

function prev() {
    currentYear = (currentMonth == 0)? currentYear - 1 : currentYear;
    currentMonth = (currentMonth == 0)? currentMonth = 11 : currentMonth - 1;
    showCalender(currentMonth, currentYear);
}

function jump() {
    currentYear = parseInt(selectYear.value);
    currentMonth = parseInt(selectMonth.value);
    showCalender(currentMonth,currentYear);
}

function showCalender(month, year) {

    let firstDay = (new Date(year, month)).getDay();
    
    tbl = document.getElementById("calendar-body");

    tbl.innerHTML = "";

    monthAndYear.innerHTML = months[month] + " " + year;
    selectYear.value = year;
    selectMonth.value = month;

    let date = 1
    for(let i = 0 ; i < 6 ; i++){
        let row = document.createElement("tr");//https://developer.mozilla.org/ja/docs/Web/API/Document/createElement
        
        for(let j = 0 ; j < 7 ; j++){//カレンダーを作る
            if(i === 0 && j < firstDay) {//カレンダーの最初を作る
                cell = document.createElement("td");
                cellText = document.createTextNode("");//textに２を入れる(<td>2</td>となる)
                cell.appendChild(cellText);//子属性に追加
                row.appendChild(cell);//rowの子供属性に追加
            } else if(date > daysInMonth(month, year)) {//カレンダーを書き終えた時
                break;
            } else {//カレンダーを作成
                cell = document.createElement("td");
                cell.setAttribute("data-date", date);//setattribute->属性を決める
                cell.setAttribute("data-month", month + 1);
                cell.setAttribute("data-year",year);
                cell.setAttribute("sata-month-name",months[month]);
                cell.className = "date-picker";
                cell.innerHTML = "<span>" + date + "</span>";//tdに入れるから、span

                if(date === today.getDate() && year === today.getFullYear() && month === today.getMonth()) {//今日の日付に印をつける
                    cell.className = "date-picker selected";
                }
                row.appendChild(cell);
                date++
            }
        }
        
        tbl.appendChild(row);
    }
    function daysInMonth(iMonth,iYear) {
        return 32 - new Date(iYear, iMonth, 32).getDate();//次の月の何日かで、終わりの日付が30か31かわかる
    }

}

console.log(selectYear.value)
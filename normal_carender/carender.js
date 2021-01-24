console.log("hello.js")
//Qiita参照

const date = new Date()
let year = date.getFullYear()
let month = date.getMonth() + 1
const nowYear = date.getFullYear()
const nowMonth = date.getMonth() + 1
const nowDate = date.getDate()

document.querySelector('#prev').addEventListener('click',moveCalender)
document.querySelector('#next').addEventListener('click',moveCalender)
createCalender(year,month)

function createCalender(year, month) {
    const startDate = new Date(year, month-1)
    const endDate = new Date(year,month,0)
    let beforeMonthLastDate = new Date()

    if (month == 1){
        beforeMonthLastDate = new Date(year-1, 12, 0)
    } else {
        beforeMonthLastDate = new Date(year, month-1, 0)
    }
    const weeks = ['日','月','火','水','木','金','土']

    const endDayCount = endDate.getDate()
    const startDay = startDate.getDay() //getDay->週を数値で表示　日->0 月->1 ...

    const weekMax = 6 //カレンダーの１ヶ月の週の最大数
    const dayMax = 7 //一週間の日の最大数
    let nowDayCount = 1
    let beforeDayCount = beforeMonthLastDate.getDate()
    let nextDayCount = 1
    let calenderHtml = '' //HTMLを組み立てる変数

    calenderHtml += '<h1>' + year + '/' + month + '</h1>'

    calenderHtml += '<table>'

    for(let i = 0; i < weeks.length; i++) {
        calenderHtml += '<td>' + weeks[i] + '</td>'
    }

    for (let w = 0; w < weekMax ; w++) {
        calenderHtml += '<tr>'
        for (let d = 0; d < dayMax ; d++){
            if (w == 0 && d < startDay) {
                let temp = beforeDayCount
                //console.log(temp,startDay,d)
                temp = temp - (startDay - d - 1)
                calenderHtml += '<td class = "is-disabled">'+ temp +'</td>'
            } else if (nowYear === year && nowMonth === month && nowDate === nowDayCount){
                calenderHtml += '<td class = "today">' + nowDayCount + '</td>'
                nowDayCount++
            } else if(nowDayCount > endDayCount){
                calenderHtml += '<td class = "is-disabled">'+ nextDayCount +'</td>'
                nextDayCount++
            } else {
                calenderHtml += '<td>' + nowDayCount + '</td>'
                nowDayCount++
            }
        }
        calenderHtml += '<tr/>'
    }

    calenderHtml+= '</table>'

    document.querySelector('#carender').innerHTML = calenderHtml //queryselecter -> https://developer.mozilla.org/ja/docs/Web/API/Document/querySelector
}

function moveCalender(e){
    if (e.target.id === 'prev') {
        if (month === 1){
            year--
            month = 12
        } else {
            month--
        }
    } else if(e.target.id === 'next') {
        if (month === 12) {
            year++
            month = 1
        } else {
            month++
        }
    } 

    createCalender(year,month)
}



document.addEventListener("click", function(e){ //addEventListener -> https://developer.mozilla.org/ja/docs/Web/API/EventTarget/addEventListener
    if(e.target.classList.contains("calender_id")){
        console.log('クリックした日付は' + e.target.dataset.date + 'です')
    }
})
/*今月のカレンダーを表示する。*/
//test
//console.log(startDate)
//console.log(endDate)
//console.log(beforeMonthLastDate)
// console.log(moon.getFullYear())
//console.log(document)
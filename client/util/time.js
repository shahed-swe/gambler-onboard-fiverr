const TIMEAGO_UTIL = require('vue-timeago');

const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'October', 'December'];
const MONTHS_ABBREVIATIONS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Nov', 'Oct', 'Dec'];


const DATE_OPTIONS = {
	year: 'numeric',
	month: 'short',
	day: 'numeric',
	hour: '2-digit',
	minute: '2-digit',
	hour12: true
};

const SHORT_DATE_OPTIONS = {
	year: 'numeric',
	month: 'short',
	day: 'numeric',
};

const SHORT_DATE_TIME_OPTIONS = {
	year: 'numeric',
	month: 'short',
	day: 'numeric',
	hour: 'numeric',
	minute: 'numeric'
};

function getReadableDate(time) {
	return new Date(time).toLocaleDateString('en-US', DATE_OPTIONS)
}

function getShortReadableDate(time) {
	return new Date(time).toLocaleDateString('en-US', SHORT_DATE_OPTIONS)
}

function getShortReadableDateTime(time) {
	return new Date(time).toLocaleDateString('en-US', SHORT_DATE_TIME_OPTIONS)
}

function formatAbbreviatedMonthDay(time) {
	return MONTHS_ABBREVIATIONS[time.month - 1] + ' ' + time.day;
}

function formatAbbreviatedMonthDayYear(time) {
	return MONTHS_ABBREVIATIONS[time.month - 1] + ' ' + time.day + ', ' + time.year;
}

function getTimeago(time, $timeago) {
	return TIMEAGO_UTIL.converter(new Date(time), $timeago.locale, { includeSeconds: true, addSuffix: true })
}

function formatIntoAbbreviatedString(ms, includeZeroes) {
    let secs = parseInt(ms / 1000);
    if (secs === 0) {
        return '0s';
    }

    let remainder = parseInt(secs % 86400);
    let days = parseInt(secs / 86400);
    let hours = parseInt(remainder / 3600);
    let minutes = parseInt(remainder / 60 - hours * 60);
    let seconds = parseInt(remainder % 3600 - minutes * 60);

    let fDays;
    if (days > 0) {
        fDays = ' ' + days + 'd';
    } else {
        fDays = '';
    }

    let fHours;
    if (hours > 0) {
        fHours = ' ' + hours + 'h';
    } else {
        fHours = '';
    }

    let fMinutes;
    if (minutes > 0) {
        fMinutes = ' ' + minutes + 'm';
    } else {
        fMinutes = '';
    }

    let fSeconds;
    if (seconds > 0) {
        fSeconds = ' ' + seconds + 's';
    } else {
        fSeconds = includeZeroes ? ' 00s' : '';
    }

    return (fDays + fHours + fMinutes + fSeconds).trim()
}

function getAbbreviatedBreakdown(ms, includeZeroes) {
    console.log({ms}, {includeZeroes})
    let secs = parseInt(ms / 1000);
    if (secs === 0) {
        return '0s';
    }

    let remainder = parseInt(secs % 86400);
    let days = parseInt(secs / 86400);
    let hours = parseInt(remainder / 3600);
    let minutes = parseInt(remainder / 60 - hours * 60);
    let seconds = parseInt(remainder % 3600 - minutes * 60);

    let fDays;
    if (days > 0) {
        fDays = days + '';
    } else {
        fDays = '';
    }

    let fHours;
    if (hours > 0) {
        fHours = hours + '';
    } else {
        fHours = '';
    }

    let fMinutes;
    if (minutes > 0) {
        fMinutes = minutes + '';
    } else {
        fMinutes = '';
    }

    let fSeconds;
    if (seconds > 0) {
        fSeconds = seconds + '';
    } else {
        fSeconds = includeZeroes ? ' 00' : '';
    }

    return [fDays.trim(), fHours.trim(), fMinutes.trim(), fSeconds.trim()]
}

export { getReadableDate, getShortReadableDate, getShortReadableDateTime, getTimeago, formatIntoAbbreviatedString, formatAbbreviatedMonthDayYear, getAbbreviatedBreakdown };
